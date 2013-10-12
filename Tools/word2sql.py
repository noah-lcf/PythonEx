# encoding: utf-8 
"""
Created on 2013年10月10日

将word文档转换为可执行SQL，该文档从word文档复制到Notepad++里面得到
 
 规则：
  1. 格式如x.x.x识别为表名,格式Name:XXX识别为表注释
  2. 小写开头的行识别为 列名,格式为 field  type  default_val comment 如果default_val不为数字或浮点数，设default_val为null
  3. 格式为 1. 或【1】或‘F’或 Bit开头的，扩充到上一个field行做注释
  4. 格式为Index:field+field,field 为索引,索引间用,格开，复合索引用+格开
  5. 不能匹配上述几种情况的行，全部删除
  6. 如果表名包含HIS，放到HIS库中
 
@author: NOAH
"""
import re

USE_DB = "iov3"
USE_DB_HIS = "iov3_his"
DEFAULT_ENGINE = "InnoDB"
DROP_STMT = True


def preDeal(lines):
    """
  文档预处理
    """
    # 记下为注解的行
    commentLines = []
    for i in range(0, len(lines)):
        line = lines[i].encode("utf-8").strip()
        if (re.match(r"^\d+", line) and not re.match(r"^\d\.\d\.\d+", line)) or re.match(r"^(【\d】)|(‘.+’)|(Bit.+).*$",
                                                                                         line):
            commentLines.append(i)
    index = 0
    appendIndex = 0
    for i in commentLines:
        if i == index + 1:
            lines[appendIndex] += lines[i] + "\t"
            index += 1
        else:
            index = i
            appendIndex = i - 1
            lines[appendIndex] = lines[appendIndex] + "\t" + lines[i]
    lines2 = []
    for line in lines:
        if re.match(r"^(Name:)|([a-z])|(\d\.\d\.\d)|(Index:)+", line):
            lines2.append(line)
        #             print "append: %s" %line
        else:
            if not ((re.match(r"^\d+", line) and not re.match(r"^\d\.\d\.\d+", line)) or re.match(
                    r"^(【\d】)|(‘.+’)|(Bit.+).*$", line.encode("utf-8"))):
                print "skip: %s" % line
    return lines2


class table(object):
    def __init__(self, name, comment):
        self.name = name
        self.comment = comment
        self.rows = []
        self.indexes = []


def getTables(lines):
    """
    解析文档中行得到表信息
   """
    tables = []
    t = None
    for line in lines:
        if re.match(r"\d\.\d\.\d", line):
            tablename = line.split()[1];
            t = table(tablename, None)
            tables.append(t)
            continue
        elif re.match(r"^Name:", line):
            tablecomment = re.findall(r'(?<=Name:).*', line)[0]
            t.comment = tablecomment.strip()
            continue
        elif re.match(r"^Index:", line):
            index = re.findall(r'(?<=Index:).*', line)[0].split(",")
            t.indexes.extend([i.strip().split("+") for i in index])
        else:
            attrs = line.split()
            t.rows.append(attrs)
            #             print "attrs:%s" % attrs
    return tables


def getSql(tables):
    """
    生成建表语句
    """
    sql = ""
    for t in tables:
        if t.name.upper().find("HIS") == -1:
            sql += "\nUSE %s;\n" % USE_DB
        else:
            sql += "\nUSE %s;\n" % USE_DB_HIS
        sql += "\n/*Table structure for table `%s` */\n" % t.name
        if DROP_STMT: sql += "\nDROP TABLE IF EXISTS `%s`;\n" % t.name
        sql += "\nCREATE TABLE `%s`(\n" % t.name
        for attr in t.rows:
            if len(attr) < 2: print str(attr)
            if re.match(r"^-?\d+\.?\d*$", attr[2]):
                sql += "\t`%s` %s DEFAULT %s COMMENT '%s',\n" % (attr[0], attr[1], attr[2], "\t".join(attr[3:]))
            else:
                sql += "\t`%s` %s DEFAULT NULL COMMENT '%s',\n" % (attr[0], attr[1], "\t".join(attr[2:]))
        if len(t.rows): sql += "\tPRIMARY KEY (`%s`)%s\n" % (t.rows[0][0], (len(t.indexes) and "," or " ")[0])
        for k in range(0, len(t.indexes)):
            index = t.indexes[k]
            if len(index): sql += "\tKEY `INDEX_%s` (%s)%s\n" % (
                "_".join([i.upper() for i in index]), ",".join(['`' + i + '`' for i in index]),
                (k != (len(t.indexes) - 1) and "," or " ")[0])
        sql += ")ENGINE=%s DEFAULT CHARSET=utf8 COMMENT='%s';\n" % (DEFAULT_ENGINE, t.comment or ' ')
    return sql


if __name__ == '__main__':
    #user_profile service_object_profile device_profile vas_profile product_profile system_profile 
    f_name = "all_profile"
    f = open(f_name + ".txt")
    sql = getSql(getTables(preDeal([a.rstrip().decode("utf-8") for a in f.readlines()])))
    fto = open("IOV3_" + f_name + ".sql", "w")
    fto.write(sql)

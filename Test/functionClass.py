#!/usr/bin/python
# coding: UTF-8

#http://www.cnblogs.com/wentingtu/archive/2012/05/23/2514776.html



"""
This code demostrates how easy to imprement an object orientated system on a functional programming language.
It only requires a nested hash table.

用function模拟类

注意这里有传送function并存在一个DICT的用法

不太同意。
有些负面情绪没必要去认同，就像阑尾一样，得想办法切掉或回避。
而且不认同的结果也不一定会是孤愤，投毒，空虚。

下面是装ability时间：

”人生就像钟摆，一边是痛苦，一边是无聊，而痛苦总比无聊好”

叔本华和楼主（按我的理解）是这样认为。

“把人们引向艺术和科学最强烈的动机之一，是要逃避日常生活中令人厌恶的粗俗和使人绝望的沉闷，这些人把和谐的世界及其构造当作他们感情生活的支点，以便获得他在狭隘的个人经验里找不到的宁静和安定”

爱因斯坦这样说。"""


def Cls(cls=None, **key):
    """ making a new class"""
    key['class'] = cls
    return key

def new(cls, **key):
    """ making an instance """
    key['class'] = cls
    return key


def geta(obj, attr):
    """ getting the attribute of object """
    if attr in obj:
        return obj[attr]
    elif(obj['class']):
        return geta(obj['class'], attr)
    else:
        return None

def tell(obj, method, *av):
    """ tell object do something"""
    fun=geta(obj, method)
    if callable(fun):
        return fun(obj, *av)

if __name__=='__main__':

    def it_work(self, n):
        """This funciton demonstrates how IT engineers work.
           Notice that arguments of thie function is identical to the method 'work' in workers.py"""

        if geta(self, 'position') == 'web creator':
            w = 'makes web site'
        elif geta(self, 'position') == 'server administrator':
            w = 'checks the trafic'
        elif geta(self, 'position') == 'programmer':
            w = 'writes programs'

        print '%s %s for %d, hours using %s on %s' %(geta(self, 'name'), w, n, geta(self, 'language'), geta(self, 'OS'))

    workers = Cls() # dummy class    
    it_workers = Cls(workers, OS='winNT', work=it_work) # class of IT workers    

    henley = new(it_workers, language='PHP', name='henley',    
                 position='web creator', email='henley@livegate.com', age=32, salary=700)    
    thomas = new(it_workers, language='Python', name='Thomas',    
                 position='server administrator', email='thomas@livegate.com', age=37, salary=900)    
    gates  = new(it_workers, language='C', name='Gates',    
                 position='programmer', email='gates@livegate.com', age=42, salary=1200)    
    henley['OS'] = 'Mac'    
    thomas['OS'] = 'Linux'    
    print henley
    tell(henley, 'work', 8)    
    tell(thomas, 'work', 7)    
    tell(gates, 'work', 10)
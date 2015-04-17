# encoding: utf-8 
'''
Created on 2013年11月29日

@author: NOAH
'''
import re

def doWithLog(filePath):
    f = open(filePath)
    fto = open("./logRes.log", "w")
    lines = f.readlines();
    for line in lines:
        destStr=""
        if re.search(r"^java.util.concurrent.ExecutionException:.*172.20.1.\d\d:60020", line):
            ip = re.findall(r"172.20.1.\d\d:60020", line)[0]
            print ip
            destStr += ip
        if re.match(r"^2013-11-2\d\s\d\d:\d\d:\d\d,\d\d\d", line):
            date = re.findall(r"^2013-11-2\d\s\d\d:\d\d:\d\d,\d\d\d", line)[0]
            print date
            destStr +="--"+date+'\n'
        fto.write(destStr)
    
    DPI scale: 1
startup, version: 3083 windows x32 channel: stable
executable: /D/develop tools/Sublime Text 3/sublime_text.exe
working dir: /D/develop tools/Sublime Text 3
packages path: /C/Users/Dell/AppData/Roaming/Sublime Text 3/Packages
state path: /C/Users/Dell/AppData/Roaming/Sublime Text 3/Local
zip path: /D/develop tools/Sublime Text 3/Packages
zip path: /C/Users/Dell/AppData/Roaming/Sublime Text 3/Installed Packages
ignored_packages: ["Vintage"]
pre session restore time: 0.134986
startup time: 0.190986
first paint time: 0.200986
reloading plugin Default.block
reloading plugin Default.comment
reloading plugin Default.copy_path
reloading plugin Default.delete_word
reloading plugin Default.detect_indentation
reloading plugin Default.duplicate_line
reloading plugin Default.echo
reloading plugin Default.exec
reloading plugin Default.fold
reloading plugin Default.font
reloading plugin Default.goto_line
reloading plugin Default.history_list
reloading plugin Default.indentation
reloading plugin Default.kill_ring
reloading plugin Default.mark
reloading plugin Default.new_templates
reloading plugin Default.open_context_url
reloading plugin Default.open_file_settings
reloading plugin Default.open_in_browser
reloading plugin Default.pane
reloading plugin Default.paragraph
reloading plugin Default.paste_from_history
reloading plugin Default.quick_panel
reloading plugin Default.save_on_focus_lost
reloading plugin Default.scroll
reloading plugin Default.set_unsaved_view_name
reloading plugin Default.side_bar
reloading plugin Default.sort
reloading plugin Default.swap_line
reloading plugin Default.switch_file
reloading plugin Default.symbol
reloading plugin Default.transform
reloading plugin Default.transpose
reloading plugin Default.trim_trailing_white_space
reloading plugin CSS.css_completions
reloading plugin Diff.diff
reloading plugin HTML.encode_html_entities
reloading plugin HTML.html_completions
reloading plugin 0_package_control_loader.00-package_control
reloading plugin 0_package_control_loader.02-bz2
reloading plugin BracketHighlighter.bh_core
reloading plugin BracketHighlighter.bh_logging
reloading plugin BracketHighlighter.bh_plugin
reloading plugin BracketHighlighter.bh_regions
reloading plugin BracketHighlighter.bh_remove
reloading plugin BracketHighlighter.bh_rules
reloading plugin BracketHighlighter.bh_search
reloading plugin BracketHighlighter.bh_swapping
reloading plugin BracketHighlighter.bh_wrapping
reloading plugin BracketHighlighter.ure
reloading plugin DocBlockr.__init__
reloading plugin DocBlockr.jsdocs
reloading plugin Emmet.emmet-plugin
reloading plugin Package Control.bootstrap
reloading plugin Package Control.Package Control
reloading plugin SideBarEnhancements.SideBar
reloading plugin SideBarEnhancements.SideBarAPI
reloading plugin SideBarEnhancements.SideBarDefaultDisable
reloading plugin Theme - Glacier.events
reloading plugin Themr.themr
reloading plugin ConvertToUTF8.ConvertToUTF8
reloading plugin Markdown Slideshow.MarkdownSlideshow
reloading plugin Pylinter.multiconf
reloading plugin Pylinter.pylinter
reloading plugin SublimeCodeIntel.ordereddict
reloading plugin SublimeCodeIntel.SublimeCodeIntel
plugins loaded
 - PyLinter: Pylint executable *not* found
 - PyLinter: Seaching for lint.py module...
error: Pylinter could not automatically determined the path to `lint.py`.

Please provide one in the settings file using the `pylint_path` variable.

NOTE:
If you are using a Virtualenv, the problem might be resolved by launching Sublime Text from correct Virtualenv.
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 158, in on_api_ready
    m.plugin_loaded()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 78, in plugin_loaded
    PYLINT_VERSION = PylSet.get_lint_version()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 239, in get_lint_version
    command = list(DEFAULT_PYLINT_COMMAND)
TypeError: 'NoneType' object is not iterable
PyV8: Creating new thread
Emmet: Creating thread
Emmet: Loading https://api.github.com/repos/emmetio/pyv8-binaries/contents
Emmet: Loading PyV8 binary from https://raw.github.com/emmetio/pyv8-binaries/master/pyv8-win32-p3.zip
Package Control: Skipping automatic upgrade, last run at 2015-04-17 14:07:52, next run at 2015-04-17 15:07:52 or after
+ Info: processing `Python': please wait...
Could not import subprocess32 module, falling back to subprocess module
current triggername: 'python-complete-object-members'
current triggername: 'python-complete-object-members'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\toCamal.py"
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Detected UTF-8 vs UTF-8 with 99% confidence
Detected UTF-8 vs UTF-8 with 88% confidence
reloading Packages/User/Preferences.sublime-settings
reloading Packages/User/Preferences.sublime-settings
reloading Packages/User/Preferences.sublime-settings
unknown include #documentation
unknown include #documentation
unknown include #documentation
unknown include #documentation
unknown include #documentation
unknown include #documentation
unknown include #documentation
unknown include #documentation
unknown include #documentation
Detected UTF-8 vs UTF-8 with 99% confidence
Detected UTF-8 vs UTF-8 with 99% confidence
Detected UTF-8 vs UTF-8 with 99% confidence
Detected UTF-8 vs UTF-8 with 99% confidence
Unable to extract text from the clipboard, available formats: DataObject, Shell IDList Array, DataObjectAttributes, DataObjectAttributesRequiringElevation, Shell Object Offsets, Preferred DropEffect, AsyncFlag, CF_HDROP, FileName, FileNameW, Ole Private Data
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Detected UTF-8 vs UTF-8 with 99% confidence
Running python -u "D:\thirdparty\PythonEx\Tools\conf_utils.py"
Running python -u "D:\thirdparty\PythonEx\Tools\conf_utils.py"
Detected ASCII vs Undefined with 100% confidence
Running python -m py_compile "D:\thirdparty\PythonEx\Tools\conf_utils.py"
Running python -m py_compile "D:\thirdparty\PythonEx\Tools\conf_utils.py"
Running python -m py_compile "D:\thirdparty\PythonEx\Tools\conf_utils.py"
Running python -u "D:\thirdparty\PythonEx\Tools\conf_utils.py"
Detected ASCII vs Undefined with 100% confidence
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\conf_utils.py"
Running python -u "D:\thirdparty\PythonEx\Tools\conf_utils.py"
Running python -u "D:\thirdparty\PythonEx\Tools\conf_utils.py"
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Detected ASCII vs Undefined with 100% confidence
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-object-members'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-object-members'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-object-members'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-object-members'
current triggername: 'python-calltip-call-signature'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-complete-literal-members'
current triggername: 'python-calltip-call-signature'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-available-imports'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-object-members'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\toCamal.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\toCamal.py"
current triggername: 'python-complete-object-members'
current triggername: 'python-calltip-call-signature'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\toCamal.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\toCamal.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-complete-object-members'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-object-members'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-calltip-call-signature'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-calltip-call-signature'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
current triggername: 'python-calltip-call-signature'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
current triggername: 'python-complete-local-symbols'
current triggername: 'python-calltip-call-signature'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-calltip-call-signature'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-complete-object-members'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
current triggername: 'python-complete-local-symbols'
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED False
reloading Packages/User/Preferences.sublime-settings
reloading Packages/User/Preferences.sublime-settings
reloading Packages/User/Preferences.sublime-settings
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
reloading Packages/User/Preferences.sublime-settings
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Running python -u "D:\thirdparty\PythonEx\Tools\db_tool.py"
reloading Packages/User/Preferences.sublime-settings
Detected ASCII vs Undefined with 100% confidence
Detected UTF-8 vs UTF-8 with 99% confidence
Detected UTF-8 vs UTF-8 with 99% confidence
Detected UTF-8 vs UTF-8 with 99% confidence
Detected ASCII vs Undefined with 100% confidence
Detected ASCII vs Undefined with 100% confidence
Detected ASCII vs Undefined with 100% confidence
Detected ASCII vs Undefined with 100% confidence
Detected UTF-8 vs UTF-8 with 99% confidence
Detected ASCII vs Undefined with 100% confidence
Running python -u "D:\thirdparty\PythonEx\AI\NqueenViolent.py"
Detected UTF-8 vs UTF-8 with 99% confidence
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED False
ignored packages updated to: ["Vintage", "GitGutter"]
reloading Packages/User/Package Control.sublime-settings
reloading Packages/User/Preferences.sublime-settings
reloading Packages/User/Package Control.sublime-settings
ignored packages updated to: ["Vintage"]
reloading plugin GitGutter.git_gutter
reloading plugin GitGutter.git_gutter_change
reloading plugin GitGutter.git_gutter_compare
reloading plugin GitGutter.git_gutter_events
reloading plugin GitGutter.git_gutter_handler
reloading plugin GitGutter.git_helper
reloading Packages/GitGutter/GitGutter.sublime-settings
reloading plugin GitGutter.view_collection
reloading Packages/User/Package Control.sublime-settings
reloading Packages/User/Preferences.sublime-settings
reloading Packages/User/Preferences.sublime-settings
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED False
ignored packages updated to: ["Vintage", "SideBarGit"]
reloading Packages/User/Package Control.sublime-settings
reloading Packages/User/Preferences.sublime-settings
reloading Packages/User/Package Control.sublime-settings
ignored packages updated to: ["Vintage"]
reloading plugin SideBarGit.SideBarGitCommands
reloading plugin SideBarGit.StatusBarBranch
Exception in thread Thread-347:
Traceback (most recent call last):
  File "./threading.py", line 901, in _bootstrap_inner
  File "sidebar.SideBarGit in C:\Users\Dell\AppData\Roaming\Sublime Text 3\Installed Packages\SideBarGit.sublime-package", line 49, in run
  File "sidebar.SideBarGit in C:\Users\Dell\AppData\Roaming\Sublime Text 3\Installed Packages\SideBarGit.sublime-package", line 142, in run2
NameError: global name 'path_to_git_unixes' is not defined

reloading Packages/User/Package Control.sublime-settings
reloading Packages/User/Preferences.sublime-settings
reloading Packages/User/Preferences.sublime-settings
Detected UTF-8 vs UTF-8 with 99% confidence
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED True
WINDOW COMMAND ENABLED False
Detected ASCII vs Undefined with 100% confidence
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
reloading Packages/Pylinter/Pylinter.sublime-settings
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable
Traceback (most recent call last):
  File "D:\develop tools\Sublime Text 3\sublime_plugin.py", line 556, in run_
    return self.run(edit)
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 273, in run
    settings = PylSet.read_settings()
  File "C:\Users\Dell\AppData\Roaming\Sublime Text 3\Packages\Pylinter\pylinter.py", line 151, in read_settings
    if PYLINT_VERSION[0] != 0:
TypeError: 'NoneType' object is not subscriptable


if __name__ == '__main__':
    testStr = "java.util.concurrent.ExecutionException: java.net.SocketTimeoutException: Call to datanode03/172.20.1.13:60020 failed on socket timeout exception: java.net.SocketTimeoutException: 60000 millis timeout while waiting for channel to be ready for read. ch : java.nio.channels.SocketChannel[connected local=/172.20.1.106:23833 remote=datanode03/172.20.1.13:60020]"
    print re.search(r"172.20.1.\d\d", testStr)
    print re.findall(r"172.20.1.\d\d", testStr)
    doWithLog("logTo.log")
    pass

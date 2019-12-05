from loger import makelog

print('\n基础输出\nbasic output:')
makelog('this is a log')


print('\n预设的输出等级是3 （inf），你可以在输出时设置level为1-4（error warning info scuess）\ndefault log level is 3 （info）,you can set 1-4 (error warning info scuess) to level to change it')
makelog('this is a error， level=1', level=1)
makelog('this is a warning， level=2', level=2)
makelog('this is a infor， level=3', 3)
makelog('this is a scuess，level=4', 4)

print('\n使用 setting 可以控制 更改loger的设置。\n use setting can change loger default setting')
from loger import setting
print('\n控制输出级别\nchange output level：')
setting(logerLevel=2)
makelog('this error will show', 1)
makelog('this is a will show', 2)
makelog('this infor will not show', 3)
makelog('this scuess will not show', 4)

print('\n使用时间戳\noutput with time mark：')
setting(logerTimeMark=True)
makelog('this is a error with time mark', 1)
makelog('this is a warning with time mark', 2)

print('\n禁用颜色输出\noutput without color：')
setting(logerColor=False)
makelog('this is a error without color', 1)
makelog('this is a warning without color', 2)

print('\n将日志输出到文件\noutput to file：')
setting(logerOutputFile='loger.log')
makelog('this is a error output to file', 1)
makelog('this is a warning output to file', 2)
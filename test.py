from loger import log, loger_setting

print('\n* 基础输出\nbasic output:')
log('this is a log')

print('\n* 预设的输出等级是3 （inf），你可以在输出时设置level为1-4（error warning info success）\ndefault log level is 3 （info）,you can set 1-4 (error warning info success) to level to change it')
log('this is a error， level=1', level=1)
log('this is a warning， level=2', level=2)
log('this is a information， level=3', 3)
log('this is a success，level=4', 4)

print('\n* 使用 setting 可以控制 更改loger的设置。\n use setting can change loger default setting')

print('\n* 控制输出级别\nchange output level：')
loger_setting(show_level=2)
log('this error will show', 1)
log('this is a will show', 2)
log('this information will not show', 3)
log('this success will not show', 4)


print('\n* 使用时间戳\noutput with time mark：')
loger_setting(time_mark=True)
log('this is a error with time mark', 1)
log('this is a warning with time mark', 2)

print('\n* 禁用颜色输出\noutput without color：')
loger_setting(color=False)
log('this is a error without color', 1)
log('this is a warning without color', 2)

print('\n* 将日志输出到文件\noutput to file：')
loger_setting(file_path='./loger.log')
log('this is a error output to file', 1)
log('this is a warning output to file', 2)

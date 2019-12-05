# loger
loger 可以轻松控制你的log打印和输出
loger can easily control your log printing and sveing 
##  安装 install 

```
pip install loger
```
## 使用

下载并运行./test.py 其中包含了loger的日常用法

1. import 

    ```
    from loger import makelog
    ```

2. 基础输出，basic output:
   ```
   makelog('this is a log')
   ```

3. 预设的输出等级是3 （inf），你可以在输出时设置level为1-4（error warning info scuess） default log level is 3 （info）,you can set 1-4 (error warning info scuess) to level to change it。
   ```
   makelog('this is a error， level=1', level=1)
   makelog('this is a warning， level=2', level=2)
   makelog('this is a infor， level=3', 3)
   makelog('this is a scuess，level=4', 4)
   ```

4. 使用 setting 可以控制 更改loger的设置。 use setting can change loger default setting。
   
   ```
    from loger import setting
   ```
5. 控制输出级别 change output level：
   ```
   setting(logerLevel=2)
   makelog('this error will show', 1)
   makelog('this is a will show', 2)
   makelog('this infor will not show', 3)
   makelog('this scuess will not show', 4)
   ```

6. 使用时间戳 output with time mark：

   ```
   setting(logerTimeMark=True)
   makelog('this is a error with time mark', 1)
   makelog('this is a warning with time mark', 2)
   ```

7. 禁用颜色输出 output without color：
   ```
   setting(logerColor=False)
   makelog('this is a error without color', 1)
   makelog('this is a warning without color', 2)
   ```

8. 将日志输出到文件 output to file：
   ```
   setting(logerOutputFile='loger.log')
   makelog('this is a error output to file', 1)
   makelog('this is a warning output to file', 2)
   ```
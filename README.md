# [UNMAINTAINED] [KHÔNG TIẾP TỤC CẬP NHẬP] MCQs assistant for SHub Classroom
TIẾNG VIỆT
------
Hướng dẫn tiếng Việt tại [đây](https://github.com/ngpnam261/shub_mcq_assistant/issues/1#issuecomment-614432741).

Disclaimer
------

I do not endorse using this to cheat on your tests

How to use
------

First, make sure you have Chrome and ChromeDriver installed properly, please refer to this [link](https://chromedriver.chromium.org/getting-started). (If you are on Windows, you can extract `chromedriver.exe` to `C:\Windows\`)\
Then, open config.ini and enter your username, password, class code, test number.


A typical SHub test url look like this: `https://shub.edu.vn/class/ABCDE/homework/12345/test` where `ABCDE` is the class code and `12345` is the test number
```
[ACCOUNT]
Username = taikhoanphu
Password = 123
[TEST]
ClassCode = ABCDE
TestNumber = 12345
```
**Please note:** Your account must have already joined in the class which contains the test that you want to get answers from.

**WARNING:** Do not use your main account as running this script will use your first take of the test and leave the record on SHub server.

Configurations
------

In config.ini, under `[SETTINGS]` section, you can change the csv file name.\
`KeyFileName = key.csv`\
You can also change the pause time (in seconds) between each reload.\
`SleepTime = 1`

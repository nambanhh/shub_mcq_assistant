# MCQs assistant for SHub Classroom

Disclaimer
------

I do not endorse using this to cheat on your tests

How to use
------

First, make sure you have Chrome and ChromeDriver installed properly, please refer to this [link](https://chromedriver.chromium.org/getting-started).\
Then, open config.ini and enter your username, password, class code, test number.


A typical SHub test url is like this: `https://shub.edu.vn/class/RDMEA/homework/91791/test` where `RMDEA` is the class code and `91791` is the test number
```
[ACCOUNT]
Username = <enter your SHub username>
Password = <enter your SHub password>
[TEST]
ClassCode = <enter your class code>
TestNumber = <enter your test number>
```
**Please note:** Your account must have already joined in the class which contains the test that you want to get answers from.

**WARNING:** Do not use your main account as running this script will use your first take of the test and leave the record on SHub server.

Configurations
------

In config.ini, under `[SETTINGS]` section, you can change the csv file name.\
`KeyFileName = key.csv`\
You can also change the pause time (in seconds) between each reload.\
`SleepTime = 1`

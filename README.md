# MCQs assistant for SHub Classroom

How to use
------

First, make sure you have Chrome and ChromeDriver installed correctedly, please follow this [link](https://chromedriver.chromium.org/getting-started).\
Open config.ini and enter your username, password, class code, test number.
```
[ACCOUNT]
Username = <enter your SHub username>
Password = <enter your SHub password>
[TEST]
ClassCode = <enter your class code>
TestNumber = <enter your test number>
```
**WARNING:** Your account must have already joined in the class which contains the test that you want to get answers from.

Configurations
------

In config.ini, under `[SETTINGS]` section, you can change the csv file name.\
`KeyFileName = key.csv`\
You can also change the pause time (in seconds) between each reload.\
`SleepTime = 1`

"""
9.4 项目：将带有美国风格日期的文件改名为欧洲风格日期
假定你的老板用电子邮件发给你上千个文件，文件名包含美国风格的日期
（MM-DD-YYYY），需要将它们改名为欧洲风格的日期（DD-MM-YYYY）。手工 完
成这个无聊的任务可能需要几天时间！让我们写一个程序来完成它。
下面是程序要做的事：
• 检查当前工作目录的所有文件名，寻找美国风格的日期。
• 如果找到，将该文件改名，交换月份和日期的位置，使之成为欧洲风格。
这意味着代码需要做下面的事情：
• 创建一个正则表达式，可以识别美国风格日期的文本模式。
• 调用 os.listdir()，找出工作目录中的所有文件。
• 循环遍历每个文件名，利用该正则表达式检查它是否包含日期。
• 如果它包含日期，用 shutil.move()对该文件改名
"""

import shutil
import os
import re

datePattern = re.compile(r"""
    ^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
""", re.VERBOSE)


for amerFilename in os.listdir("."):
    mo = datePattern.search(amerFilename)

    if mo is None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    array = [beforePart, dayPart, monthPart, yearPart, afterPart]

    euroFilename = '-'.join([el for el in array if el != ''])

    absWorkingPath = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingPath, amerFilename)
    euroFilename = os.path.join(absWorkingPath, euroFilename)

    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)

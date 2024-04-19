"""
regex
"""

import re
import pyperclip


def isPhoneNumber(text):
    """
    假设你希望在字符串中查找电话号码。你知道模式：3个数字，一个短横线，
    3个数字，一个短横线，再是4个数字。例如：415-555-4242。

    search()将返回一个 Match 对象，包含被查找字符串中的“第一次”匹配的文本
    """
    reg = re.compile('[0-9]{3,4}')
    return bool(reg.search(text))


print(isPhoneNumber('415-555-5555'))
print(isPhoneNumber('(415)-555-5555'))
print(isPhoneNumber('415.555.5555'))


def numberGroup(text):
    """
    假设你希望在字符串中查找电话号码。你知道模式：3个数字，一个短横线，
    3个数字，一个短横线，再是4个数字。例如：415-555-4242。
    使用 group()，从一个分组中获取匹配的文本
    使用groups(),获取所有分组
    """
    reg = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d)')
    return reg.search(text)


mo = numberGroup('(415) 555-5555')
print(mo.group(1))
print(mo.group(2))


def textPipe(text):
    """
    字符|称为“管道”。希望匹配许多表达式中的一个时，就可以使用它
    """
    reg = re.compile(r'Batman|Tina Fey')
    return reg.search(text)


mo1 = textPipe('Tina Fey and Batman')
print(mo1.group())


def textPipeMulti(text):
    reg = re.compile(r'Bat(man|mobile|copter|bat)')
    return reg.search(text)


mo2 = textPipeMulti('Batmobile lost a wheel')
print(mo2.group())
print(mo2.group(1))


def isFileType(file_type):
    reg = re.compile(r'png|jpg|jpeg|bmp|gif')
    return bool(reg.search(file_type))


print(isFileType('png'))
print(isFileType('jpg'))
print(isFileType('jpeg'))
print(isFileType('py'))


def commandInstall(text):
    """字符?表明它前面的分组在这个模式中是可选的"""
    reg = re.compile(r'npm i(ntsall)?')
    return bool(reg.search(text))


print(commandInstall('npm i'))
print(commandInstall('npm install'))


def commandLoop(text):
    """匹配零次或多次"""
    reg = re.compile(r'Bat(wo)*man')
    return reg.search(text)


m3 = commandLoop('Batman')
m4 = commandLoop('Batwoman')
m5 = commandLoop('Batwowowowoman')
print(m3.group())
print(m4.group())
print(m5.group())


def commandLoopMulti(text):
    """匹配一次或多次"""
    reg = re.compile(r'Bat(wo)+man')
    return reg.search(text)


m6 = commandLoop('Batman')
m7 = commandLoop('Batwoman')
m8 = commandLoop('Batwowowowoman')
print(m6.group())
print(m7.group())
print(m8.group())

# findall()方法将返回一组字符串，包含被查找字符串中的所有匹配
mo9 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
print(mo9.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# 7.5
# 假设你有一个无聊的任务，要在一篇长的网页或文章中，找出所有电话号码和
# 邮件地址。如果手动翻页，可能需要查找很长时间。如果有一个程序，可以在剪贴
# 板的文本中查找电话号码和 E-mail 地址，那你就只要按一下 Ctrl-A 选择所有文本，
# 按下 Ctrl-C 将它复制到剪贴板，然后运行你的程序。它会用找到的电话号码和 E-mail
# 地址，替换掉剪贴板中的文本。
# 当你开始接手一个新项目时，很容易想要直接开始写代码。但更多的时候，最
# 好是后退一步，考虑更大的图景。我建议先草拟高层次的计划，弄清楚程序需要做
# 什么。暂时不要思考真正的代码，稍后再来考虑。现在，先关注大框架。
# 例如，你的电话号码和 E-mail 地址提取程序需要完成以下任务：
# 从剪贴板取得文本。
# 找出文本中所有的电话号码和 E-mail 地址。
# 将它们粘贴到剪贴板。
# 现在你可以开始思考，如何用代码来完成工作。代码需要做下面的事情：
# 使用 pyperclip 模块复制和粘贴字符串。
# 创建两个正则表达式，一个匹配电话号码，另一个匹配 E-mail 地址。
# 对两个正则表达式，找到所有的匹配，而不只是第一次匹配。
# 将匹配的字符串整理好格式，放在一个字符串中，用于粘贴。
# 如果文本中没有找到匹配，显示某种消息
# 13212344321
# 17232343424
# 15623442498
# info@nostarch.com
# media@nostarch.com
# academic@nostarch.com
# help@nostarch.com


phoneRegex = re.compile(r'1[3-9]\d+')
emailRegex = re.compile(r'\w+@\w+\.com')

text = str(pyperclip.paste())

matches = []

for match in phoneRegex.finditer(text):
    matches.append('* ' + match[0])

for match in emailRegex.finditer(text):
    matches.append('* ' + match[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('\n'.join(matches))
else:
    print('No matches found.')

mo10 = re.compile(r'(?<=of)\W+')
with open('./test/test1.txt', 'r') as file:
    content = file.read()

newContent = re.sub(mo10, ' ', content)
with open('./test/test1.txt', 'w') as file:
    file.write(newContent)


def strongPwd(pwd):
    """长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字"""
    # reg = re.compile(r'([a-z]+[A-Z]+[0-9]+){8,}')
    reg = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}')
    return bool(re.search(reg, pwd))


print(strongPwd('123112414412As'))
print(strongPwd('A13awerwr23'))

numRegex = re.compile(r'''
    \d+     # number
''', re.VERBOSE)

newContent = numRegex.sub('*', '12 drummers, 11 pipers, five rings, 3 hens')
print(newContent)


def numberMatch(number):
    """
    匹配每 3 位就有一个逗号的数字
    必须匹配以下数字：
    '42'
    '1,234'
    '6,368,745'
    但不会匹配：
    '12,34,567' （逗号之间只有两位数字）
    '1234' （缺少逗号）
    """
    reg = re.compile(r'^\d{1,3}(?:,\d{3})*$')
    return bool(reg.search(number))


print(numberMatch('42'))
print(numberMatch('1,234'))
print(numberMatch('6,368,745'))
print(numberMatch('12,34,567'))
print(numberMatch('1234'))


def nameMatch(name):
    """
    假定名字总是出现在姓前面，是一个大写字母开头的单词
    必须匹配
    'Satoshi Nakamoto'
    'Alice Nakamoto'
    'RoboCop Nakamoto'
    但不匹配：
    'satoshi Nakamoto'（名字没有大写首字母）
    'Mr. Nakamoto'（前面的单词包含非字母字符）
    'Nakamoto' （没有名字）
    'Satoshi nakamoto'（姓没有首字母大写）
    """
    reg = re.compile(r'''
    ^
    [A-Z]
    [a-z]*
    (?:\s[A-Z][a-z]*)*    # 非捕获分组，匹配一个空格后跟着一个以大写字母开头的单词，可以重复零次或多次。
    \s
    [A-Z][a-z]*
    $
    ''', re.VERBOSE)
    return bool(reg.search(name))


print('--------')
print(nameMatch('Satoshi Nakamoto'))
print(nameMatch('Alice Nakamoto'))
print(nameMatch('RoboCop Nakamoto'))

print(nameMatch('satoshi Nakamoto'))
print(nameMatch('Mr. Nakamoto'))
print(nameMatch('Nakamoto'))
print(nameMatch('Satoshi nakamoto'))


def wordMatch(word):
    """
    第一个词是 Alice、Bob 或Carol，
    第二个词是 eats、pets 或 throws，
    第三个词是 apples、cats 或 baseballs。
    该句子以句点结束。这个正则表达式应该不区分大小写。它必须匹配：
    'Alice eats apples.'
    'Bob pets cats.'
    'Carol throws baseballs.'
    'Alice throws Apples.'
    'BOB EATS CATS.'
    但不匹配：
    'RoboCop eats apples.'
    'ALICE THROWS FOOTBALLS.'
    'Carol eats 7 cats.'
    """
    reg = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$', re.IGNORECASE)
    return bool(reg.search(word))


print('-------------------')
print(wordMatch('Alice eats apples.'))
print(wordMatch('Bob pets cats.'))
print(wordMatch('Carol throws baseballs.'))
print(wordMatch('Alice throws Apples.'))
print(wordMatch('BOB EATS CATS.'))

print(wordMatch('RoboCop eats apples.'))
print(wordMatch('ALICE THROWS FOOTBALLS.'))
print(wordMatch('Carol eats 7 cats.'))


def strip(strs, chars=None):
    """
    写一个函数，它接受一个字符串，做的事情和 strip()字符串方法一样。如果只
    传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。
    否则，函数第二个参数指定的字符将从该字符串中去除。
    """
    if chars is None:
        return re.sub(r'^\s+|\s+$', '', strs)
    return re.sub(rf'^[{chars}]+|[{chars}]+$', '', strs)


print(strip(' Alice eats apples '))
print(strip('** & Alice eats apples & **', '*'))


"""
regex
"""

import re


def isPhoneNumber(text):
    """
    假设你希望在字符串中查找电话号码。你知道模式：3个数字，一个短横线，
    3个数字，一个短横线，再是4个数字。例如：415-555-4242。
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

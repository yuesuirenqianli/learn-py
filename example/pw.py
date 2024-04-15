"""
6.3 口令保管箱
你可能在许多不同网站上拥有账号，每个账号使用相同的口令是个坏习惯。如
果这些网站中任何一个有安全漏洞，黑客就会知道你所有的其他账号的口令。最好
是在你的计算机上，使用口令管理器软件，利用一个主控口令，解锁口令管理器。
然后将某个账户口令拷贝到剪贴板，再将它粘贴到网站的口令输入框
"""
import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}


if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - coy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

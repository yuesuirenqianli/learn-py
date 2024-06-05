"""
    10.2
"""

import traceback


def spam():
    bacon()


def bacon():
    try:
        raise Exception('This is the error message.')
    except:
        errorFile = open('error.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written to errorInfo.txt.')


spam()


podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = "I\'m sorry, Dave. I\'m afraid I can't do that.'"
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'


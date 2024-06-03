import random


arr = random.sample(range(1, 101), 10)


for i in arr:
    open('./numbers/spam_' + str(i) + '.txt', 'w').write(str(i))

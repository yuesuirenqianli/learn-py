# 8.5 项目：生成随机的测验试卷文件
# 假如你是一位地理老师，班上有 35 名学生，你希望进行美国各州首府的一个
# 小测验。不妙的是，班里有几个坏蛋，你无法确信学生不会作弊。你希望随机调整
# 问题的次序，这样每份试卷都是独一无二的，这让任何人都不能从其他人那里抄袭
# 答案。当然，手工完成这件事又费时又无聊。好在，你懂一些 Python。
# 下面是程序所做的事：
# • 创建 35 份不同的测验试卷。
# • 为每份试卷创建 50 个多重选择题，次序随机。
# • 为每个问题提供一个正确答案和 3 个随机的错误答案，次序随机。
# • 将测验试卷写到 35 个文本文件中。
# • 将答案写到 35 个文本文件中。
# 这意味着代码需要做下面的事：
# • 将州和它们的首府保存在一个字典中。
# • 针对测验文本文件和答案文本文件，调用 open()、write()和 close()。
# • 利用 random.shuffle()随机调整问题和多重选项的次序

import random
import asyncio

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


async def generate_quiz(quizNum):
    quizFile = open('./test/test%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('./test/test_answer%s.txt' % (quizNum + 1), 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write('%s. What is the capital of  %s? \n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))

        quizFile.write('\n')
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()


async def main():
    task = [generate_quiz(quizNum) for quizNum in range(35)]
    await asyncio.gather(*task)


if __name__ == '__main__':
    asyncio.run(main())

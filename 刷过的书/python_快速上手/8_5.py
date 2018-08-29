#python3
#随机生成试卷和答案
import random
#正确答案
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
#生成35份
for quizNum in range(35):
	#生成考卷
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1),'w')
	#生成考卷答案
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1),'w')
    #向考卷中写入名称、日期、阶段
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    #将正确答案中的键生成一个列表states
    states = list(capitals.keys())
    #随机打乱states列表的顺序
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.
    #35份考卷，每份考卷50个题
    for questionNum in range(50):
    # Get right and wrong answers.
    #states[1]随机获取一个state的一个值，也相当于capitals中的一个键
    #capitals[states[1]]等于一个capitals中的一个值
        correctAnswer = capitals[states[questionNum]]
    #list(capitals.values())将错误答案生成一个列表
    #wrongAnswers是一个50项 值的列表
        wrongAnswers = list(capitals.values())
    #wrongAnswers.index(correctAnswer)
    #将正确答案从错误列表中删除
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
    #随机从错误答案中选取3个作为错误答案选项
        wrongAnswers = random.sample(wrongAnswers, 3)
    #答案选项等于错误答案+上争取答案
    #不明白为什么正确答案要用[],两个列表相加 
        answerOptions = wrongAnswers + [correctAnswer]
    #打乱答案选项
        random.shuffle(answerOptions)
    # Write the question and the answer options to the quiz file.
    #写入问题的描述
    #questionNum + 1 问题序号
    #states[questionNum] 州
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,states[questionNum]))
    #问题有四个选项    
        for i in range(4):
    #选项格式写入，A.四个选项之一        
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
    #换行
        quizFile.write('\n')
    # Write the answer key to a file.
    #往答案文件写入正确答案
    #'ABCD'[answerOptions.index(correctAnswer)
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
            answerOptions.index(correctAnswer)]))
    #关闭考卷和答案文件，开始写下一个
    quizFile.close()
    answerKeyFile.close()
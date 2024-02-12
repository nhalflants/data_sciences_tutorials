import os

dir_path = os.path.dirname(os.path.abspath(__file__))
questions_file_path = os.path.join(dir_path, 'questions.txt')

quizz = open(questions_file_path, 'r')
questions = [question.strip().split('=') for question in quizz.readlines()]
quizz.close()

correct_answer = 0
for question in questions:
    print(f'{question[0]}=')
    answer = int(input('Answer: '))
    if answer == int(question[1]):
        correct_answer += 1

result_file = open('result.txt', 'w')
result_file.write(f'Your final score is {correct_answer}/{len(questions)}')
result_file.close()
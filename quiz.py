import datetime
import random

from questions import Add, Subtract, Multiply, Divide


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        question_types = (Add, Subtract, Multiply, Divide)

        for _ in range(10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2)
            self.questions.append(question)

    def take_quiz(self):
        self.starttime = datetime.datetime.now()

        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.endtime = datetime.datetime.now()
        return self.summary()

    def ask(self, question):
        correct = False
        question_start = datetime.datetime.now()
        answer = input(question.text + ' = ')

        if answer == str(question.answer):
            correct = True

        question_end = datetime.datetime.now()
        return correct, question_end - question_start

    def total_correct(self):
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1

    def summary(self):
        print(
            f'You got {self.total_correct()} out of {len(self.questions)} right.')

        print(
            f'The quiz took you {self.endtime-self.starttime} seconds total.')


Quiz().take_quiz()

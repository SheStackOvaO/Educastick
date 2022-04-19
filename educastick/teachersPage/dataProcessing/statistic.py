from django.shortcuts import render

from teachersPage import models
from teachersPage import forms
from django.views.generic.edit import CreateView
import matplotlib.pyplot as plt

def getModule():
    answer = models.Answer.objects.first()
    return answer.test


def abStatistic():
    # Добавить айди препода и группы и проверку относительно их
    answers = models.Answer.objects.all()
    teacher = models.Teacher.objects.get(pk=1)
    students = models.Student.objects.all()
    unbalancing = teacher.unbalancing.split('/')
    markStud = [[] for i in range(0, len(unbalancing) + 1)]
    for answer in answers:
        for i in range(1, len(unbalancing)):
            if int(answer.score) > int(unbalancing[int(int(len(unbalancing) / 2)-1)]):
                if i != 1 and i != len(unbalancing):
                    if int(unbalancing[i - 1]) >= int(answer.score) > int(unbalancing[i - 2]):
                        markStud[i].append(answer.score)
                if i == len(unbalancing) - 1:
                    if int(answer.score) >= int(unbalancing[i]):
                        markStud[i + 1].append(answer.score)
                if i == 1:
                    if int(unbalancing[0]) >= int(answer.score):
                        markStud[i-1].append(answer.score)

    absolute = sum([(len(markStud[i])) for i in range(0, len(markStud))])*100/len(students)
    return "Абсолютная успеваемость: " + str(absolute) + " %"


def qualityStatistic():
    # Добавить айди препода и группы и проверку относительно их
    answers = models.Answer.objects.all()
    teacher = models.Teacher.objects.get(pk=1)
    students = models.Student.objects.all()
    unbalancing = teacher.unbalancing.split('/')
    markStud = [[] for i in range(0, len(unbalancing)+1)]
    for answer in answers:
        for i in range(1, len(unbalancing)):
            if int(answer.score) > int(unbalancing[int(int(len(unbalancing)/2)-1)]):
                if i != 1 and i != len(unbalancing):
                    if int(unbalancing[i - 1]) >= int(answer.score) > int(unbalancing[i - 2]):
                        markStud[i].append(answer.score)
                if i == len(unbalancing) - 1:
                    if int(answer.score) >= int(unbalancing[i]):
                        markStud[i + 1].append(answer.score)
                if i == 1:
                    if int(unbalancing[0]) >= int(answer.score):
                        markStud[i-1].append(answer.score)

    quality = sum([(len(markStud[i])) for i in range(0, len(markStud))])*100/len(students)

    return "Качественная успеваемость: " + str(quality) + " %"


def averageScore():
    # Добавить айди препода, теста и группы и проверку относительно их
    answers = models.Answer.objects.all()
    teacher = models.Teacher.objects.get(pk=1)
    unbalancing = teacher.unbalancing.split('/')
    markStud = [[] for i in range(0, len(unbalancing)+1)]
    avgStud = 0

    for answer in answers:
        for i in range(1, len(unbalancing)):
            if i !=1 and i!=len(unbalancing):
                if int(unbalancing[i-1]) >= int(answer.score) > int(unbalancing[i-2]):
                    markStud[i].append(answer.score)
            if i==len(unbalancing)-1:
                if int(answer.score) >= int(unbalancing[i]):
                    markStud[i+1].append(answer.score)
            if i == 1:
                if int(unbalancing[0]) >= int(answer.score):
                    markStud[i-1].append(answer.score)

    for i in range(0, len(markStud)):
        avgStud += (i+2)*len(markStud[i])

    return "Средний балл: " + str(avgStud/len(answers))


def minScore():
    answers = models.Answer.objects.all()

    return "min балл: " + str(min([int(answer.score) for answer in answers]))


def maxScore():
    answers = models.Answer.objects.all()

    return "max балл: " + str(max([int(answer.score) for answer in answers]))


def hardQuestion(): #Вопросы с наименьшим кол-ом правильных ответов
    # Добавить айди препода и группы и проверку относительно их
    rightAnswersSt = {'right':[],'wrong':[]}
    answers = models.Answer.objects.filter(test=2)
    rightAnswers = models.QuestionVariantAnswer.objects.filter(correctAnswer=True)


    answersSt = [answer.studentAnswer.split('/') for answer in answers]
    for i in range(0, len(answersSt)):
        for questionAnswer in range(0, len(rightAnswers)):
            if int(answersSt[i][questionAnswer]) == int(rightAnswers[questionAnswer].number):
                rightAnswersSt['right'].append(rightAnswers[questionAnswer].question.number)
            else:
                rightAnswersSt['wrong'].append(rightAnswers[questionAnswer].question.number)

    result = {}
    rasultarray = set(rightAnswersSt['wrong'])
    for question in rasultarray:
        questions = models.Question.objects.filter(number=question)[0].description
        result[question] = [questions, rightAnswersSt['wrong'].count(question)]
    return result


def chart():
    rightAnswersSt = {'right':[],'wrong':[]}
    answers = models.Answer.objects.filter(test=2)
    rightAnswers = models.QuestionVariantAnswer.objects.filter(correctAnswer=True)


    answersSt = [answer.studentAnswer.split('/') for answer in answers]
    for i in range(0, len(answersSt)):
        for questionAnswer in range(0, len(rightAnswers)):
            if int(answersSt[i][questionAnswer]) == int(rightAnswers[questionAnswer].number):
                rightAnswersSt['right'].append(rightAnswers[questionAnswer].question.number)
            else:
                rightAnswersSt['wrong'].append(rightAnswers[questionAnswer].question.number)

    result = []
    rasultarray = set(rightAnswersSt['right'])
    for question in rasultarray:
        #questions = models.Question.objects.filter(number=question)[0].description
        result.append([question, rightAnswersSt['right'].count(question)/len(answers)])
    return plt.plot(result)


def notWrite(): #Список тех, кто не писал тест
    answers = models.Answer.objects.all()
    students = models.Student.objects.all()
    return "Список тех, кто не писал тест: " + str(int(len(answers)/len(students)))


def quantityByDisassembly(): # количество по разбаловке (распередение по полученным оценкам)
    # Добавить айди препода и группы и проверку относительно их
    answers = models.Answer.objects.all()
    teacher = models.Teacher.objects.get(pk=1)
    unbalancing = teacher.unbalancing.split('/')
    balancing = []
    markStud = [[] for i in range(0, len(unbalancing) + 1)]
    for answer in answers:
        for i in range(1, len(unbalancing)):
            if i != 1 and i != len(unbalancing):
                balancing.append(unbalancing[i - 1] + '-' + unbalancing[i])
                balancing.append(unbalancing[i - 2] + '-' + unbalancing[i-1])
                if int(unbalancing[i - 1]) >= int(answer.score) > int(unbalancing[i - 2]):
                    markStud[i].append(answer.score)
            if i == len(unbalancing) - 1:
                balancing.append( '>=' + unbalancing[i])
                if int(answer.score) >= int(unbalancing[i]):
                    markStud[i + 1].append(answer.score)
            if i == 1:
                balancing.append( '<' + unbalancing[i-1])
                if int(unbalancing[0]) >= int(answer.score):
                    markStud[i-1].append(answer.score)

    return [sorted(set(balancing)), markStud] # dict(zip(markStud, set(balancing)))
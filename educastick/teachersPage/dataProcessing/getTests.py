from teachersPage import models
from teachersPage import forms
from django.views.generic.edit import CreateView


def grouping():
    array_test = models.Test.objects.all()
    result = []

    for tests in array_test:
        array_question = models.Question.objects.filter(test_id=tests.id)
        questions = {'question': []}
        for question in array_question:
            variantAnswer = {'correct': [], 'wrong': []}
            questionVariantAnswer = models.QuestionVariantAnswer.objects.filter(question_id=question.id)
            for answer in questionVariantAnswer:
                if answer.correctAnswer == True:
                    variantAnswer['correct'].append([answer.number, answer.VariantAnswer])
                else:
                    variantAnswer['wrong'].append([answer.number, answer.VariantAnswer])
            questions['question'].append([question.number, question.description, question.photo, variantAnswer])
        result.append([question.test.module, question.test.topic, question.test.module.subject, questions])

    return result


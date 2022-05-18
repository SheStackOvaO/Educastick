from teachersPage import models
from teachersPage import forms
from django.views.generic.edit import CreateView
import json


class TestClass:
    def __init__(self, idTest, module, topic, subject, questions):
        self.idTest = idTest
        self.module = module
        self.topic = topic
        self.subject = subject

        self.questions = questions or None


class TestEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, TestClass):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


def grouping():
    array_test = models.Test.objects.all()
    result = []

    for tests in array_test:
        array_question = models.Question.objects.filter(test_id=tests.id)
        questions = {'question': []}
        testId = ''
        module = ''
        topic = ''
        subject = ''
        for question in array_question:
            variantAnswer = {'correct': [], 'wrong': []}
            questionVariantAnswer = models.QuestionVariantAnswer.objects.filter(question_id=question.id)
            for answer in questionVariantAnswer:
                if answer.correctAnswer == True:
                    variantAnswer['correct'].append([answer.number, answer.VariantAnswer])
                else:
                    variantAnswer['wrong'].append([answer.number, answer.VariantAnswer])
            questions['question'].append([question.number, question.description, str(question.photo), variantAnswer])

            testId = question.test.id
            module = str(question.test.module)
            topic = question.test.topic
            subject = str(question.test.module.subject)

        testClass = TestClass(testId, module, topic, subject, questions)

        result.append(json.dumps(testClass, cls=TestEncoder, ensure_ascii=False))

        # result.append([question.test.id, question.test.module, question.test.topic, question.test.module.subject, questions])

    return result
    # return result


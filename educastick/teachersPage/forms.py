from django import forms
from django.forms import ModelForm
from teachersPage import models

class TypeGroupForm(ModelForm):
    class Meta:
        model = models.TypeGroup
        fields = ('name',)

class SubjectForm(ModelForm):
    class Meta:
        model = models.Subject
        fields = ('name',)

class Teacher(ModelForm):
    class Meta:
        model = models.Teacher
        fields = ('surname', 'firstname', 'patronymic', 'job', 'unbalancing', 'subject',)


class StGroup(ModelForm):
    class Meta:
        model = models.StGroup
        fields = ('name', 'dateAdmission', 'typeGroup', 'teacher',)


class Student(ModelForm):
    class Meta:
        model = models.Student
        fields = ('surname', 'firstname', 'patronymic', 'sex', 'birthdate', 'email', 'fioGuardian', 'phone', 'stGroup',)


class Module(ModelForm):
    class Meta:
        model = models.Module
        fields = ('module_name', 'subject',)


class Test(ModelForm):
    class Meta:
        model = models.Test
        fields = ('module', 'topic', 'manyVariables', 'teacher',)


class Variant(ModelForm):
    class Meta:
        model = models.Variant
        fields = ('number', 'orderQuestions', 'test',)


class CheckQuestion(ModelForm):
    class Meta:
        model = models.CheckQuestion
        fields = ('checkQ', 'description',)


class Question(ModelForm):
    class Meta:
        model = models.Question
        fields = ('number', 'description', 'photo', 'test', 'checkQ',)


class QuestionVariantAnswer(ModelForm):
    class Meta:
        model = models.QuestionVariantAnswer
        fields = ('VariantAnswer', 'correctAnswer', 'question',)


class Answer(ModelForm):
    class Meta:
        model = models.Answer
        fields = ('variant', 'uploadDate', 'studentAnswer', 'score', 'photo', 'student', 'test',)

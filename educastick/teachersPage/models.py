from django.db import models
import math
import datetime

# Create your models here.


def get_st_name(obj):
        if obj.typeGroup.name == "Класс":
            current_year = abs(datetime.date.today()-obj.dateAdmission).days/360
            return (str)(math.ceil(current_year))+"-"+obj.name
        return obj.name


class TypeGroup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    surname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255)
    unbalancing = models.CharField(max_length=255)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return " ".join([self.surname, self.firstname, self.patronymic])


class StGroup(models.Model):
    name = models.CharField(max_length=255)
    dateAdmission = models.DateField(auto_now=False)
    typeGroup = models.ForeignKey(TypeGroup, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return get_st_name(self)


class Student(models.Model):
    surname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    sex = models.BooleanField()
    birthdate = models.DateField(auto_now=False)
    email = models.EmailField(max_length=255, blank=True, null=True)
    fioGuardian = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    stGroup = models.ManyToManyField(StGroup)

    def __str__(self):
        return " ".join([self.surname, self.firstname, self.patronymic])


class Module(models.Model):
    module_name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.module_name


class Test(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, blank=True, null=True)
    topic = models.CharField(max_length=255)
    manyVariables = models.IntegerField(default=1)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return " ".join([self.module.module_name, self.topic])


class Variant(models.Model):
    number = models.IntegerField()
    orderQuestions = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

class CheckQuestion(models.Model):
    checkQ = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.checkQ


class Question(models.Model):
    number = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to="photosQuestions/%Y/%m/%d/", blank=True, null=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    checkQ = models.ForeignKey(CheckQuestion, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.description


class QuestionVariantAnswer(models.Model):
    VariantAnswer = models.TextField()
    correctAnswer = models.BooleanField()
    number = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.VariantAnswer)


class Answer(models.Model):
    variant = models.IntegerField()
    uploadDate = models.DateField(auto_now=False)
    studentAnswer = models.TextField()
    score = models.IntegerField()
    photo = models.ImageField(upload_to="photosAnswer/%Y/%m/%d/")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

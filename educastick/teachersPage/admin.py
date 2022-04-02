from django.contrib import admin

# Register your models here.

import math
import datetime
import inspect

from teachersPage import models


def get_st_name(obj):
        if obj.typeGroup.name == "Класс":
            current_year = abs(datetime.date.today()-obj.dateAdmission).days/360
            return (str)(math.ceil(current_year))+"-"+obj.name
        return obj.name


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('get_name',)

    def get_name(self, obj):
        return obj.name

    get_name.short_description = 'Название предмета'


class TypeGroupAdmin(admin.ModelAdmin):
    list_display = ('get_name',)

    def get_name(self, obj):
        return obj.name

    get_name.short_description = 'Тип группы'


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("get_full_name", 'get_job', 'get_unbalancing', "get_subject")

    def get_subject(self, obj):
        return "\n".join([p.name for p in obj.subject.all()])

    def get_full_name(self, obj):
        return " ".join([obj.surname, obj.firstname, obj.patronymic])

    def get_unbalancing(self, obj):
        return obj.unbalancing

    def get_job(self, obj):
        return obj.job

    get_subject.short_description = 'Предметы'
    get_full_name.short_description = 'ФИО Преподавателя'
    get_unbalancing.short_description = 'Разбалловка (3/4/5)'
    get_job.short_description = 'Место работы'


class StGroupAdmin(admin.ModelAdmin):
    list_display = ("get_name", 'get_dateAdmission', 'get_typeGroup', "get_teacher")

    def get_typeGroup(self, obj):
        return obj.typeGroup.name

    def get_teacher(self, obj):
        return "\n".join([" ".join([p.surname, p.firstname, p.patronymic]) for p in obj.teacher.all()])

    def get_name(self, obj):
        return get_st_name(obj)

    def get_dateAdmission(self, obj):
        return obj.dateAdmission

    get_typeGroup.short_description = 'Тип группы'
    get_teacher.short_description = 'ФИО Преподавателя'
    get_name.short_description = 'Название группы'
    get_dateAdmission.short_description = 'Дата поступления'


class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'get_sex', 'get_birthdate', 'get_email', 'get_fioGuardian', 'get_phone', 'get_stGroup',)

    def get_full_name(self, obj):
        return " ".join([obj.surname, obj.firstname, obj.patronymic])

    def get_sex(self, obj):
        return obj.sex

    def get_birthdate(self, obj):
        return obj.birthdate

    def get_email(self, obj):
        return obj.email

    def get_fioGuardian(self, obj):
        return obj.fioGuardian

    def get_phone(self, obj):
        return obj.phone

    def get_stGroup(self, obj):
        return "\n".join([get_st_name(p) for p in obj.stGroup.all()])

    get_full_name.short_description = 'ФИО студента'
    get_sex.short_description = 'Пол'
    get_birthdate.short_description = 'Дата рождения'
    get_email.short_description = 'Почта'
    get_fioGuardian.short_description = 'ФИО опекуна'
    get_phone.short_description = 'Номер телефона опекуна'
    get_stGroup.short_description = 'Группа'


class TestAdmin(admin.ModelAdmin):
    list_display = ('get_subject', 'get_module', 'get_topic', 'get_manyVariables', 'get_teacher',)
    list_display_links = ('get_module', )

    def get_subject(self, obj):
        return obj.module.subject.name

    def get_module(self, obj):
        return obj.module

    def get_topic(self, obj):
        return obj.topic

    def get_manyVariables(self, obj):
        return obj.manyVariables

    def get_teacher(self, obj):
        return " ".join([obj.teacher.surname, obj.teacher.firstname, obj.teacher.patronymic])

    get_module.short_description = 'Модуль'
    get_topic.short_description = 'Тема'
    get_manyVariables.short_description = 'Количество вариантов'
    get_teacher.short_description = 'Преподаватель'
    get_subject.short_description = 'Предмет'


class VariantAdmin(admin.ModelAdmin):
    list_display = ('get_number', 'get_orderQuestions', 'get_test')
    list_display_links = ('get_number', )
    search_fields = ('get_number', )

    def get_number(self, obj):
        return obj.number

    def get_orderQuestions(self, obj):
        return obj.orderQuestions

    def get_test(self, obj):
        return obj.test

    get_number.short_description = 'Номер варианта'
    get_orderQuestions.short_description = 'Порядок вопросов'
    get_test.short_description = 'Тест'


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'get_subject')

    def get_name(self, obj):
        return obj.module_name

    def get_subject(self, obj):
        return obj.subject

    get_name.short_description = 'Модуль'
    get_subject.short_description = 'Предмет'


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('get_number', 'get_description', 'get_photo', 'get_test')
    list_display_links = ('get_test',)

    def get_number(self, obj):
        return obj.number

    def get_description(self, obj):
        return obj.description

    def get_photo(self, obj):
        return obj.photo

    def get_test(self, obj):
        return obj.test

    get_number.short_description = 'Номер вопроса'
    get_description.short_description = 'Описание вопроса'
    get_photo.short_description = 'Фотография'
    get_test.short_description = 'Тест'


class QuestionVariantAnswer(admin.ModelAdmin):
    list_display = ('get_VariantAnswer', 'get_correctAnswer', 'get_question',)

    def get_VariantAnswer(self, obj):
        return obj.VariantAnswer

    def get_correctAnswer(self, obj):
        return obj.correctAnswer

    def get_question(self, obj):
        return obj.question

    get_VariantAnswer.short_description = 'Вариант ответа'
    get_correctAnswer.short_description = 'Правильный ответ'
    get_question.short_description = 'Вопрос'


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('get_variant', 'get_uploadDate', 'get_studentAnswer', 'get_score', 'get_photo', 'get_student', 'get_test')
    list_display_links = ('get_variant',)

    def get_variant(self, obj):
        return obj.variant

    def get_uploadDate(self, obj):
        return obj.uploadDate

    def get_studentAnswer(self, obj):
        return obj.studentAnswer

    def get_score(self, obj):
        return obj.score

    def get_photo(self, obj):
        return obj.photo

    def get_student(self, obj):
        return obj.student

    def get_test(self, obj):
        return obj.test

    get_variant.short_description = 'Номер варианта'
    get_uploadDate.short_description = 'Дата проведения'
    get_studentAnswer.short_description = 'Ответ студента'
    get_score.short_description = 'Процент правильных ответов'
    get_student.short_description = 'ФИО студента'
    get_photo.short_description = 'Фотография'
    get_test.short_description = 'Тест'


admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.TypeGroup, TypeGroupAdmin)
admin.site.register(models.Teacher, TeacherAdmin)
admin.site.register(models.StGroup, StGroupAdmin)
admin.site.register(models.Student, StudentAdmin)

admin.site.register(models.Test, TestAdmin)
admin.site.register(models.Variant, VariantAdmin)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Answer, AnswerAdmin)
admin.site.register(models.Module, ModuleAdmin)
admin.site.register(models.QuestionVariantAnswer, QuestionVariantAnswer)

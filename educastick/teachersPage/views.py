from django.shortcuts import render

from teachersPage import models
from teachersPage import forms
from teachersPage.dataProcessing import statistic
from django.views.generic.edit import CreateView

# Create your views here.


def calcStatistic(request):
    hq = statistic.hardQuestion()
    abStatistic = statistic.abStatistic()
    quality = statistic.qualityStatistic()
    avgStud = statistic.averageScore()
    minScore = statistic.minScore()
    maxScore = statistic.maxScore()
    notWrite = statistic.notWrite()
    quantityByDisassembly = statistic.quantityByDisassembly()
    getModule = statistic.getModule()
    chart = statistic.chart()
    context = {'count': abStatistic, 'quality': quality, 'avgStud': avgStud, 'minScore': minScore, 'maxScore': maxScore,
               'notWrite': notWrite, 'quantityByDisassembly': quantityByDisassembly, 'getModule': getModule, 'hq': hq, 'chart': chart}
    return render(request, 'statistic.html', context)


def main(request):
    return render(request, 'index.html')



def account(request):
    return render(request, 'account.html')


class TypeGroupCreateView(CreateView):
    template_name = 'create.html'  # путь к файлу шаблона, для вывода страницы с формой;
    form_class = forms.TypeGroupForm  # класс формы, связанной с моделью;
    success_url = '/index/'  # адрес, по которому будет выполнено перенаправление после успешного сохранения данных
    # def get_context_data(self, **kwargs):
    # # метод, чтобы добавить в контекст список рубрик.
    #     context = super().get_context_data(**kwargs)
    #     context['rubrics'] = Rubric.objects.all()
    #     return context


def test(request):
    submitbutton = request.POST.get("submit")

    img = ''

    form = forms.TestForm(request.POST or None)
    if form.is_valid():
        img = form.cleaned_data.get("img")

    context = {'form': form, 'img': img}

    return render(request, 'testimg.html', context)

def tests(request):
    return render(request, 'tests.html')


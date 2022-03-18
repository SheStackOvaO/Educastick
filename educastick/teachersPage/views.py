from django.shortcuts import render
from teachersPage import forms
from django.views.generic.edit import CreateView

# Create your views here.


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


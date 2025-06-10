from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages


from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

from .models import Human, Profession
from .forms import NewsForm, UserRegisterForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно")
            user = form.save()
            login(request,user)
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request, 'Project/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('Login')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(request, 'Project/login.html', {'form': form})

class HomeNew(ListView, MyMixin):
    model = Human
    context_object_name = 'new'
    template_name = 'Project/home_new_list.html'
    extra_context = {'title':'Главная'}
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Главная страница'
        return context

    def get_queryset(self):
        return Human.objects.filter(is_published=True).select_related('profession')

class NewByProfession(ListView, MyMixin):
    model = Human
    template_name = 'Project/home_new_list.html'
    context_object_name = 'new'
    allow_empty= False
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= Profession.objects.get(pk=self.kwargs['profession_id'])
        return context

    def get_queryset(self):
        return Human.objects.filter(profession=self.kwargs['profession_id'], is_published=True).select_related('profession')

class ViewNew(DetailView):
    model = Human
    context_object_name = 'project_item'

class AddNew(CreateView):
    form_class = NewsForm
    template_name = 'Project/add_project.html'
    login_url = '/admin/'

# def test(request):
#     objects = ['Join', 'Paul', 'George', 'Ringo', 'Join2', 'Paul2', 'George2', 'Ringo2']
#     paginator = Paginator(objects, 2)
#     page_num = request.GET.get('page', 1)
#     page_objects = paginator.get_page(page_num)
#     return render(request, 'Project/test.html', {'page_obj':page_objects})


# def index(request):
#     human = Human.objects.all()
#     professions = Profession.objects.all()
#     context = {
#         'new': human,
#         'title': 'Список сотрудников'
#
#     }
#     return render(request, 'Project/index.html', context=context)


# def get_profession(request, profession_id):
#     human = Human.objects.filter(profession_id=profession_id)
#     professions = Profession.objects.all()
#     profession = Profession.objects.get(pk=profession_id)
#     context = {
#         'new': human,
#         'profession': profession
#     }
#     return render(request, 'Project/profession.html', context=context)


# def view_project(request, project_id):
#     # new_item = Human.objects.get(pk=new_id)
#     project_item = get_object_or_404(Human, pk=project_id)
#     context = {
#         'project_item': project_item
#     }
#     return render(request, 'Project/view_project.html', context=context)


# def add_project(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # new = Human.objects.create(**form.cleaned_data)
#             new = form.save()
#             return redirect(new)
#     else:
#         form = NewsForm()
#     return render(request, 'Project/add_project.html', {'form': form})

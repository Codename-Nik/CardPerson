from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from Project.views import HomeNew, NewByProfession, ViewNew, AddNew, register, user_login, user_logout
#from Project.views import index, get_profession, view_project, add_project, test

urlpatterns = [
   #path('', index, name='Home'),
   #path('profession/<int:profession_id>/', get_profession, name="Profession"),
   #path('project/<int:project_id>/', view_project, name='View_project'),
   #path('project/add_project', add_project, name='Add_project'),
   #path('test/', test, name='Test')
    path('', HomeNew.as_view(), name='Home'),
    path('profession/<int:profession_id>/', NewByProfession.as_view(), name="Profession"),
    path('project/<int:pk>/', ViewNew.as_view(), name='View_project'),
    path('project/add_project', AddNew.as_view(), name='Add_project'),
    path('register/', register, name='Register'),
    path('login/', user_login, name='Login'),
    path('logout/', user_logout, name='Logout'),
]


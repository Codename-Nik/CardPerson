from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Human, Profession

class NewsAdminForm(forms.ModelForm):
    name = forms.CharField(widget=CKEditorUploadingWidget())
    surname = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Human
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'get_photo', 'date_birth', 'is_published', 'profession', 'place_residence')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'surname')
    list_filter = ('is_published', 'id')
    list_editable = ['is_published', 'profession']
    fields = ('name', 'surname', 'photo', 'get_photo', 'date_birth', 'is_published')
    readonly_fields = ('get_photo', 'date_birth')
    form = NewsAdminForm

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=75>')
        else:
            return 'Фото нет'

    get_photo_description = 'Миниатюра'

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Human, NewsAdmin)
admin.site.register(Profession, ProfessionAdmin)

admin.site.site_title = "Страница администрирование"
admin.site.site_header = "Страница администрирование"

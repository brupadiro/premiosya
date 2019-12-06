from django.contrib import admin
from django import forms
from .models.users import Users

class usuariosAdminForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'


class usuariosAdmin(admin.ModelAdmin):
    form = usuariosAdminForm
    list_display = ['username', 'phone']
    readonly_fields = ['username', 'phone']

admin.site.register(Users, usuariosAdmin)



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from import_export import resources
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from .models import All_knifes, Account_table
from .utilities import send_email_for_varify
import datetime


class All_knifesResource(resources.ModelResource):
    class Meta:
        model = All_knifes


class Account_tableResource(resources.ModelResource):
    class Meta:
        model = Account_table


@admin.register(All_knifes)
class All_knifesAdmin(ImportExportModelAdmin):
    resource_class = All_knifesResource
    list_display = ['brend', 'series', 'steel', 'carbon', 'CrMoV', 'angle', 'honing_add', 'category']


@admin.register(Account_table)
class Account_tableAdmin(ImportExportModelAdmin):
    resource_class = Account_tableResource
    list_display = ['date', 'brend', 'series', 'steel', 'carbon', 'CrMoV', 'length', 'width', 'grinding_angle',
                    'honing_add', 'comments', 'user']


# class NonactivatedFilter(admin.SimpleListFilter):
#     title = 'Прошли активацию?'
#     parameter_name = 'actstate'
#
#     def lookups(self, request, model_admin):
#         return (('activated', 'Прошли'), ('threedays', 'He прошли более 3 дней'), ('week', 'He прошли более недели'),)
#
#
# def send_activation_notifications(modeladmin, request, queryset):
#     for rec in queryset:
#         if not rec.is_activated:
#             send_email_for_varify(rec)
#         modeladmin.message_user(request, 'Письма с требованиями отправлены')
#         send_activation_notifications.short_description = 'Отправка писем с требованиями активации'
#
#
# def queryset(self, request, queryset):
#     val = self.value()
#     if val == 'activated':
#         return queryset.filter(is_active=True, is_activated=True)
#     elif val == 'threedays':
#         d = datetime.date.today() - datetime.timedelta(days=3)
#         return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)
#     elif val == 'week':
#         d = datetime.date.today() - datetime.timedelta(weeks=1)
#         return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)


# class EditUserAdmin(admin.ModelAdmin):
#     list_display = ('__str__', 'is_activated', 'date_joined')
#     search_fields = ('username', 'email', 'first_name', 'last_name')
#     # list_filter = (NonactivatedFilter,)
#     fields = (('username', 'email'), ('first_name', 'last_name'),
#               ('send—messages', 'is_active', 'is_activated'),
#               ('is_staff', 'is_superuser'), 'groups', 'user_permissions', ('last—login', 'date_joined'))
#     readonly_fields = ('last_login', 'date_joined')
#     actions = (send_email_for_varify,)


# admin.site.register(User, EditUserAdmin)

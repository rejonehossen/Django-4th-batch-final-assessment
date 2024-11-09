from django.contrib import admin
from ManageCash.models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(AddCash)
admin.site.register(Expense)
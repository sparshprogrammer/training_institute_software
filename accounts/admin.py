from django.contrib import admin
from accounts.models import User


class UserAdmin(admin.ModelAdmin):
    fields = []


admin.site.register(User, UserAdmin)

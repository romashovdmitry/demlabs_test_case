""" admin interface setup """
# Django imports
from django.contrib import admin

# import models
from user.models.user import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']


admin.site.register(User, UserAdmin)

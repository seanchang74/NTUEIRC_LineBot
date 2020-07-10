from django.contrib import admin
from ircbot.models import users

class usersAdmin(admin.ModelAdmin):
    list_display=('uid','question')
admin.site.register(users, usersAdmin)

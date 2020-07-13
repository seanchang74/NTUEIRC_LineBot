from django.contrib import admin
from ircbot.models import users
from ircbot.models import registerform

class usersAdmin(admin.ModelAdmin):
    list_display=('uid','question')
    
class registerformAdmin(admin.ModelAdmin):
     list_display = ('cid', 'name', 'phone', 'email', 'fbname', 'lineid', 'willing', 'firsttime')
     ordering = ('-willing',)
     
admin.site.register(users, usersAdmin)
admin.site.register(registerform, registerformAdmin)

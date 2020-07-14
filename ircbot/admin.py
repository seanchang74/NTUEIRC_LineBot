from django.contrib import admin
from ircbot.models import users
from ircbot.models import registerform

admin.site.site_title="國北資研"
admin.site.site_header="國北資訊研究社"
admin.site.index_title="後臺管理"

class usersAdmin(admin.ModelAdmin):
    list_display=('uid','question')
    
class registerformAdmin(admin.ModelAdmin):
     list_display = ('cid', 'name', 'phone', 'email', 'fbname', 'lineid', 'willing', 'firsttime')
     ordering = ('-willing',)
     
admin.site.register(users, usersAdmin)
admin.site.register(registerform, registerformAdmin)



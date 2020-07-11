from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, PostbackEvent
from urllib.parse import parse_qsl
from ircbot.models import users
from module import func

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                user_id = event.source.user_id
                if not (users.objects.filter(uid = user_id).exists()):
                    unit = users.objects.create(uid = user_id)
                    unit.save()
                mtext = event.message.text
                if mtext == '@使用說明':
                    func.sendUse(event)
                elif mtext == '@我想入社':
                    func.sendData(event, user_id)
                elif mtext[:3] == '###' and len(mtext) > 3:
                    func.manageForm(event, mtext, user_id)
                elif mtext == '@個人資料清除':
                    func.sendCancel(event, user_id)
                elif mtext[:11] == 'ntueircsean' and len(metext) > 11:
                    func.pushMessage(event, mtext)
                else:
                    func.sendQnA(event, mtext)
            if isinstance(event, PostbackEvent):  
                backdata = dict(parse_qsl(event.postback.data))  
                if backdata.get('action') == 'yes':
                    func.sendYes(event, event.source.user_id)

        return HttpResponse()

    else:
        return HttpResponseBadRequest()



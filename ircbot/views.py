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
                if not (users.object.filter(uid=user_id).exists()):
                    unit = users.objects.create(uid=user_id)
                    unit.save()
                mtext = event.message.text
            if isinstance(event, PostbackEvent):
                backdata = dict(parse_qsl(event.postback.data))
                if backdata.get('action') == 'yes':
                    ques = func.sendYes(event, event.source.user_id)
                if mtext == '@課程安排':
                    func.sendCourse(event)
                elif mtext == '@我想入社':
                    func.sendData(event, user_id)
                elif mtext[:3] == '###' and len(mtext) > 3:
                    func.manageForm(event, mtext, user_id)
                elif mtext == '@我要請假':
                    func.sendLeave(event, user_id)
                elif mtext[:3] == '***' and len(mtext) > 3:
                    func.manageForm2(event, mtext, user_id)
                elif mtext[:11] == 'ntueircsean' and len(mtext) > 11:
                    func.pushMessage(event, mtext)
                elif mtext == '@我想詢問':
                    func.callService(event)
                elif ques == 1:
                    func.saveQuestion(event, mtext, user_id)
                    ques = 2
                else:
                    func.sendWait(event)

        return HttpResponse()

    else:
        return HttpResponseBadRequest()



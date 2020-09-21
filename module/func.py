from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, TemplateSendMessage, ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction

import http.client, json
from ircbot.models import users, registerform

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

admin_uid = "Ua8f3111b954407dcccd457aaaefe23bc"
'''host = "ntueircbot02.azurewebsites.net"
endpoint_key = "8aa14541-c826-43de-8585-d1e388b4f96e"
kb = "ba477641-32e6-4681-8385-c1c84c52c445"
method = "/qnamaker/knowledgebases/" + kb + "/generateAnswer"'''

def sendUse(event):  #@使用說明
    try:
        text1 ="對於初次接觸的使用者，可以透過下方的圖文選單，點選你想要使用的功能\n如果有其他問題想要諮詢的話，可以私訊社團臉書粉專，我們會盡快為你解惑!"
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='系統好像有點問題，請再試一次!'))

def sendData(event, user_id):
    try:
        '''if not (registerform.objects.filter(cid=user_id).exists()):'''
            message = TemplateSendMessage(
                alt_text = '填寫正式入社表單',
                template = ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/CBilkHy.png',
                    title='填寫正式入社表單',
                    text='歡迎加入國北資研的大家庭!',
                    actions=[
                        URITemplateAction(label='前往填寫', uri='https://liff.line.me/1654433071-DPGqaOv2')
                    ]
                )
            )
        '''else:
            message = TextSendMessage(text = '你已經填寫過表單囉!')'''
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='資料處理發生錯誤！'))

def manageForm(event, mtext, user_id):
    try:
        flist = mtext[3:].split('/')
        cname = flist[0]
        cgender = flist[1]
        cbirth = flist[2]
        cdepartment = flist[3]
        cstudentid = flist[4]
        cfbname = flist[5]
        clineid = flist[6]
        cfirsttime = flist[7]
        '''unit = registerform.objects.create(cid=user_id, name=cname, studentid=cstudentid, gender=cgender, 
        fbname=cfbname, lineid=clineid, department=cdepartment, birth=cbirth, firsttime=cfirsttime)
        unit.save()'''
        text1 = "我們已收到你的回覆，資料如下:"
        text1 +="\n 姓名:" + cname
        text1 +="\n 學號:" + cstudentid
        text1 +="\n 性別:" + cgender
        text1 +="\n 系級:" + cdepartment
        text1 +="\n 生日:" + cbirth
        text1 +="\n FB名稱:" + cfbname
        text1 +="\n LINE ID:" + clineid
        text1 +="\n 未來欲參加的班級:" + cfirsttime
        message = TextSendMessage(  #顯示表單資料
                    text = text1
                )
        line_bot_api.reply_message(event.reply_token,message)
        line_bot_api.push_message(admin_uid, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='資料處理發生錯誤！'))
        
'''def sendCancel(event, user_id):
    try:
        if registerform.objects.filter(cid=user_id).exists():
            formdata = registerform.objects.get(cid=user_id)
            cname = formdata.name
            cphone = formdata.phone
            cemail = formdata.email
            cfbname = formdata.fbname
            clineid = formdata.lineid
            cwilling = formdata.willing
            cfirsttime = formdata.firsttime
            text1 = "您填寫的資料如下:"
            text1 +="\n 姓名:" + cname
            text1 +="\n 電話:" + cphone
            text1 +="\n 電子郵件:" + cemail
            text1 +="\n FB名稱:" + cfbname
            text1 +="\n LINE ID:" + clineid
            text1 +="\n 目前入社意願:" + cwilling
            text1 +="\n 是否想參加體驗社課:" + cfirsttime
            message = [TextSendMessage(  #顯示表單資料
                    text = text1
                ),
                TemplateSendMessage(
                alt_text="表單資料清除確認",
                template=ConfirmTemplate(
                    text="你確定要清除表單資料嗎?",
                    actions=[
                        PostbackTemplateAction(
                            label='是',
                            data='action=yes'),
                        PostbackTemplateAction(
                            label='否',
                            data='action=no')]
                    )
                )
            ]
        else:
            message = TextSendMessage(text = '您目前尚未填寫入社意願調查表!')
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='資料處理發生錯誤！'))
        
def sendYes(event, user_id):
    try:
        line_bot_api.push_message(admin_uid, TextSendMessage(text='系統收到新生欲清除資料，資料如下'))
        datadel = registerform.objects.get(cid=user_id)
        cname = datadel.name
        cphone = datadel.phone
        cemail = datadel.email
        cfbname = datadel.fbname
        clineid = datadel.lineid
        cwilling = datadel.willing
        cfirsttime = datadel.firsttime
        text1 = "您填寫的資料如下:"
        text1 +="\n 姓名:" + cname
        text1 +="\n 電話:" + cphone
        text1 +="\n 電子郵件:" + cemail
        text1 +="\n FB名稱:" + cfbname
        text1 +="\n LINE ID:" + clineid
        text1 +="\n 目前入社意願:" + cwilling
        text1 +="\n 是否想參加體驗社課:" + cfirsttime
        line_bot_api.push_message(admin_uid, TextSendMessage(text=text1))
        datadel.delete()
        message = TextSendMessage(
            text = "您的資料已成功清除。\n期待您再次填寫表單，謝謝!")
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='資料處理發生錯誤！'))
        
def pushMessage(event, mtext):  ##推播訊息給所有顧客
    try:
        msg = mtext[11:]  #取得訊息
        userall = users.objects.all()
        for user in userall:  #逐一推播
            message = TextSendMessage(
                text = msg
            )
            line_bot_api.push_message(to=user.uid, messages=[message])  #推播訊息
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="資料處理發生錯誤！"))        
        
def sendQnA(event, mtext):  #QnA
    question = {
        'question': mtext,
    }
    content = json.dumps(question)
    headers = {
        'Authorization': 'EndpointKey ' + endpoint_key,
        'Content-Type': 'application/json',
        'Content-Length': len(content)
    }
    conn = http.client.HTTPSConnection(host)
    conn.request ("POST", method, content, headers)
    response = conn.getresponse ()
    result = json.loads(response.read())
    result1 = result['answers'][0]['answer']
    if 'No good match' in result1:
        text1 = "咦!你問的是關於社團的問題嗎?\n要不要換句話再問問看"
        #將沒有解答的問題寫入資料庫
        userid = event.source.user_id
        unit = users.objects.create(uid=userid, question=mtext)
        unit.save()
    else:  
        text1 = result1  
    message = TextSendMessage(
        text = text1
    )
    line_bot_api.reply_message(event.reply_token,message)'''

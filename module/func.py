from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, TemplateSendMessage, ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction

import http.client, json
from ircbot.models import users

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

admin_uid = "Admin_Uid"
'''host = "Your_Azure_Host"
endpoint_key = Endpoint_Key"
kb = "Kb_token"
method = "/qnamaker/knowledgebases/" + kb + "/generateAnswer"'''

def sendCourse(event):  #@使用說明
    try:
        text1 ="以下為我們這學期的課程規劃:\n"
        text1 +="基礎班\n1.認識Python\n2.邏輯與迴圈\n3.串列與字典\n4.函式與例外處理\n5.檔案的寫入與讀取\n"
        text1 +="進階班\n1.網頁基礎知識介紹\n2.擷取JSON/HTML格式資料\n3.發送API請求\n4.Numpy&Pandas介紹\n5.資料視覺化\n6.瀏覽器自動化"
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
                    URITemplateAction(label='前往填寫', uri='https://liff.line.me/1654949355-0OZEoq6d')
                ]
            )
        )
        '''else:
            message = TextSendMessage(text = '你已經填寫過表單囉!')'''
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='資料處理發生錯誤！'))

def sendLeave(event, user_id):
    try:
        '''if not (registerform.objects.filter(cid=user_id).exists()):'''
        message = TemplateSendMessage(
            alt_text = '填寫社團請假表單',
            template = ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/CBilkHy.png',
                title='填寫社團請假表單',
                text='請假的同學一定要記得補課哦!',
                actions=[
                    URITemplateAction(label='前往填寫', uri='https://liff.line.me/1654949349-byenoVgg')
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
        csex = flist[1]
        cstudentid = flist[2]
        cdepartment = flist[3]
        cbirth = flist[4]
        cfbname = flist[5]
        clineid = flist[6]
        cfirsttime = flist[7]
        '''unit = registerform.objects.create(cid=user_id, name=cname, studentid=cstudentid, gender=cgender, 
        fbname=cfbname, lineid=clineid, department=cdepartment, birth=cbirth, firsttime=cfirsttime)
        unit.save()'''
        text1 = "我們已收到你的回覆，資料如下:"
        text1 +="\n 姓名:" + cname
        text1 +="\n 學號:" + cstudentid
        text1 +="\n 性別:" + csex
        text1 +="\n 系級:" + cdepartment
        text1 +="\n 生日:" + cbirth
        text1 +="\n FB名稱:" + cfbname
        text1 +="\n LINE ID:" + clineid
        text1 +="\n 社團班級選擇:" + cfirsttime
        message = TextSendMessage(  #顯示表單資料
                    text = text1
                )
        line_bot_api.reply_message(event.reply_token,message)
        line_bot_api.push_message(admin_uid, message)
        line_bot_api.push_message(jessie_uid, message)
        line_bot_api.push_message(jenny_uid, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='資料處理發生錯誤！'))

def manageForm2(event, mtext, user_id):
    try:
        flist = mtext[3:].split('/')
        cname = flist[0]
        cstudentid = flist[1]
        cdate = flist[2]
        ctype = flist[3]
        creason = flist[4]
        '''unit = registerform.objects.create(cid=user_id, name=cname, studentid=cstudentid, gender=cgender, 
        fbname=cfbname, lineid=clineid, department=cdepartment, birth=cbirth, firsttime=cfirsttime)
        unit.save()'''
        text1 = "我們已收到你的回覆，資料如下:"
        text1 +="\n 姓名:" + cname
        text1 +="\n 學號:" + cstudentid
        text1 +="\n 請假日期:" + cdate
        text1 +="\n 請假類別:" + ctype
        text1 +="\n 請假事由:" + creason
        message = TextSendMessage(  #顯示表單資料
                    text = text1
                )
        line_bot_api.reply_message(event.reply_token,message)
        line_bot_api.push_message(admin_uid, message)
        line_bot_api.push_message(jessie_uid, message)
        line_bot_api.push_message(jenny_uid_uid, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='資料處理發生錯誤！'))

def sendWait(event):
    try:
        text1 = "如有問題可以點選圖文選單中的我想詢問\n此外也歡迎直接私訊臉書粉專或IG官方帳號!"
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='系統好像有點問題，請再試一次!'))

def callService(event):
    try:
        message = TemplateSendMessage(
                    alt_text="轉接真人",
                    template=ConfirmTemplate(
                        text="請問需要幫你轉接社長大人嗎?",
                        actions=[
                            PostbackTemplateAction(
                                label='麻煩了',
                                data='action=yes'),
                            PostbackTemplateAction(
                                label='不需要',
                                data='action=no')]
                        )
                    )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='系統好像有點問題，請再試一次!'))
    
def sendYes(event):
    text1 = "請輸入你的問題，社長會盡快回覆你~"
    message = TextSendMessage(
            text = text1
        )
    line_bot_api.reply_message(event.reply_token,message)
    return 1

def saveQuestion(event,mtext,user_id):
    profile = line_bot_api.get_profile(user_id)
    text1 = "剛剛"
    text1 += profile.display_name
    text1 += "問說:\n"
    text1 += mtext
    text1 += "\n請盡快回覆"
    message = TextSendMessage(  #顯示表單資料
                text = text1
            )
    line_bot_api.reply_message(admin_uid,message)
    line_bot_api.reply_message(event.reply_token,TextSendMessage("已將你的問題通知社長大人\n請靜待回覆~謝謝!"))

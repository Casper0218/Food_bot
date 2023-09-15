from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from .Clicker import *
from .onegoogle import *
from .gotourl import *
# from .scraper import IFoodie

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
 
 
@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件

            print(events) #印出來看看

        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
               
                #印出訊息來看看
                print(event.message.text)
                print(f'type= {type(event.message.text)}')
                
                ####處理來自Google Map的商家分享資料解析#########
                data = event.message.text

                # # 使用換行符分割資料
                # parts = data.split('\n')

                # # 分割後的部分包含商家名稱、地址、電話號碼和 Google 地圖連結
                # store_name = parts[0]
                # address = parts[1]
                # phone_number = parts[2]
                # google_maps_link = parts[3]

                # print("商家名稱:", store_name)
                # print("地址:", address)
                # print("電話號碼:", phone_number)
                # print("Google 地圖連結:", google_maps_link)
                # ###############################################

                #current_url = clicker(store_name)  #參數改過
                #current_url = google_maps_link #跳過 Clicker()
                current_url = httpfilter(data)

                if current_url:
                    RES=tmd(current_url)
                else:
                    RES='訊息裡沒有連結，正在嘗試搜尋 Google 地圖...'
                    try:
                        current_url=clicker(data)
                        RES=tmd(current_url)
                    except:
                        break
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TextSendMessage(text=RES)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

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
from .test import *
from linebot.models import *
# from .scraper import IFoodie

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
 
# 在 views.py 的顶部定义全局变量 df
df = None


@csrf_exempt
def callback(request):
    global df  # 使用全局变量 df
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
                    RES,df=tmd(current_url)
                else:
                    RES='訊息裡沒有連結，Google 地圖也搜尋不到該商家的資訊'
                    try:
                        current_url=clicker(data)
                        RES,df=tmd(current_url)
                    except:
                        break
                score = model(df)
                # 调用 choose_sticker 函数并将其返回的消息对象添加到 messages 列表
                messages = [choose_sticker(score, RES), TextSendMessage(text=f'{RES}, 綜合評分為 {score*10:.1f} 分')]

                line_bot_api.reply_message(event.reply_token, messages)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()




from linebot.models import StickerMessage, TextSendMessage

def choose_sticker(score, RES):
    if score > 0.65:  # 假設 0.65 是最高評分
        return StickerMessage(
            package_id='446',  # 第一組貼圖包 ID，根據你的需求更改
            sticker_id='1992'   # 第一組貼圖 ID，根據你的需求更改
        )
    elif score <0.35:  # 如果分數低於 0.35，包括所有其他情況
        return StickerMessage(
            package_id='6632',  # 第三組貼圖包 ID，根據你的需求更改
            sticker_id='11825394'   # 第三組貼圖 ID，根據你的需求更改
        )
    else:  # 假設 0.5 是中等評分
        return StickerMessage(
            package_id='789',  # 第二組貼圖包 ID，根據你的需求更改
            sticker_id='10877'   # 第二組貼圖 ID，根據你的需求更改
        )
    




from flask import Flask,request
from Modules.ReplyMessage import ReplyMessage
import random
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

#HTTP請求方式
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.get_json().get('events')[0]
        print(message)
        replyToken = message.get('replyToken')
        userMessage = message.get("message").get("text")
        print(userMessage)
#猜拳
        if userMessage == "剪刀" or userMessage == "石頭" or userMessage == "布" :
            AI = random.choice(["剪刀","石頭","布"])
            if str(AI) == userMessage:
                result = f"{AI}\n平手"
            elif (AI == "剪刀" and userMessage == "石頭") or (AI == "布"and userMessage == "剪刀") or (AI == "石頭"and userMessage == "布"):
                if userMessage == "石頭":
                   result = f"{AI}\n你贏了\n不對我剛剛出布\n我贏了" 
                elif userMessage == "剪刀":
                    result = f"{AI}\n你贏了\n不對我剛剛出石頭\n我贏了"
                else:
                    result = f"{AI}\n你贏了\n不對我剛剛出剪刀\n我贏了"

            else:
                result= f"{AI}\n你輸了"
            messages = [{
                "type":"text",
                "text":result
            }]
        elif userMessage == "嗨" or userMessage == "在嗎" or userMessage == "安安" or userMessage == "在嗎?":
            print(userMessage, 'elif的狀態')
            messages = [
                {
                    "type": "sticker",
                    "packageId": "11537",
                    "stickerId": "52002738", 
                },
                {
                    "type":"text",
                    "text":"怎麼了"
                }
            ]
#print(userMessage, 'else的狀態')
#message.get("message").get("type"==sticker) 
        elif userMessage == "..." or userMessage == "沒事啦":
            print(userMessage, 'else ... 的狀態')
            messages = [
                {
                    #"text":userMessage
                    "type": "sticker",
                    "packageId": "11537",
                    "stickerId": "52002742", 
                }
            ]
        elif userMessage == "變拳欸" or userMessage == "幹變拳" or userMessage == "你明明就出剪刀" or userMessage == "你明明就出石頭" or userMessage == "你明明就出布" or userMessage == "屁拉":
            print(userMessage, 'else 變拳欸 的狀態')
            messages = [
                {
                    "type":"text",
                    "text":"你才變拳你 全家都變拳"
                }
            ]
        elif userMessage == "打傳" or userMessage == "打傳啦":
            messages = [
                {
                    "type":"text",
                    "text":"叫楊"
                }
            ]
        elif userMessage == "如果他說不要呢?" or userMessage == "如果他說不要呢" or userMessage == "如果他說不呢" or userMessage == "如果他不要呢A" or userMessage == "他不要呢":
            messages = [
                {
                    "type":"text",
                    "text":"叫她閉嘴,然後逼他打"
                }
            ]
#星座運勢

#成語接龍
        else:
            url = f'https://www.moedict.tw/pua/{userMessage}'
            r = requests.get(url)
            result = r.json().get("heteronyms")
            # print(result)
            if result != None and "的意思" in userMessage.split("的意思"):
                resultMessage = result[0].get("definitions")[0].get("def")
                messages = [
                    {
                        "type":"text",
                        "text":resultMessage
                    }
                ]
            else:
                messages = [
                    {
                        "type":"text",
                        "text":"你給我閉嘴"
                    }
                ]
        
        ReplyMessage(replyToken,messages)

        return 'succeed'
    elif request.method == 'GET':
        return 'succeed'
    else:
        return 'succeed'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True, use_reloader=False)


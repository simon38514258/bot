from flask import Flask,request
from Modules.ReplyMessage import ReplyMessage
import random

app = Flask(__name__)

#HTTP請求方式
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.get_json().get('events')[0]
        print(message)
        replyToken = message.get('replyToken')
        userMessage = message.get("message").get("text")
        
        #猜拳
        if userMessage == "剪刀":
            AI = random.randint(0,2)
            if AI == 0:
                print("剪刀")
                result = "平手"
            elif AI == 2:
                print("布")
                result = "你贏了"
            else:
                print("石頭")
                result = "你輸了"
        elif userMessage == "石頭":
            AI = random.randint(0,2)
            if AI == 1:
                print("石頭")
                result = "平手"
            elif AI == 0:
                print("剪刀")
                result = "你贏了"
            else:
                print("布")
                result = "你輸了"
        elif userMessage == "布":
            AI = random.randint(0,2)
            if AI == 2:
                print("布")
                result = "平手"
            elif AI == 1:
                print("石頭")
                result = "你贏了"
            else:
                print("剪刀")
                result = "你輸了"
        else
            if userMessage == "嗨":#message.get("message").get("type") 
                messages = [
                    {
                        #"text":userMessage
                        "type": "sticker",
                        "packageId": "11537",
                        "stickerId": "52002742", 
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


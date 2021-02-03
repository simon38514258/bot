from flask import Flask,request
from Modules.ReplyMessage import ReplyMessage

app = Flask(__name__)

#HTTP請求方式
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.get_json().get('events')[0]
        print(message)
        reply_token = params['events'][0]['replyToken']
        #replyToken = message.get('replyToken')
        userMessage = message.get("message").get("text")
        messages = [
            {
                "type":"text",
                #"text":userMessage
                "text":reply_text
                #"text":"你給我閉嘴"
            }
        ]
        line.reply_message(reply_token, message)
        ReplyMessage(replyToken,messages)

        return 'succeed'
    elif request.method == 'GET':
        return 'succeed'
    else:
        return 'succeed'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True, use_reloader=False)


from flask import Flask,request
from Modules.ReplyMessage import ReplyMessage
import random
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

#HTTP請求方式
@app.route('/', methods=['GET', 'POST'])
def index():

    #星座運勢
    astroDict = {
        "牡羊座":"Aries",
        "獅子座":"Leo",
        "金牛座":"Taurus",
        "射手座":"Sagittarius",
        "雙子座":"Gemini",
        "巨蟹座":"Cancer",
        "處女座":"Virgo",
        "天秤座":"Libra",
        "天蠍座":"Scorpio",
        "魔羯座":"Capricorn",
        "水瓶座":"Aquarius",
        "雙魚座":"Pisces"
    }
    astroImg = {
        "金牛座":"https://www.csie.ntu.edu.tw/~b6506019/stuff/12stars/zodiac02.jpg",
        "牡羊座":"https://www.csie.ntu.edu.tw/~b6506019/stuff/12stars/zodiac01.jpg",
        "雙子座":"https://www.csie.ntu.edu.tw/~b6506019/stuff/12stars/zodiac03.jpg",
        "巨蟹座":"https://www.csie.ntu.edu.tw/~b6506019/stuff/12stars/zodiac04.jpg",
        "獅子座":"https://www.csie.ntu.edu.tw/~b6506019/stuff/12stars/zodiac05.jpg",
        "處女座":"https://www.csie.ntu.edu.tw/~b6506019/stuff/12stars/zodiac06.jpg",
        "天秤座":"https://www.csie.ntu.edu.tw/~b6506019/stuff/12stars/zodiac07.jpg",
        "天蠍座":"https://www.csie.ntu.edu.tw/~b6506019/stuff/12stars/zodiac08.jpg",
        "射手座":"https://www.csie.ntu.edu.tw/~b6506019/stuff/12stars/zodiac09.jpg",
        "摩羯座":"https://www.csie.ntu.edu.tw/~b6506019/stuff/12stars/zodiac10.jpg",
        "水瓶座":"https://www.csie.ntu.edu.tw/~b6506019/stuff/12stars/zodiac11.jpg",
        "雙魚座":"https://www.csie.ntu.edu.tw/~b6506019/stuff/12stars/zodiac12.jpg"
    }

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
                result= f"{AI}\n你輸了\n你出{userMessage}的行為簡直是楊皓鈞"
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
        elif userMessage == "變拳欸" or userMessage == "你變拳" or userMessage == "幹變拳" or userMessage == "你明明就出剪刀" or userMessage == "你明明就出石頭" or userMessage == "你明明就出布" or userMessage == "屁拉":
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
        elif userMessage in astroDict:
            url = f"https://www.daily-zodiac.com/zodiac/{astroDict[userMessage]}"
            r = requests.get(url)
            soup = BeautifulSoup(r.text,"html.parser")

            #取出星座名稱，並利用replace將空白及換行清除
            title = soup.select("h2")[0].text.replace(" ","").replace("\n","")
            #取出日期，並利用replace將空白及換行清除
            subtitle = soup.select("h3")[0].text.replace(" ","").replace("\n","")
            #取出運勢，並做資料處理
            content = soup.select("p.article")
            #將bs4類型強制轉為srting
            tmp = str(content[0])
            #自切割，利用<botton做為切割基礎，並保留第一段
            tmp = tmp.split("<button")[0]
            #將str型態的html利用BeautifulSoup轉換成可操作的資料型態
            soup = BeautifulSoup(tmp,"html.parser")
            #利用beautifulsoup取出文字，並利用replace將空白及換行清除
            content = soup.text.replace(" ","").replace("\n","")
            print(title,subtitle,content)
            flexMessage = {
            "type": "bubble",
            "direction": "ltr",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": title,
                    "size": "xxl",
                    "color": "#ECA910FF",
                    "align": "center",
                    "contents": []
                }
                ]
            },
            "hero": {
                "type": "image",
                "url": astroImg[userMessage],
                "size": "full",
                "aspectRatio": "1.51:1",
                "aspectMode": "fit"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": subtitle,
                    "color": "#000000FF",
                    "align": "start",
                    "contents": []
                }
                {
                    "type": "text",
                    "text": content,
                    "size": "md",
                    "color": "#246CC0FF",
                    "align": "center",
                    "wrap": True,
                    "contents": []
                },
                
                ]
            }
            }
            messages = [{
            "type": "flex",
            "altText": "星座運勢",
            "contents": flexMessage
            }]

    #成語接龍
        else:
            # print(result)
            if "的意思" in userMessage:
                userMessage = userMessage.split("的意思")
                url = f'https://www.moedict.tw/pua/{userMessage[0]}'
                r = requests.get(url)
                result = r.json().get("heteronyms")
                if result != None:
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
                            "text":"查無資料"
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


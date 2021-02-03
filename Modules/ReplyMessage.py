import requests
import json

def ReplyMessage(replyToken,messages):
    #請使用自己的token
    accessToken = "l7llJ3W9l369bgoXjKeyl0v5b5JPvYWQh6RYkISoit71uat3iubKKG2yC/GL/F9qLF00K5xENA3hxsZUkk/A+4Ud4JJiMQbOCgKero9XVhWWxKdiabn+nsXTOPk3RVzGdPmpqAeFzV+zgK+GOxXXAAdB04t89/1O/w1cDnyilFU="
    
    headers ={
        'Content-Type':'application/json',
        'Authorization': 'Bearer '+accessToken
    }
    data ={
        "replyToken":replyToken,
        'messages':messages
    }
    url = 'https://api.line.me/v2/bot/message/reply'
    r = requests.post(url,headers=headers,data=json.dumps(data))
    return r
from flask import Flask,request, abort
from google import genai
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)
client = genai.Client()

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

@app.route("/")
@app.route("/<string:question>")
def index(question:str=''):
    if question=='':
        return "<h1>我是Gemini的小助手</h1>"
    else:        
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=f"{question},回應請輸出成為html格式"
        )
        html_format = response.text
        html_format = response.text.replace("```html","").replace("```","")
        return html_format
         
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=event.message.text
    )
    message = TextSendMessage(text=response.text)
    line_bot_api.reply_message(event.reply_token, message)
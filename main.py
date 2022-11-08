# https://www.youtube.com/watch?v=Al7hkU6RO9M&t=2287s&ab_channel=OlegMolchanov
# https://api.telegram.org/bot5366368085:AAFh8_k9XN315LzbsAVq1XK0FF_t-LOdMEA/setWebhook?url=https://8839-176-52-99-158.eu.ngrok.io
# https://mastergroosha.github.io/telegram-tutorial/docs/lesson_12/
# https://stackoverflow.com/questions/66101749/how-to-run-multiple-telegram-bots-on-the-same-port
# https://dvmn.org/encyclopedia/about-chatbots/long-polling/
from flask import Flask, request, jsonify
import requests
import json
import urllib3

bot1 = '5366368085:AAFh8_k9XN315LzbsAVq1XK0FF_t-LOdMEA'
URL = 'https://api.telegram.org/bot' + bot1 + '/'
ngrok = 'https://78c8-176-52-99-158.ngrok.io'

app = Flask(__name__)

def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def send_message(chat_id, text='bla'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()

@app.route('/', methods=['POST', 'GET'])
def index():
    return '<h1>Hi</h1>'

@app.route('/bot/<bot_id>', methods=['POST', 'GET'])
def bot(bot_id):
    if request.method == 'POST':
        r = request.get_json()
        write_json(r)
        chat_id = r['message']['chat']['id']
        send_message(chat_id, text='blayyzyzyzyzy')
        return jsonify(r)
    if request.method == 'GET':
        return "Profile page of user"

def make_urls(tokens):
    pass
    # url = 'https://api.telegram.org/bot' + token + '/setWebhook?url=' + ngrok + '/bot/' + bot_id

def set_webhook(token):
    http = urllib3.PoolManager()
    resp = http.request('GET', url)
url1 = 'https://api.telegram.org/bot5366368085:AAFh8_k9XN315LzbsAVq1XK0FF_t-LOdMEA/setWebhook?url=https://78c8-176-52-99-158.ngrok.io/bot/a'
url2 = 'https://api.telegram.org/bot5264941039:AAEIZ318TErur-JAGX3F1CZSyCd241Aic1M/setWebhook?url=https://78c8-176-52-99-158.ngrok.io/bot/b'
urls = [url1, url2]
http = urllib3.PoolManager()
for url in urls:
    resp = http.request('GET', url)
    print(resp.status)

if __name__ == '__main__':
    app.run(debug=True)
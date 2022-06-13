from flask import Flask, Response,render_template, request
from urllib.parse import urlparse
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import re,struct, sys, os, time,requests
app = Flask(__name__)

def start(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(f'Hello {update.effective_user.first_name}\nI am a sample Telegram bot made with python-telegram-bot!n\ncode{update.get_updates()}')
# REQUEST_KWARGS={
#     'proxy_url': 'http://127.0.0.1:10809',
# }
updater = Updater(os.environ.get("TOKEN"), use_context=True)
# updater = Updater('5548984433:AAFl5rTKpJRij88tu6sHqhvYpvogqFCYp88', use_context=True, request_kwargs=REQUEST_KWARGS)

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()

# 首页
@app.route('/', methods=['GET'])
def show():
    return {'code':200,'msg':'hello word'}

# 推送
@app.route('/u/<path:users>/t/<path:texts>', methods=['POST'])
def api_query_ip_input(texts,users):
    if not texts and not users:
        return render_template('404.html'), 404
    print(texts,users)
    updater.send_message(text='Hi John!', chat_id=users)
    return {'code':200}

# 404
@app.errorhandler(404)
def page_not_found(error):
    return {'code':404,'msg':'not find'}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
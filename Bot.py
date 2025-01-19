from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import threading

class Bot:
    def __init__(self, token):
        self.token = token
        self.user_message = ""
        self.update = ""

    async def start(self, update: Update, context: CallbackContext) -> None:
        await update.message.reply_text("این بات جهت کار با یکسری دستورات کنترلی آماده ساخته شده! خوش آمدید 💓")

    async def handle_user_message(self, update: Update, context: CallbackContext) -> None:
        user_message = update.message.text
        await update.message.reply_text("درخواست شما با موفقیت ارسال شد✅")
        await update.message.reply_text("منتظر دریافت پاسخ از AI هستم...🔍")
        self.user_message = user_message
        self.update = update

        thread = threading.Thread(target=self.handle_message_in_background)
        thread.start()

    def handle_message_in_background(self):
        return(self.user_message)


    def run(self):
        application = Application.builder().token(self.token).build()

        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_user_message))

        application.run_polling()

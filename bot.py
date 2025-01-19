from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import threading

class Bot:
    def __init__(self, token, main_instance):
        self.token = token
        self.main_instance = main_instance

    async def start(self, update: Update, context: CallbackContext) -> None:
        await update.message.reply_text("این بات جهت کار با یکسری دستورات کنترلی آماده ساخته شده! خوش آمدید 💓")

    async def handle_user_message(self, update: Update, context: CallbackContext) -> None:
        user_message = update.message.text  
        await update.message.reply_text("درخواست شما با موفقیت ارسال شد✅")
        await update.message.reply_text("منتظر دریافت پاسخ از AI هستم...🔍")

        thread = threading.Thread(target=self.handle_message_in_background, args=(user_message, update))
        thread.start()

    def handle_message_in_background(self, message, update):
        ai_response = self.main_instance.get_ai_response(message)
        update.message.reply_text(f"پاسخ AI: {ai_response}")

    def run(self):
        application = Application.builder().token(self.token).build()

        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_user_message))

        application.run_polling()

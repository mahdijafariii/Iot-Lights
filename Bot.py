import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters

class Bot:
    def __init__(self, token, message_queue):
        self.token = token
        self.message_queue = message_queue
        self.user_message = ""

    async def start(self, update: Update, context: CallbackContext) -> None:
        await update.message.reply_text("این بات جهت کار با یکسری دستورات کنترلی آماده ساخته شده! خوش آمدید 💓")

    async def handle_user_message(self, update: Update, context: CallbackContext) -> None:
        self.user_message = update.message.text
        await update.message.reply_text("درخواست شما با موفقیت ارسال شد✅")
        await update.message.reply_text("منتظر دریافت پاسخ از AI هستم...🔍")

        self.message_queue.put(self.user_message)

    def run(self):
        application = Application.builder().token(self.token).build()

        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_user_message))

        application.run_polling()

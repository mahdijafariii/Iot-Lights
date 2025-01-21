import asyncio
import threading
import queue
from Bot import Bot
from Ai import Ai
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

def bot_thread(message_queue):
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)

    bot = Bot(BOT_TOKEN, message_queue)
    new_loop.run_until_complete(bot.run())


def main():
    message_queue = queue.Queue()
    bot_thread_instance = threading.Thread(target=bot_thread, args=(message_queue,))
    bot_thread_instance.start()

    while True:
        if not message_queue.empty():
            user_message = message_queue.get()
            print(user_message)
            response = Ai().handle_request(user_message)
            print(response)


if __name__ == "__main__":
    main()

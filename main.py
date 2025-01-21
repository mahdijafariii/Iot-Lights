import asyncio
import threading
import queue
from Bot import Bot


def bot_thread(message_queue):
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)

    bot = Bot("7906117866:AAFVuWuO0oU1tyAYPwWEEcN7W-3dsJhVq2k", message_queue)
    new_loop.run_until_complete(bot.run())


def main():
    message_queue = queue.Queue()
    bot_thread_instance = threading.Thread(target=bot_thread, args=(message_queue,))
    bot_thread_instance.start()

    while True:
        if not message_queue.empty():
            user_message = message_queue.get()
            print(user_message)


if __name__ == "__main__":
    main()

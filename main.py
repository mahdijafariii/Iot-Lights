import Bot
def main():

    bot = Bot.Bot("7906117866:AAFVuWuO0oU1tyAYPwWEEcN7W-3dsJhVq2k")

    bot.run()
    print(bot.handle_message_in_background())
    


if __name__ == "__main__":
    main()
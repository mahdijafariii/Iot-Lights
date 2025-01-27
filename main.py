import serial
import time
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
arduino_port = "COM5"  
baud_rate = 115200       
timeout = 1           
try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=timeout)
    print(f"Connected to Arduino on {arduino_port}")
    time.sleep(2)  

    while True:
        if ser.in_waiting > 0: 
            client_data = ser.readline().decode('utf-8').strip() 
            print(f"Received from Arduino: {client_data}")
            if(client_data != ("New Client Connected")):
                response=Ai().handle_request(client_data)
                ser.write(response.encode('utf-8'))
                print(f"Sent to Arduino: {response}")


except serial.SerialException as e:
    print(f"Serial Error: {e}")
except KeyboardInterrupt:
    print("\nProgram stopped.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial connection closed.")

   



if __name__ == "__main__":
    main()

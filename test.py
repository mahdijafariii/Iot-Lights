import serial
import time

# تنظیمات پورت سریال
arduino_port = "COM5"  # پورت آردوینو (مطمئن شوید صحیح است)
baud_rate = 115200       # نرخ انتقال داده (همان تنظیم شده در آردوینو)
timeout = 1            # مدت زمان انتظار برای داده‌ها

try:
    # اتصال به پورت سریال
    ser = serial.Serial(arduino_port, baud_rate, timeout=timeout)
    print(f"Connected to Arduino on {arduino_port}")
    time.sleep(2)  # انتظار برای آماده شدن آردوینو

    while True:
        if ser.in_waiting > 0:  # بررسی وجود داده
            client_data = ser.readline().decode('utf-8').strip()  # خواندن داده
            print(f"Received from Arduino: {client_data}")


except serial.SerialException as e:
    print(f"Serial Error: {e}")
except KeyboardInterrupt:
    print("\nProgram stopped.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial connection closed.")

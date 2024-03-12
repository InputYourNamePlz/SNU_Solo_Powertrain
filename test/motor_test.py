import serial
import threading
import time
from tkinter import *


ser = serial.Serial(
    port='COM7',
    baudrate=115200,
    timeout=1)

def write_to_port():
    time.sleep(0.5)
    while True:
        send_data=str(var1.get())+'\n'
        ser.write(send_data.encode())
        print(send_data)
        time.sleep(0.2)


write_thread = threading.Thread(target=write_to_port, args=(ser,))
write_thread.daemon = True
write_thread.start()

root = Tk()
root.title("SNU SOLO-RTY Motor Test")
root.geometry("320x75")
root.resizable(False,False)

var1=IntVar()
motor_scale_bar = Scale(root, variable=var1,orient="horizontal", \
                        showvalue=True, tickinterval=50, to=255,length=255)
motor_scale_bar.pack()

var1.get()

root.mainloop()


'''
# 키보드 입력을 받아 시리얼 포트로 전송하는 함수
def write_to_port(ser):
    while True:
        # 사용자로부터 키보드 입력 받기
        user_input = input('\n')
        user_input+='\r\n'
        # 시리얼 포트로 데이터 전송
        ser.write(user_input.encode())


# 키보드 입력을 받아 시리얼 포트로 전송하는 스레드 시작
write_thread = threading.Thread(target=write_to_port, args=(ser,))
write_thread.daemon = True
write_thread.start()


# 메인 스레드 유지
while True:
    pass
    
'''

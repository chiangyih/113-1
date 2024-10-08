# 按鈕測試(pull down類型，按下時為低電位，GPIO設為INPUT，並設為PULL_DOWN)

import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
button1=13 #設定按鈕接腳
gpio.setup(button1, gpio.IN, pull_up_down=gpio.PUD_DOWN) #設定 GPIO13 為輸入，並設為PULL_DOWN

while True:
    try:
        if gpio.input(button1)==1: #當按鈕被按下
            print("偵測到按鈕壓下")
            print("GPIO pin=", button1, "為高電位")
            time.sleep(0.5)
    except KeyboardInterrupt:
        gpio.cleanup()
        break
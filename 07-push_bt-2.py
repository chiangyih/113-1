# 當按鈕按下時，點亮 LED，再按一次熄滅 LED

import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
button1=13 #設定按鈕接腳
led1=17 #設定 LED 接腳
gpio.setup(button1, gpio.IN, pull_up_down=gpio.PUD_DOWN) #設定 GPIO13 為輸入，並設為PULL_DOWN
gpio.setup(led1, gpio.OUT) #設定 GPIO17 為輸出


led_status=False #設定目前 LED 狀態為關閉
while True:
    try:
        if gpio.input(button1)==1: #當按鈕被按下
            print("偵測到按鈕壓下")
            time.sleep(0.2) #測試按鈕彈跳，延遲 0.2 秒為最佳狀況，小於0.2秒會有按鈕彈跳問題
            if led_status==False:
                gpio.output(led1, gpio.HIGH) #點亮 LED
                led_status=True
            else:
                gpio.output(led1, gpio.LOW) #熄滅 LED
                led_status=False
    except KeyboardInterrupt:
        gpio.cleanup()
        break
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)  #設為 BCM 模式

delay_time=0.05 #延遲時間

led=[17,27,22,10,9,11,5,6] #設定 LED 接腳,使用list(串列)儲存
for i in led:
    gpio.setup(i, gpio.OUT) #設定 GPIO 為輸出

while True:
    try:
        for i in led: 
            gpio.output(i, gpio.HIGH) #點亮 LED
            time.sleep(delay_time) #延遲 delay_time秒
            gpio.output(i, gpio.LOW) #熄滅 LED
        # time.sleep(delay_time) 
        for i in reversed(led): #反轉串列
            gpio.output(i, gpio.HIGH) #點亮 LED
            time.sleep(delay_time)
            gpio.output(i, gpio.LOW)
        # time.sleep(delay_time)
            
    except KeyboardInterrupt:
        gpio.cleanup() #釋放 GPIO 資源
        break #結束程式



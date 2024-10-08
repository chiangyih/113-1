import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)  #設為 BCM 模式
gpio.setup(17, gpio.OUT) #設定 GPIO17 為輸出

delay_time=0.5 #延遲時間

while True:
    try:
        gpio.output(17, gpio.HIGH) #點亮 LED
        time.sleep(delay_time) #延遲 delay_time秒
        gpio.output(17, gpio.LOW) #熄滅 LED
        time.sleep(delay_time) #延遲 delay_time 秒
    except KeyboardInterrupt:
        gpio.cleanup() #釋放 GPIO 資源
        break
  



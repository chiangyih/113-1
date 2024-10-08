import RPi.GPIO as gpio
import time
led=17 #設定 LED 接腳
delay_time=0.05 #延遲時間

gpio.setmode(gpio.BCM) 
gpio.setup(led,gpio.OUT)
l1=gpio.PWM(led,100)  #設定 PWM 頻率為 100Hz

while True:
	try:
		for a in range(0,101,2): #設定迴圈，dutycycle從0~100，間隔2
			l1.start(a)  #啟動 PWM
			time.sleep(delay_time) #延遲 delay_time 秒
	except KeyboardInterrupt:
            gpio.cleanup()
            break

		


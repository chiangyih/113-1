import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM) 
delay_time=0.03 #延遲時間

led=[17,27,22,10,9,11,5,6] #設定 LED 接腳,使用list(串列)儲存
for i in led:
	gpio.setup(i, gpio.OUT) #設定上述串列中的每個元素為輸出

pwm_leds = [gpio.PWM(pin, 100) for pin in led] #設定 PWM 頻率為 100Hz, 使用串列生成式, 產生一個包含8個PWM物件的串列, 串列中的每個PWM物件對應一支LED, 串列中的每個PWM物件的GPIO腳位對應led串列中的每個元素

for pwm_led in pwm_leds:
	pwm_led.start(0) #啟動 PWM, 設定dutycycle為0
 
while True:
	try:
		for a in range(0,101,2): #設定迴圈，dutycycle從0~100，間隔2
			for pwm_led in pwm_leds: #迴圈讀取pwm_leds串列中的每個PWM物件, 串列中的每個PWM物件對應一支LED, 串列中的每個PWM物件的GPIO腳位對應led串列中的每個元素
				pwm_led.start(a) #啟動 PWM, 設定dutycycle為a, 亮度隨a值改變, a值從0~100, 間隔2,
			time.sleep(delay_time) #延遲 delay_time 秒
		for a in range(100,-1,-2): #設定迴圈，dutycycle從100~0，間隔-2
			for pwm_led in pwm_leds:
				pwm_led.start(a)
			time.sleep(delay_time)
	except KeyboardInterrupt:
		for pwm_led in pwm_leds:
			pwm_led.stop() #停止 PWM
		gpio.cleanup() #釋放 GPIO 資源
		break #結束程式
		


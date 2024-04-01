import os
import time
import adafruit_dht
import board
import busio
import adafruit_ssd1306
import digitalio
import prometheus_client
from prometheus_client import start_http_server, Gauge
from PIL import Image, ImageDraw, ImageFont

#Display Param
WIDTH = 128
HEIGHT = 64
BORDER = 5

#init
print("Initializing Sensors...")
dht22 = adafruit_dht.DHT22(board.D17)
mq135 = digitalio.DigitalInOut(board.D27)
print("Starting Prometheus Client... on PORT 8599")
start_http_server(8599)
prom_url = "\033[4m" + "http://localhost:8599/metrics" + "\033[0m"
i2c = board.I2C()
oled_reset = digitalio.DigitalInOut(board.D4)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)
oled.contrast(1)

#instrument
TEMP_1C = Gauge('DHT22_TEMP_C', 'Current Temperature in C')
TEMP_1F = Gauge('DHT22_TEMP_F', 'Current Temperature in F')
HUMIDITY_1 = Gauge('DHT22_HUMIDITY', 'Current Humidity')
Air_Quality_inf = Gauge('MQ135_AirQuality', 'Current Air Quality')

oled.fill(0)
oled.show()

image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,oled.width,oled.height), outline=255, fill=255)
font = ImageFont.load_default()

while True:
	try:
		draw.rectangle((0,0, oled.width, oled.height), outline=0, fill=0)

		temp_c = dht22.temperature
		temp_f = temp_c * (9 / 5) + 32
		humidity = dht22.humidity
		TEMP_1C.set(temp_c)
		TEMP_1F.set(temp_f)
		HUMIDITY_1.set(humidity)
		if mq135.value:
			Air_Q = "Normal"
			Air_Quality_inf.set(0)
		else:
			Air_Q = "Abnormal"
			Air_Quality_inf.set(1)

		print('Temp: {:.1f}C / {:.1f}F | Humidity: {} | Air Quality: {}'.format(temp_c, temp_f, humidity, Air_Q))

		#OLED
		draw.text((0,0),"Temperature: {:.1f}C".format(temp_c), font=font, fill=255)
		draw.text((0,16),"Temperature: {:.1f}F".format(temp_f), font=font, fill=255)
		oled.image(image)
		oled.show()
		time.sleep(2)
		draw.rectangle((0,0, oled.width, oled.height), outline=0, fill=0)
		draw.text((0,32),"Humidity: " + str(humidity), font=font, fill=255)
		draw.text((0,48),"Air Quality: " + Air_Q, font=font, fill=255)
		oled.image(image)
		oled.show()

	except (KeyboardInterrupt, RuntimeError) as e:
		if isinstance(e, RuntimeError):
			print(e)
		if isinstance(e, KeyboardInterrupt):
			print("EXIT")
			del dht22
			del mq135
	#WAIT
	time.sleep(2)
	#os.system('clear')

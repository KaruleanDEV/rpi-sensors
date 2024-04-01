# rpi-sensors
Sample python script to push sensors data to Prometheus for display in frontend like Grafana. 
If using Grafana Cloud, use the agent for your platform. https://github.com/grafana/agent and edit the yaml config with your auth.

Item List:
Raspberry Pi4 Model B
MQ135 Air Quality Sensors
DHT22 Humidity & Temperature (I would use alternative like SHT3x or SHT40 refer to https://www.airgradient.com/documentation/diy-v4/)
IC2 128x64 OLED using SSD1306 drivers

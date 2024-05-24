# rpi-sensors ![Static Badge](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)![Static Badge](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)![Static Badge](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)
Python script to push sensors data to Prometheus for display in frontend like Grafana. 
If using Grafana Cloud, use the agent for your platform. https://github.com/grafana/agent and edit the yaml config with your auth.

### Item List:
+ Raspberry Pi4 Model B
+ MQ135 Air Quality Sensors
+ DHT22 Humidity & Temperature (I would use alternative like SHT3x or SHT40 refer to https://www.airgradient.com/documentation/diy-v4/)
+ IC2 128x64 OLED using SSD1306 drivers

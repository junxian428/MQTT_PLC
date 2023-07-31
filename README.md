# MQTT_PLC
Client to trigger (in Frontend_DB and run node express.js and visit localhost:3000 . https://github.com/junxian428/RealTime_Monitor_PLC_Python_Socket_HTML

Need to run client.py to keep prompt the PLC,

Secondly, need to run ./start.sh where the shell script to change to PUBSUBPLC.py provided by AWS IoT Core

Thirdly, you need to run client web by download https://github.com/junxian428/RealTime_Monitor_PLC_Python_Socket_HTML and run node express.js 
which will connect websocket (PUBSUBPLC) real time 


What this repository have accomplished?

![Untitled Diagram drawio (11)](https://github.com/junxian428/MQTT_PLC/assets/58724748/10753568-b58e-4f21-bb47-e81c937125b0)


System Design: 

One topic (declared in AWS) -> Many PLC 

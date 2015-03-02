#source: http://pdwhomeautomation.blogspot.com/2012/10/the-udp-interface-again.html
#source: http://stackoverflow.com/questions/9384247/android-python-get-gps-status
import android, string, time, socket

UDP_IP = '192.168.1.105'
UDP_PORT = 50000
INET_ADDR = (UDP_IP,UDP_PORT)

droid = android.Android()
droid.startLocating()
time.sleep(10)
coords = droid.readLocation()

#MESSAGE = "123,@?\0"

#TODO Find out how SensorUDP gathers and sends the data to Matlab
MESSAGE = {
	'SENSORTYPE':'Android', 
	'Latitude': coords.latitude,
	'Longitude', coords.longitude
	}

#compact the json to send via UDP
MESSAGE = MESSAGE.toString()

print "UDP target IP:", UDP_IP 
print "UDP target port:", UDP_PORT 
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

#send message every 10 seconds
while True:
  sock.sendto(MESSAGE, INET_ADDR)
  print "done sending udp"
  time.sleep(10)

import socket
import os


#rec_ip = "192.168.10.101"
rec_ip = "127.0.0.1"
rec_port = 9090   # port > 6000 are generally free to use

# calling udp protocol
# socket.AF.INET = IPV4 , socket.SOCK_DGRAM = UDP

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

# this section is common for both sender and receiver
# binding ip and port

s.bind((rec_ip,rec_port))   # providing a way to connect

while 3 > 2:
    rec_data = s.recvfrom(100)
    print rec_data[0]
    # buffersize = 1
   # checking for command
if os.system(rec_data[0] == 0):
    print("success")
    s.sendto("right command",rec_data[1])
else:
    s.sendto(rec_data[0]+"not found",rec_data[1])




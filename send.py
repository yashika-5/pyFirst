import socket


#rec_ip = "192.168.10.101"
rec_ip = "127.0.0.1"
rec_port = 9090   # port > 6000 are generally free to use

# calling udp protocol
# socket.AF.INET = IPV4 , socket.SOCK_DGRAM = UDP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#sending msg to target

while True:

    data = raw_input("enter msg :")
    s.sendto(data,(rec_ip,rec_port))
    # this is from receiving sender
    #print(s.recvfrom(10))
    print s.recvfrom(100)


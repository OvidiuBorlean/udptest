import socket


Index               = 0
msgFromClient       = "Hello UDP Server"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024


# Create a UDP socket at client side
while Index <= 1000:

  UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

  # Send to server using created UDP socket

  UDPClientSocket.sendto(bytesToSend, serverAddressPort)

  msgFromServer = UDPClientSocket.recvfrom(bufferSize)

  msg = "Message from Server {}".format(msgFromServer[0])
  print(Index)
  Index += 1
  #print(msg)

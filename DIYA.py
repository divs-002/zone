import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "192.168.100.6"
port = 8002
client.connect((server_ip, port))
print(f"connected to :{server_ip}:{port}")

while True:
    msg = input("Enter msg:")
    client.send(msg.encode('utf-8'))
    response = client.recv(1024).decode()
    print(f"server:{response}")
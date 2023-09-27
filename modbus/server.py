import socket
import sys
import struct

class ModbusServer:
    def __init__(self, dest, port):
        self.server_port = port
        self.server_addr = dest
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.server_addr, self.server_port))

    def forward_message(self, msg, addr_port_tuple):
        forward_msg = "forward_message" + " " + msg
        self.sock.sendto(forward_msg.encode("utf-8"), addr_port_tuple)

    def process_modbus_frame(self, frame, addr_port_tuple):
        # Simulação: analisar o quadro Modbus RTU simulado
        data = struct.unpack(">BBH", frame.encode("latin-1"))
        if data[0] == 1 and data[1] == 3:
            # Simulação: responder com um valor de registro holding simulado
            response_data = struct.pack(">BBHH", 1, 3, 2, 5678)  # Endereço, Função, Número de bytes, Dado
            self.forward_message(response_data.decode("latin-1"), addr_port_tuple)

    def start(self):
        while True:
            client_message, client_addr_port = self.sock.recvfrom(4096)
            client_message = client_message.decode("utf-8")
            datalist = client_message.split()

            if datalist[0] == "join":
                print(datalist[1], "joined the chatroom")

            elif datalist[0] == "msg":
                sender_client = datalist[1]
                client = datalist[2]
                actual_message = " ".join(datalist[3:])
                actual_message = sender_client + ": " + actual_message
                self.forward_message(actual_message, (client_addr_port))

            elif datalist[0] == "modbus_frame":
                modbus_frame = datalist[1].encode("latin-1")
                self.process_modbus_frame(modbus_frame, (client_addr_port))

if __name__ == "__main__":
    PORT = 11000
    DEST = "localhost"

    print("Server started. Address:", DEST, "Port:", PORT)
    SERVER = ModbusServer(DEST, PORT)
    try:
        SERVER.start()
    except (KeyboardInterrupt, SystemExit):
        exit()

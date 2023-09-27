import socket
import sys
import random
import struct

class Client:
    def __init__(self, username, dest, port):
        self.server_addr = dest
        self.server_port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("", random.randint(10000, 40000)))
        self.name = username

    def join(self):
        join_message = "join" + " " + self.name
        self.sock.sendto(join_message.encode("utf-8"), (self.server_addr, self.server_port))

    def send_message(self, msg):
        # Simula um quadro Modbus RTU com um único registro holding de 16 bits
        modbus_frame = struct.pack(">BBH", 1, 3, 1234)  # Endereço, Função, Dado (registro 1234)
        actual_message = "msg" + " " + modbus_frame.decode("latin-1")
        self.sock.sendto(actual_message.encode("utf-8"), (self.server_addr, self.server_port))

    def start(self):
        self.join()

        while True:
            userinput = input("Digite sua mensagem ('msg mensagem'): ")

            input_recv = userinput.split()

            if input_recv[0] == "msg":
                self.send_message(" ".join(input_recv[1:]))
            else:
                print("Formato de entrada incorreto. Use 'msg mensagem'.")

    def receive_handler(self):
        while True:
            server_message, server_addr_port = self.sock.recvfrom(4096)
            server_message = server_message.decode("utf-8")
            datalist = server_message.split()

            if datalist[0] == "forward_message":
                modbus_frame = datalist[1].encode("latin-1")
                # Analise o quadro Modbus RTU simulado
                data = struct.unpack(">BBH", modbus_frame)
                if data[0] == 1 and data[1] == 3:
                    print(f"Registro holding lido: {data[2]}")

if __name__ == "__main__":
    DEST = '35.174.244.165'
    PORT = 8333

    # USER_NAME = input("Digite seu nome de usuário: ")

    S = Client("SeuNome", DEST, PORT)

    try:
        S.receive_handler()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()

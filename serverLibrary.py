import socket


#Package struct: packageType@packageData@MessageEnd

class client():

    def __init__(self):
        self.sock = socket.socket()

    def connect(ip, port):
        self.sock.connect((ip, int(port)))

    def disconnect():
        self.sock.close()

    def getData(data):
        dataType, dataValue = encodeData(encode(data, "utf-8"))

    def encodeData(data):
        data = data.split("@")
        return data[0], data[1]
        

    

class server():
    
    def __init__(self, ip, adress, listenValue):
        self.ip = ip
        self.adress = adress
        self.sock = socket.socket()
        self.sock.bind((ip,int(port)))
        self.sock.listen(int(listenValue))

    """def recieveData(data):
        stringData = encode(data, "utf-8")
        stringData = stringData.split("@")
        stringData = stringData[0]"""
    def sendData(data):
        self.conn.send(bytes(data))

    def waitForConnection():
        self.conn, self.addr = self.sock.accept()

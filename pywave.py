import socket
import json


class pyWave:

    configStr = "{ 'enableRawOutput': 'enableRawOutput', 'format': 'Json'}"
    configByte = configStr.encode()
    val = 0

    def __init__(self, _host, _port):
        self.host = _host
        self.port = _port

    def connect(self):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the Thinkgear Connector
        client.connect((self.host, self.port))
        # calling this client to implement elsewhere

        client.send(self.configByte)

        return client

    def readData(self, _client):


        try:
            data = _client.recv(1024)

            data_json = json.loads(data)
            e_sense_data = data_json["eSense"]


            return self.val

        except Exception as e:
            print(e)
            return None



# testing code

if __name__ == '__main__':

    pywave = pyWave("localhost", 13854)
    client = pywave.connect()

    print("Waiting for data")
    while True:
        val = pywave.readData(client)
        print(val)



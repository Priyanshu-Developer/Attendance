from Secure import Main
import socket
import ssl
import time
from os.path import dirname,join
class ClientConnection:

    __host = "192.168.43.36"
    __port = 8080
    server=join(dirname(__file__),"server_cert.pem")
    client = join (dirname(__file__),"kwnjknwkdkwnknkw_cert.pem")
    key = join (dirname(__file__),"kwnjknwkdkwnknkw_key.pem")

    def __init__(self):
        sock = socket.create_connection((self.__host, self.__port))
        context = ssl.SSLContext()
        context.load_verify_locations(ClientConnection.server)
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_cert_chain(certfile=ClientConnection.client,keyfile=ClientConnection.key)
        ssock = context.wrap_socket(sock)
        self.secure = Main()
        # self.Authenticator(ssock)

    # "countryName:IN ,organizationName:00000000000000000000 ,organizationalUnitName:ProjectHID ,commonName:ProjectHid ,organizationalUnitName:ProjectHID"
    # def Authenticator(self, conn):
    #     print("started auth")
    #     __file = open("Auth_files/server.txt", "r")
    #     __cert = conn.getpeercert()
    #     print(__cert)
    #     __data = __file.readlines()
    #     print(__data[0].replace("\n",""))
    #     __auth = self.secure.Decryption(__data[0].replace("\n", ""))
    #     print(__auth)
    #     print("before while")
    #     conn.send(__data[1].replace("\n", "").encode("utf-16"))
    #     __dic = {}
    #     for i in __auth.split(","):
    #         val = i.split(':')
    #         __dic[val[0]] = val[1]
    #     print("done")
    #     time.sleep(3)
    #     if __cert["issuer"][0][0][1] == __dic["countryName"]:
    #         return False
    #
    #     elif __cert["issuer"][2][0][1] == __dic["organizationName"]:
    #         return False
    #     elif __cert["issuer"][3][0][1] == __dic["organizationalUnitName"]:
    #         return False
    #
    # def Start_communication(self, conn):
    #     if not self.Authenticator(conn):
    #         conn.close()
    #     else:
    #         self.reciver(conn)
    #
    # def reciver(self, conn):
    #
    #     maindata = bytes()
    #     data = conn.recv(2048)
    #     while True:
    #         if len(data) < 2048:
    #             maindata += data
    #             print(len(data))
    #             break
    #         else:
    #             maindata += data
    #             print(len(data))
    #             data = conn.recv(2048)
    #     return maindata


def main():
    ClientConnection()
    return "succesfull"

#
# {'subject': ((('countryName', 'IN'),), (('stateOrProvinceName', 'Jharkhand'),), (('organizationName', '00000000000000000000'),),
# (('organizationalUnitName', 'ProjectHID'),), (('localityName', 'Jamshedpur'),), (('commonName', 'ProjectHid'),),
# (('emailAddress', 'projecthid2002@gmial.com'),)), 'issuer': ((('countryName', 'IN'),), (('stateOrProvinceName', 'Jharkhand'),),
# (('organizationName', '00000000000000000000'),), (('organizationalUnitName', 'ProjectHID'),), (('localityName', 'Jamshedpur'),),
# (('commonName', 'ProjectHid'),), (('emailAddress', 'projecthid2002@gmial.com'),)), 'version': 1, 'serialNumber': '00',
#  'notBefore': 'Feb 11 14:04:31 2022 GMT', 'notAfter': 'Feb 11 14:04:31 2023 GMT'}

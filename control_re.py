import serial
import struct

class Tip:
        def __init__(self,port = 'COM1',rate = 38400,timeout = 3):
                '''初始化串口'''
                self.port = serial.Serial(port,rate,timeout)
                
        def send(self,msg = "",addr = 1): # addr:0-0xff,默认为1
                '''封装并发送帧'''
                head = int("AA")
                
        def check(self):
                '''接收返回状态码并处理'''
                
        def command(self):
                '''处理指令'''
                def It(vel=16000, power=100, mode=0):
                        '''初始化移液枪位置'''
                        msg = "It" + str(vel) + "," + str(power) + "," + str(mode)
                        self.send(msg)
                
def Pack(msg):
        '''数据打包'''
        head = bytes([0xAA])
        data = struct.pack('>b',msg[0])
        

def Unpack(Data):
        '''数据解包'''
        
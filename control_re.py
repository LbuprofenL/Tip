import serial
import struct
import tools
import serial.tools.list_ports


class Tip:
    tip_count = 0

    def __init__(self):
        '''初始化串口'''
        if Tip.tip_count == True:
            return False

        ports_list = list(serial.tools.list_ports.comports())
        if len(ports_list) <= 0:
            print("无串口设备")
            # TODO 设计状态码
        else:
            # TODO 设计返回值
            print("可使用的串口设备如下：")
            for comport in ports_list:
                print(comport[0], comport[1])
        Tip.tip_count += 1

    def open_serial(self, port='COM1', rate=38400):
        '''打开端口'''
        self.ports = serial.Serial(port, rate)

    def send(self, msg="", addr=1):  # addr:0-0xff,默认为1
        '''封装并发送帧'''
        pkg = tools.Pack_command(msg, addr)
        # print(pkg)
        if self.ports.is_open:
            write_len = self.ports.write(pkg)
        else:
            # TODO 设计返回值
            print("打开串口失败.")
            return False
        return True

    def check(self):
        '''接收返回状态码并处理'''

    def It(self, vel=16000, power=100, mode=0):
            '''初始化移液枪位置'''
            msg = "It" + str(vel) + "," + str(power) + "," + str(mode)
            self.send(msg)

    def Ia(self, vol, imbi_vel=500, stop_vel=10):
            '''吸液'''
            msg = "Ia" + str(vol) + "," + str(imbi_vel) + "," + str(stop_vel)
            self.send(msg)

    def Da(self, vol, back_vol=0, run_vel=500, stop_vel=10):
            # 排液
            msg = "Da" + str(vol) + "," + str(back_vol) + \
                "," + str(run_vel) + "," + str(stop_vel)
            self.send(msg)

    def Dt(self, vel=16000, mode=0):
            # 排除tip头
            msg = "Dt" + str(vel) + "," + str(mode)
            self.send(msg)

    def Ld(self, mode=1, timeout=10000):
            # 页面检测
            msg = "Ld" + str(mode) + "," + str(timeout)
            self.send(msg)


if __name__ == '__main__':
    tip = Tip()
    tip.open_serial()
    tip.It(16000, 100, 0)
    tip.Ia(10000,200,10)
    tip.Da(1000,500,200,100)
    tip.Ld(1,5000)

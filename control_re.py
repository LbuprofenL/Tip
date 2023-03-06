import serial
import struct
import tools
import serial.tools.list_ports
PKG_SIZE = 5
addr = 1

class Tip:
    tip_count = 0

    def __init__(self):
        '''初始化串口'''
        if Tip.tip_count == True:
            raise Exception("超过最多打开设备数量.")

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

    def recv(self):
        '''监听返回的数据'''
        if self.ports.is_open:
            pkg = self.ports.read(PKG_SIZE)
            print(pkg)
            return pkg
        else:
            raise Exception
        
        
    def It(self, vel=16000, power=100, mode=0):
            '''初始化移液枪位置'''
            msg = "It" + str(vel) + "," + str(power) + "," + str(mode)
            self.send(msg)
            try:
                pkg = self.recv()
                try:
                    status, data = tools.Unpack(pkg,addr)
                    try: 
                        tools.check_status(status)
                    except:
                        print("")
                except:
                    print("解包出错,请重试.")
            except:
                print("端口未打开,请打开后重试.")
            

    def Ia(self, vol, imbi_vel=500, stop_vel=10):
            '''吸液'''
            msg = "Ia" + str(vol) + "," + str(imbi_vel) + "," + str(stop_vel)
            self.send(msg)
            try:
                pkg = self.recv()
                try:
                    status, data = tools.Unpack(pkg, addr)
                    try:
                        tools.check_status(status)
                    except:
                        print("")
                except:
                    print("解包出错,请重试.")
            except:
                print("端口未打开,请打开后重试.")

    def Da(self, vol, back_vol=0, run_vel=500, stop_vel=10):
            # 排液
            msg = "Da" + str(vol) + "," + str(back_vol) + \
                "," + str(run_vel) + "," + str(stop_vel)
            self.send(msg)
            try:
                pkg = self.recv()
                try:
                    status, data = tools.Unpack(pkg, addr)
                    try:
                        tools.check_status(status)
                    except:
                        print("")
                except:
                    print("解包出错,请重试.")
            except:
                print("端口未打开,请打开后重试.")

    def Dt(self, vel=16000, mode=0):
            # 排除tip头
            msg = "Dt" + str(vel) + "," + str(mode)
            self.send(msg)
            try:
                pkg = self.recv()
                try:
                    status, data = tools.Unpack(pkg, addr)
                    try:
                        tools.check_status(status)
                    except:
                        print("")
                except:
                    print("解包出错,请重试.")
            except:
                print("端口未打开,请打开后重试.")

    def Ld(self, mode=1, timeout=10000):
            # 液面检测
            # TODO 模式0
            msg = "Ld" + str(mode) + "," + str(timeout)
            self.send(msg)
            if mode == 1:
                try:
                    pkg = self.recv()
                    try:
                        status, data = tools.Unpack(pkg, addr)
                        try:
                            tools.check_status(status)
                        except:
                            print("")
                    except:
                        print("解包出错,请重试.")
                except:
                    print("端口未打开,请打开后重试.")
            else:
                # TODO
                return


if __name__ == '__main__':
    tip = Tip()
    tip.open_serial()
    for i in range(0,2):
        tip.It(16000, 100, 0)
        
    # tip.Ia(10000,200,10)
    # tip.Da(1000,500,200,100)
    # tip.Ld(1,5000)

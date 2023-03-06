import serial
import tools
import serial.tools.list_ports
import config


class Tip:
    tip_count = 0

    def __init__(self,port='COM1',rate=38400):
        '''初始化串口'''
        self.tip_count = self.tip_count + 1

    def link_serial(self, port='COM1', rate=38400):
        '''打开端口'''
        output = "端口连接成功"
        ports_list = list(serial.tools.list_ports.comports())
        if len(ports_list) <= 0:
            output = "无串口设备"
        else:
            try:
                self.ports = serial.Serial(port, rate)
            except:
                output = "端口连接失败"
        return output
    
    def close_serial(self):
        self.ports.close()
        if self.ports.is_open:
            output = "关闭端口失败"
        else:
            output = "关闭端口成功"
        return output
    
    def send(self, msg="", addr=1):  # addr:0-0xff,默认为1
        '''封装并发送帧'''
        out = "发送成功"
        try:
            pkg = tools.Pack_command(msg, addr)
        # print(pkg)
        except:
            out = "发送失败"
        return out

    def recv(self):
        '''监听返回的数据'''
        if self.ports.is_open:
            pkg = self.ports.read(config.PKG_SIZE)
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
                    status, data = tools.Unpack(pkg,config.ADDR)
                    out = tools.check_status(status)
                except:
                    out="解包出错,请重试."
            except:
                out="端口未打开,请打开后重试."
            return out
            

    def Ia(self, vol, imbi_vel=500, stop_vel=10):
            '''吸液'''
            msg = "Ia" + str(vol) + "," + str(imbi_vel) + "," + str(stop_vel)
            self.send(msg)
            try:
                pkg = self.recv()
                try:
                    status, data = tools.Unpack(pkg, config.ADDR)
                    out = tools.check_status(status)
                except:
                    out="解包出错,请重试."
            except:
                out="端口未打开,请打开后重试."
            return out

    def Da(self, vol, back_vol=0, run_vel=500, stop_vel=10):
            # 排液
            msg = "Da" + str(vol) + "," + str(back_vol) + \
                "," + str(run_vel) + "," + str(stop_vel)
            self.send(msg)
            try:
                pkg = self.recv()
                try:
                    status, data = tools.Unpack(pkg, config.ADDR)
                    out = tools.check_status(status)
                except:
                    out="解包出错,请重试."
            except:
                out="端口未打开,请打开后重试."
            return out

    def Dt(self, vel=16000, mode=0):
            # 排除tip头
            msg = "Dt" + str(vel) + "," + str(mode)
            self.send(msg)
            try:
                pkg = self.recv()
                try:
                    status, data = tools.Unpack(pkg, config.ADDR)
                    out = tools.check_status(status)
                except:
                    out="解包出错,请重试."
            except:
                out="端口未打开,请打开后重试."
            return out

    def Ld(self, mode=1, timeout=10000):
            # 液面检测
            # TODO 模式0
            msg = "Ld" + str(mode) + "," + str(timeout)
            self.send(msg)
            try:
                pkg = self.recv()
                try:
                    status, data = tools.Unpack(pkg,config.ADDR)
                    out = tools.check_status(status)
                except:
                        out="解包出错,请重试."
            except:
                    out="端口未打开,请打开后重试."
            return out


'''if __name__ == '__main__':
    tip = Tip()
    tip.link_serial()
    for i in range(0,2):
        tip.It(16000, 100, 0)
        '''
    # tip.Ia(10000,200,10)
    # tip.Da(1000,500,200,100)
    # tip.Ld(1,5000)

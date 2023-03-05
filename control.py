import time
import serial

#RS232指令，使用一个字典，把需要被操作的RS232命令封装到一起
RS232_Command = {
	# 'It': 'It', # 初始化
	# 'Ia': 'Ia', # 吸液
	# 'Da': 'Da', # 排液
	# 'Dt': 'Dt', # 去掉TIP头
	# 'Ld': 'Ld', # 液面探测
}

#把字符串类型转换为bytes数据流进行发送，RS232命令发送函数

def It(vel=16000, power = 100, mode = 0):
        '''初始化移液枪位置'''
        command = "It" + str(vel) + ","+ str(power) + "," + str(mode)
        serial_sent_utf(command)

def Ia(vol, imbi_vel = 500, stop_vel = 10):
	'''吸液'''
	command = "Ia" + str(vol) + "," + str(imbi_vel) + "," + str(stop_vel)
	serial_sent_utf(command)

def Da(vol, back_vol = 0, run_vel = 500, stop_vel = 10):
        # 排液
	command = "Da" + str(vol) + "," + str(back_vol) +"," + str(run_vel) + "," + str(stop_vel)
	serial_sent_utf(command)

def Dt(vel=16000,mode = 0):
        # 排除tip头
	command = "Dt" + str(vel) + "," + str(mode)
	serial_sent_utf(command)

def Ld(mode = 1,timeout = 10000):
        # 页面检测
        command = "Ld" + str(mode) + "," + str(timeout)
        serial_sent_utf(command)

def serial_sent_utf(command):
	#从字典里获取对应的RS232命令
	var = "%s" % command
	#encode()函数是编码，把字符串数据转换成bytes数据流
	ser.write(var.encode())
	data = ser.read(1)
	# 获取指令的返回值，并且进行类型转换，转换为字符串后便可以进行字符串对比，因而便可以根据返回值进行判断是否执行特定功能
	data = str(data, encoding="utf-8")
	return data


if __name__ == '__main__':
	#实现串口的连接
	ser = serial.Serial('COM1', 38400, timeout=3)
	It()
	Ia(25)
	Da(25)
	Dt()
	Ld()

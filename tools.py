import struct

def check_sum(msg):
        
    check = sum(msg)  # 计算校验和
    check = check & 0xff  # 与计算 保留后8位
    #check = check.to_bytes(1, "big")  # 转化为1个字节
    return check


def Pack_command(msg, addr):
	values = (170, addr, len(msg), msg.encode("utf-8"))
	#print(values)

	fmt = "> B B B" + str(len(msg))+"s"  # 格式

	packed_data = struct.pack(fmt, *values)

	check = check_sum(packed_data).to_bytes(1,"big")
	packed_data = packed_data + check
	#print(packed_data)

	return(packed_data)

# TODO 设计解包程序
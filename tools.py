import struct

def Pack(msg, addr=1):
	values = (170, addr, len(msg), msg.encode("utf-8"))
	#print(values)

	fmt = "> B B B" + str(len(msg))+"s"  # 格式

	packed_data = struct.pack(fmt, *values)

	check = sum(packed_data)  # 计算校验和
	check = check & 0xff  # 与计算 保留后8位
	check = check.to_bytes(1, "big")  # 转化为1个字节
	packed_data = packed_data + check
	#print(packed_data)

	return(packed_data)

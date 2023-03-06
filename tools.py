import struct


def check_sum(msg):

    check = sum(msg)  # 计算校验和
    check = check & 0xff  # 与计算 保留后8位
    # check = check.to_bytes(1, "big")  # 转化为1个字节
    return check


def Pack_command(msg, addr):
    '''将指令封装成帧'''
    values = (170, addr, len(msg), msg.encode("utf-8"))
    # print(values)

    fmt = "> B B B" + str(len(msg))+"s"  # 格式

    packed_data = struct.pack(fmt, *values)

    check = check_sum(packed_data).to_bytes(1, "big")
    packed_data = packed_data + check
    # print(packed_data)

    return(packed_data)


def Unpack(pkg, addr=1):
    "将返回的帧解包"
    fmt = "> B B B B" + str((len(pkg)-5)) + "s B"
    msg = struct.unpack_from(fmt, pkg)

    # 校验帧头
    if msg[0] != 85:
        raise Exception
    # 校验地址
    if addr != msg[1]:
        raise Exception
    # 判断返回数据长度
    if len(pkg)-5 == 0:
        check_fmt = "> B B B B"
    else:
        check_fmt = "> B B B B" + str(len(pkg)-5) + "s"

    check_values = msg[:len(pkg)-1]
    check_msg = struct.pack(check_fmt, *check_values)
    # 检验校验和
    if msg[len(pkg)] != check_sum(check_msg):
        raise Exception
    # 返回状态处理
    status = msg[2]
    # 返回数据
    data_len = msg[3]
    data = str(msg[4:4+data_len-1])
    # print(type(data))
    return status, data


def check_status(status):
    '''接收返回状态码并处理'''
    if status in range(0, 9):
        if status == 0:
            print("设备空闲")
        elif status == 1:
            print("设备忙")
        elif status == 2:
            print("执行成功")
        elif status == 3:
            print("执行完成")
        elif status == 4:
            print("探测到液面")
        else:
            print("未定义状态值")
    elif status in range(10, 19):
        if status == 10:
            print("参数超出范围")
        elif status == 11:
            print("参数错误")
        elif status == 12:
            print("指令语法错误")
        elif status == 13:
            print("无效指令")
        elif status == 14:
            print("地址错误")
        elif status == 15:
            print("禁止写")
        elif status == 16:
            print("禁止读")
        elif status == 17:
            print("未初始化")
        else:
            print("未定义状态值")
    elif status >= 20:
        if status == 20:
            print("未检测到TIP头报警")
        elif status == 21:
            print("顶出TIP头报警")
        elif status == 22:
            print("超时报警")
        elif status == 23:
            print("吸气凝块检测报警")
        elif status == 24:
            print("吸气气泡检测报警")
        elif status == 25:
            print("吸气空检测报警")
        elif status == 50:
            print("电机堵转错误")
        elif status == 51:
            print("驱动器故障")
        elif status == 52:
            print("零位光耦故障")
        elif status == 53:
            print("TIP头光耦错误")
        elif status == 54:
            print("传感器错误")
        elif status == 55:
            print("存储错误")
        else:
            print("未定义状态值")

from tip import Tip

if __name__ == '__main__':
	while input() != "quit":
		Atip = Tip()
		cmd = input("请输入命令:")
		print(cmd)
		input_list = cmd.split(',')
		len_ele = len(input_list)
		print(input_list)
		print(len_ele)
		if input_list[0] == "link":
			if len_ele == 1:
				out = Atip.link_serial()
			elif len_ele == 2:
				out = Atip.link_serial(input_list[1])
			elif len_ele == 3:
				out = Atip.link_serial(input_list[1],int(input_list[2]))
			else:
				out = "参数太多请重试"
			print(out)

		if input_list[0] == "close":
			out = Atip.close_serial()
			print(out)
		if input_list[0] == "It":
			if len_ele == 1:
				out = Atip.It()
			elif len_ele == 2:
				out = Atip.It(int(input_list[1]))
			elif len_ele == 3:
				out = Atip.It(int(input_list[1]),int(input_list[2]))
			elif len_ele == 4:
				out = Atip.It(int(input_list[1]),int(input_list[2]),int(input_list[3]))
			else:
				out = "参数太多请重试"
			print(out)
		if input_list[0] == "Ia":
			if len_ele == 1:
				out = "参数太少请重试"
			elif len_ele == 2:
				out = Atip.Ia(int(input_list[1]))
			elif len_ele == 3:
				out = Atip.Ia(int(input_list[1]),int(input_list[2]))
			elif len_ele == 4:
				out = Atip.Ia(int(input_list[1]),int(input_list[2]),int(input_list[3]))
			else:
				out = "参数太多请重试"
			print(out)
		if input_list[0] == "Da":
			if len_ele == 1:
				out = "参数太少请重试"
			elif len_ele == 2:
				out = Atip.Da(int(input_list[1]))
			elif len_ele == 3:
				out = Atip.Da(int(input_list[1]),int(input_list[2]))
			elif len_ele == 4:
				out = Atip.Da(int(input_list[1]),int(input_list[2]),int(input_list[3]))
			elif len_ele == 5:
				out = Atip.Da(int(input_list[1]),int(input_list[2]),int(input_list[3]),int(input_list[4]))			
			else:
				out = "参数太多请重试"
			print(out)
		if input_list[0] == "Dt":
			if len_ele == 1:
				out = Atip.Dt()
			elif len_ele == 2:
				out = Atip.Dt(int(input_list[1]))
			elif len_ele == 3:
				out = Atip.Dt(int(input_list[1]),int(input_list[2]))
			else:
				out = "参数太多请重试"
			print(out)
		if input_list[0] == "Ld":
			if len_ele == 1:
				out = Atip.Ld()
			elif len_ele == 2:
				out = Atip.Ld(int(input_list[1]))
			elif len_ele == 3:
				out = Atip.Ld(int(input_list[1]),int(input_list[2]))
			else:
				out = "参数太多请重试"
			print(out)
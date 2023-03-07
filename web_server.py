from flask import Flask,request
from tip import Tip
import json

app = Flask(__name__)

# 只接受POST方法访问

class TipApi():
    tip = Tip("COM1", 38400)

    @app.route("/test_1.0", methods=["POST"])
    def check(self):
        # 默认返回内容
        return_dict = {'return_code': '200',
                   'return_info': '处理成功', 'result': False}
        # 判断传入的json数据是否为空
        if request.get_data() is None:
            return_dict['return_code'] = '5004'
            return_dict['return_info'] = '请求参数为空'
            return json.dumps(return_dict, ensure_ascii=False)
        # 获取传入的参数
        get_Data = request.get_data()
        # 传入的参数为bytes类型，需要转化成json
        get_Data = json.loads(get_Data)
        serial_cmd = get_Data.get("serial_cmd")
        if serial_cmd == "link":
            out = self.init()
        elif serial_cmd == "close":
            out = self.close()
        else:
            out="未定义串口操作"
        
        tip_cmd = get_Data("tip_cmd")
        num_param = get_Data.get("num_param")
        if tip_cmd == "It":
            input_list =num_param.split(',')
            len_ele = len(input_list)
            if len_ele == 1:
                out = self.It()
            elif len_ele == 2:
                out = self.It(input_list[1])
            elif len_ele == 3:
                out = self.It(input_list[1],int(input_list[2]))
            else:
                out = "参数太多请重试"
        elif tip_cmd == "Ia":
            input_list =num_param.split(',')
            len_ele = len(input_list)
            if len_ele == 1:
                out = "参数太少请重试"
            elif len_ele == 2:
                out = self.Ia(int(input_list[1]))
            elif len_ele == 3:
                out = self.Ia(int(input_list[1]),int(input_list[2]))
            elif len_ele == 4:
                out = self.Ia(int(input_list[1]),int(input_list[2]),int(input_list[3]))
            else:
                out = "参数太多请重试"
        elif tip_cmd == "Da":
            input_list =num_param.split(',')
            len_ele = len(input_list)
            if len_ele == 1:
                out = "参数太少请重试"
            elif len_ele == 2:
                out = self.Da(int(input_list[1]))
            elif len_ele == 3:
                out = self.Da(int(input_list[1]),int(input_list[2]))
            elif len_ele == 4:
                out = self.Da(int(input_list[1]),int(input_list[2]),int(input_list[3]))
            elif len_ele == 5:
                out = self.Da(int(input_list[1]),int(input_list[2]),int(input_list[3]),int(input_list[4]))			
            else:
                out = "参数太多请重试"
        elif tip_cmd == "Dt":
            input_list =num_param.split(',')
            len_ele = len(input_list)
            if len_ele == 1:
                out = self.Dt()
            elif len_ele == 2:
                out = self.Dt(int(input_list[1]))
            elif len_ele == 3:
                out = self.Dt(int(input_list[1]),int(input_list[2]))
            else:
                out = "参数太多请重试"
        elif tip_cmd == "Ld":
            input_list =num_param.split(',')
            len_ele = len(input_list)
            if len_ele == 1:
                out = self.Ld()
            elif len_ele == 2:
                out = self.Ld(int(input_list[1]))
            elif len_ele == 3:
                out = self.Ld(int(input_list[1]),int(input_list[2]))
            else:
                out = "参数太多请重试"
        else:
            out = "未定义tip命令"
        
        return_dict['result'] = out
        return json.dumps(return_dict, ensure_ascii=False)

    # 功能函数
    def init(self):
        out = self.tip.link_serial()
        return out
    
    def close(self):
        out = self.tip.close_serial()
        return out

    def It(self,vel=16000,power=100,mode=0):
        out = self.tip.It(vel,power,mode)
        return out
        
    def Ia(self, vol, imbi_vel=500, stop_vel=10):
        out = self.tip.Ia(vol,imbi_vel,stop_vel)
        return out
    
    def Da(self, vol, back_vol=0, run_vel=500, stop_vel=10):
        out = self.tip.Da(vol,back_vol,run_vel,stop_vel)
        return out
    
    def Dt(self, vel=16000, mode=0):
        out = self.tip.Dt(vel,mode)
        return out
    
    def Ld(self, mode=1, timeout=10000):
        out = self.tip.Ld(mode,timeout)
        return out
        
if __name__ == "__main__":
    ip ="127.0.0.1"
    port = 8888
    app.run(ip,port,debug=True)
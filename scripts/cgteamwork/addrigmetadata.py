#coding:utf-8
import os
import socket
import sys,uuid,json


#加载ct_plu库
# sys.path.append("D:/cgteamwork/bin/base/ct_plu/")
# sys.path.append("D:/cgteamwork/bin/base/")

from cgtw2 import *
import ct_plu
   
def addtask(args):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 10340))
    xx=json.dumps({"Cmd":1,"Args":args})
    s.send(xx.encode("utf-8"))
    msg = s.recv(1024)
    s.close()

    return msg.decode('utf-8')
def checktask(id):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(("127.0.0.1", 10340))

    xx=json.dumps({"Cmd":2,"Args":id})
    s.send(xx.encode("utf-8"))

    msg = s.recv(512)
    s.close()

    if msg.decode('utf-8') == "True":
        return True
    else:
        return False
def getScriptPath():
    _qntools = os.path.join(os.environ["QNTOOLS"],"scripts\\maya\\maya_rigmetadata.py")
    return _qntools
class ct_base(ct_plu.extend):
    def __init__(self):
        ct_plu.extend.__init__(self)#继承 

    def run(self, a_dict_data):
        t_argv          = ct_plu.argv(a_dict_data)  
        t_version_id    = t_argv.get_version_id()      #获取版本ID
        t_database      = t_argv.get_sys_database()    #获取数据库
        t_id_list       = t_argv.get_sys_id()          #获取界面选择ID列表
        t_module        = t_argv.get_sys_module()      #获取当前模块
        t_module_type   = t_argv.get_sys_module_type() #获取当前模块类型
        t_file_list     = t_argv.get_sys_file()        #获取拖入的源文件列表
        t_des_file_list = t_argv.get_sys_des_file()    #获取拖入后的目标文件列表
        t_folder_path   = t_argv.get_sys_folder()      #获取文件框所在的目录路径
        t_filebox_id    = t_argv.get_sys_filebox_id()  #获取文件框ID
        k_hello         = t_argv.get_argv_key("hello") #获取当前插件配置的参数值
        
        t_tw = tw()
        #-返回错误,拖入进程将不再往下继续执行

        infos=t_tw.task.get(t_database,t_module,t_id_list,['asset.entity','asset_type.entity'])[0]

        for idx,fm in enumerate(t_file_list):
            modify_file_name = os.path.splitext(fm)[0]+"_checked.ma"
            is_exister_modify = os.path.exists(modify_file_name)
            try:
                if is_exister_modify:
                    os.remove(modify_file_name)
            except:
                pass
            id = addtask("{} {} {} {}".format(getScriptPath(),fm,infos['asset.entity'],infos['asset_type.entity']))


            while checktask(id):
                time.sleep(3)


            if not os.path.exists(modify_file_name):
                return self.ct_false("失败")
            
            t_file_list[idx] = modify_file_name
        
if __name__ == "__main__":
    # 调试数据,前提需要在拖入进程中右键菜单。发送到调试
    t_debug_argv_dict=ct_plu.argv().get_debug_argv_dict()
    print(ct_base().run(t_debug_argv_dict))
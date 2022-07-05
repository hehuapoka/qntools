#coding:utf-8
from distutils.log import info
import os
import shutil
import sys,uuid,json
import traceback
import multiprocessing

#加载ct_plu库
# sys.path.append("D:/cgteamwork/bin/base/ct_plu/")
# sys.path.append("D:/cgteamwork/bin/base/")

from cgtw2 import *
import ct_plu
   
def runtask():
    os.system("cmd.exe /s /c \"C:\\Program Files\\Autodesk\\Maya2022\\bin\\mayapy.exe\" D:\\hehua\\dev\\QNTools\\scripts\\cgteamwork\\maya_rigmetadata.py")#maya_rigmetadata.
#ct_base类名是固定的
class ct_base(ct_plu.extend):
    def __init__(self):
        ct_plu.extend.__init__(self)#继承 

    def getMayaPyDir(self):
        try:
            MAYA_LOCATION = os.environ["MAYA_LOCATION"]
            return os.path.join(MAYA_LOCATION,"bin\\mayapy.exe")
        except:
            return "C:\\Program Files\\Autodesk\\Maya2022\\bin\\mayapy.exe"
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
        #t_tw.filebox.get(t_database,t_module,[t_filebox_id],)
        #infos=t_tw.task.get(t_database,t_module,t_id_list,['asset.entity','asset_type.entity'])
        for fm in t_file_list:

            runtask()

        return self.ct_false(self.getMayaPyDir())
        
if __name__ == "__main__":
    # 调试数据,前提需要在拖入进程中右键菜单。发送到调试
    t_debug_argv_dict=ct_plu.argv().get_debug_argv_dict()
    print(ct_base().run(t_debug_argv_dict))
#coding:utf-8
import os
import socket
import sys,uuid,json


#加载ct_plu库
# sys.path.append("D:/cgteamwork/bin/base/ct_plu/")
# sys.path.append("D:/cgteamwork/bin/base/")

from cgtw2 import *
import ct_plu,re
   


class ct_base(ct_plu.extend):
    def __init__(self):
        ct_plu.extend.__init__(self)#继承

    def InAssetLib(self,asset_name,asset_type,infos):
        for info in infos:
            if info['asset.entity'] == asset_name and info['asset.link_asset_type'] == asset_type:
                return True
        return False

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

        ids=t_tw.info.get_id(db=t_database, module="asset", filter_list=[])

        infos = t_tw.info.get(db=t_database, module="asset", id_list=ids, field_sign_list=['asset.entity','asset.link_asset_type'])


        for idx,fm in enumerate(t_file_list):
            filename = os.path.basename(fm)
            d=re.match(r"^([a-z]+)_([a-z]+)_[0-9]+\.[a-z]+$",filename,re.I)
            if d != None:
                asset_type = d.group(1)
                asset_name = d.group(2)
                if self.InAssetLib(asset_name,asset_type,infos):
                    target_dir = os.path.dirname(t_des_file_list[idx])
                    target_filename = os.path.join(target_dir,filename).replace("\\","/")
                    t_des_file_list[idx] = target_filename
                else:
                    return self.ct_false(u"失败,请检查你的文件名称")
            else:
                return self.ct_false(u"失败,请检查你的文件名称格式")
        
if __name__ == "__main__":
    # 调试数据,前提需要在拖入进程中右键菜单。发送到调试
    t_debug_argv_dict=ct_plu.argv().get_debug_argv_dict()
    print(ct_base().run(t_debug_argv_dict))
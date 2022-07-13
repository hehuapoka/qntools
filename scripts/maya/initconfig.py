import sys,os

plugin_root = os.environ['QNTOOLS'].replace("\\","/")
cgteamwork_python_lib = os.path.join(os.environ['CGTEAMWORK_LOCATION'],"bin\\base").replace("\\","/")

sys.path.append(plugin_root)
sys.path.append(cgteamwork_python_lib)

def icon_path(name):
    return plugin_root+"/icon/"+name
def icon_path2(id,disk_img:dict,name,index=0):
    ret=plugin_root+"/icon/"+name
    try:
        ret=disk_img[id][index].replace("\\","/")
    except:
        pass
    return ret
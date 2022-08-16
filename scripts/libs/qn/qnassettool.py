#coding:utf-8
from imp import reload
from itertools import count
import re
import qn.env as env
import qn.qnusdtool as qnusdtool
import qn.log as log
env.setCgTeamWorkEnv()


from cgtw2 import *


# new_log = log.Log("C:/test2.txt")

def InAssetLib(asset_name,asset_type,infos):
        for info in infos:
            if info['asset.entity'] == asset_name and info['asset.link_asset_type'] == asset_type:
                return True
        return False

def CacheUSDInAssetLibs(t_tw,db,filepath):
    ids=t_tw.info.get_id(db=db, module="asset", filter_list=[])

    infos = t_tw.info.get(db=db, module="asset", id_list=ids, field_sign_list=['asset.entity','asset.link_asset_type'])

    filename = os.path.basename(filepath)
    d=re.match(r"^([a-z]+)_([a-z]+)_([0-9]+)\.[a-z]+$",filename,re.I)
    if d != None:
        asset_type = d.group(1)
        asset_name = d.group(2)
        asset_number = d.group(3)
        if InAssetLib(asset_name,asset_type,infos):
            return {"asset_type":asset_type,"asset_name":asset_name,"asset_number":asset_number}
        else:
            return None
    else:
        return None


def GetUSDSetsProcessData(t_tw,db,files,target_dir,profix="lookdev"):
    # new_log.cout(json.dumps(files,indent=4))
    data = []
    for f in files:
        filedir = target_dir#os.path.dirname(f)

        d=CacheUSDInAssetLibs(t_tw,db,f)
        if d != None:
            asset_type = d["asset_type"]
            asset_name = d["asset_name"]
            asset_num = d["asset_number"]

            prim_path = "{}_{}_{}".format(asset_type,asset_name,asset_num)

            asset_ids=t_tw.info.get_id(t_tw.client.get_database(),"asset",[["asset.entity", "=",asset_name],["asset.link_asset_type", "=",asset_type]])
            asset_dir = t_tw.info.get_dir(t_tw.client.get_database(),"asset",asset_ids,folder_sign_list=['asset'])[0]['asset']
            asset_path = os.path.join(asset_dir,"USD","{}_{}_{}.usd".format(asset_type,asset_name,profix)).replace("\\","/")
            anim_path = f
            if os.path.exists(asset_path) and os.path.exists(anim_path):
                try:
                    data.append(
                        {"prim_path":prim_path,
                        "asset_path":os.path.relpath(asset_path,filedir).replace("\\","/"),
                        "anim_path":os.path.relpath(anim_path,filedir).replace("\\","/")}
                        )
                except:
                    data.append(
                    {"prim_path":prim_path,
                    "asset_path":asset_path,
                    "anim_path":anim_path}
                    )
    return data
def GetUSDAnimProcessData(t_tw,db,files,target_dir,profix="lookdev"):
    # new_log.cout(json.dumps(files,indent=4))
    data = []
    for f in files:
        filedir = target_dir#os.path.dirname(f)

        d=CacheUSDInAssetLibs(t_tw,db,f)
        if d != None:
            asset_type = d["asset_type"]
            asset_name = d["asset_name"]
            asset_num = d["asset_number"]

            prim_path = "{}_{}_{}".format(asset_type,asset_name,asset_num)

            asset_ids=t_tw.info.get_id(t_tw.client.get_database(),"asset",[["asset.entity", "=",asset_name],["asset.link_asset_type", "=",asset_type]])
            asset_dir = t_tw.info.get_dir(t_tw.client.get_database(),"asset",asset_ids,folder_sign_list=['asset'])[0]['asset']
            asset_path = os.path.join(asset_dir,"USD","{}_{}_{}.usd".format(asset_type,asset_name,profix)).replace("\\","/")
            anim_path = f
            if os.path.exists(asset_path) and os.path.exists(anim_path):
                try:
                    data.append(
                        {"prim_path":prim_path,
                        "asset_path":os.path.relpath(asset_path,filedir).replace("\\","/"),
                        "anim_path":os.path.relpath(anim_path,filedir).replace("\\","/")}
                        )
                except:
                    data.append(
                    {"prim_path":prim_path,
                    "asset_path":asset_path,
                    "anim_path":anim_path}
                    )
        elif os.path.basename(f) == "main_camera.usd":
            data.append(
                {"prim_path":"Cameras",
                        "asset_path":"",
                        "anim_path":os.path.relpath(f,filedir).replace("\\","/")}
                )
    return data

# def GetShotTaskPublishVersion(t_tw,db,id,sign='anim_usd'):
#     t_fields = t_tw.version.fields(db=db)
#     t_version_id_list =  t_tw.version.get_id(db=db, filter_list=[
#         ['module','=','shot'],'and',
#         ['module_type','=','task'],'and',
#         ['#link_id','=',id],'and' ,
#         ['sign','=',sign]])
    
#     all_ver=t_tw.version.get(db=db, id_list=t_version_id_list, field_list=['entity'])
#     if len(all_ver) > 0:
#         return all_ver[-1]
    
#     return None



def CreateSetsLayer(t_tw,db,module,shot_id,seq_id,light_path,sets_output_path,anims_output_path):
    #try:
    anims_task_id = t_tw.task.get_id(db,module,[['shot.id','=',shot_id],['seq.id','=',seq_id],['pipeline.entity','=','Animation']])[0]
    anims_filebox_info_keys=t_tw.task.get_sign_filebox(db,module,anims_task_id,filebox_sign="anim_usd")

    anims_max_version = anims_filebox_info_keys['last_max_version']
    anims_max_version_id = anims_filebox_info_keys['last_max_version_id']


    anims_t_id_list =  t_tw.file.get_id(db,filter_list=[['#link_id','=',anims_task_id],['#version_id','=',anims_max_version_id]])
    anims_cc=t_tw.file.get(db, id_list=anims_t_id_list, field_list=['sys_local_full_path'])

    data = GetUSDSetsProcessData(t_tw,db,[i['sys_local_full_path'] for i in anims_cc],light_path)
    # except:
    #     data = []



    #生成sets文件
    sucess_sets=qnusdtool.CreateAnimLayer(data,sets_output_path,1)

    return sucess_sets

def CreateAnimLayer(t_tw,db,module,shot_id,seq_id,light_path,sets_output_path,anims_output_path):
    #try:
    anims_task_id = t_tw.task.get_id(db,module,[['shot.id','=',shot_id],['seq.id','=',seq_id],['pipeline.entity','=','Animation']])[0]
    anims_filebox_info_keys=t_tw.task.get_sign_filebox(db,module,anims_task_id,filebox_sign="anim_usd")

    anims_max_version = anims_filebox_info_keys['last_max_version']
    anims_max_version_id = anims_filebox_info_keys['last_max_version_id']


    anims_t_id_list =  t_tw.file.get_id(db,filter_list=[['#link_id','=',anims_task_id],['#version_id','=',anims_max_version_id]])
    anims_cc=t_tw.file.get(db, id_list=anims_t_id_list, field_list=['sys_local_full_path'])

    data = GetUSDAnimProcessData(t_tw,db,[i['sys_local_full_path'] for i in anims_cc],light_path)
    # except:
    #     data = []



    #生成sets文件
    sucess_anims=qnusdtool.CreateAnimLayer(data,anims_output_path,0)
    #print([i['sys_local_full_path'] for i in anims_cc])

    return sucess_anims


def CreateCFXLayer(t_tw,db,module,shot_id,seq_id,light_path,cfxs_output_path):

    #生成cfxs文件
    try:
        cfxs_task_id = t_tw.task.get_id(db,module,[['shot.id','=',shot_id],['seq.id','=',seq_id],['pipeline.entity','=','CFX']])[0]
        cfxs_filebox_info_keys=t_tw.task.get_sign_filebox(db,module,cfxs_task_id,filebox_sign="cfx_mesh")

        cfxs_max_version = cfxs_filebox_info_keys['last_max_version']
        cfxs_max_version_id = cfxs_filebox_info_keys['last_max_version_id']


        cfxs_t_id_list =  t_tw.file.get_id(db,filter_list=[['#link_id','=',cfxs_task_id],['#version_id','=',cfxs_max_version_id]])
        cfxs_cc=t_tw.file.get(db, id_list=cfxs_t_id_list, field_list=['sys_local_full_path'])

        data = GetUSDAnimProcessData(t_tw,db,[i['sys_local_full_path'] for i in cfxs_cc],light_path)
    except:
        data = []



    #生成sets文件
    return qnusdtool.CreateCFXLayer(data,cfxs_output_path)


def GetRelPath(path,t_path):
    return os.path.relpath(path.replace("/","\\"),t_path.replace("/","\\")).replace("\\","/")
def CreateShotSetsLayer():
    t_tw = tw()
    id = t_tw.client.get_id()
    db = t_tw.client.get_database()
    module = t_tw.client.get_module()
    module_type = t_tw.client.get_module_type()

    #当前filebox_dir
    light_filebox_info_keys=t_tw.task.get_sign_filebox(db,module,id[0],filebox_sign="light_usd")
    light_max_version = light_filebox_info_keys['last_max_version']
    light_path = light_filebox_info_keys['path'].replace("{ver}","temp").replace("\\","/")

    if not os.path.exists(light_path):
        os.makedirs(light_path)

    
    
    #获取当前镜头的名称和ID

    shot_info_keys=t_tw.task.get(db,module,id,['shot.entity','seq.entity','shot.id','seq.id'])
    shot_id = shot_info_keys[0]['shot.id']
    seq_id = shot_info_keys[0]['seq.id']
    shot_entity = shot_info_keys[0]['shot.entity']
    seq_entity = shot_info_keys[0]['seq.entity']

    #all_layer
    sets_output_path = os.path.join(light_path,"{}_{}_sets.usda".format(seq_entity,shot_entity)).replace("\\","/")
    anims_output_path = os.path.join(light_path,"{}_{}_anims.usda".format(seq_entity,shot_entity)).replace("\\","/")
    cfxs_output_path = os.path.join(light_path,"{}_{}_cfxs.usda".format(seq_entity,shot_entity)).replace("\\","/")

    comps_output_path = os.path.join(light_path,"{}_{}_all.usda".format(seq_entity,shot_entity)).replace("\\","/")



    #动画和资产层
    CreateSetsLayer(t_tw,db,module,shot_id,seq_id,light_path,sets_output_path,anims_output_path)
    CreateAnimLayer(t_tw,db,module,shot_id,seq_id,light_path,sets_output_path,anims_output_path)
    CreateCFXLayer(t_tw,db,module,shot_id,seq_id,light_path,cfxs_output_path)

    qnusdtool.CompositeLayer((GetRelPath(cfxs_output_path,light_path),GetRelPath(anims_output_path,light_path),GetRelPath(sets_output_path,light_path)),comps_output_path)

    t_tw.task.publish(db,module,id[0],[sets_output_path,anims_output_path,cfxs_output_path,comps_output_path],"light_usd")

    #print(comps_output_path)
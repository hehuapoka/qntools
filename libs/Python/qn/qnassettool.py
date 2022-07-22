from itertools import count
import re
import qn.env as env
import qn.qnusdtool as qnusdtool
import qn.log as log
env.setCgTeamWorkEnv()


from cgtw2 import *


new_log = log.Log("C:/test.txt")

def InAssetLib(asset_name,asset_type,infos):
        for info in infos:
            if info['asset.entity'] == asset_name and info['asset.link_asset_type'] == asset_type:
                return True
        return False

def CacheUSDInAssetLibs(t_tw,db,filepath):
    ids=t_tw.info.get_id(db=db, module="asset", filter_list=[])

    infos = t_tw.info.get(db=db, module="asset", id_list=ids, field_sign_list=['asset.entity','asset.link_asset_type'])

    filename = os.path.basename(filepath)
    d=re.match(r"^([a-z]+)_([a-z]+)_anim_([0-9]+)\.[a-z]+$",filename,re.I)
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

def CFXMeshUSDInAssetLibs(t_tw,db,filepath):
    ids=t_tw.info.get_id(db=db, module="asset", filter_list=[])

    infos = t_tw.info.get(db=db, module="asset", id_list=ids, field_sign_list=['asset.entity','asset.link_asset_type'])

    filename = os.path.basename(filepath)
    d=re.match(r"^([a-z]+)_([a-z]+)_cfx_mesh_([0-9]+)\.[a-z]+$",filename,re.I)
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

def GetUSDAnimProcessData(t_tw,db,files):
    # new_log.cout(json.dumps(files,indent=4))
    data = []
    for f in files:
        filedir = os.path.dirname(f)

        d=CacheUSDInAssetLibs(t_tw,db,f)
        if d != None:
            asset_type = d["asset_type"]
            asset_name = d["asset_name"]
            asset_num = d["asset_number"]

            prim_path = "{}_{}_{}".format(asset_type,asset_name,asset_num)

            asset_ids=t_tw.info.get_id(t_tw.client.get_database(),"asset",[["asset.entity", "=",asset_name],["asset.link_asset_type", "=",asset_type]])
            asset_dir = t_tw.info.get_dir(t_tw.client.get_database(),"asset",asset_ids,folder_sign_list=['asset'])[0]['asset']
            asset_path = os.path.join(asset_dir,"USD","{}_{}_lookdev.usd".format(asset_type,asset_name)).replace("\\","/")
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

def GetUSDCFXMeshProcessData(t_tw,db,files):
    # new_log.cout(json.dumps(files,indent=4))
    data = []
    for f in files:
        filedir = os.path.dirname(f)

        d=CFXMeshUSDInAssetLibs(t_tw,db,f)
        if d != None:
            asset_type = d["asset_type"]
            asset_name = d["asset_name"]
            asset_num = d["asset_number"]

            prim_path = "{}_{}_{}".format(asset_type,asset_name,asset_num)

            asset_ids=t_tw.info.get_id(t_tw.client.get_database(),"asset",[["asset.entity", "=",asset_name],["asset.link_asset_type", "=",asset_type]])
            asset_dir = t_tw.info.get_dir(t_tw.client.get_database(),"asset",asset_ids,folder_sign_list=['asset'])[0]['asset']
            asset_path = os.path.join(asset_dir,"USD","{}_{}_lookdev.usd".format(asset_type,asset_name)).replace("\\","/")
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
def GetUSDAnimLayerOutPath(t_tw,source_path):
    task_id=t_tw.client.get_id()
    c_db = t_tw.client.get_database()
    c_module = t_tw.client.get_module()
    ak=t_tw.task.get(db=c_db,module=c_module,id_list=task_id,field_sign_list=['seq.entity','shot.entity'])[0]
    out_path=os.path.join(os.path.dirname(source_path),"{}_{}_anims.usda".format(ak['seq.entity'],ak['shot.entity'])).replace("\\","/")
    
    return out_path
def GetUSDAnimLayerOutPath_BY(t_tw,source_path):
    task_id=t_tw.client.get_id()
    c_db = t_tw.client.get_database()
    c_module = t_tw.client.get_module()

    ak=t_tw.task.get(db=c_db,module=c_module,id_list=task_id,field_sign_list=['seq.entity','shot.entity'])[0]
    anim_task_id=t_tw.task.get_id(c_db,c_module,[['seq.entity','=',ak['seq.entity']],['shot.entity','=',ak['shot.entity']],['pipeline.entity','=','Animation']])[0]
    f_box=t_tw.task.get_sign_filebox(c_db,c_module,anim_task_id,'anim_usd_comp')

    max_version = f_box['last_max_version']
    max_version_id = f_box['last_max_version_id']


    t_id_list =  t_tw.file.get_id(c_db,filter_list=[['#link_id','=',anim_task_id],['#version_id','=',max_version_id]])
    cc=t_tw.file.get(c_db, id_list=t_id_list, field_list=['sys_local_full_path'])[0]['sys_local_full_path']


    #out_path=os.path.join(os.path.dirname(source_path),"{}_{}_anims.usda".format(ak['seq.entity'],ak['shot.entity'])).replace("\\","/")
    #new_log.coutJson(cc)
    return os.path.relpath(cc,os.path.dirname(source_path)).replace("\\","/")

def CompositionAnims(t_tw):
    new_log.cout("__Start_Anim__")
    id = t_tw.client.get_id()[0]
    db = t_tw.client.get_database()
    module = t_tw.client.get_module()
    filebox_infos=t_tw.task.get_sign_filebox(db,module,id,'anim_usd')

    max_version = filebox_infos['last_max_version']
    max_version_id = filebox_infos['last_max_version_id']


    t_id_list =  t_tw.file.get_id(db,filter_list=[['#link_id','=',id],['#version_id','=',max_version_id]])
    cc=t_tw.file.get(db, id_list=t_id_list, field_list=['sys_local_full_path'])

    data = GetUSDAnimProcessData(t_tw,db,[i['sys_local_full_path'] for i in cc])

    out_path = GetUSDAnimLayerOutPath(t_tw,cc[0]['sys_local_full_path'])
    # new_log.cout(max_version)
    if(qnusdtool.CreateAnimLayer(data,out_path)):
        t_tw.task.publish(t_tw.client.get_database(),t_tw.client.get_module(),t_tw.client.get_id()[0],[out_path],"anim_usd_comp",max_version)

    new_log.coutJson(data)
    new_log.cout("__End_Anim__")

def CompositionCFXMesh(t_tw):
    new_log.cout("__Start_CFX_MESH__")

    id = t_tw.client.get_id()[0]
    db = t_tw.client.get_database()
    module = t_tw.client.get_module()
    filebox_infos=t_tw.task.get_sign_filebox(db,module,id,'cfx_mesh')

    max_version = filebox_infos['last_max_version']
    max_version_id = filebox_infos['last_max_version_id']


    t_id_list =  t_tw.file.get_id(db,filter_list=[['#link_id','=',id],['#version_id','=',max_version_id]])
    cc=t_tw.file.get(db, id_list=t_id_list, field_list=['sys_local_full_path'])

    data = GetUSDCFXMeshProcessData(t_tw,db,[i['sys_local_full_path'] for i in cc])

    animlayer_path=GetUSDAnimLayerOutPath_BY(t_tw,cc[0]['sys_local_full_path'])
    # out_path = GetUSDAnimLayerOutPath(t_tw,cc[0]['sys_local_full_path'])
    # new_log.cout(max_version)
    # if(qnusdtool.CreateAnimLayer(data,out_path)):
    #     t_tw.task.publish(t_tw.client.get_database(),t_tw.client.get_module(),t_tw.client.get_id()[0],[out_path],"anim_usd_comp",max_version)

    new_log.coutJson(animlayer_path)

    new_log.cout("__End_CFX_MESH__")


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



# def PublishAnimsLayer(t_tw:tw,files:list):
#     db = t_tw.client.get_database()
#     module = t_tw.client.get_module()
#     module_type = t_tw.client.get_module_type()
#     id = t_tw.client.get_id()

#     current_anims_ver = GetShotTaskPublishVersion(t_tw,db,t_tw.client.get_id())['entity']

#     if(current_anims_ver == None):
#         return False
#     current_anims_dir = t_tw.task.get_dir(db,module,[id],['anim_usd'])[0]['anim_usd']

#     data = GetUSDAnimProcessData(t_tw,db,files)
#     if len(data)>0:
#         ak=t_tw.task.get(db=t_tw.client.get_database(),module=t_tw.client.get_module(),id_list=t_tw.client.get_id(),field_sign_list=['shot.entity','seq.entity'])[0]
#         out_path=os.path.join(os.path.dirname(files[0]),"{}_{}_anims.usda".format(ak['seq.entity'],ak['shot.entity'])).replace("\\","/")
#         if(qnusdtool.CreateAnimLayer(data,out_path)):
#             t_tw.task.publish(t_tw.client.get_database(),t_tw.client.get_module(),t_tw.client.get_id()[0],[out_path],"anim_usd_comp")


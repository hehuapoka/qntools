#coding:utf-8
import sys,os
_qntools = os.path.join(os.environ["QNTOOLS"],"libs\Python").replace("\\","/")
if _qntools not in sys.path:
    sys.path.append(_qntools)
import qn.env as qn_env
import qn.qnassettool as qn_asset
qn_env.setCgTeamWorkEnv()
import cgtw2

t_tw = cgtw2.tw()
c_db = "proj_test1"
c_module = "shot"
# t_fields = t_tw.version.fields(db='proj_test1')
# t_version_id_list =  t_tw.version.get_id(db='proj_test1', filter_list=[
#     ['module','=','shot'],'and',
#     ['module_type','=','task'],'and',
#     ['#link_id','=','BAD29AC8-AE8C-2733-452B-550453447071'],'and' ,
#     ['sign','=','anim_usd']])
# print(t_tw.version.get(db='proj_test1', id_list=t_version_id_list, field_list=['entity']))
# print(qn_asset.GetShotTaskPublishVersion(t_tw,"proj_test1",'BAD29AC8-AE8C-2733-452B-550453447071'))
# print(qn_asset.CacheUSDInAssetLibs(t_tw,"proj_test1",r"D:\test\Elements_chuang_0.usd"))
# print(qn_asset.CacheUSDInAssetLibs(t_tw,"proj_test1",r"D:\test\Elements_chuang_0.usd"))
# filebox_infos=t_tw.task.get_sign_filebox('proj_test1','shot','BAD29AC8-AE8C-2733-452B-550453447071','anim_usd')

# max_version = filebox_infos['last_max_version']
# max_version_id = filebox_infos['last_max_version_id']

# t_fields = t_tw.file.fields(db='proj_test1')
# t_id_list =  t_tw.file.get_id(db='proj_test1',filter_list=[['#link_id','=','BAD29AC8-AE8C-2733-452B-550453447071'],['#version_id','=',max_version_id]])
# cc=t_tw.file.get(db='proj_test1', id_list=t_id_list, field_list=['sys_local_full_path'])
# print("============================")
# for i in cc:
#     print(i)
id='BAD29AC8-AE8C-2733-452B-550453447071'
a=t_tw.task.get(db=c_db,module=c_module,id_list=[id],field_sign_list=['seq.entity','shot.entity'])
print(a)
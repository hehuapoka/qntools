from PySide6.QtWidgets import QComboBox
import cgtw2
import qn.env as env
env.setCgTeamWorkEnv()

def addProjectCombox(tw:cgtw2.tw,widget:QComboBox):
    t_id_list =  tw.info.get_id(db='public', module='project', filter_list=[['project.status','=','Active']])
    t_projs = tw.info.get(db='public', module='project', id_list=t_id_list, field_sign_list=['project.entity','project.database','project.template','project.full_name'])

    #init proj
    for p in t_projs:
        if p['project.template'] == "千鸟动画模板Katana":
            # {'project.entity': 'LDSF', 'project.database': 'proj_ldsf', 'id': '1A99F25C-BACA-442D-9892-8A8CD11DA2D3'}
            widget.addItem(f'{p["project.full_name"]}',userData=p)



def addScCombobox(tw:cgtw2.tw,widget:QComboBox,data_db:str):
    widget.clear()
    t_id_list=tw.info.get_id(db=data_db,module='seq',filter_list=[])
    a=tw.info.get(db=data_db,module='seq',id_list=t_id_list,field_sign_list=['seq.entity'])

    #init frist
    for i in a:
        widget.addItem(f'{i["seq.entity"]}',userData=i)

def addShotCombobox(tw:cgtw2.tw,widget:QComboBox,data_db:str,sc_id:str):
    widget.clear()
    t_id_list=tw.info.get_id(db=data_db,module='shot',filter_list=[["seq.id","=",sc_id]])
    a=tw.info.get(db=data_db,module='shot',id_list=t_id_list,field_sign_list=['shot.entity',"seq.entity"])

    #init frist
    for i in a:
        widget.addItem(f'{i["shot.entity"]}',userData=i)

def addShotAnimVerCombobox(tw:cgtw2.tw,widget:QComboBox,data_db:str,shot_id:str):
    widget.clear()

    task_ids=tw.task.get_id(data_db,"shot",filter_list=[['shot.id','=',shot_id],['pipeline.entity','=','Animation']])

    if len(task_ids) < 1:return

    anims=tw.task.get_sign_filebox(db=data_db,module="shot",id=task_ids[0],filebox_sign="anim_usd")
    max_version = anims['last_max_version']

    widget.addItem('默认(递增)',userData=task_ids[0])
    if max_version != "":
        for i in range(int(max_version)):
            widget.addItem(f'v{i+1:03}',userData=task_ids[0])


def addShotCfxVerCombobox(tw:cgtw2.tw,widget:QComboBox,data_db:str,shot_id:str):
    widget.clear()

    task_ids=tw.task.get_id(data_db,"shot",filter_list=[['shot.id','=',shot_id],['pipeline.entity','=','CFX']])

    if len(task_ids) < 1:return

    anims=tw.task.get_sign_filebox(db=data_db,module="shot",id=task_ids[0],filebox_sign="cfx_mesh")
    max_version = anims['last_max_version']

    widget.addItem('默认(递增)',userData=task_ids[0])
    if max_version != "":
        for i in range(int(max_version)):
            widget.addItem(f'v{i+1:03}',userData=task_ids[0])

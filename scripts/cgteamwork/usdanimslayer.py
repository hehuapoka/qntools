#coding:utf-8
import json,sys
sys.path.append("D:/CgTeamWork_v6.2/bin/base") 

import cgtw2
t_tw = cgtw2.tw()
id = t_tw.client.get_id()
ff=t_tw.task.get_submit_file(db=t_tw.client.get_database(), module=t_tw.client.get_module(), id_list=id, submit_type="file")
with open("C:/test.txt","w+") as pf:
    pf.write(json.dumps(ff,indent=4))

#coding:utf-8
import json,sys,os

sys.path.append("D:/CgTeamWork_v6.2/bin/base")

_qntools = os.path.join(os.environ["QNTOOLS"],"libs\Python").replace("\\","/")
if _qntools not in sys.path:
    sys.path.append(_qntools)
from qn import qnusdtool

import cgtw2,re
try:
    from PySide6.QtWidgets import *
except:
    #from ct_plu.qt import *
    from PySide2.QtWidgets import *

def run():
    t_tw = cgtw2.tw()

    fs = t_tw.client.get_file()
    data = []
    for f in fs:
        filename = os.path.basename(f)
        filedir = os.path.dirname(f)
        d=re.match(r"^([a-z]+)_([a-z]+)_([0-9]+)\.[a-z]+$",filename,re.I)
        if d != None:
            asset_type = d.group(1)
            asset_name = d.group(2)
            asset_num = d.group(3)

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

# with open("C:/test.txt","w+") as pf:
#         pf.write(json.dumps(data,indent=4))
# if len(data)>0:
#     out_path=os.path.join(os.path.dirname(fs[0]),"Anims.usda").replace("\\","/")
#     with open("C:/test.txt","w+") as pf:
#         pf.write(out_path)
#         pf.write(json.dumps(data,indent=4))
#         #pf.write(repr(qnusdtool.CreateAnimLayer(data,out_path)))

if __name__ == "__main__":

    app = QApplication(sys.argv)
    a=QWidget()
    a.resize(400,300)
    a.show()
    app.exec_()

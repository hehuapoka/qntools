#coding:utf-8
import json,sys,os

sys.path.append("D:/CgTeamWork_v6.2/bin/base")

_qntools = os.path.join(os.environ["QNTOOLS"],"libs\Python").replace("\\","/")
if _qntools not in sys.path:
    sys.path.append(_qntools)
from qn import qnusdtool
from qn import qnassettool

import cgtw2,re

if __name__ == "__main__":
    t_tw = cgtw2.tw()
    qnassettool.CompositionCFXMesh(t_tw)


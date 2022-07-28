#coding:utf-8
import json,sys,os

sys.path.append("D:/CgTeamWork_v6.2/bin/base")

_qntools = os.path.join(os.environ["QNTOOLS"],"libs\Python").replace("\\","/")
if _qntools not in sys.path:
    sys.path.append(_qntools)
from qn import qnassettool

import cgtw2,re

if __name__ == "__main__":
    qnassettool.CreateShotSetsLayer()


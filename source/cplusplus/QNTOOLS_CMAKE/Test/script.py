import os,sys
__ok = True

cgtw_env=os.environ['CGTEAMWORK_LOCATION']
sys.argv.append(os.path.join(cgtw_env,"bin/base"))

import cgtw2
class UpDataAssetTool:
    _cgtw = None
    def __init__(self):
        _cgtw = cgtw2.tw()
    def updataAsset(self,dir:str):
        path=os.listdir(dir)
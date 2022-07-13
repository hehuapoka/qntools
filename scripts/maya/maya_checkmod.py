#coding:utf-8
import sys,os,json
sys.path.append(os.path.join(os.environ['QNTOOLS'],"scripts\\maya"))

import maya.cmds as cmds

import maya.mel as mel

import maya.standalone
try: 			
    maya.standalone.initialize() 		
except: 			
    pass
from qn.checkUtils import checkRootHierarchy
from qn.cleanupUtils import cleanUnknown
##################################


if len(sys.argv) >= 2:
    input_file = sys.argv[1].replace("\\","/")
    if os.path.exists(input_file):
        out_file_name = (os.path.splitext(sys.argv[1])[0]+"_checked.ma").replace("\\","/")
        #print(out_file_name+"\n\n\n\n")
        try:
            cmds.file(input_file,open=True,force=True)
            if checkRootHierarchy():
                cleanUnknown()
                cmds.file( out_file_name, force=True, options="v=0;", type="mayaAscii", ea=True)
        except:
            pass



try: 			
    maya.standalone.uninitialize() 		
except: 			
    pass
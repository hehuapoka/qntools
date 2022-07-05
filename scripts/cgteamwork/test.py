# import sys,os

# bin=os.path.join(os.environ['MAYA_LOCATION'],"bin")
# bin2=os.path.join(os.environ['MAYA_LOCATION'],"bin2")
# bin3=os.path.join(os.environ['MAYA_LOCATION'],"bin3")

# path2=os.path.join(os.environ['MAYA_LOCATION'],r"Python27\Lib\site-packages")
# path3=os.path.join(os.environ['MAYA_LOCATION'],r"Python37\Lib\site-packages")

# _pv = sys.version.split(".")[0][-1]
# if _pv == "3":
#     os.environ['PATH'] = "{};{};{}".format(bin,bin3,os.environ['PATH'])
#     sys.path.append(path3)
# else:
#     os.environ['PATH'] = "{};{};{}".format(bin,bin2,os.environ['PATH'])
#     sys.path.append(path2)


# import maya.standalone
# try: 			
#     maya.standalone.initialize() 		
# except: 			
#     pass

# import maya.cmds as cmds

# cmds.file("D:/test/a.ma",open=True,force=True)
# cmds.file( "D:/test/b.ma", force=True, options="v=0;", type="mayaAscii", ea=True)


# try: 			
#     maya.standalone.uninitialize() 		
# except: 			
#     pass
import time
time.sleep(2)
print("hello")
#coding:utf-8
import ctypes
import os,sys
import qn.env as env
class AnimInfo(ctypes.Structure):
    _fields_ = [
        ("prim_path",ctypes.c_char_p),
        ("asset_path",ctypes.c_char_p),
        ("anim_path",ctypes.c_char_p)
    ]

#const char* prim_path;
#	const char* asset_path;
#	const char* anim_path;

_pv = env.getPythonVersion()
env.setUSDEnv()
_lib_add= ctypes.cdll.LoadLibrary("qnusdtool.dll")
# if _pv == "3":
#     _pxr = os.path.join(os.environ["QNTOOLS"],"libs\\USD\\lib\\python").replace("\\","/")
#     if _pxr not in sys.path:
#         sys.path.append(_pxr)

#检查模型层级
def AssetModHierarchyCheckFunc(path):
    if _pv == "3": 
        return _lib_add.AssetModHierarchyCheck(bytes(path,"utf-8"))
    else:
        return _lib_add.AssetModHierarchyCheck(bytes(path))

#检查模型面数量以及是否包括Mesh和Xform以外的类型
def AssetModTopologyCheckFunc(path,min_pt=4,max_pt=4):
    if _pv == "3": 
        return _lib_add.AssetModTopologyCheck(bytes(path,"utf-8"),min_pt,max_pt)
    else:
        return _lib_add.AssetModTopologyCheck(bytes(path),min_pt,max_pt)

#检查模型面数量以及是否包括Mesh和Xform以外的类型 and 检查模型层级
def AssetModCheckFunc(path,min_pt=4,max_pt=4):
    if _pv == "3": 
        return _lib_add.AssetModCheck(bytes(path,"utf-8"),min_pt,max_pt)
    else:
        return _lib_add.AssetModCheck(bytes(path),min_pt,max_pt)

#检查模型面数量以及是否包括Mesh和Xform以外的类型 and 检查模型层级
def AssetAnimCheckFunc(path):
    if _pv == "3": 
        return _lib_add.AssetAnimCheck(bytes(path,"utf-8"))
    else:
        return _lib_add.AssetAnimCheck(bytes(path))

def CreateAnimLayer(a,path,type=0):
    if type == 0:
        func=_lib_add.CreateAnimLayer
    else:
        func=_lib_add.CreateAnimRef
    func.restype = ctypes.c_bool

    if _pv == "3":
        #func.argtypes = (ctypes.c_int,ctypes.POINTER(ctypes.POINTER(AnimInfo)),ctypes.c_char_p)
        c=(ctypes.POINTER(AnimInfo)*len(a))()
        for idx,i in enumerate(a):
            ix = AnimInfo(bytes(i['prim_path'],'utf-8'),bytes(i['asset_path'],'utf-8'),bytes(i['anim_path'],'utf-8'))
            c[idx] = ctypes.pointer(ix)
        return func(len(a),c,bytes(path,'utf-8'))

    else:
        #func.argtypes = (ctypes.c_int,ctypes.POINTER(ctypes.POINTER(AnimInfo)),ctypes.c_char_p)
        c=(ctypes.POINTER(AnimInfo)*len(a))()
        for idx,i in enumerate(a):
            ix = AnimInfo(bytes(i['prim_path']),bytes(i['asset_path']),bytes(i['anim_path']))
            c[idx] = ctypes.pointer(ix)
        return func(len(a),c,bytes(path))

def CreateCFXLayer(a,path):
    return CreateAnimLayer(a,path,0)

def CompositeLayer(a,path):
    if _pv == "3":
        func=_lib_add.CompositeLayer
        func.restype = ctypes.c_bool
        #func.argtypes = (ctypes.c_int,ctypes.POINTER(ctypes.POINTER(AnimInfo)),ctypes.c_char_p)
        c=(ctypes.c_char_p*len(a))()
        for idx,i in enumerate(a):
            c[idx] = ctypes.c_char_p(bytes(i,'utf-8'))
        return func(len(a),c,bytes(path,'utf-8'))

    else:
        func=_lib_add.CompositeLayer
        func.restype = ctypes.c_bool
        #func.argtypes = (ctypes.c_int,ctypes.POINTER(ctypes.POINTER(AnimInfo)),ctypes.c_char_p)
        c=(ctypes.c_char_p*len(a))()
        for idx,i in enumerate(a):
            c[idx] = ctypes.c_char_p(bytes(i))
        return func(len(a),c,bytes(path))


def SolverUSDPathToRelation(path):
    if _pv == "3":
        func=_lib_add.ModifyUsdFilePath
        #func.argtypes = (ctypes.c_int,ctypes.POINTER(ctypes.POINTER(AnimInfo)),ctypes.c_char_p)
        func(bytes(path,'utf-8'))

    else:
        func=_lib_add.ModifyUsdFilePath

        func(bytes(path))

def TestA():
    a = CreateAnimLayer([{'prim_path':"Elements_chuang",
                            'asset_path':"./Elements_chuang_mod.usd",
                            'anim_path':"./Elements_chuang_0.usd"}],
                "Z:/CGTeamWorkProject/Test1/USD/Shot/SC01/Shot001/Lighting/temp/SC01_Shot001_sets.usda",0)
    b = CreateAnimLayer([{'prim_path':"Elements_chuang",
                            'asset_path':"./Elements_chuang_mod.usd",
                            'anim_path':"./Elements_chuang_0.usd"}],
                "Z:/CGTeamWorkProject/Test1/USD/Shot/SC01/Shot001/Lighting/temp/SC01_Shot001_sets.usda",1)
    print(a)
    print(b)
# def TestB():
#     a = CompositeLayer(["./Elements_chuang_0.usd","./Elements_chuang_1.usd","./Elements_chuang_2.usd"],"D:/test/f.usda")
#     print(a)
def TestC():
    SolverUSDPathToRelation("D:/test/comps2.usda")
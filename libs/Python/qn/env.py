import ctypes
import os,sys
def getPythonVersion():
    _pv = sys.version.split(".")[0][-1]
    return _pv
    
def setUSDEnv():
    _pv = getPythonVersion()
    _QNTOOLS = os.path.join(os.environ["QNTOOLS"],"bin")
    if _QNTOOLS not in os.environ["PATH"].split(";"):
        os.environ["PATH"] = os.environ["PATH"]+";"+_QNTOOLS

    _QNTOOLS_BIN = os.path.join(os.environ["QNTOOLS"],"libs\\USD\\bin")
    if _QNTOOLS_BIN not in os.environ["PATH"].split(";"):
        os.environ["PATH"] = os.environ["PATH"]+";"+_QNTOOLS_BIN

    _QNTOOLS_LIB = os.path.join(os.environ["QNTOOLS"],"libs\\USD\\lib")
    if _QNTOOLS_LIB not in os.environ["PATH"].split(";"):
        os.environ["PATH"] = os.environ["PATH"]+";"+_QNTOOLS_LIB

    if _pv == "3":
        _pxr = os.path.join(os.environ["QNTOOLS"],"libs\\USD\\lib\\python").replace("\\","/")
        if _pxr not in sys.path:
            sys.path.append(_pxr)
def setCgTeamWorkEnv():
    _cgtw_location = os.environ['CGTEAMWORK_LOCATION']
    _cgtw_python_base = os.path.join(_cgtw_location,"bin\\base").replace("\\","/")
    _cgtw_python_ct_plu = os.path.join(_cgtw_location,"bin\\base\\ct_plu").replace("\\","/")

    if _cgtw_python_base not in sys.path:
        sys.path.append(_cgtw_python_base)
    if _cgtw_python_ct_plu not in sys.path:
        sys.path.append(_cgtw_python_ct_plu)

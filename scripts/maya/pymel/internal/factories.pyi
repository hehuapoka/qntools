from typing import *
import pymel.core.uitypes
import pymel.util as util
from . import apicache as apicache, cmdcache as cmdcache, docstrings as docstrings, plogging as plogging, pmcmds as pmcmds
from collections import namedtuple
from pymel.internal.pwarnings import deprecated as deprecated, maya_deprecated as maya_deprecated
from pymel.util.conditions import Always as Always, Condition as Condition
from typing import Any, Optional, TypeVar

C = TypeVar('C', bound=Callable)
apiTypesToApiEnums: Dict[str, int]
apiEnumsToApiTypes: Dict[int, str]
mayaTypesToApiTypes: Dict[str, str]
apiTypesToApiClasses: Dict[str, Type]
apiClassInfo: Any
mayaTypesToApiEnums: Dict[str, int]
apiToMelData: Any
apiClassOverrides: Any
cmdlist: Any
nodeHierarchy: Any
uiClassList: Any
nodeCommandList: Any
moduleCmds: Any
building: bool

class MissingInCacheError(Exception): ...

class MelCommandMissingError(MissingInCacheError):
    cmdName: Any = ...
    def __init__(self, cmdName: Any) -> None: ...
    def str(self): ...

class ApiMethodMissingError(MissingInCacheError):
    apiClassName: Any = ...
    methodName: Any = ...
    def __init__(self, apiClassName: Any, methodName: Any) -> None: ...
    def str(self): ...

def loadApiCache() -> None: ...
def loadCmdCache() -> None: ...
def saveApiCache() -> None: ...
def saveApiMelBridgeCache() -> None: ...
def mergeApiClassOverrides() -> None: ...

EXCLUDE_METHODS: Any
docstringMode: Any
pyNodeNamesToPyNodes: Dict[str, Type]
apiClassNamesToPyNodeNames: Dict[str, str]
apiClassNamesToPymelTypes: Dict[str, Type]
mayaTypeNameToPymelTypeName: Any
pymelTypeNameToMayaTypeName: Any
apiEnumsToPyComponents: Any
pyNodeTypesHierarchy: Any
nodeTypeToInfoCommand: Any

def toPyNode(res: Optional[str]) -> Optional[pymel.core.general.PyNode]: ...
def unwrapToPyNode(res: List[str]) -> Optional[pymel.core.general.PyNode]: ...
def toPyUI(res: Optional[str]) -> Optional[pymel.core.uitypes.PyUI]: ...
def toPyType(moduleName: str, objectName: str) -> Callable[[Any], Any]: ...
def toPyNodeList(res: Optional[List[str]]) -> List[pymel.core.general.PyNode]: ...
def splitToPyNodeList(res: str) -> List[pymel.core.general.PyNode]: ...
def toPyUIList(res: str) -> List[pymel.core.uitypes.PyUI]: ...
def toPyTypeList(moduleName: str, objectName: str) -> Callable[[Any], List[Any]]: ...
def raiseError(typ: Any, *args: Any): ...

class Flag(Condition):
    shortName: Any = ...
    longName: Any = ...
    truthValue: Any = ...
    def __init__(self, longName: Any, shortName: Any, truthValue: bool = ...) -> None: ...
    def eval(self, kwargs: Any): ...

simpleCommandWraps: Any
examples: Any

def getUncachedCmds(): ...

docCacheLoaded: bool

def loadCmdDocCache(ignoreError: bool = ...) -> None: ...
def getCmdFunc(cmdName: str) -> Callable: ...
def addCmdDocs(func: C, cmdName: Optional[str]=...) -> C: ...
def addCmdDocsCallback(cmdName: Any, docstring: str = ...): ...
docBuilderCls = docstrings.RstDocstringBuilder
docBuilderCls = docstrings.NumpyDocstringBuilder
docBuilderCls = docstrings.PyDocstringBuilder

def addFlagCmdDocsCallback(cmdName: Any, flag: Any, docstring: Any): ...

class Callback:
    MAX_RECENT_ERRORS: int = ...
    recentErrors: Any = ...

    CallbackErrorLog = namedtuple('CallbackErrorLog', 'callback exception trace creationTrace')
    @classmethod
    def logCallbackError(cls, callback: Any, exception: Optional[Any] = ..., trace: Optional[Any] = ..., creationTrace: Optional[Any] = ...) -> None: ...
    @classmethod
    def formatRecentError(cls, index: int = ...): ...
    @classmethod
    def printRecentError(cls, index: int = ...) -> None: ...
    func: Any = ...
    args: Any = ...
    kwargs: Any = ...
    traceback: Any = ...
    def __init__(self, func: Any, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, *args: Any): ...

class CallbackWithArgs(Callback):
    def __call__(self, *args: Any, **kwargs: Any): ...

def makeUICallback(origCallback: Any, args: Any, doPassSelf: Any): ...
def fixCallbacks(inFunc: Any, commandFlags: Any, funcName: Optional[Any] = ...): ...
def convertTimeValues(rawVal: Any): ...
def maybeConvert(val: Any, castFunc: Any): ...
def functionFactory(funcNameOrObject: Any, returnFunc: Optional[Any] = ..., module: Optional[Any] = ..., rename: Optional[Any] = ..., uiWidget: bool = ...): ...
def makeCreateFlagMethod(inFunc: Any, flag: Any, newMethodName: Optional[Any] = ..., docstring: str = ..., cmdName: Optional[Any] = ..., returnFunc: Optional[Any] = ...): ...
def createflag(cmdName: Any, flag: Any): ...
def makeQueryFlagMethod(inFunc: Any, flag: Any, newMethodName: Optional[Any] = ..., docstring: str = ..., cmdName: Optional[Any] = ..., returnFunc: Optional[Any] = ...): ...
def queryflag(cmdName: Any, flag: Any): ...
def handleCallbacks(args: Any, kwargs: Any, callbackFlags: Any) -> None: ...
def asEdit(self, func: Any, kwargs: Any, flag: Any, val: Any): ...
def asQuery(self, func: Any, kwargs: Any, flag: Any): ...
def makeEditFlagMethod(inFunc: Any, flag: Any, newMethodName: Optional[Any] = ..., docstring: str = ..., cmdName: Optional[Any] = ...): ...
def editflag(cmdName: Any, flag: Any): ...
def addMelDocs(cmdName: Any, flag: Optional[Any] = ...): ...
def listForNoneQuery(res: Any, kwargs: Any, flags: Any): ...

class ApiTypeRegister:
    types: Dict[str, str] = ...
    inCast: Dict[str, Callable[[Any], Any]] = ...
    outCast: Dict[str, Callable[[Any, Any], Any]] = ...
    refInit: Any = ...
    refCast: Any = ...
    arrayItemTypes: Any = ...
    doc: Any = ...
    @classmethod
    def getPymelType(cls, apiType: Any, allowGuess: Any=...) -> Optional[str]: ...
    @classmethod
    def isRegistered(cls, apiTypeName: Any): ...
    @classmethod
    def register(cls, apiTypeName: str, pymelType: Type, inCast: Optional[Callable[[Any], Any]]=..., outCast: Optional[Callable[[Any], Any]]=..., apiArrayItemType: Optional[Type]=...) -> None: ...

class ApiArgUtil:
    apiClassName: Any = ...
    methodName: Any = ...
    basePymelName: Any = ...
    methodInfo: Any = ...
    methodIndex: Any = ...
    def __init__(self, apiClassName: str, methodName: str, methodIndex: int=...) -> None: ...
    def iterArgs(self, inputs: bool = ..., outputs: bool = ..., infoKeys: Any = ...): ...
    def inArgs(self) -> List[str]: ...
    def outArgs(self) -> List[str]: ...
    def argList(self) -> List[str]: ...
    def argInfo(self): ...
    def getGetterInfo(self) -> Optional[ApiArgUtil]: ...
    @staticmethod
    def isValidEnum(enumTuple: Any): ...
    def hasOutput(self): ...
    def canBeWrapped(self): ...
    def getInputTypes(self) -> List[str]: ...
    def getOutputTypes(self) -> List[str]: ...
    def getReturnType(self): ...
    def getPymelName(self): ...
    def getMethodDocs(self): ...
    def getPrototype(self, className: bool = ..., methodName: bool = ..., outputs: bool = ..., defaults: bool = ...): ...
    def getTypeComment(self): ...
    def castInput(self, argName: str, input: Any) -> Any: ...
    @classmethod
    def castInputEnum(cls, apiClassName: Any, enumName: Any, input: Any): ...
    @staticmethod
    def fromInternalUnits(result: Any, returnType: Any, unit: Optional[Any] = ...): ...
    @staticmethod
    def toInternalUnits(input: Any, unit: Any): ...
    def castResult(self, pynodeInstance: Any, result: Any): ...
    @staticmethod
    def initReference(argtype: Any): ...
    @classmethod
    def castReferenceResult(cls, argtype: Any, outArg: Any): ...
    def getDefaults(self): ...
    def isStatic(self): ...
    def isDeprecated(self): ...

class ApiUndo:
    node_name: str = ...
    cb_enabled: bool = ...
    undo_queue: Any = ...
    redo_queue: Any = ...
    undoStateCallbackId: Any = ...
    def __init__(self) -> None: ...
    def installUndoStateCallbacks(self) -> None: ...
    def flushCallback(self, undoOrRedoAvailable: Any, *args: Any) -> None: ...
    def append(self, cmdObj: Any, undoName: Optional[Any] = ...) -> None: ...
    def execute(self, cmdObj: Any, *args: Any): ...
    def flushUndo(self, *args: Any) -> None: ...

apiUndo: Any

class ApiUndoItem:
    def __init__(self, setter: Any, redoArgs: Any, undoArgs: Any, redoKwargs: Optional[Any] = ..., undoKwargs: Optional[Any] = ...) -> None: ...
    def redoIt(self) -> None: ...
    doIt: Any = ...
    def undoIt(self) -> None: ...

class ApiRedoUndoItem(ApiUndoItem):
    def __init__(self, redoer: Any, redoArgs: Any, undoer: Any, undoArgs: Any, redoKwargs: Optional[Any] = ..., undoKwargs: Optional[Any] = ...) -> None: ...
    def undoIt(self) -> None: ...

class MAnimCurveChangeUndoItem(ApiRedoUndoItem):
    def __init__(self, curveChangeObj: Any) -> None: ...

def getUndoArgs(args: List[Any], argList: List[Tuple[str, Union[str, Tuple[str, str]], str, Optional[str]]], getter: Callable, getterInArgs: List[str]) -> List[Any]: ...
def getDoArgs(args: List[Any], argList: List[Tuple[str, Union[str, Tuple[str, str]], str, Optional[str]]]) -> Tuple[List[Any], List[Any], List[Tuple[str, int]]]: ...
def getDoArgsGetterUndo(args: List[Any], argList: List[Tuple[str, Union[str, Tuple[str, str]], str, Optional[str]]], getter: Callable, setter: Callable, getterInArgs: List[str]) -> Tuple[List[Any], List[Any], List[Tuple[str, int]], ApiUndoItem]: ...
def getDoArgsAnimCurveUndo(args: List[Any], argList: List[Tuple[str, Union[str, Tuple[str, str]], str, Optional[str]]]) -> Tuple[List[Any], List[Any], List[Tuple[str, int]], ApiUndoItem]: ...
def processApiResult(result: Any, outTypeList: List[Tuple[str, int]], do_args: List[Any]) -> Any: ...
def getProxyResult(self, apiClass: Any, method: Any, final_do: Any = ...): ...
def wrapApiMethod(apiClass: Type, methodName: str, newName: str=..., proxy: bool=..., overloadIndex: Optional[int]=...) -> None: ...
def addApiDocs(apiClass: Any, methodName: Any, overloadIndex: Optional[Any] = ..., undoable: bool = ...): ...
def addApiDocsCallback(apiClass: Any, methodName: Any, overloadIndex: Optional[Any] = ..., undoable: bool = ..., origDocstring: str = ...): ...

class ClassConstant:
    value: Any = ...
    def __init__(self, value: Any) -> None: ...
    def __get__(self, instance: Any, owner: Any): ...
    def __set__(self, instance: Any, value: Any) -> None: ...
    def __delete__(self, instance: Any) -> None: ...

class MetaMayaTypeRegistry(util.metaReadOnlyAttr):
    def __new__(cls, classname: Any, bases: Any, classdict: Any): ...

class MetaMayaTypeWrapper(MetaMayaTypeRegistry):
    class ClassConstant:
        value: Any = ...
        def __init__(self, value: Any) -> None: ...
        def __get__(self, instance: Any, owner: Any): ...
        def __set__(self, instance: Any, value: Any) -> None: ...
        def __delete__(self, instance: Any) -> None: ...
    def __new__(cls, classname: Any, bases: Any, classdict: Any): ...
    @staticmethod
    def setattr_fixed_forDataDescriptorBug(self, name: Any, value: Any): ...

class _MetaMayaCommandWrapper(MetaMayaTypeWrapper):
    def __new__(cls, classname: Any, bases: Any, classdict: Any): ...
    @classmethod
    def getMelCmd(cls, classdict: Any): ...
    @classmethod
    def docstring(cls, melCmdName: Any): ...

class MetaMayaNodeWrapper(_MetaMayaCommandWrapper):
    def __new__(cls, classname: Any, bases: Any, classdict: Any): ...
    @classmethod
    def getMelCmd(cls, classdict: Any): ...

class MetaMayaUIWrapper(_MetaMayaCommandWrapper):
    def __new__(cls, classname: Any, bases: Any, classdict: Any): ...
    @classmethod
    def getMelCmd(cls, classdict: Any): ...

def addCustomPyNode(module: Any, mayaType: Any, extraAttrs: Any=...) -> Optional[str]: ...
def getPymelTypeName(mayaTypeName: str, create: bool=...) -> str: ...
def removePyNode(module: Any, mayaType: Any) -> None: ...
def addPyNodeType(pyNodeType: Any, parentPyNode: Any) -> None: ...
def removePyNodeType(pyNodeTypeName: Any) -> None: ...
def clearPyNodeTypes() -> None: ...
def addMayaType(mayaType: Any, apiType: Optional[Any] = ...) -> None: ...
def removeMayaType(mayaType: Any) -> None: ...

VirtualClassInfo = namedtuple('VirtualClassInfo', 'vclass parent nameRequired isVirtual preCreate create postCreate')

class VirtualClassError(Exception): ...

class VirtualClassManager:
    INVALID_ATTRS: Any = ...
    def __init__(self) -> None: ...
    def register(self, vclass: Any, nameRequired: bool=..., isVirtual: None=..., preCreate: None=..., create: None=..., postCreate: None=...) -> None: ...
    def unregister(self, vcls: Any) -> None: ...
    def getVirtualClass(self, baseClass: Any, obj: Any, name: Optional[Any] = ..., fnDepend: Optional[Any] = ...): ...
    def getVirtualClassInfo(self, vclass: Any): ...

virtualClasses: Any
registerVirtualClass: Any

def isValidPyNode(arg: Any): ...
def isValidPyNodeName(arg: Any): ...
def toApiTypeStr(obj: Union[int, str, util.ProxyUnicode], default: Optional[str]=...) -> Optional[str]: ...
def toApiTypeEnum(obj: Union[str, util.ProxyUnicode], default: Optional[int]=...) -> Optional[int]: ...
def toApiFunctionSet(obj: Union[str, int]) -> Optional[Type]: ...
def apiClassNameToPymelClassName(apiName: str, allowGuess: bool=...) -> Optional[str]: ...
def isMayaType(mayaType: str) -> bool: ...
def getComponentTypes(): ...

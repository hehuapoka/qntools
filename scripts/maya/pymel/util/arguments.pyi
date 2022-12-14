from typing import *
from .utilitytypes import ProxyUnicode as ProxyUnicode
from typing import Any

def isIterable(obj: Any) -> bool: ...
def isScalar(obj: Any) -> bool: ...
def isNumeric(obj: Any) -> bool: ...
def isSequence(obj: Any) -> bool: ...
def isMapping(obj: Any) -> bool: ...

clsname: Any

def convertListArgs(args: Any): ...
def expandArgs(*args: Any, **kwargs: Any): ...
def preorderArgs(limit: Any = ..., testFn: Any = ..., *args: Any): ...
def postorderArgs(limit: Any = ..., testFn: Any = ..., *args: Any): ...
def breadthArgs(limit: Any = ..., testFn: Any = ..., *args: Any): ...
def iterateArgs(*args: Any, **kwargs: Any): ...
def preorderIterArgs(limit: Any = ..., testFn: Any = ..., *args: Any) -> None: ...
def postorderIterArgs(limit: Any = ..., testFn: Any = ..., *args: Any) -> None: ...
def breadthIterArgs(limit: Any = ..., testFn: Any = ..., *args: Any) -> None: ...
def preorder(iterable: Any, testFn: Any = ..., limit: Any = ...) -> None: ...
def postorder(iterable: Any, testFn: Any = ..., limit: Any = ...) -> None: ...
def breadth(iterable: Any, testFn: Any = ..., limit: Any = ...) -> None: ...
def listForNone(res: Any): ...
def pairIter(sequence: Any): ...
def reorder(x: Any, indexList: Any = ..., indexDict: Any = ...): ...

class RemovedKey:
    oldVal: Any = ...
    def __init__(self, oldVal: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...

class AddedKey:
    newVal: Any = ...
    def __init__(self, newVal: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...

class ChangedKey:
    oldVal: Any = ...
    newVal: Any = ...
    def __init__(self, oldVal: Any, newVal: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...

def compareCascadingDicts(dict1: Union[dict, list, tuple], dict2: Union[dict, list, tuple], encoding: Union[str, bool, None]=..., useAddedKeys: bool=..., useChangedKeys: bool=...) -> Tuple[set, set, set, dict]: ...
def mergeCascadingDicts(from_dict: Any, to_dict: Any, allowDictToListMerging: bool = ..., allowNewListMembers: bool = ...): ...
def setCascadingDictItem(dict: Any, keys: Any, value: Any) -> None: ...
def getCascadingDictItem(dict: Any, keys: Any, default: Any = ...): ...
def deepPatch(input: Any, predicate: Any, changer: Any): ...
def deepPatchAltered(input: Any, predicate: Any, changer: Any): ...
def sequenceToSlices(intList: Any, sort: bool = ...): ...
def izip_longest(*args: Any, **kwds: Any) -> None: ...

from .path import path as path
from re import escape as escape
from typing import Any, Optional

def inMaya(): ...
def capitalize(s: Any) -> str: ...
def uncapitalize(s: Any, preserveAcronymns: Any=...) -> str: ...
def unescape(s: Any) -> str: ...
def cacheProperty(getter: Any, attr_name: Any, fdel: Optional[Any] = ..., doc: Optional[Any] = ...): ...
def timer(command: str = ..., number: int = ..., setup: str = ...): ...
def interpreterBits() -> int: ...
def toZip(directory: Any, zipFile: Any): ...
def subpackages(packagemod: Any) -> None: ...

from typing import *
from builtins import str
from pymel.core.language import mel as mel, melGlobals as melGlobals
from pymel.internal.factories import Callback as Callback, CallbackWithArgs as CallbackWithArgs
from typing import Any, Optional

thisModuleCmd: Any

def lsUI(**kwargs: Any): ...

scriptTableCmds: Any

def scriptTable(*args: Any, **kwargs: Any): ...
def getPanel(*args: Any, **kwargs: Any): ...
def verticalLayout(*args: Any, **kwargs: Any): ...
def horizontalLayout(*args: Any, **kwargs: Any): ...
def promptBox(title: Any, message: Any, okText: Any, cancelText: Any, **kwargs: Any): ...
def promptBoxGenerator(*args: Any, **kwargs: Any) -> None: ...
def confirmBox(title: str, message: str, yes: str=..., no: str=..., *moreButtons: str, **kwargs: Any) -> Union[bool, str]: ...
def informBox(title: Any, message: Any, ok: str = ...) -> None: ...

class PopupError(Exception):
    def __new__(cls, msgOrException: Union[str, Exception], title: str=..., button: str=..., msg: Optional[str]=..., icon: str=...) -> PopupError: ...
    def __init__(self, msg: Any, *args: Any, **kwargs: Any) -> None: ...

def promptForFolder(): ...
def promptForPath(**kwargs: Any): ...
def fileDialog(*args: Any, **kwargs: Any): ...
def showsHourglass(func: Any): ...
def pathButtonGrp(name: Optional[Any] = ..., *args: Any, **kwargs: Any): ...
def folderButtonGrp(name: Optional[Any] = ..., *args: Any, **kwargs: Any): ...
def vectorFieldGrp(*args: Any, **kwargs: Any): ...
def uiTemplate(name: Optional[Any] = ..., force: bool = ..., exists: Optional[Any] = ...): ...
def setParent(*args: Any, **kwargs: Any): ...
def currentParent(): ...
def currentMenuParent(): ...
def menu(*args: Any, **kwargs: Any): ...
def autoLayout(*args: Any, **kwargs: Any): ...
def subMenuItem(*args: Any, **kwargs: Any): ...
def valueControlGrp(name: Any=..., create: Any=..., dataType: Union[str, type]=..., slider: bool=..., value: Union[int, bool, float, str, Path, Vector, List[Union[int, bool, float]]]=..., numberOfControls: int=..., **kwargs: Any) -> None: ...
def getMainProgressBar(): ...
def attrColorSliderGrp(*args: Any, **kwargs: Any): ...
def attrControlGrp(*args: Any, **kwargs: Any): ...
def attrEnumOptionMenu(*args: Any, **kwargs: Any): ...
def attrEnumOptionMenuGrp(*args: Any, **kwargs: Any): ...
def attrFieldGrp(*args: Any, **kwargs: Any): ...
def attrFieldSliderGrp(*args: Any, **kwargs: Any): ...
def attrNavigationControlGrp(*args: Any, **kwargs: Any): ...
def attributeMenu(*args: Any, **kwargs: Any): ...
def colorIndexSliderGrp(*args: Any, **kwargs: Any): ...
def colorSliderButtonGrp(*args: Any, **kwargs: Any): ...
def colorSliderGrp(*args: Any, **kwargs: Any): ...
def columnLayout(*args: Any, **kwargs: Any): ...
def colorEditor(*args: Any, **kwargs: Any): ...
def floatField(*args: Any, **kwargs: Any): ...
def floatFieldGrp(*args: Any, **kwargs: Any): ...
def floatScrollBar(*args: Any, **kwargs: Any): ...
def floatSlider(*args: Any, **kwargs: Any): ...
def floatSlider2(*args: Any, **kwargs: Any): ...
def floatSliderButtonGrp(*args: Any, **kwargs: Any): ...
def floatSliderGrp(*args: Any, **kwargs: Any): ...
def frameLayout(*args: Any, **kwargs: Any): ...
def iconTextButton(*args: Any, **kwargs: Any): ...
def iconTextCheckBox(*args: Any, **kwargs: Any): ...
def iconTextRadioButton(*args: Any, **kwargs: Any): ...
def iconTextRadioCollection(*args: Any, **kwargs: Any): ...
def iconTextScrollList(*args: Any, **kwargs: Any): ...
def iconTextStaticLabel(*args: Any, **kwargs: Any): ...
def intField(*args: Any, **kwargs: Any): ...
def intFieldGrp(*args: Any, **kwargs: Any): ...
def intScrollBar(*args: Any, **kwargs: Any): ...
def intSlider(*args: Any, **kwargs: Any): ...
def intSliderGrp(*args: Any, **kwargs: Any): ...
def paneLayout(*args: Any, **kwargs: Any): ...
def panel(*args: Any, **kwargs: Any): ...
def radioButton(*args: Any, **kwargs: Any): ...
def radioButtonGrp(*args: Any, **kwargs: Any): ...
def radioCollection(*args: Any, **kwargs: Any): ...
def radioMenuItemCollection(*args: Any, **kwargs: Any): ...
def symbolButton(*args: Any, **kwargs: Any): ...
def symbolCheckBox(*args: Any, **kwargs: Any): ...
def textCurves(*args: Any, **kwargs: Any): ...
def textField(*args: Any, **kwargs: Any): ...
def textFieldButtonGrp(*args: Any, **kwargs: Any): ...
def textFieldGrp(*args: Any, **kwargs: Any): ...
def text(*args: Any, **kwargs: Any): ...
def textScrollList(*args: Any, **kwargs: Any): ...
def toolButton(*args: Any, **kwargs: Any): ...
def toolCollection(*args: Any, **kwargs: Any): ...
def window(*args: Any, **kwargs: Any): ...
def blendShapeEditor(*args: Any, **kwargs: Any): ...
def blendShapePanel(*args: Any, **kwargs: Any): ...
def button(*args: Any, **kwargs: Any): ...
def checkBox(*args: Any, **kwargs: Any): ...
def checkBoxGrp(*args: Any, **kwargs: Any): ...
def confirmDialog(*args: Any, **kwargs: Any): ...
def fontDialog(*args: Any, **kwargs: Any): ...
def formLayout(*args: Any, **kwargs: Any): ...
def menuBarLayout(*args: Any, **kwargs: Any): ...
def menuEditor(*args: Any, **kwargs: Any): ...
def menuItem(*args: Any, **kwargs: Any): ...
def menuSet(*args: Any, **kwargs: Any): ...
def promptDialog(*args: Any, **kwargs: Any): ...
def scrollField(*args: Any, **kwargs: Any): ...
def scrollLayout(*args: Any, **kwargs: Any): ...
def scriptedPanel(*args: Any, **kwargs: Any): ...
def scriptedPanelType(*args: Any, **kwargs: Any): ...
def shelfButton(*args: Any, **kwargs: Any): ...
def shelfLayout(*args: Any, **kwargs: Any): ...
def shelfTabLayout(*args: Any, **kwargs: Any): ...
def tabLayout(*args: Any, **kwargs: Any): ...
def outlinerEditor(*args: Any, **kwargs: Any): ...
def optionMenu(*args: Any, **kwargs: Any): ...
def outlinerPanel(*args: Any, **kwargs: Any): ...
def optionMenuGrp(*args: Any, **kwargs: Any): ...
def animCurveEditor(*args: Any, **kwargs: Any): ...
def animDisplay(*args: Any, **kwargs: Any): ...
def separator(*args: Any, **kwargs: Any): ...
def visor(*args: Any, **kwargs: Any): ...
def layout(*args: Any, **kwargs: Any): ...
def layoutDialog(*args: Any, **kwargs: Any): ...
def layerButton(*args: Any, **kwargs: Any): ...
def hyperGraph(*args: Any, **kwargs: Any): ...
def hyperPanel(*args: Any, **kwargs: Any): ...
def hyperShade(*args: Any, **kwargs: Any): ...
def rowColumnLayout(*args: Any, **kwargs: Any): ...
def rowLayout(*args: Any, **kwargs: Any): ...
def renderWindowEditor(*args: Any, **kwargs: Any): ...
def glRenderEditor(*args: Any, **kwargs: Any): ...
def keyframeStats(*args: Any, **kwargs: Any): ...
def keyframeOutliner(*args: Any, **kwargs: Any): ...
def canvas(*args: Any, **kwargs: Any): ...
def channelBox(*args: Any, **kwargs: Any): ...
def gradientControl(*args: Any, **kwargs: Any): ...
def gradientControlNoAttr(*args: Any, **kwargs: Any): ...
def gridLayout(*args: Any, **kwargs: Any): ...
def messageLine(*args: Any, **kwargs: Any): ...
def popupMenu(*args: Any, **kwargs: Any): ...
def modelEditor(*args: Any, **kwargs: Any): ...
def modelPanel(*args: Any, **kwargs: Any): ...
def helpLine(*args: Any, **kwargs: Any): ...
def hardwareRenderPanel(*args: Any, **kwargs: Any): ...
def image(*args: Any, **kwargs: Any): ...
def nodeIconButton(*args: Any, **kwargs: Any): ...
def commandLine(*args: Any, **kwargs: Any): ...
def progressBar(*args: Any, **kwargs: Any): ...
def defaultLightListCheckBox(*args: Any, **kwargs: Any): ...
def exclusiveLightCheckBox(*args: Any, **kwargs: Any): ...
def clipSchedulerOutliner(*args: Any, **kwargs: Any): ...
def clipEditor(*args: Any, **kwargs: Any): ...
def deviceEditor(*args: Any, **kwargs: Any): ...
def devicePanel(*args: Any, **kwargs: Any): ...
def dynPaintEditor(*args: Any, **kwargs: Any): ...
def nameField(*args: Any, **kwargs: Any): ...
def cmdScrollFieldExecuter(*args: Any, **kwargs: Any): ...
def cmdScrollFieldReporter(*args: Any, **kwargs: Any): ...
def cmdShell(*args: Any, **kwargs: Any): ...
def palettePort(*args: Any, **kwargs: Any): ...

saveShelf: Any

def runTimeCommand(*args: Any, **kwargs: Any): ...

saveAllShelves: Any

def soundControl(*args: Any, **kwargs: Any): ...
def flowLayout(*args: Any, **kwargs: Any): ...

toggleWindowVisibility: Any
webBrowserPrefs: Any
thumbnailCaptureComponent: Any
disableIncorrectNameWarning: Any
saveViewportSettings: Any

def hotBox(*args: Any, **kwargs: Any): ...
def componentBox(*args: Any, **kwargs: Any): ...
def hotkeyCheck(*args: Any, **kwargs: Any): ...

outputWindow: Any

def rangeControl(*args: Any, **kwargs: Any): ...

overrideModifier: Any

def webBrowser(*args: Any, **kwargs: Any): ...

workspaceControlState: Any
spreadSheetEditor: Any
createEditor: Any

def nodeEditor(*args: Any, **kwargs: Any): ...
def hudSliderButton(*args: Any, **kwargs: Any): ...
def hudButton(*args: Any, **kwargs: Any): ...
def treeLister(*args: Any, **kwargs: Any): ...

objectTypeUI: Any
menuSetPref: Any
setStartupMessage: Any

def timeControl(*args: Any, **kwargs: Any): ...

multiTouch: Any
renameUI: Any
grabColor: Any
connectControl: Any

def hotkey(*args: Any, **kwargs: Any): ...

windowPref: Any
lsUI: Any

def colorInputWidgetGrp(*args: Any, **kwargs: Any): ...

canCreateCaddyManip: Any
progressWindow: Any

def timeField(*args: Any, **kwargs: Any): ...
def nameCommand(*args: Any, **kwargs: Any): ...

minimizeApp: Any
loadUI: Any
refreshEditorTemplates: Any
panelConfiguration: Any

def annotate(*args: Any, **kwargs: Any): ...

setUITemplate: Any
defaultNavigation: Any
contentBrowser: Any

def nodeOutliner(*args: Any, **kwargs: Any): ...
def falloffCurveAttr(*args: Any, **kwargs: Any): ...

editor: Any
showSelectionInTitle: Any
inViewMessage: Any
setNodeTypeFlag: Any
buttonManip: Any
inViewEditor: Any
editorTemplate: Any

def timeFieldGrp(*args: Any, **kwargs: Any): ...

componentEditor: Any

def dockControl(*args: Any, **kwargs: Any): ...

mayaDpiSetting: Any
setFocus: Any

def headsUpDisplay(*args: Any, **kwargs: Any): ...

deleteUI: Any
setMenuMode: Any
workspacePanel: Any

def workspaceControl(*args: Any, **kwargs: Any): ...
def falloffCurve(*args: Any, **kwargs: Any): ...

panelHistory: Any

def control(*args: Any, **kwargs: Any): ...
def hudSlider(*args: Any, **kwargs: Any): ...

savePrefObjects: Any
linearPrecision: Any

def swatchDisplayPort(*args: Any, **kwargs: Any): ...

hotkeySet: Any
autoPlace: Any
dimWhen: Any
uiTemplate: Any
savePrefs: Any
textManip: Any

def nodeTreeLister(*args: Any, **kwargs: Any): ...
def viewManip(*args: Any, **kwargs: Any): ...
def treeView(*args: Any, **kwargs: Any): ...

artBuildPaintMenu: Any

def picture(*args: Any, **kwargs: Any): ...
def switchTable(*args: Any, **kwargs: Any): ...
def timePort(*args: Any, **kwargs: Any): ...

loadPrefObjects: Any

def soundPopup(*args: Any, **kwargs: Any): ...

disable: Any
scmh: Any

def hotkeyEditorPanel(*args: Any, **kwargs: Any): ...

setParent: Any
scriptEditorInfo: Any
saveMenu: Any
headsUpMessage: Any
showWindow: Any
workspaceLayoutManager: Any

def toolBar(*args: Any, **kwargs: Any): ...

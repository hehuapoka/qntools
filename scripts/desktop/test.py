from pxr import UsdGeom,Usd

stage = Usd.Stage.Open("D:/test/test/a.usda")


for i in stage.TraverseAll():
    print(i.GetName())
    print(i.GetAttribute("id:info"))


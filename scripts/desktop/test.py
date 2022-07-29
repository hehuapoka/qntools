from pxr import UsdGeom,Usd

stage = Usd.Stage.Open("D:/test/test/grid.usd")


for i in stage.TraverseAll():
    for i in i.GetAttributes():
        print(i.GetName())
        print(i.GetTypeName())
        print(i.Get())


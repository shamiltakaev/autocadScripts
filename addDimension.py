import pyautocad
from pyautocad.api import Autocad
from pyautocad.types import APoint


app = Autocad()

lays = list(app.get_selection("Select Object"))[0]
# print(lays.InsertionPoint)

for i in range(len(lays) - 1):
    
    #region Pts
    p1 = APoint(lays[i].InsertionPoint)
    p2 = APoint(lays[i+1].InsertionPoint)
    #endregion

    #region GeometryFigure
    # p1 = APoint(lays[i].Center)
    # p2 = APoint(lays[i + 1].Center)
    #endregion

    # app.model.DimLineInside(p1, p2, p1)
    app.model.AddDimAligned(p1, p2, p1)
import pyautocad
from pyautocad.api import Autocad
from pyautocad.types import APoint


app = Autocad()

lays = list(app.get_selection("Select Object"))

# f = lays[0]


for i in range(len(lays) - 1):
    p1 = APoint(lays[i].Center)
    p2 = APoint(lays[i+1].Center)

    app.model.AddDimAligned(p1, p2, p1)
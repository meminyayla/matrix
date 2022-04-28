#Strassen algoritması ile matris çarpımı
from __future__ import annotations
import math

def matris_tanim(Satir, Sutun):
    matris = [[1 for i in range(Satir)] for j in range(Sutun)]
    return matris

X = matris_tanim(500, 500)
Y = matris_tanim(500, 500)

result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
print("result", result)

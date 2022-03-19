# ctrl+d = 해당 줄 복사, ctrl+/ = 주석처리, shift + d / = 여러줄, ctrl shift alt j = 전체변환

import os

# from IPython.display import HTML as html_print
from pyNastran.bdf.bdf import BDF, CaseControlDeck
model = BDF()

idSectList = []
xLeList = []
yLeList = []
zLeList = []
cList = []

# open sections.dat file_Wing
with open("sections.dat") as datFile:
    sectValueList = [data.split() for data in datFile]
    del sectValueList[0] # 0번 행을 지워라
    for v in sectValueList:
        idSectList.append(v[0])
        xLeList.append(v[1]) # list 원소 추가
        yLeList.append(v[2])
        zLeList.append(v[3])
        cList.append(v[4])

eId = 101
ptList = [] # [ [], [], [] ]
# insert model.add_point(id_no, x, y, z)
for x, y, z, c in zip(xLeList, yLeList, zLeList, cList):
    model.add_point(eId, [float(x), float(y), float(z)])
    ptList.append([float(x), float(y), float(z)])
    eId = eId + 1
    model.add_point(eId, [float(x) + float(c), float(y), float(z)])
    eId = eId + 1


eId2 = 100001
nCh = 5 #나스트란 기본설정. chord 박스 5개
b1Span = float(yLeList[1]) - float(yLeList[0]) # span 길이를 균일하게 하기위한.
for i in range(len(idSectList)-1): #leg, list = 길이, 원소의 갯수
    bSpan = round((float(yLeList[i+1]) - float(yLeList[i])) * nCh / b1Span) #round 반올림
    model.add_paero1(eId2)
    model.add_caero1(eId2, eId2, 1, ptList[i], float(cList[i]), ptList[i+1], float(cList[i+1]), 0, bSpan, 0, nCh, 0)
    eId2 += 1000
#여기서 하고싶은것. 섹션 아이디는 n개이고, 여기서 생성되는 면은 n-1개이므로 섹션아이디-1 = n-1개로 표현
#ptList는 [ [], [], [] ]형태이므로, float 불가. cList는 리스트-플롯 바로적용


bdf_filename_out = os.path.join('sol145_OUT.bdf')
model.write_bdf(bdf_filename_out, enddata=True)
print(bdf_filename_out)

print('----------------------------------------------------------------------------------------------------')
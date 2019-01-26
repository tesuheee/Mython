class Gakubu:
    cant = []
    bacho = 0
    def __init__(self, _cant, _bacho):
        self.cant = _cant
        self.bacho = _bacho
    
class Manager:
    month = 0
    memorial = []
    sun = [1,8,15,22,29]
    
yasumi = [1,8,15,22,29]

gakubusei = []
gakubu1 = Gakubu([3,24], 1)
gakubusei.append(gakubu1)
gakubu2 = Gakubu([1,6], 0)
gakubusei.append(gakubu2)
gakubu3 = Gakubu([15,23], 5)
gakubusei.append(gakubu3)

# 1. 全部の日付に是認を代入
possi = []
for day in range(0,30):
    print(day)
    possi.append(gakubusei)

print(possi[4])



# 2. 一人ひとりのだめな日を取り出して削除
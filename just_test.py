import kppr.models.models as models
from pytorch_lightning.core.lightning import LightningModule
import pickle
# d = dict(name='Bob', age=20, score=88)
# print(d)
# f = open('C:/Users/nulls/Desktop/aa.txt', 'wb',0)
# #对象写入文件
# pickle.dump(d,f)
# f.close()

#文件读取
g = open('/home/yy/oxford_compressed/oxford_evaluation_query.pickle', 'rb')
e=pickle.load(g)
print(e)

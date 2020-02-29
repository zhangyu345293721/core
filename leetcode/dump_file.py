import pickle
from sklearn.externals import joblib
from sklearn.svm import SVC
from sklearn import datasets

#定义一个分类器
svm = SVC()

iris = datasets.load_iris()
X = iris.data
y = iris.target

#训练模型
svm.fit(X,y)

#1.保存成Python支持的文件格式Pickle
#在当前目录下可以看到svm.pickle
with open('svm.pickle','wb') as fw:
    pickle.dump(svm,fw)
#加载svm.pickle
with open('svm.pickle','rb') as fr:
    new_svm1 = pickle.load(fr)

#2.保存成sklearn自带的文件格式Joblib
joblib.dump(svm,'vm.pkl')
#加载svm.pkl
new_svm2 = joblib.load('svm.pkl')
print (new_svm2.predict(X[0:1]))
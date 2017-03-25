from sklearn import tree
import json

file = open("features.txt","r")
text = file.read()

"""lines[0] = lines[0].rstrip()"""

json_data = json.loads(text)
print(json_data)

"""features=[[140,1],[130,1],[150,0],[170,0]]
labels=[0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print(clf.predict([[160,0]]))"""

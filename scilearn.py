from sklearn import tree
import json

data = 0
with open('./training_data/data.txt') as json_data:
    data = json.load(json_data)

targets = 0
with open('./training_data/targets.txt') as json_data:
    targets = json.load(json_data)

#print(data[0][3]);

"""print(data)"""
clf = tree.DecisionTreeClassifier()
clf = clf.fit(data,targets)

print('Loaded model ...')
while(1):
	print('Enter data')
	mi = float(input('Enter monthly income'))
	me = float(input('Enter monthly expenditure'))
	ti = mi*12
	rcs = float(input('Enter rate of change of savings'))
	age = float(input('Enter age'))
	ta = float(input('Enter monthly bank balance'))
	print('Predicting ...')
	print(clf.predict([[mi, me, ti, rcs, age, ta]]))

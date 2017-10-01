from sklearn import tree

## smooth 0 vs bumpy 1
features = [[140, 1],[130, 1],[150,0],[170,0]]

## to lable apple with 0 and orage 1
labels = [0,0,1,1]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(features, labels)

print clf.predict([[155,0]])

print '1 is Apple 0 is Orange'
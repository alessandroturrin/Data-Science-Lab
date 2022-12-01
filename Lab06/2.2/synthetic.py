from sklearn.tree import DecisionTreeClassifier, plot_tree
import pandas as pd
import matplotlib.pyplot as plt

#2.1
df = pd.read_csv('2d-synthetic.csv')
print(df.values.shape)
X = df.values[:,:2]
y = df.values[:,2]
plt.scatter(X[:,0],X[:,1],c=y)
plt.xlabel('x0')
plt.ylabel('x1')
plt.show()

#2.2
clf = DecisionTreeClassifier()
clf.fit(X,y)
plot_tree(clf)
plt.show()

#2.3
X_r = (X[:,0] + X[:,1]).reshape(500,1)
clf_r = DecisionTreeClassifier()
clf_r.fit(X_r, y)
plot_tree(clf)
plt.show()
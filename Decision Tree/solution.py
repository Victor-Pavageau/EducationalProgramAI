from sklearn import tree
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("source (edited).csv", sep=';')
inputs = df.drop('type de voiture', axis='columns')
target = df.drop(['hauteur (en m)', 'vitesse max (en km/h)', 'energie', 'nombre de places'], axis='columns')

feature_names = ["Hauteur", "Vitesse", "Energie", "Nombres de places"]
class_names = ["4x4", "Berline", "Bus", "Sportive"]

model = tree.DecisionTreeClassifier()
model.fit(inputs, target)

print(model.predict([[35, 200, 0, 25]]))

fig = plt.figure(figsize=(25,20))
tree = tree.plot_tree(model, filled=True, feature_names=feature_names, rounded=True, class_names=class_names)
fig.savefig("tree.png")

from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import pandas
from csv import writer


def GetDecisionTreeModel(filename):
    dataframe = pandas.read_csv(filename)

    inputs = dataframe.drop('type de voiture', axis='columns')
    target = dataframe.drop(['hauteur (en cm)', 'vitesse max (en km/h)', 'energie', 'nombre de places'], axis='columns')

    DecisionTree = tree.DecisionTreeClassifier()
    DecisionTree.fit(inputs, target)

    return DecisionTree

def GetKNeighborsModel(filename, neighborsNumber):
    dataframe = pandas.read_csv(filename)

    x = dataframe.loc[:,"hauteur (en cm)"]
    y = dataframe.loc[:,"vitesse max (en km/h)"]
    target = dataframe.loc[:,"type de voiture"]
    d=list(zip(x, y))

    KNeighbors = KNeighborsClassifier(n_neighbors = neighborsNumber, metric='euclidean', weights='distance')
    KNeighbors.fit(d,target)

    return KNeighbors

def MakePrediction(valuesList):
    print(valuesList)
    decisionTreePredict = int(DecisionTreeModel.predict([[valuesList[0], valuesList[1], valuesList[2], valuesList[3]]]))
    KNeighborsPredict = int(KNeighborsModel.predict([[valuesList[0], valuesList[1]]]))

    if(decisionTreePredict == valuesList[4]):
        print("Le decision tree modèle à trouvé qu'il s'agissait de : " + str(decisionTreePredict) + "\n")
    else:
        print("Le decision tree modèle s'est trompé et à trouvé : " + str(decisionTreePredict) + " au lieu de : " + str(valuesList[4]) + "\n")

    if(KNeighborsPredict == valuesList[4]):
        print("Le K proches voisins modèle à trouvé qu'il s'agissait de : " + str(KNeighborsPredict) + "\n")
    else:
        print("Le K proches voisins modèle s'est trompé et à trouvé : " + str(KNeighborsPredict) + " au lieu de : " + str(valuesList[4]) + "\n")


def AddValuesToCSV(filename, valuesList):
    with open(filename, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(valuesList)


filename = "source.csv"
# ["4x4", "Berline", "Bus", "Sportive"]
Continue = True

neighborsNumber = int(input("Combien de voisins voulez vous utiliser ?\n"))

while(Continue):
    KNeighborsModel = GetKNeighborsModel(filename, neighborsNumber)
    DecisionTreeModel = GetDecisionTreeModel(filename)
    valuesList = [int(input("Hauteur de la prédiction ?\n")), int(input("Vitesse de la prédiction ?\n")), int(input("Energie de la prédiction ?\n")), int(input("Nombre de places de la prédiction ?\n")), int(input("Réponse de la prédiction ?\n"))]
    MakePrediction(valuesList)
    addValue = input("Voulez-vous ajouter cette valeur au jeu de données ?")
    if(addValue in ["yes", "Yes", "y", "oui", "Oui", "o"]):
        AddValuesToCSV(filename, valuesList)
        KNeighborsModel = GetKNeighborsModel(filename, neighborsNumber)
        DecisionTreeModel = GetDecisionTreeModel(filename)
    stop = input("Voulez-vous continuer ?\n")
    if(stop in ["no", "No", "non", "Non", "n"]):
        Continue = False


#print(DecisionTree.predict([[350, 200, 0, 25]]))





##dataframe = pandas.read_csv("source (edited).csv")
##
##x = dataframe.loc[:,"hauteur (en cm)"]
##y = dataframe.loc[:,"vitesse max (en km/h)"]
##lab = dataframe.loc[:,"type de voiture"]
##
##hauteur = 350
##vitesse = 200
##
##k = 7
##
##plt.scatter(x[lab == 0], y[lab == 0], color='g', label='4x4')
##plt.scatter(x[lab == 1], y[lab == 1], color='r', label='Berline')
##plt.scatter(x[lab == 2], y[lab == 2], color='b', label='Bus')
##plt.scatter(x[lab == 3], y[lab == 3], color='m', label='Sportive')
##plt.scatter(hauteur, vitesse, color='k')
##
##plt.legend()
##plt.axis('equal')
##
##d = list(zip(x, y))
##model = KNeighborsClassifier(n_neighbors=k, metric='euclidean', weights='distance')
##model.fit(d, lab)
##print(model.predict([[hauteur, vitesse]]))
##print(model.predict_proba([[hauteur, vitesse]]))
##
##plt.show()

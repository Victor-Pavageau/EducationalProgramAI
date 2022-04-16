import pandas as pd

df = pd.read_csv('./countries (edited).csv', sep=';')

def request1():
    habitants = df["Population"] == 3042004

    print(df[habitants]["Country"])


def request2():
    habitants = df["Population"] <= 50000
    contientG = df["Country"].str.contains('G' or 'g')
    littoral = df["Coastline (coast/area ratio)"] >= "100"

    print(df[habitants & littoral & contientG]["Country"])

    """Other solution (by lenght) :

    littoral = df["Coastline (coast/area ratio)"].str.rpartition(',')[0].str.len() >= 3

    """


def request3():
    phone = df["Phones (per 1000)"] == df["Phones (per 1000)"].max()

    print(df[phone]["Country"])

    """Other solutions (by index) :

    phone = df["Phones (per 1000)"].idxmax()
    print(df.iloc[phone]["Country"])

    """


print("Premier client : \n")
request1()

print("\n\nDeuxième client : \n")
request2()

print("\n\nTroisième client : \n")
request3()

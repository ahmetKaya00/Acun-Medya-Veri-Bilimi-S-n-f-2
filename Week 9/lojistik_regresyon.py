from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data_classification = {
    "Age": [22,25,47,52,46,56,55,60,62,61],
    "Income": [25000,32000,47000,52000,46000,58000,60000,62000,64000,63000],
    "Purchased": [0,0,1,1,1,1,1,1,1,1],
}

dt_classication = pd.DataFrame(data_classification)

print("Lojistik Regresyon Veri Seti:")
print(dt_classication.head())

print("\n Lojistik Regresyon İçin Veri Eğitim ve Test Setine Aytılıyor...\n")

x_cls = dt_classication[["Age","Income"]]
y_cls = dt_classication["Purchased"]

x_train_cls,x_test_cls,y_train_cls,y_test_cls = train_test_split(x_cls,y_cls,test_size=0.2,random_state=42)
print(f"Eğitim Seti Boyutu: {x_train_cls.shape}")
print(f"Test Seti Boyutu: {x_test_cls.shape}")

print("\n Lineer Regresyon Modeli Eğitiliyor...\n")

model = LogisticRegression()

model.fit(x_train_cls,y_train_cls)

print("\n Logistic Regresyon Modeli Eğitildi!")
print("Katsayılar:")
print(model.coef_)
print(f"Intercept (b0): {model.intercept_}")
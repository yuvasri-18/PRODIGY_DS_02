Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: D:/intern/task 2/tsk pg 2.py
First few rows of the dataset:
   PassengerId  Survived  Pclass     Sex  ...  Title  GrpSize FareCat AgeCat
0            1         0       3    male  ...     Mr   couple    0-10  16-32
1            2         1       1  female  ...    Mrs   couple  70-100  32-48
2            3         1       3  female  ...   Miss     solo    0-10  16-32
3            4         1       1  female  ...    Mrs   couple   40-70  32-48
4          138         0       1    male  ...     Mr   couple   40-70  32-48

[5 rows x 11 columns]

Missing values in the dataset:
PassengerId    0
Survived       0
Pclass         0
Sex            0
SibSp          0
Parch          0
Embarked       0
Title          0
GrpSize        0
FareCat        0
AgeCat         0
dtype: int64

Basic statistics of the dataset:
        PassengerId    Survived      Pclass   Sex  ...  Title  GrpSize FareCat AgeCat
count    891.000000  891.000000  891.000000   891  ...    891      891     891    891
unique          NaN         NaN         NaN     2  ...      5        4       6      5
top             NaN         NaN         NaN  male  ...     Mr     solo    0-10  16-32
freq            NaN         NaN         NaN   577  ...    517      462     325    490
mean     446.000000    0.383838    2.308642   NaN  ...    NaN      NaN     NaN    NaN
std      257.353842    0.486592    0.836071   NaN  ...    NaN      NaN     NaN    NaN
min        1.000000    0.000000    1.000000   NaN  ...    NaN      NaN     NaN    NaN
25%      223.500000    0.000000    2.000000   NaN  ...    NaN      NaN     NaN    NaN
50%      446.000000    0.000000    3.000000   NaN  ...    NaN      NaN     NaN    NaN
75%      668.500000    1.000000    3.000000   NaN  ...    NaN      NaN     NaN    NaN
max      891.000000    1.000000    3.000000   NaN  ...    NaN      NaN     NaN    NaN

[11 rows x 11 columns]

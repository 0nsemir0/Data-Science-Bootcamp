# Numpy Questions
import numpy as np
import pandas as pd 
#1 
A = np.array([2,3,5,7,11])
B = np.array([4,6,8,9,10])
vert = np.vstack((A,B))
hori = np.hstack((A,B))
print(vert) 
print(hori)
#2
print(np.intersect1d(A,B))
#One can also run a for loop if need be. 

#3 
mask = (A>= 5) & (A<=10)
result = A[mask]
print(result)

#4
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

condition = (iris_2d[:,2]>1.5) &  (iris_2d[:, 0]<5.0) 

filtered_iris = iris_2d[condition]

print(filtered_iris)

#5 

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

filtered_df = df.iloc[0::20][['Manufacturer', 'Model', 'Type']]
print(filtered_df)

#6 

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

means = {
    'Min.Price': df['Min.Price'].mean(),
    'Max.Price': df['Max.Price'].mean()
}

df.fillna(value=means, inplace=True)

print(df)

#7

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
filtered_rows = df[df.sum(axis=1) > 100]
print(filtered_rows)



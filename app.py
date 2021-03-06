import numpy as np 
import streamlit as st 
from sklearn.datasets import load_iris   #load the dataset
from sklearn.neighbors import KNeighborsClassifier  #import the knn alg
st.title("IRIS FLOWER CLASSIFICATION")

var=load_iris()#load the ddata set

#divide the dataset into input and output
x=var.data  #input
y=var.target  #out[ut]
#print(x)
#print(y)

# call the knn classifier
model=KNeighborsClassifier(n_neighbors=15)

#fit the model
model.fit(x,y)

#to take inputs we are creating sliders
xmin=np.min(x,axis=0)
xmax=np.max(x,axis=1)

#sliders creation
sepal_length=st.slider("Sepal Length",float(xmin[0]),float(xmax[0]))
sepal_width=st.slider("Sepal width",float(xmin[1]),float(xmax[1]))
petal_length=st.slider("Sepal Length",float(xmin[2]),float(xmax[2]))
petal_width=st.slider("Sepal Length",float(xmin[3]),float(xmax[3]))

#predict the model 
y_pred=model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
y_pred

#print the output class
op=['Iris-setosa','Iris-versicolor','Iris-virginica']
if st.button('PREDICT'):
  st.title(op[y_pred[0]])

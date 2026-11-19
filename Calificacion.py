import numpy as np
import streamlit as st
import pandas as pd

st.write(''' # Predicción de calificacion  ''')
st.image("calificacionFoto.png", caption="Predicción la calificacion de una persona.")

st.header('Datos personales')

def user_input_features():
  # Entrada
    Horas de estudio = st.number_input('Horas de estudio:', min_value=1, max_value=140, value = 0, step = 1)
    Horas de sueño = st.number_input('Horas de sueño:', min_value=4, max_value=9, value = 0, step = 1)
  Asistencia = st.number_input('Asistencia:',  min_value=50, max_value=100, value = 0, step = 1)
  Calificaciones previas = st.number_input('Calificaciones previas:', min_value=40, max_value=95, value = 0, step = 1)
  Horas de estudio = st.number_input('Horas de estudio:', min_value=1, max_value=140, value = 0, step = 1)


  user_input_data = {'hours_studied': Edad,
                     'sleep_hours': Genero,
                     'attendance_percent': Altura,
                     'previous_scores': Cintura,
                     }

  features = pd.DataFrame(user_input_data, index=[0])

  return features

df = user_input_features()
prediccion=0
datos =  pd.read_csv('student_exam_scores.csv', encoding='latin-1')
X = datos.drop(columns='exam_score')
y = datos['exam_score']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=7)
LR = LinearRegression()
LR.fit(X_train,y_train)

b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*df['hours_studied'] + b1[1]*df['sleep_hours'] + b1[2]*df['attendance_percent'] + b1[3]*df['previous_scores']

st.subheader('Cálculo de calificacion')
st.write('la calificacion de la persona es ', prediccion)


import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Генерация выдуманных данных
np.random.seed(42)

# Пример данных
data = {
    'Возраст': np.random.choice([18, 25, 35, 45, 55], 100),
    'Пол': np.random.choice(['Мужской', 'Женский'], 100),
    'Тип местности': np.random.choice(['Город', 'Деревня'], 100),
    'Чистота и благоустройство': np.random.randint(1, 6, 100),
    'Качество коммунальных услуг': np.random.randint(1, 6, 100),
    'Наличие школы': np.random.randint(1, 6, 100),
    'Участие в муниципальных выборах': np.random.choice([1, 0], 100),
    'Реакция службы спасения': np.random.randint(1, 6, 100),
    'Дороги ремонтируются': np.random.randint(1, 6, 100),
    'Общественный транспорт': np.random.randint(1, 6, 100)
}

# Создаем DataFrame
df = pd.DataFrame(data)

# Преобразуем категориальные переменные в числовые с помощью Label Encoding
df['Пол'] = df['Пол'].map({'Мужской': 0, 'Женский': 1})
df['Тип местности'] = df['Тип местности'].map({'Город': 0, 'Деревня': 1})

# Настроим Streamlit
st.title("Анализ данных об оценке муниципальных услуг")

# Визуализация распределений
st.subheader("Распределение по возрасту")
fig_age = px.histogram(df, x='Возраст', title="Распределение по возрасту")
st.plotly_chart(fig_age)

st.subheader("Распределение по полу")
fig_gender = px.pie(df, names='Пол', title="Распределение по полу")
st.plotly_chart(fig_gender)

# Визуализация качества муниципальных услуг
st.subheader("Чистота и благоустройство по типу местности")
fig_cleanliness = px.box(df, x='Тип местности', y='Чистота и благоустройство', title="Чистота и благоустройство по типу местности")
st.plotly_chart(fig_cleanliness)

st.subheader("Участие в муниципальных выборах")
fig_participation = px.bar(df, x='Участие в муниципальных выборах', title="Участие в муниципальных выборах")
st.plotly_chart(fig_participation)

# Корреляционная тепловая карта (только для числовых столбцов)
st.subheader("Корреляции между переменными")
fig_corr = px.imshow(df.corr(), text_auto=True, title="Корреляции между переменными")
st.plotly_chart(fig_corr)

# Возможность просмотра таблицы данных
st.subheader("Данные респондентов")
st.dataframe(df)

# Запуск приложения
if __name__ == '__main__':
    st.write("Анализ завершён!")

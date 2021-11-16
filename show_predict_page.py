import streamlit as st
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_model():
    with open('saved_steps.pk', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data['model']
le_country = data['le_country']
le_education = data['le_education']



def show_predict_page():
    @st.cache
    def load_data():
        df = pd.read_csv('stackoverflow_df_final.csv')
        return df

    df = load_data()

    st.title('Salary Prediction for Developers')
    st.subheader('Based on 2021 Stack Overflow Annual Developer Survey')
    st.write('')
    st.write('')
    st.write("""
            ### Enter Info to Predict Salary
            """)
    st.write('')

    countries = (
        'United States of America',
        'India',
        'Germany',
        'United Kingdom of Great Britain and Northern Ireland',
        'Canada',
        'France',
        'Brazil',
        'Spain',
        'Netherlands',
        'Australia',
        'Poland',
        'Italy',
        'Russian Federation',
        'Sweden',
        'Turkey',
        'Switzerland',
        'Israel',                                                    
        'Norway'
    )

    education = (
        'Bachelor',
        'Master',
        'Post Grad',
        'No College'
    )

    col1, col2 = st.columns(2)

    with col1:
        country = st.selectbox('Select Country', countries)

    with col2:
        education = st.selectbox('Select Level of Education', education)

    experience = st.slider('Years of Experience', 0, 50, 3)

    ok = st.button('Predict Salary')
    
    st.write('')
    st.write('')
    
    if ok:
        Z = np.array([[country, education, experience]])
        Z[:, 0] = le_country.transform(Z[:, 0])
        Z[:, 1] = le_education.transform(Z[:, 1])
        Z = Z.astype(float)

        salary = model.predict(Z)

        st.subheader(f'Estimated Salary: ${salary[0]:,.0f}')
        st.write('')

    # exh_1 = df['Country'].value_counts()

    # fig1, ax1 = plt.subplots()
    # ax1.pie(exh_1, labels=exh_1.index, autopct="%1.1f%%", shadow=True, startangle=90)
    # ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    # st.write("""#### Number of Data from different countries""")

    # st.pyplot(fig1)

    st.write(
        """
    #### Mean Salary Based On Country
    """
    )

    exh_2 = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(exh_2)

    st.write(
        """
    #### Mean Salary Based On Experience
    """
    )

    exh_3 = df.groupby(["Experience"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(exh_3)


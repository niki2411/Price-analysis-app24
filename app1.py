import streamlit as st
import numpy as np
import pandas as pd
import datetime
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("customer_shopping_data.csv")
st.title("Price Analysis Based on the Customer Shopping Data")
st.sidebar.title("Set the Parameters")
cust_cols = ['invoice_no','customer_id']
categorical_cols = ['gender','category','payment_method','shopping_mall']
numerical_cols = ['age','quantity','price']

#all_columns =  categorical_cols + numerical_cols
select = st.sidebar.selectbox("Choose a Customer ID or Invoice Number:",cust_cols)
select_cols = st.sidebar.selectbox("Select a column:",categorical_cols)
select_cols1 = st.sidebar.selectbox("Choose a Column for Comparison:",numerical_cols)

st.subheader("Spending of Male and Female Customers")
st.markdown("---------------------------------------------------------------------------")
female_customers = df[df['gender'] == 'Female'].head(10)
male_customers = df[df['gender'] == 'Male'].head(10)
gender_option = st.radio("Select Gender:", ["Female", "Male"])



if cust_cols:
    if select in cust_cols:
        if gender_option == "Female":
            fig =px.line(female_customers,x=select,y="price",title="Spending of Female Customers",
                         labels={select: select.capitalize(), "price": "Spending"})
        else:
            fig =px.line(male_customers,x=select,y="price",title="Spending of male Customers",
                         labels={select: select.capitalize(), "price": "Spending"})
    st.plotly_chart(fig)

st.subheader("Price Variation Across Different Parameters")
st.markdown("---------------------------------------------------------------------------")
if select_cols:
    if select_cols in categorical_cols:
        fig = px.bar(df,x=select_cols,y="price",title=f"Price Variation According to {select_cols}")
    else:
        fig = px.box(df, x=select_cols,y="price",trendline="ols",title=f"price vs {select_cols}")
    st.plotly_chart(fig)

st.subheader("Price Analysis Across Shopping Malls by Gender and Selected Column")
st.markdown("---------------------------------------------------------------------------")
if select_cols1:
    if select_cols in numerical_cols:
        fig = px.box(df,x=select_cols1,y="price",title=f"price variation by {select_cols1}")
    else:
        fig = px.scatter(df, x=select_cols1,y="price",color='shopping_mall',symbol='gender',trendline="ols",title=f"Price vs {select_cols1}")
    st.plotly_chart(fig)

st.subheader("Payment Method Distribution by Gender")
st.markdown("---------------------------------------------------------------------------")
fig1 = plt.figure(figsize=(14,4))
sns.countplot(x='payment_method',data=df,hue='gender')
st.pyplot(fig1)

st.subheader("Price Distribution Across Categories by Gender")
st.markdown("---------------------------------------------------------------------------")
fig2 = px.histogram(df,x="category",y="price",color="gender",marginal="box")
st.plotly_chart(fig2)


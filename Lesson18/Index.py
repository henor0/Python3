import pandas as pd
import streamlit as st
import plotly.express as px  # Corrected import

st.header('Displaying DataFrames')


data = pd.DataFrame({
    'Name': ['Alice', 'Michael', 'Andy'],
    'Age': [20, 58, 13],
    'City': ['NYC', 'MIAMI', 'London']
})

st.dataframe(data)


books_df = pd.read_csv('Lesson18/bestsellers_with_categories_2022_03_27.csv')


st.title('Bestseller Books Analysis')
st.write('This app analyzes the Amazon Top selling books from 2009 to 2022')


st.subheader("Summary Statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()


col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
col4.metric("Average Price", f"${average_price:.2f}")


st.subheader("Dataset Preview")
st.write(books_df.head())


col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

    st.subheader("Genre Distribution")
    fig= px.pie(books_df, names='Genre', title='Most Liked Genre(2009 - 2022)', color='Genre', color_discrete_sequence=px.colors.sequential.Plasma)

    st.plotly_chart(fig)

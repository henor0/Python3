import pandas as pd
import streamlit as st
import plotly.express as px  # Corrected import

# Header of the app
st.header('Displaying DataFrames')

# Sample data for illustration
data = pd.DataFrame({
    'Name': ['Alice', 'Michael', 'Andy'],
    'Age': [20, 58, 13],
    'City': ['NYC', 'MIAMI', 'London']
})

# Display the sample DataFrame
st.dataframe(data)

# Load the dataset from Kaggle CSV file
books_df = pd.read_csv('Lesson18/bestsellers_with_categories_2022_03_27.csv')

# App title and description
st.title('Bestseller Books Analysis')
st.write('This app analyzes the Amazon Top-selling books from 2009 to 2022')

# Subheader and statistics
st.subheader("Summary Statistics")

total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

# Display metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
col4.metric("Average Price", f"${average_price:.2f}")

# Preview the dataset
st.subheader("Dataset Preview")
st.write(books_df.head())

# Create two columns for separate visualizations
col1, col2 = st.columns(2)

# Column 1: Top 10 Book Titles
with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

# Column 2: Top 10 Authors and Genre Distribution
with col2:
    # Displaying the top 10 authors
    st.subheader("Top 10 Authors")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

    # Pie chart for Genre Distribution
    st.subheader("Genre Distribution")
    fig = px.pie(books_df, names='Genre', title='Most Liked Genre (2009 - 2022)', color='Genre',
                 color_discrete_sequence=px.colors.sequential.Plasma)
    st.plotly_chart(fig)

# Adding a scatter plot to visualize relationships between price and rating
st.subheader("Price vs. User Rating")
fig2 = px.scatter(books_df, x='Price', y='User Rating', color='Genre', title="Price vs. User Rating",
                  color_discrete_sequence=px.colors.qualitative.Set1)
st.plotly_chart(fig2)

# Filter options for users
st.subheader("Filter Books")
genre = st.selectbox('Select Genre', books_df['Genre'].unique())
filtered_books = books_df[books_df['Genre'] == genre]
st.write(f"Books filtered by genre: {genre}")
st.dataframe(filtered_books)

# Displaying more statistics after filter
st.subheader(f"Statistics for {genre} Books")
filtered_total = filtered_books.shape[0]
filtered_average_rating = filtered_books['User Rating'].mean()
filtered_average_price = filtered_books['Price'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Books in Genre", filtered_total)
col2.metric("Average Rating in Genre", f"{filtered_average_rating:.2f}")
col3.metric("Average Price in Genre", f"${filtered_average_price:.2f}")

# Creating a bar chart to show the distribution of User Ratings for the selected genre
st.subheader(f"User Rating Distribution for {genre}")
rating_dist = filtered_books['User Rating'].value_counts().sort_index()
st.bar_chart(rating_dist)

import pandas as pd
import streamlit as st
import plotly.express as px


# Title for the Streamlit app
st.title('Data Visualization and Analysis App')

# Sidebar for data input
st.sidebar.header('Data Input Options')

# Create session state to store data
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Name', 'Age', 'City'])

# Data Insertion: Choose between uploading CSV or entering data manually
data_option = st.sidebar.radio("Choose Data Input Method", ["Upload CSV", "Insert Data Manually"])

# If CSV is selected, allow file upload
if data_option == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        # Read and display the uploaded data
        st.session_state.data = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(st.session_state.data.head())

# If "Insert Data Manually" is selected, allow manual entry
elif data_option == "Insert Data Manually":
    st.sidebar.subheader("Enter Data")
    name = st.sidebar.text_input("Name")
    age = st.sidebar.number_input("Age", min_value=1, step=1)
    city = st.sidebar.text_input("City")

    # Button to add data to session state
    if st.sidebar.button("Add Data"):
        new_data = pd.DataFrame({'Name': [name], 'Age': [age], 'City': [city]})
        st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
        st.write("New Data Added!")
        st.dataframe(st.session_state.data)

# Display data if available
if st.session_state.data.shape[0] > 0:
    st.subheader("Full Data")
    st.dataframe(st.session_state.data)

    # Sidebar for filtering data
    st.sidebar.header("Filter Data")
    city_filter = st.sidebar.selectbox("Select a City to filter", st.session_state.data['City'].unique())
    filtered_data = st.session_state.data[st.session_state.data['City'] == city_filter]

    st.write(f"Filtered Data (City: {city_filter}):")
    st.dataframe(filtered_data)

    # Display some statistics
    st.subheader("Summary Statistics")
    total_entries = len(st.session_state.data)
    avg_age = st.session_state.data['Age'].mean()
    st.write(f"Total Entries: {total_entries}")
    st.write(f"Average Age: {avg_age:.2f}")



    # Plot City distribution (Pie Chart)
    st.subheader("City Distribution")
    fig2 = px.pie(st.session_state.data, names='City', title="City Distribution", color='City')
    st.plotly_chart(fig2)

else:
    st.write("No data yet. Please upload a CSV or insert data manually.")

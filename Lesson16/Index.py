import streamlit as st


def main():
    st.title('Hello World!')

if __name__ == "__main__":
    main()


if st.button("Click me"):
    st.write("Button Clicked")

if st.checkbox("Check me"):
    st.write("Checkbox Checked")


if st.checkbox("Click me to show you some text"):
    st.text("You are seeing this text because you checked the button")


    user_input = st.text_input("Enter text", "Shenoni nje tekst")
    st.write("You Entered:", user_input)


    age = st.number_input("Enter your age", min_value=1, max_value=100)
    st.write(f'Your age: {age}')


    user_message = st.text_area("Enter a message")
    st.write(f"Your message: {user_message}")

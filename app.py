import streamlit as st 
st.title("Power Calculator...")
st.write("Enter a number to calculate the power")
n=st.number_input("Enter an integer:", value=1, step=1)

st.write(f"square of the number is {n**2}")
 
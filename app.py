import streamlit as st
import pandas as pd


def main():
    st.title("SQLPlayground")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Homepage")

    else:
        st.subheader("About")


if __name__ == "__main__":
    main()

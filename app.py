import streamlit as st
import pandas as pd


def main():
    st.title("SQLPlayground")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Homepage")

        col1, col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("SQL Code Here")
                submit_code = st.form_submit_button("Execute")

            with col2:
                if submit_code:
                    st.info("Query submitted")
                    st.write(raw_code)


    else:
        st.subheader("About")


if __name__ == "__main__":
    main()

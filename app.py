import streamlit as st
import pandas as pd

import sqlite3
conn = sqlite3.connect("data/world.sqlite")
c = conn.cursor()


def sql_executor(raw_code):
    c.execute(raw_code)
    conn.commit()
    data = c.fetchall()
    return data



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
                    st.code(raw_code)

                    query_result = sql_executor(raw_code)
                    with st.expander("Result"):
                        st.write(query_result)


    else:
        st.subheader("About")


if __name__ == "__main__":
    main()

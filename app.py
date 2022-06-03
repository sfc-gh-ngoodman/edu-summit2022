
import streamlit as st
import snowflake.connector

st.title("Hello World!")

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return snowflake.connector.connect(**st.secrets["snowflake"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT current_account();")

# Print results.
for row in rows:
    st.write(f"Result : {row[0]}")

    
with st.form(key='my_form'):
    text_input = st.text_input(label='Enter your question:')
    submit_button = st.form_submit_button(label='Submit Question'                                      
    if submit_button:
        st.write(f'hello {text_input}')

import streamlit as st

st.title("Hello world!")

st.info(
    """
🎊 Congrats, here's your running Streamlit app! Now go ahead and fill in your credentials using
[local secrets](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management#develop-locally-with-secrets)!

We count on you to achieve your missions! :muscle:
"""
)

# Hint...
# import snowflake_conn as sf
# st.write(sf.sql_to_dataframe("select 1"))

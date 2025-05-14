import streamlit as st
from checker.analyzer import analyze_site
from checker.report import format_report

st.set_page_config(page_title="Website Legitimacy Checker Bot")
st.title("Legitimacy Checker Chatbot")

user_input = st.text_input("Ask if a website is legit (e.g. 'Is example.com safe?')")

if user_input:
    with st.spinner("Analyzing site..."):
        site_url = user_input.strip().split()[-1]  # naive URL grab
        result = analyze_site(site_url)
        message = format_report(result)
        st.markdown(message, unsafe_allow_html=True)
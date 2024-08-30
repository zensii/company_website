import streamlit as st
from email_sender import send_mail


with st.form(key='email_form'):
    usr_email = st.text_input('Your Email Address')
    topic = st.selectbox('Select a topic to discuss', ['Job Inquiries', 'Project Proposals', 'Other'], index=None)
    message = st.text_area('Your message here')
    button = st.form_submit_button('Send')

if button:
    if topic:
        send_mail(usr_email, topic, message)
        st.info('Message sent!')
    else:
        st.warning('Please select a topic first')

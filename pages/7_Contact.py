import streamlit as st


st.set_page_config(page_title="Contact Information")

st.title(':mailbox: Contact Information')

st.markdown(
    """
        - [LinkedIn](https://www.linkedin.com/in/muhammad-ahsan/)
        - [Twitter](https://twitter.com/_muhammad_ahsan)
        - [Github](https://github.com/muhammad-ahsan)
    """
)

contact_form = """
<form action="https://formsubmit.co/0cf83266170d5d1f16791d7395c5e8fa" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <input type="text" name="subject" placeholder="Subject" optional>
     <textarea name="message" placeholder="Your Message"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


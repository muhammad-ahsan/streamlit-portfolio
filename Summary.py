import json

import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(layout="wide")


def read_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def read_custom_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


lottie_firstpage = read_lottie_file("code.json")
lottie_coding = read_lottie_file("summary.json")
lottie_project = read_lottie_file("projects.json")
lottie_ds = read_lottie_file("ds.json")
lottie_de = read_lottie_file("de.json")
lottie_da = read_lottie_file("da.json")
lottie_ga = read_lottie_file("ga.json")

with st.container():
    backgroundColor = "#FFC0CB"
    left_column, right_column = st.columns(2)
    with right_column:
        st.write("##")
        st.subheader("Bonjour!")
        st.header("I'm Ahsan 🇬🇧🇩🇪")
        st.markdown('**Lead Data Scientist & Engineer**')
        # Add Link to your repo
        '''
            [![Repo](https://badgen.net/badge/icon/LinkedIn?icon=linkedin&label)](https://www.linkedin.com/in/muhammad-ahsan/)
            [![Repo](https://flat.badgen.net/badge/icon/GitHub?icon=xyz&label)](https://github.com/muhammad-ahsan)
            [![Repo](https://flat.badgen.net/badge/icon/Twitter?icon=xyz&label)](https://twitter.com/_muhammad_ahsan) 
             
        '''
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(''' <a target="_self" href="#contact-me">
                            <button type=submit>
                                Get in touch →
                            </button>
                        </a>''', unsafe_allow_html=True)

    with left_column:
        st_lottie(lottie_firstpage, height=600, key="coding1")

with st.container():
    st.markdown("<h2 style='text-align: center; '>My Services</h2>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; '>I help businesses solve problems using data and "
                "machine learning</h6>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st_lottie(lottie_ds, height=300, width=300)
        st.markdown("<h4 style='text-align: left; '>Data Science & Engineering</h4>", unsafe_allow_html=True)
        st.markdown("<ul>"
                    "<li>Machine Learning Model Development</li>"
                    "<li>Predictive Analytics</li>"
                    "<li>Recommendation Systems</li>"
                    "<li>Time Series and Anomaly Detection</li>"
                    "<li>Data Pipeline Development</li>"
                    "</ul>", unsafe_allow_html=True)
    with col2:
        st_lottie(lottie_de, height=300, width=300)
        st.markdown("<h4 style='text-align: left; '>MLOps</h4>", unsafe_allow_html=True)
        st.markdown("<ul>"
                    "<li>Automated Model Training</li>"
                    "<li>Model Validation and Evaluation</li>"
                    "<li>Model Deployment</li>"
                    "<li>Model Monitoring and Maintenance</li>"
                    "<li>Model Versioning and Management</li>"
                    "</ul>", unsafe_allow_html=True)

    with col3:
        st_lottie(lottie_da, height=300, width=300)
        st.markdown("<h4 style='text-align: left; '>Data Product Development</h4>", unsafe_allow_html=True)
        st.markdown("<ul>"
                    "<li>Software Development and Testing</li>"
                    "<li>Software Release Management</li>"
                    "<li>Deployment and Integration</li>"
                    "<li>Monitoring and Maintenance</li>"
                    "<li> User Feedback and Iteration</li>"
                    "</ul>", unsafe_allow_html=True)

    with col4:
        st_lottie(lottie_ga, height=300, width=300)
        st.markdown("<h4 style='text-align: left; '>Generative AI</h4>", unsafe_allow_html=True)
        st.markdown("<ul>"
                    "<li>LLM based data services</li>"
                    "<li>24/7 Customer Support</li>"
                    "<li>Search Engine powered by LLMs</li>"
                    "<li>Code Generation using LLMs</li>"
                    "<li>Integrating LLMs with existing software</li>"
                    "</ul>", unsafe_allow_html=True)

# Experiences
with st.container():
    st.write("---")
    st.markdown("<h2 style='text-align: center; '> Experiences</h2>", unsafe_allow_html=True)
    st.text("")
    st.text("")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<h4 style='text-align: center; '>Data Science & Engineering</h4>", unsafe_allow_html=True)
        st.write("I have hands-on experience of complete 'Data Science Lifecycle' and developing ml application. "
                 "I have released various machine learning models used by millions of users worldwide. "
                 "I have worked with big data in terms of volume, variety, veracity and velocity. "
                 "I have been working with data lake and setting up data pipelines for data ingestion. These workflows "
                 "included data selection, data preprocessing, data transformation, data mining, interpretation and "
                 "evaluation.")

    with col2:
        st.markdown("<h4 style='text-align: center; '>Leadership</h4>", unsafe_allow_html=True)
        st.write("I provided technical leadership at multiple organizations including carve out data science vision "
                 "and roadmaps for the organizations. I have experience of building, scaling and leading data science "
                 "department one of the largest tech based  mobility company based in Europe.")

    with col3:
        st.markdown("<h4 style='text-align: center; '>Software Engineering</h4>", unsafe_allow_html=True)
        st.write("I have been hands-on as part of core engineering teams involved in implementing multiple software "
                 "products and services including designs, prototyping and roll out over production systems. I worked "
                 "extensively with OLTP systems, relational and NoSQL databases using Python, Java, SQL and C/C++")

# Client Testimonials
with st.container():
    st.write("---")
    st.markdown("<h2 style='text-align: center; '> Client Testimonials</h2>", unsafe_allow_html=True)
    st.text("")
    st.text("")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<h4 style='text-align: center; '>Tim Klama 🇩🇪</h4>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; '>Freelance Product Owner </h6>", unsafe_allow_html=True)
        st.write("Ahsan has worked with me as a senior data scientist on establishing an AI platform for "
                 "a leading telco company in Germany. He is a proactive and professional team member who "
                 "consistently delivers high-quality work. He willingly takes on tasks outside of his core "
                 "field of expertise and has been instrumental in the success of our ai platform. He conducts "
                 "himself with integrity, communicates effectively, and is always willing to assist colleagues."
                 " Ahsan is skilled at managing difficult conversations constructively and maintains a calm "
                 "demeanour in high-pressure situations. Overall, he is an outstanding performer who would be a "
                 "valuable addition to any future projects.")

    with col2:
        st.markdown("<h4 style='text-align: center; '>Steffen Maas 🇩🇪</h4>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; '>Managing Director</h6>", unsafe_allow_html=True)
        st.write("Ahsan is a highly energetic person with deep technological understanding. He is a great "
                 "sparring partner for data architecture and the big picture, but is also able to implement "
                 "hands-on and deliver tangible results in a short amount of time. During his work at Ginkgo "
                 "Analytics he successfully led a small team at one of our automotive customers. It was a pleasure "
                 "working with him and I can highly recommend him for any tech team, in management but also in "
                 "tech lead roles.")

    with col3:
        st.markdown("<h4 style='text-align: center; '>Daniel Meyer 🇩🇪</h4>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; '>Senior Data Scientist</h6>", unsafe_allow_html=True)
        st.write("I worked with Ahsan in a project in which we developed an AI platform for Inventory Image "
                 "Classification. It was a pleasure working with him together. He demonstrated great competence "
                 "in cloud infrastructure, CI/CD Pipeline, database cloud design and deployment, which helped us "
                 "greatly to automate and optimize our machine learning solutions. Ahsan is a true professional "
                 "with a passion for excellence, always eager to help and lead by example. His feedback and "
                 "suggestions are always honest and very helpful. Having Ahsan in your team will make your project "
                 "successful.")

# Contact Me
with st.container():
    st.write("---")
    st.markdown("<h2 style='text-align: center; '>Contact Me</h2>", unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
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
    with right_column:
        st.empty()


read_custom_css("style/style.css")

st.markdown("<h3 style='text-align: center; '>Ahsan</h3>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; '>Full Stack Data Scientist & Engineer</h6>", unsafe_allow_html=True)

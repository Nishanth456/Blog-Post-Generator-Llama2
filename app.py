import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

def getLLamaresponse(input_text, no_words, blog_style):
    try:
        # Load the model
        llm = CTransformers(
            model='C:/Users/aicod/Downloads/llama-2-7b-chat.ggmlv3.q6_K.bin',
            model_type='llama',
            config={'max_new_tokens': 256, 'temperature': 0.01}
        )

        # Prompt Template
        template = """
            Write a blog for {blog_style} job profile for a topic {input_text}
            within {no_words} words.
        """

        prompt = PromptTemplate(
            input_variables=["blog_style", "input_text", 'no_words'],
            template=template
        )

        # Generate response
        response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
        return response
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit app configuration
st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.title("Blog Post Creator 📝")

# User inputs
topic = st.text_input("What should the blog be about?")

col1, col2 = st.columns([6, 4])

with col1:
    length = st.number_input('Desired Length (words):', min_value=100, max_value=5000, step=100)

with col2:
    audience = st.selectbox(
        'Target Audience:',
        ['Academics', 'Data Professionals', 'General Readers'],
        index=2
    )

generate = st.button("Create Blog")

if generate:
    with st.spinner("Generating your blog post..."):
        response = getLLamaresponse(topic, length, audience)
        st.write(response)

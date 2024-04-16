import openai
import streamlit as st

# Read the API key from a file
with open("D:\AI\OPENAI\.openai_api_key.txt") as f:
    api_key = f.read().strip()

# Set up the OpenAI client
openai.api_key = api_key

# Set Streamlit page title and icon
st.title("🎖️AI Code Reviewer")

# Take the user input
prompt = st.text_area("Enter your Python code...")

# If the button is clicked, generate the responses
if st.button("Check"):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "system", "content": "As an AI Code Reviewer, I'm here to improve your code."},
            {"role": "user", "content": prompt}
        ]
    )
    # Print the response on the web page
    st.write(response.choices[0].message.content)

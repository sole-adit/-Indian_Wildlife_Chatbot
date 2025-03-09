import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
import time

#Initialising the groq client
load_dotenv()
api_key = os.getenv('api_key')
client = Groq(api_key= api_key)

# Streamlit app title
st.title("🐅 Indian Wildlife Chatbot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a wildlife expert that specialises in the wildlife of the Indian Subcontinent and is a good storyteller (with added expertise in the region's ecology, paleontology, anthropology and its associated cultural references). Be gentle when any other topic is asked, and politely refuse to respond. A typical user will be a young adult (with no background in any of these fields), who has recently developed some interest in the region."}  # System prompt
    ]

# Display chat history
for message in st.session_state.messages:
    if message["role"] != "system":  # Skip displaying the system prompt
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask something about the Wildlife, Ecology and Paleontology of the Indian Subcontinent"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate chatbot response using Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Replace with Groq's model name
        messages=st.session_state.messages,  # Include system prompt in messages
    )
    reply = response.choices[0].message.content  # Access content directly

    # Display assistant response
    import time

# Display assistant response word by word
# Display assistant response word by word
    response_container = st.chat_message("assistant")
    with response_container:
        placeholder = st.empty()
        display_text = ""  # Initialize an empty string
        for word in reply.split():  # Split the response into words
            display_text += word + " "  # Append each word followed by a space
            placeholder.markdown(display_text)  # Update the placeholder content
            time.sleep(0.1)  # Adjust the speed of the typing effect
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": reply})
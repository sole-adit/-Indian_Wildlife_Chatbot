---
title: Indian Wildlife Chatbot
emoji: 🏃
colorFrom: pink
colorTo: gray
sdk: streamlit
sdk_version: 1.42.1
app_file: app.py
pinned: false
short_description: Wildlife, ecology and paleontology (and cultural references)
---

Indian Wildlife Chatbot 🌿🐾
Overview
The Indian Wildlife Chatbot is a Streamlit-based app designed to provide an engaging and educational experience about the wildlife, ecology, and paleontology of the Indian subcontinent. The app is powered by Groq's AI model and is tailored to offer insights, fascinating stories, and cultural references, all through the lens of an expert in Indian wildlife.

Features

Interactive Chat: Users can ask questions and learn about the diverse wildlife of the Indian subcontinent.

Expert Persona: The chatbot takes on the role of a wildlife expert with a flair for storytelling, making every interaction engaging and immersive.

Dynamic Responses: The chatbot generates thoughtful and contextual answers based on user queries.

Streamlined Interface: Streamlit provides a clean and user-friendly experience.

Cultural and Ecological Insights: The app integrates anthropological and cultural references alongside ecological information for a holistic learning experience.

Tech Stack

Streamlit: For creating the interactive web app.
Groq AI: For generating intelligent and conversational responses.
Python Libraries:
dotenv: To securely manage API keys.
os: For environment variable management.

How to Use

Clone the repository to your local machine.

Create a virtual environment and install dependencies:

bash
pip install -r requirements.txt
Add your Groq API key to a .env file in the following format:

api_key=your_groq_api_key
Run the app using Streamlit:

bash
streamlit run app.py

Ask your wildlife-related questions via the chat input and let the expert guide you!

How It Works

System Prompt Initialization: The chatbot begins by initializing its persona using a system-level prompt.
Message History Maintenance: Previous conversations are preserved in the session state to maintain context.
AI-Powered Responses: Every query is processed via Groq's AI model, which generates accurate and creative responses.
Interactive Chat Interface: Users can seamlessly interact with the chatbot via Streamlit's chat components.

Future Enhancements

Based on user requirements and feedback, the app will be updated.

Acknowledgments

This project combines the cutting-edge capabilities of Groq AI, the simplicity of Streamlit, and a passion for the incredible biodiversity of the Indian subcontinent. We hope it inspires users to learn more about this extraordinary part of the world!

Enjoy your journey into the wild wonders of India! 🐅✨

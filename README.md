STREAMING APP USING STREAMLIT
This is an AI chatbot application built using Streamlit LangChain and OpenAI.
This project is a simple yet powerful AI-powered chatbot built using Streamlit and LangChain, designed to provide real-time conversational interaction through natural language processing. The chatbot can be integrated with language models like OpenAI's GPT or Google Gemini, allowing it to answer questions, hold conversations, or assist users with various tasks depending on how the underlying model is configured.
The application is built with user interactivity in mind. The Streamlit framework handles the frontend, providing a clean and responsive web interface without requiring any frontend development. The chatbot maintains a session-based history, so conversations persist while the app is running, enabling a more coherent and engaging chat experience.
The core of the chatbot is powered by LangChain, a framework designed to simplify working with large language models. It manages the prompt structure, handles message types (like HumanMessage and AIMessage), and provides flexibility in switching or extending the language model backend. The prompt logic is defined using ChatPromptTemplate, and the output is parsed using StrOutputParser, making the response formatting straightforward and customizable.
The app securely loads API keys using the python-dotenv library, keeping sensitive information out of the codebase. Users can switch between OpenAI or Gemini APIs just by modifying their environment setup.
This chatbot can serve as a base for various real-world applications, including customer support bots, educational assistants, productivity tools, or personal AI companions. It is also ideal for developers looking to experiment with or learn how to integrate LLMs into Python apps.
Features

Chat interface with AI and Human messages
Maintains session history across interactions
Easily switchable backend model (OpenAI or Gemini)
Structured prompt templates using LangChain.

🛠️ Tools & Libraries Used
Tool / Library	Purpose
Streamlit	Frontend UI and interactivity
LangChain	Language model abstraction and pipeline
OpenAI or Gemini	Language model providers for chatbot responses
python-dotenv	For loading environment variables securely

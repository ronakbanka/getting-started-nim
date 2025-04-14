import gradio as gr
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_nvidia_ai_endpoints import ChatNVIDIA

# connect to a LLM NIM running at localhost:8000, specifying a specific model
llm = ChatNVIDIA(base_url="http://llama:8000/v1", model="meta/llama-3.2-3b-instruct")

# Set up a basic LangChain runnable chain
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}")
])

chain = prompt | llm | StrOutputParser()

# Gradio interface function
def chat_with_nim(user_input):
    response = chain.invoke({"input": user_input})
    return response

# Gradio UI
iface = gr.Interface(
    fn=chat_with_nim,
    inputs=gr.Textbox(lines=4, placeholder="Ask me anything..."),
    outputs="text",
    title="Chat with NVIDIA NIM via LangChain",
    description="This app lets you talk to a NVIDIA NIM LLM using LangChain.",
)

proxy_prefix = os.environ.get("PROXY_PREFIX")
iface.launch(server_name="0.0.0.0", server_port=8080, root_path=proxy_prefix)

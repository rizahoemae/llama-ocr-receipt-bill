from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama3.2",temperature=1.0, max_tokens=100)
messages = [
    ("human", "Can you do an image processing?"),
]
llm_resp = llm.invoke(messages)
print(llm_resp.content)
from langchain_ollama.llms import OllamaLLM #type: ignore
from langchain_core.prompts import ChatPromptTemplate #type: ignore

model = OllamaLLM(model="llama3")

template = """
You are an expert in answering questions about a pizza restaurant. 
Here are some relevant reviews: {reviews}
Here is the question to answer: {question}
""" 

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------------------")
    question = input("(q to quit) Ask your question: ")
    if question == "q":
        break
    result = chain.invoke({"reviews": [], "question": question})
    print(result)
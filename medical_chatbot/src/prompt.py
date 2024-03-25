prompt_template="""
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
try to give short and clear answers to general conversation questions.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""
from medical_chatbot.src.code import retrieve_answers

def chat(query):
    input = query
    print(input)
    result = retrieve_answers({"query": input})
    yanit_metni = result.get('output_text', 'Yanıt bulunamadı.')
    print(yanit_metni)
    
if __name__ == '__main__':
    chat("Hi, How are you ?")
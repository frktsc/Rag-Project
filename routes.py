from flask import Flask, render_template, request
from medical_chatbot.src.code import retrieve_answers


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')



@app.route("/medicus")
def medicus():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        msg = request.form["msg"]
        input = msg
        print(input)
        result = retrieve_answers({"query": input})
        last_result = result.get('output_text', 'Yanıt bulunamadı.')
        print(last_result)
        return str(last_result)
        
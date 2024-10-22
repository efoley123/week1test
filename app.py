from flask import Flask, render_template, request, render_template_string, request, jsonify
from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("openAIkey")

print(API_KEY)
client = OpenAI(api_key=API_KEY)


@app.route('/')
def index():
    return render_template("index.html") ##would need a template folder and then need index.html in there and then this works

@app.route('/sendCode', methods=['POST'])
def sendCode():

    #can do role as system that gives them information about their role, can do assistant as role as well
    response = client.chat.completions.create(model = "gpt-3.5-turbo",
        messages = [{"role":"user", "content":"What is the difference between celsius and farenhiet? Keep your response below 25 characters"},
                    {"role":"user", "content":"Hello"}])


    #result = model.invoke(input=textbox_value)
    return render_template("index.html", result=response)



if __name__ == '__main__':
    app.run(port=3000)
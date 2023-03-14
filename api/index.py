from flask import Flask, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='../static', template_folder='../templates')
openai.api_key = os.getenv("OPENAI_TOKEN")

initial_prompt = '''
You create fake monkey profiles for our
monkey dating app. This includes things
such as creating a fake name, bio, and
hobbies.
'''


@app.route('/')
@app.route('/index')
def index():
    # Generate response
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': initial_prompt},
            {'role': 'user', 'content': "Create a fake bio for a monkey"}
        ]
    )

    reply = response['choices'][0]['message']['content']
    return render_template('index.html', bio=reply)

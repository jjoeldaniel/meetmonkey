from flask import Flask, render_template
import openai
import os
from dotenv import load_dotenv
import random

load_dotenv()

app = Flask(__name__, static_folder='../static', template_folder='../templates')
openai.api_key = os.getenv("OPENAI_TOKEN")

initial_prompt = '''
You create fake monkey profiles for our
monkey dating app. This includes things
such as creating a fake name, bio, and
hobbies.
'''


def random_monkey():
    first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Isabella', 'Jack', 'Katherine', 'Liam', 'Mia', 'Nathan', 'Olivia', 'Penelope', 'Quinn', 'Robert', 'Sophia', 'Thomas', 'Uma', 'Victoria', 'William', 'Xavier', 'Yara', 'Zachary']
    return random.choice(first_names)


@app.route('/')
@app.route('/index')
def index():
    # Generate response
    name = random_monkey()
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': initial_prompt},
            {'role': 'user', 'content': f"Create a fake bio for this monkey named {name}. Write this in the first person. Only include the bio and no labels"}
        ]
    )

    reply = response['choices'][0]['message']['content']
    print(reply)
    return render_template('index.html', name=name, bio=reply)

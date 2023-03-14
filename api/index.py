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


def get_likes_and_dislikes():
    # Define a list of likes and dislikes
    likes_and_dislikes = [
        "Reading", "Cooking", "Traveling", "Watching movies", "Playing sports",
        "Listening to music", "Gardening", "Eating spicy food", "Hiking",
        "Shopping", "Watching TV", "Playing video games", "Swimming",
        "Learning new languages", "Taking naps", "Camping", "Painting",
        "Dancing", "Meditating", "Collecting things", "Binge-watching shows",
        "Playing musical instruments", "Solving puzzles", "Going to concerts",
        "Trying new foods", "Playing board games", "Fishing", "Running",
        "Yoga", "Singing", "Playing with pets", "Going to the beach",
        "Photography", "Playing chess", "Skiing", "Snowboarding",
        "Working out", "Reading comics", "Going to museums",
        "Playing poker", "Watching sports", "Making crafts",
        "Watching stand-up comedy", "Playing basketball", "Playing tennis",
        "Going to the theater", "Playing card games", "Playing golf",
        "Watching documentaries", "Attending live events"
    ]

    # Shuffle the list of likes and dislikes
    random.shuffle(likes_and_dislikes)

    # Select 3 random items from the list
    likes = random.sample(likes_and_dislikes, 3)
    return likes


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
            {'role': 'user', 'content': f"Create a fake bio for this monkey named {name}. Write this in the first person. Only include the bio and no labels"},
        ]
    )

    reply = response['choices'][0]['message']['content']
    return render_template('index.html', name=name, bio=reply, likes=get_likes_and_dislikes())

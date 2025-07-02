# app/script_generator.py

import openai
import os

openai.api_key = os.getenv(\"OPENAI_API_KEY\")

def generate_podcast_script(topic=\"Benefits of Remote Work\"):
    prompt = f\"Create a 5-minute podcast script about: {topic}\\nMake it engaging and informative.\"
    response = openai.ChatCompletion.create(
        model=\"gpt-4o\",
        messages=[{\"role\": \"user\", \"content\": prompt}]
    )
    script = response.choices[0].message.content
    return script

if __name__ == \"__main__\":
    script = generate_podcast_script(\"How to Start a Successful Side Hustle\")
    print(\"Generated Script:\\n\", script)

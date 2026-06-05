from openai import OpenAI

# 🔑 Replace with your API key
client = OpenAI(api_key="YOUR_API_KEY_HERE")


def get_explanation(topic):
    prompt = f"Explain {topic} in simple terms with examples"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def get_notes(topic):
    prompt = f"Summarize {topic} into short bullet points"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def get_quiz(topic):
    prompt = f"Generate 5 MCQ questions with answers on {topic}"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def ask_question(question):
    prompt = f"Answer clearly and simply: {question}"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
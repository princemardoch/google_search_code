from openai import OpenAI

def resumegpt(page):
    client = OpenAI(
        api_key="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",
        )
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Tu sert a resumé tout ce qu'ont te donne en moins de 100mots. Traduit et Parle uniquement en français"},
        {"role": "user", "content": page}
    ]
    )

    message_content = completion.choices[0].message.content
    print(message_content)
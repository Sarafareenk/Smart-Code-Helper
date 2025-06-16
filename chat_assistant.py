# chat_assistant.py

from openai import OpenAI
import os
from dotenv import load_dotenv

# 🔐 Load API key securely
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🎭 Tone prompt templates
tone_prompts = {
    "friendly": "You are a friendly assistant who explains things casually and simply.",
    "formal": "You are a professional assistant who explains things in a formal and technical way.",
    "motivational": "You are a motivating assistant who encourages users warmly while helping.",
    "debugger": "You are a smart code debugging assistant. Explain code errors clearly and help fix them."
}

def ask_gpt(prompt, tone):
    system_prompt = tone_prompts.get(tone, tone_prompts["friendly"])
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message.content

def main():
    print("🧠 Welcome to Smart Code Helper – AI Chat Companion (v2)")
    print("Available tones: friendly, formal, motivational, debugger")
    
    tone = input("Choose a tone: ").strip().lower()
    if tone not in tone_prompts:
        print("❌ Invalid tone. Choose from: friendly, formal, motivational, debugger")
        return

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Happy coding.")
            break

        reply = ask_gpt(user_input, tone)
        print("\nAI:", reply)

if __name__ == "__main__":
    main()


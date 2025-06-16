# chat_assistant.py
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 🎭 Define tone prompt templates
tone_prompts = {
    "friendly": "You are a friendly assistant who explains things clearly and casually.",
    "formal": "You are a professional assistant who answers formally with technical clarity.",
    "motivational": "You are an encouraging coach who explains the answer with positivity and warmth.",
    "debugger": "You are a helpful debugging assistant who fixes code and explains errors clearly."
}

def ask_gpt(prompt, tone):
    full_prompt = f"{tone_prompts[tone]}\nUser asked: {prompt}\nAssistant:"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": tone_prompts[tone]},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

def main():
    print("🧠 Welcome to Smart Code Helper – AI Chat Companion")
    print("Available tones: friendly, formal, motivational, debugger")
    
    tone = input("Choose your assistant tone: ").strip().lower()
    if tone not in tone_prompts:
        print("Invalid tone selected.")
        return

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting. Happy coding!")
            break

        reply = ask_gpt(user_input, tone)
        print("\nAI:", reply)

if __name__ == "__main__":
    main()

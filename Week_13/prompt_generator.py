import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genrativeai
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genrativeai.configure(api_key=GOOGLE_API_KEY)

def generate_itinerary(destination, duration, interests="general"):
    model = genrativeai.GenerativeModel('models/gemini-pro-latest')
 
    prompt = (f"Create a detailed travel itinerary for a trip to {destination} "
              f"for {duration} days. The traveler has {interests} interests. "
              "Please include daily activities, suggested meals, and transportation tips. "
              "Structure the output clearly with day-by-day breakdowns.")

    try:   
        response = model.generate_content(prompt)

        
        if response.candidates:            
            return response.candidates[0].content.parts[0].text
        else:            
            print("Warning: AI generated no candidates for the given prompt.")
            return "No itinerary generated. The AI might have filtered the content or had an issue."

    except Exception as e:
        return f"An error occurred while generating itinerary: {e}"


def main():
    destination = input("Enter your destination (e.g., Paris): ")
    duration = input("Enter duration in days (e.g., 5): ")
    interests = input("Enter your interests (e.g., history, food, art, adventure - optional): ")

    itinerary = generate_itinerary(destination, duration, interests)
    print("\nGenerated Itinerary:\n")
    print(itinerary)

if __name__ == "__main__":
    main()


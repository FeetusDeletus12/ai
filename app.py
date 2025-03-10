import google.generativeai as genai

# Configure the Gemini API with your API key
genai.configure(api_key="AIzaSyBi4BaxHfhc5oxgcPOJxMDSjt2A3wBKNxs")

# Load the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Start the chat loop
print("🤖 Gemini AI Chatbot (type 'exit' to quit)\n")

while True:
    # Get user input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("Goodbye! 👋")
        break

    try:
        # Generate response from the model
        response = model.generate_content(user_input)
        print("Gemini:", response.text)
    except Exception as e:
        print("Error:", e)

import streamlit as st
import speech_recognition as sr
from textblob import TextBlob
import openai
import os
import requests
from PIL import Image
import base64

# Set your OpenAI API key and Imagga API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
imagga_api_key = os.getenv("IMAGGA_API_KEY")
imagga_api_secret = os.getenv("IMAGGA_API_SECRET")

# Define common themes and related tags
common_themes = {
    "person": ["people", "human", "man", "woman"],
    "nature": ["sky", "tree", "flower", "landscape"],
    "technology": ["computer", "phone", "screen", "device"],
    "animals": ["animal", "dog", "cat", "wildlife"]
    # Add more themes and related tags as needed
}

# Function to correct the spelling of input text
def correct_spelling(input_text):
    if not input_text:
        return input_text

    blob = TextBlob(input_text)
    corrected_text = blob.correct()
    return str(corrected_text)

# Function to chat with GPT using OpenAI API
def chat_with_gpt(input_topic):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=input_topic,
            max_tokens=100
        )
        answer = response['choices'][0]['text'].strip()
        return answer
    except openai.OpenAIError as e:
        st.write(f"An error occurred: {e}")
        return "An error occurred."

# Function for image recognition using Imagga API
def recognize_image(image_content, confidence_threshold=50):
    url = "https://api.imagga.com/v2/tags"
    headers = {
        "Authorization": f"Basic {base64.b64encode(f'{imagga_api_key}:{imagga_api_secret}'.encode()).decode()}",
    }
    files = {"image": ("image.jpg", image_content)}
    try:
        response = requests.post(url, headers=headers, files=files)
        response.raise_for_status()
        result = response.json()
        tags = result.get("result", {}).get("tags", [])

        # Extract tags with confidence above the threshold
        tags_above_threshold = [tag for tag in tags if tag.get("confidence", 0) >= confidence_threshold]

        # Construct a sentence based on relationships between tags
        sentence = generate_intelligent_sentence(tags_above_threshold)

        return sentence
    except requests.exceptions.HTTPError as errh:
        st.write(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        st.write(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        st.write(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        st.write(f"Request Error: {err}")

    return ""

def generate_intelligent_sentence(tags):
    # Identify common themes in the tags
    detected_themes = set()
    for theme, related_tags in common_themes.items():
        if any(tag["tag"]["en"] in related_tags for tag in tags):
            detected_themes.add(theme)

    # Determine the environment or context from additional tags
    environment_tags = ["indoor", "outdoor", "city", "landscape"]
    detected_environment = {tag["tag"]["en"] for tag in tags if tag["tag"]["en"] in environment_tags}

    # Identify specific objects in the image
    detected_objects = [tag["tag"]["en"] for tag in tags if tag["tag"]["en"] not in detected_themes.union(detected_environment)]

    # Initialize an empty sentence
    sentence = ""

    # Include detected themes in the sentence
    if detected_themes:
        sentence += f"The image features {', '.join(detected_themes)}."

    # Include detected environment in the sentence
    if detected_environment:
        sentence += f" It appears to be in {', '.join(detected_environment)}."

    # Include detected objects in the sentence
    if detected_objects:
        object_description = ", ".join(detected_objects)
        sentence += f" It includes {object_description}."

    # If no themes, environment, or objects detected, provide a default sentence
    if not sentence:
        sentence = "The image contains various objects."

    return sentence



def main():

    st.title("Ask your Chatbot")
    st.markdown('<style>h1{color: #000000;}</style>', unsafe_allow_html=True)

    # Sidebar with black background containing chat history and previous chats
    st.sidebar.title("Chat History")
    chat_history = st.sidebar.empty()
    previous_chats = []

    # Text input box for the user to type or use speech recognition
    input_topic = st.text_input("Your Message:")
    voice_button = st.button("🎤 Voice Recognize")

    if voice_button:
        # Use speech recognition to get user input
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Start asking your question...")
            audio = recognizer.listen(source)

        try:
            st.write("Please wait...")
            input_topic = recognizer.recognize_google(audio)
            st.text_area("Your Message:", value=input_topic, key='input_text')
        except sr.UnknownValueError:
            st.write("Speech Recognition could not understand audio.")
        except sr.RequestError:
            st.write("Could not request results from Speech Recognition service.")

    # Image recognition
    image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    if image is not None:
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Classifying...")

        # Perform image recognition using Imagga API
        image_content = image.read()
        sentence = recognize_image(image_content)

        # Display image recognition results
        st.subheader("Image Recognition Results:")
        st.write(sentence)

    if input_topic:
        # Correct the input sentence for spelling mistakes
        corrected_topic = correct_spelling(input_topic)

        # Chat with GPT and get the answer
        answer = chat_with_gpt(corrected_topic)

        # Save chat history
        previous_chats.append((corrected_topic, answer))

        # Display previous chats in the sidebar
        chat_history.markdown("\n\n".join([f"**You:** {chat[0]}\n\n**Bot:** {chat[1]}" for chat in previous_chats]))

        # Display the answer
        st.subheader("Answer:")
        st.write(answer)

if __name__ == "__main__":
    main()

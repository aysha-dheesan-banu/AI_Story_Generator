import streamlit as st
from transformers import pipeline, set_seed
import random
from dotenv import load_dotenv
import os

load_dotenv()

# Page config
st.set_page_config(page_title="🎮 AI Dungeon", layout="wide")

# Load GPT-2
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()
set_seed(random.randint(1, 9999))

# Initialize story state
if "full_story" not in st.session_state:
    st.session_state.full_story = ""

# Theme
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Trebuchet MS', sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: #f1f1f1;
        }

        .story-card {
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid #00bcd4;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            backdrop-filter: blur(8px);
        }

        .stButton button {
            background-color: #00bcd4 !important;
            color: white !important;
            border-radius: 12px;
            padding: 0.6em 1.2em;
            font-size: 1.1em;
            font-weight: bold;
        }

        .stTextArea textarea {
            background-color: #0d1b2a !important;
            color: white !important;
            border: 1px solid #00bcd4 !important;
        }

        h1, h2, h4 {
            text-shadow: 2px 2px 5px black;
        }

        .glow {
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 0 0 10px #00bcd4; }
            to { text-shadow: 0 0 20px #00ffff; }
        }

    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='glow'>🎮 AI Dungeon Story Generator</h1>", unsafe_allow_html=True)
st.caption("Craft magical tales with a tap of AI power.")

# Sidebar
st.sidebar.header("🛠️ Character Builder")
char_name = st.sidebar.text_input("Name", "Tog")
char_traits = st.sidebar.text_input("Traits (comma-separated)", "Brave, Wise")
char_location = st.sidebar.text_input("Location", "Mystic Vale")

# Genre
genres = {
    "Fantasy": "🧝‍♂️ Once upon a time in a mystical land, ",
    "Sci-Fi": "🚀 In the year 3022, the stars whispered, ",
    "Mystery": "🕵️‍♂️ On a rainy night, the shadows moved when ",
    "Horror": "👻 The lantern flickered as the ghost appeared ",
    "Adventure": "🌋 Through ancient ruins, they ventured when ",
    "Romance": "💖 Beneath the cherry blossom sky, ",
    "Comedy": "🎭 With a pie in the face and no clue, "
}

col1, col2 = st.columns([1, 1])
with col1:
    genre = st.selectbox("🎭 Choose Genre", list(genres.keys()))
with col2:
    num_stories = st.slider("🔁 Story Variants", 1, 5, 2)

# Prompt Builder
def build_prompt():
    return f"In {char_location}, {char_name}, a {' and '.join(t.strip() for t in char_traits.split(','))} soul, begins a quest..."

user_input = st.text_area("✍️ Prompt:", build_prompt())

# Generate Stories
if st.button("✨ Generate Story"):
    if not user_input.strip():
        st.warning("Please enter a story prompt.")
    else:
        base_prompt = genres[genre] + user_input.strip()
        with st.spinner("Summoning the AI Bard..."):
            responses = generator(base_prompt, max_length=250, num_return_sequences=num_stories, do_sample=True, temperature=0.9)
            all_stories = []
            for i, r in enumerate(responses):
                story = r["generated_text"]
                st.markdown(f'<div class="story-card"><h4>📜 Story {i+1}</h4><p>{story}</p></div>', unsafe_allow_html=True)
                all_stories.append(story)
            st.session_state.full_story = "\n\n---\n\n".join(all_stories)

# Continue Story
if st.button("🔁 Continue Story"):
    with st.spinner("Expanding the tale..."):
        try:
            cont = generator(st.session_state.full_story, max_length=200, num_return_sequences=1, do_sample=True, temperature=0.9)[0]["generated_text"]
            st.session_state.full_story += "\n\n" + cont
            st.markdown(f'<div class="story-card"><h4>📜 Continued</h4><p>{cont}</p></div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {e}")

# Download
if st.session_state.full_story:
    st.download_button("💾 Save Story", st.session_state.full_story, file_name="ai_dungeon.txt")

# Reset
if st.button("🧹 Clear Story"):
    st.session_state.full_story = ""
    st.success("Story cleared.")

# Footer
st.markdown("<hr><center><small>Made with ❤️ and GPT-2 | Powered by Streamlit</small></center>", unsafe_allow_html=True)


🧙 AI Dungeon Story Generator
Introduction
The AI Dungeon Story Generator is an interactive web application that leverages advanced Natural Language Processing (NLP) techniques to create engaging, genre-specific narratives. Inspired by classic text-based adventure games, this project allows users to input prompts and receive multiple creative story continuations powered by generative models.

Features
Genre Selection: Choose from various genres like Fantasy, Sci-Fi, Horror, and more to set the tone of your story.

Character Builder: Customize your character's name, traits, and location to personalize your adventure.

Multiple Story Variations: Generate multiple story continuations to explore different narrative paths.

Story Continuation: Extend your stories with additional content to build a comprehensive narrative.

Download Option: Save your generated stories as text files for future reference or sharing.

Theme Switching: Toggle between Dark and Light themes for a comfortable reading experience.

Tools Used
Tool/Library	Purpose
Python	Core programming language
Streamlit	Web application framework
Hugging Face Transformers	Provides GPT-2 model for text generation
dotenv	Manages environment variables securely

Installation
Clone the Repository:
git clone https://github.com/yourusername/ai-dungeon-story-generator.git
cd ai-dungeon-story-generator

Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

Install Dependencies:
pip install -r requirements.txt
Set Up Environment Variables:
Create a .env file in the project root directory.

Add your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key

Run the Application:
streamlit run your_script_name.py

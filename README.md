# simple-chatbot
simple chatbot using langchain and integration with fastapi and streamlit

This project is a **simple chatbot application** built using **FastAPI** for the backend and **Streamlit** for the frontend. It demonstrates how to integrate a frontend interface with a backend service to handle conversations while maintaining session-based chat history. The chatbot uses a simple rule-based logic implemented in `graph.py`.

## Features

- **Frontend:** Streamlit-based chat interface.
- **Backend:** FastAPI handles chat requests.
- **Session Management:** Maintains session context for multiple messages.
- **Simple Chat Logic:** Implemented in `graph.py`, responds to:
  - Greetings like `hello`.
  - Phrases like `how are you`.
  - Farewells like `bye`.
  - Echoes other messages for general inputs.
- **Lightweight & Easy to Run:** No heavy AI model required, works locally.

## Project Structure

├── app.py # Streamlit frontend
├── backend.py # FastAPI backend
├── graph.py # Chatbot logic
├── requirements.txt # Python dependencies
├── .gitignore # Files to ignore in Git
├── README.md # Project documentation
└── .env (optional) # Environment variables (if needed)


### Notes on project structure:

- `graph.py`: Contains the chatbot logic. You can add more rules or responses here.
- `backend.py`: FastAPI app that exposes `/chat` endpoint.
- `app.py`: Streamlit frontend that interacts with the backend.
- `.env`: Optional file for environment variables (not required for this simple version).
- `__pycache__/`, `.venv/` and other temporary files are **ignored** in `.gitignore`.

## .gitignore

Typical `.gitignore` for Python projects:

Python
pycache/
*.py[cod]
*.pyo
*.pyd

Virtual Environment
.venv/
venv/

IDEs
.vscode/
.idea/

Environment variables
.env

Streamlit cache
.streamlit/

## Environment Variables (.env)

This project can optionally use a `.env` file to store environment variables, such as:

BOT_NAME=SimpleBot
DEBUG=True

pgsql
Copy code

- Keep your configuration separate from the code.
- Useful for future features like API keys or custom settings.
- Make sure to add `.env` to `.gitignore` to avoid committing sensitive data.
  
## Installation

1. **Clone the repository**

git clone https://github.com/yourusername/simple-chatbot.git
cd simple-chatbot

2. **Create and activate a virtual environment**
   
# Windows
python -m venv venv
venv\Scripts\activate

3. **Install dependencies**

pip install -r requirements.txt

> If `requirements.txt` is not available, install manually:

pip install fastapi uvicorn streamlit requests

## Running the Project

### 1. Start the Backend (FastAPI)

uvicorn backend:app --reload

* This will start the backend server on `http://127.0.0.1:8000`.
* The backend exposes a `/chat` endpoint to handle chat messages.

### 2. Start the Frontend (Streamlit)

streamlit run app.py

* Streamlit will open a local URL (usually `http://localhost:8501`) where you can interact with the chatbot.
* Enter your messages in the input box and click **Send** to get responses.

## Example Conversation

| You         | Bot                             |
| ----------- | ------------------------------- |
| hello       | Hi there! How can I help you?   |
| how are you | I'm a bot, but I'm doing great! |
| what's up?  | You said: what's up?            |
| bye         | Goodbye! Have a nice day.       |

## Integration

1. **Frontend → Backend:** Streamlit sends POST requests with user input to the FastAPI `/chat` endpoint.
2. **Backend → Chat Logic:** FastAPI calls `run_agent()` from `graph.py` to generate a response.
3. **Backend → Frontend:** The response is returned to Streamlit and displayed in the chat interface.
4. **Session Tracking:** Each user session is tracked using a unique session ID to maintain conversation history.

## Notes

* The chatbot is **rule-based**, so it provides predefined responses based on user input.
* Easy to extend and customize in `graph.py`.
* FastAPI ensures the backend can handle multiple users simultaneously.
* Streamlit provides a simple and interactive UI.

## Requirements

* Python 3.10+
* Libraries:

  * `fastapi`
  * `uvicorn`
  * `streamlit`
  * `requests`

## License

This project is open-source and available under the **MIT License**.

This README now includes:  

- Project description & features  
- Full folder structure  
- `.gitignore` info for `.env` and caches  
- Installation & running instructions  
- Integration flow explanation  


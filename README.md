# 🕰️ Interactive Fiction Engine: Midnight Clocktower

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)

A full-stack, AI-powered interactive fiction engine featuring persistent state tracking, cloud database integration, and a dynamic AI narrator. 

**🎮 Play the live game here:** [Midnight Clocktower](https://midnight-clocktower-binuumat.up.railway.app/)

---

## ✨ Features

* **Dynamic AI Narrator:** Integrated with the `google-genai` SDK to process free-text player input and generate real-time, context-aware responses from the game's narrator without breaking the story flow.
* **Cloud State Management:** Connects to **MongoDB Atlas** to pull story nodes dynamically, meaning the game's narrative can be updated in the cloud without altering the local codebase.
* **Inventory & Puzzle Mechanics:** Features a robust state manager that tracks player inventory and utilizes conditional logic to lock/unlock specific story branches based on acquired items.
* **Interactive CLI Tool:** Includes a custom Python utility (`utils/story_builder.py`) to easily write, format, and push new JSON narrative nodes directly to the database.
* **Web UI:** A fully responsive, Gothic-themed web interface built with **Flask**, HTML, CSS, and JavaScript.

## 🛠️ Architecture & Tech Stack

* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Backend:** Python, Flask, Gunicorn (WSGI)
* **Database:** MongoDB Atlas (via `pymongo`)
* **AI Integration:** Google Gemini 2.5 Flash (`google-genai` modern SDK)
* **Hosting/Deployment:** Railway

---

## 🚀 Local Development Setup

To run this engine locally, you will need Python 3.8+ and your own API keys for MongoDB and Google Gemini.

**1. Clone the repository**
```bash
git clone [https://github.com/umandathathsarani/interactive-fiction-engine.git](https://github.com/umandathathsarani/interactive-fiction-engine.git)
cd interactive-fiction-engine
```

**2. Create a virtual environment and install dependencies**
```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

**3. Configure Environment Variables**
Create a `.env` file in the root directory and add your secret keys:
```env
MONGODB_URI="your_mongodb_atlas_connection_string"
GEMINI_API_KEY="your_google_gemini_api_key"
```

**4. Run the Local Server**
```bash
python app.py
```
After running the command, check your terminal output for the local development server address and open that link in your browser to play the game.

---

## 📜 License

This project is proprietary. All rights reserved by Mummullage Binuri Umanda Thathsarani. See `LICENSE.md` for details.
﻿# 🧠 JARVIS AI Assistant

> Your own voice-activated personal assistant powered by OpenAI and Python.

JARVIS is a smart, conversational AI built to assist you with tasks, answer questions, and eventually control devices or systems — just like Iron Man's virtual assistant, but running on your machine.

---

## 🚀 Features

- 🎙️ **Wake Word Activation** — Listens for "Hey Jarvis" to activate.
- 🤖 **Voice-to-Text** — Uses `SpeechRecognition` to capture what you say.
- 💬 **OpenAI-Powered Brain** — Integrates with GPT to generate dynamic, human-like responses.
- 🔄 **Command Parser** — Understands and executes contextual commands.
- 🧩 **Modular Design** — Easy to scale with new modules like automation, system control, or APIs.

---

## 🧰 Tech Stack

| Component       | Tech Used             |
|----------------|------------------------|
| Voice Input     | `speech_recognition`, `pyaudio` |
| AI Brain        | `openai` GPT (via API) |
| Text-to-Speech  | `pyttsx3`              |
| Wake Word       | `vosk` (or placeholder logic)  |
| Orchestration   | Pure Python (modular scripts)  |

---

## 📂 Project Structure

```bash
JARVIS_AI_Assistant/
├── core/
│   ├── wake_word.py         # Wake word detection logic
│   ├── command_parser.py    # Extracts & executes commands
│   └── jarvis_brain.py      # Main AI logic with OpenAI
├── config.py                # Environment variable loading
├── main.py                  # Launcher file
├── requirements.txt
├── .env                     # 🔐 Your secret OpenAI API key
└── README.md

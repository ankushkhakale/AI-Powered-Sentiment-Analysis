# AI-Powered Sentiment Analysis

A lightweight sentiment analysis application powered by DeepSeek AI, offering both a web API and an intuitive web interface for real-time sentiment classification.

---

## 🎯 Overview

This project provides two interfaces to analyze text sentiment using the DeepSeek-R1 AI model:
- **REST API** (FastAPI) - for programmatic access
- **Web UI** (Gradio) - for interactive analysis

The application runs locally with Ollama, requiring no external API keys.

```
┌─────────────────────────────────────────────────┐
│         User Input (Text)                       │
└────────────────┬────────────────────────────────┘
                 │
        ┌────────┴────────┐
        │                 │
    ┌───▼────┐      ┌────▼────┐
    │ Gradio │      │ FastAPI │
    │  UI    │      │   API   │
    └───┬────┘      └────┬────┘
        │                │
        └────────┬───────┘
                 │
        ┌────────▼────────┐
        │  Ollama Local   │
        │  (DeepSeek-R1)  │
        └────────┬────────┘
                 │
        ┌────────▼────────────────────┐
        │ Sentiment Classification    │
        │ + Contributing Words        │
        └─────────────────────────────┘
```

---

## 📋 Features

| Feature | Details |
|---------|---------|
| **AI Model** | DeepSeek-R1 (local inference via Ollama) |
| **Sentiment Classes** | Positive, Negative, Neutral |
| **Analysis Depth** | Highlights contributing words/phrases |
| **Interfaces** | Web UI (Gradio) + REST API (FastAPI) |
| **Language Support** | Multi-language capable |
| **Setup** | Simple, no external API keys required |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai) installed with deepseek-r1 model
- Windows/Mac/Linux

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd AI-Powered-Sentiment-Analysis

# Install dependencies
pip install fastapi uvicorn requests gradio

# Verify Ollama is running
ollama serve  # Run in separate terminal
```

### Running the Application

**Option 1: Gradio Web Interface** (Recommended for beginners)
```bash
python sentiment.py
# Opens at http://localhost:7860
```

**Option 2: FastAPI REST Endpoint**
```bash
uvicorn app:app --reload
# API available at http://localhost:8000
# Docs at http://localhost:8000/docs
```

---

## 📁 Project Structure

```
AI-Powered-Sentiment-Analysis/
├── app.py              # FastAPI REST endpoint
├── sentiment.py        # Gradio web interface + logic
├── README.md           # This file
├── LICENSE             # Project license
└── __pycache__/        # Python cache
```

---

## 💻 Code Architecture

### sentiment.py (Main Application)
- **Gradio Interface**: User-friendly text input form
- **DeepSeek Integration**: Local AI analysis via Ollama
- **Analysis Function**: Accepts text, returns sentiment + keywords

### app.py (REST API)
- **FastAPI Endpoint**: `/analyze_sentiment/` (POST)
- **JSON Interface**: Send text, receive sentiment classification
- **Scalable**: Supports batch processing

---

## 🛠️ How It Works

1. **User Input** → Text is submitted via Gradio or API
2. **Prompt Engineering** → Text formatted for DeepSeek analysis
3. **Local Inference** → Ollama processes via deepseek-r1 model
4. **Output Processing** → Sentiment classification + key phrase extraction
5. **Response** → Results returned to user (UI or JSON)

---

## 📦 Dependencies

```
fastapi          - REST API framework
uvicorn          - ASGI server
gradio           - Web UI framework
requests         - HTTP client
ollama           - Local AI inference
```

---

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Gradio Guide](https://gradio.app/)
- [Ollama Models](https://ollama.ai)
- [DeepSeek](https://www.deepseek.com/)

---

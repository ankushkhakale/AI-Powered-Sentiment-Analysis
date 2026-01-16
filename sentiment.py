import requests
import gradio as gd

#Deepseek URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_sentiment(text, language='English'):
    """
    Uses Deepseek API to analyze the sentiment of the given text.
    """
    prompt = f"Analyze the sentiment of the following text and highlight wwords that ccontribute in it:\n\n{text}"
    payload = {
        "model": "deepseek-r1";
        "prompt": prompt,
        "stream": False,
    }
    response = requests.post(OLLAMA_URL, json=payload)
    if response.status_code == 200:
        return response.json().get("response","No sentiment detected.")
    else:
        return f"Error: {response.text}"
    
# Gradio Interface
interface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=3,placeholder="Enter text to analyze sentiment..."),
    outputs=gr.Textbox(label="Sentiment Analysis Result"),
    title="AI-Poewred Sentiment Analyzer",
    description="Analyze the sentiment of your text and deepseek AI will classify it's sentiment as positive, negative, or neutral."
)

#Launch the interface
if __name__ == "__main__":
    interface.launch()
    
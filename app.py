import gradio as gr
from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization")

def summarize_text(input_text):
    summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Create a Gradio interface
interface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=5, placeholder="Enter text to summarize"),
    outputs="text",
    title="Text Summarizer"
)

if __name__ == "__main__":
    interface.launch(share=True)

from transformers import pipeline

# Explicitly specify the model and tokenizer for summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn")

def summarize_text(text):
    try:
        # Perform summarization with max_length and min_length settings
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error during summarization: {str(e)}"

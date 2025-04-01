from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object for the input text
    blob = TextBlob(text)
    
    # Analyze the sentiment polarity: ranges from -1 (negative) to 1 (positive)
    polarity = blob.sentiment.polarity
    
    # Handle extreme cases (e.g., if polarity is exactly 0)
    if polarity > 0:
        positive = polarity
        negative = 0
    elif polarity < 0:
        positive = 0
        negative = -polarity
    else:
        positive = 0
        negative = 0
    
    # Neutral sentiment is based on the absolute value of polarity
    neutral = 1 - abs(polarity)

    # Return sentiment scores with proper labeling
    return {
        "positive": positive,  # Positive sentiment
        "negative": negative,  # Negative sentiment
        "neutral": neutral     # Neutral sentiment
    }


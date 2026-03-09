from textblob import TextBlob


def analyze_sentiment(reviews):
    if not reviews:
        return {"positive": 0, "negative": 0, "neutral": 0}

    counts = {"positive": 0, "negative": 0, "neutral": 0}
    for r in reviews:
        score = TextBlob(r).sentiment.polarity
        if score > 0.1:
            counts["positive"] += 1
        elif score < -0.1:
            counts["negative"] += 1
        else:
            counts["neutral"] += 1


    total = len(reviews)
    return {k: round((v / total) * 100, 2) for k, v in counts.items()}



if __name__ == "__main__":
    test_reviews = [
        "This product is amazing and works perfectly!",
        "Terrible experience, it broke on the first day.",
        "It is okay, nothing special but does the job."
    ]

    print("--- Starting Sentiment Analysis Test ---")
    report = analyze_sentiment(test_reviews)
    print(f"Analysis Results: {report}")
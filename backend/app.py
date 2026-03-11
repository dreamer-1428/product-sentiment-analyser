from flask import Flask, request, jsonify
from flask_cors import CORS
from classifier import analyze_sentiment  # Uses your existing logic

# import your_scraper_function from scraper.py

app = Flask(__name__)
CORS(app)  # This allows your React app to talk to this Python script


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url')

    # 1. Trigger Scraper: Call your Selenium script here using the 'url'
    # sampled_reviews = your_scraper_function(url)

    # Placeholder data for testing until your scraper is linked:
    sampled_reviews = [
        "This product is amazing!",
        "Terrible quality, broke immediately.",
        "It's okay for the price."
    ]

    # 2. Analyze Sentiment: Using your classifier.py logic [cite: 5, 12]
    results = analyze_sentiment(sampled_reviews)

    # 3. Format Response for React
    response = {
        "product_name": "Scraped Product",
        "total_reviews": len(sampled_reviews),
        "sentiment": {
            "positive": results.get('positive', 0),
            "negative": results.get('negative', 0),
            "neutral": results.get('neutral', 0)
        },
        "reviews": [{"text": r, "sentiment": "positive" if "amazing" in r else "negative"} for r in sampled_reviews]
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
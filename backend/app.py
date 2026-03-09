from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import get_product_reviews
from classifier import analyze_sentiment  # Import your verified logic

app = Flask(__name__)
CORS(app)


@app.route('/analyze', methods=['POST'])
def analyze():
    product_name = request.json.get('name')
    reviews = get_product_reviews(product_name)
    sentiment_data = analyze_sentiment(reviews)

    return jsonify({
        "status": "success",
        "product": product_name,
        "sentiment": sentiment_data,
        "total_reviews": len(reviews),
        "reviews": reviews  # Add this line to send the text to React
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
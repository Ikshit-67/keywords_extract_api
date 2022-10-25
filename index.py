from flask import Flask, jsonify
import yake


app = Flask(__name__)


@app.route("/")
def start():
    return "hello"


@app.route("/keywords/<string:text>")
def extract_keywords(text):
    kw_model = yake.KeywordExtractor()
    keywords = kw_model.extract_keywords(text)
    result = {
        "input_text": text,
        "keywords": keywords
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

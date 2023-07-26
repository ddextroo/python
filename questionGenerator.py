from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

def generate_review_material_with_gpt3(topic):
    prompt = f"Generate a reviewer material and cheat sheet for the topic: {topic}"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=4000,
        temperature=0.8,
        n=1,
        stop=None,
    )

    review_material = response["choices"][0]["text"].strip()
    return review_material

@app.route('/generate_review', methods=['POST'])
def generate_review():
    data = request.get_json()
    if 'topic' in data:
        user_topic = data['topic']
        review_material = generate_review_material_with_gpt3(user_topic)
        return jsonify({"review_material": review_material})
    else:
        return jsonify({"error": "Topic not provided."}), 400

if __name__ == "__main__":
    app.run(debug=True)

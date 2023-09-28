from flask import Flask, request, jsonify
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import openai
import base64
import io

app = Flask(__name__)
#ee
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

@app.route('/generate_reviewer', methods=['POST'])
def generate_review():
    data = request.get_json()
    if 'topic' in data:
        user_topic = data['topic']
        review_material = generate_review_material_with_gpt3(user_topic)
        return jsonify({"review_material": review_material})
    else:
        return jsonify({"error": "Topic not provided."}), 400

@app.route('/formula_converter', methods=['POST'])
def generate_plot():
    data = request.json
    math_expression = data.get('math_expression')

    custom_font_path = 'Poppins-Regular.ttf'

    custom_font = FontProperties(fname=custom_font_path)

    # Create a plot
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.text(0, 0.5, math_expression, fontsize=16, ha='left', va='center', fontproperties=custom_font)

    # Set axis limits and labels (optional)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()

    # Save the plot to a bytes buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    plt.close()

    # Convert the image to a Base64 string
    buffer.seek(0)
    base64_string = base64.b64encode(buffer.read()).decode('utf-8')

    return jsonify({'formula': base64_string})

if __name__ == "__main__":
    app.run(debug=True)

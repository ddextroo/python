import base64
from flask import Flask, request, jsonify
from matplotlib import mathtext
from io import BytesIO

app = Flask(__name__)

def generate_image_from_math_expression(math_expression):
    output_file = BytesIO()
    mathtext.math_to_image(math_expression, output_file)
    encoded_image = base64.b64encode(output_file.getvalue()).decode('utf-8')
    output_file.close()
    return encoded_image

@app.route('/convert_math_to_image', methods=['POST'])
def convert_math_to_image():
    try:
        data = request.get_json()

        # Extract the math expression from the JSON data
        math_expression = data['math_expression']

        # Split the multiline expression into individual expressions
        expressions = math_expression.split('\n')

        # Generate images for each expression
        images_dict = {}
        for idx, expr in enumerate(expressions, start=1):
            image_key = f"formula{idx}"
            images_dict[image_key] = generate_image_from_math_expression(expr)

        # Return the dictionary of base64-encoded images as JSON
        return jsonify(images_dict)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)






def convert_math_to_image():
    try:
        data = request.get_json()

        # Extract the math expression from the JSON data
        math_expression = data['math_expression']

        # Perform the math-to-image conversion
        output_file = "output.png"
        mathtext.math_to_image(math_expression, output_file)

        # Convert the image to base64 string
        with open(output_file, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        # Delete the image file
        import os
        #os.remove(output_file)

        # Return the base64 string as JSON
        return jsonify({"formula": encoded_image})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

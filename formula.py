import io
import base64
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify
from matplotlib.font_manager import FontProperties

app = Flask(__name__)

@app.route('/generate_plot', methods=['POST'])
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

    return jsonify({'image_base64': base64_string})

if __name__ == '__main__':
    app.run(debug=True)

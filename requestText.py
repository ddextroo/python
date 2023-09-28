import requests

url = 'https://dextro.pythonanywhere.com/formula_converter'
data = {
    "math_expression": "Find the x of this yehey \n a. $y = mx + b$ \n b.$\\Sigma_{C}$ \n c. $\\frac{1}{2}$ \nd. $x^2 + y^2 = r^2$"
}

response = requests.post(url, json=data)
if response.status_code == 200:
    result = response.json()
    base64_string = result.get('image_base64')
    print(base64_string)
else:
    print('API request failed.')

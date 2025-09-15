# app.py
from flask import Flask, request, render_template
from main import detect_sensitive_content

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        try:
            content = file.read().decode('utf-8')
        except UnicodeDecodeError:
            content = file.read().decode('latin1')  # fallback for non-UTF-8
        result = detect_sensitive_content(content)
        return render_template('result.html', result=result)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

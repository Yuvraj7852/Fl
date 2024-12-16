from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def print_name():
    name = "Yuvraj Singh"  # Replace with your desired name
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Print Name</title>
    </head>
    <body>
        <h1>Hello, {{ name }}!</h1>
    </body>
    </html>
    """
    return render_template_string(html, name=name)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask,
render_template

app = Flask(__name__)

@app.route("/")
def home():
    return
    render_template("index.html")
    @app.route("/about")
    def about():
        return
        render_template("about.html")
    <html>
    <head>
        <title>Golsarotter</title>
        <style>
            body {
                background: #fff0f5;
                color: #633b50;
                font-family: Georgia, serif;
                text-align: center;
                padding: 50px;
            }

            h1 {
                color: #c45b83;
            }

            .card {
                background: white;
                padding: 25px;
                margin: 20px auto;
                max-width: 400px;
                border-radius: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to my channel, girlies!</h1>
        <div class="card">
            <h2>Hello! ♡</h2>
            <p>here we have my first website!</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)

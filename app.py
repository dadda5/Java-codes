from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Ubuntu Store</title>

        <style>

            body {
                font-family: Arial;
                background-color: #f4f4f4;
                text-align: center;
                margin: 0;
                padding: 0;
            }

            header {
                background-color: black;
                color: orange;
                padding: 20px;
            }

            .container {
                margin-top: 50px;
            }

            .card {
                background: white;
                width: 300px;
                margin: auto;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px gray;
            }

            img {
                width: 100%;
                border-radius: 10px;
            }

            button {
                background: orange;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
            }

        </style>

    </head>

    <body>

        <header>
            <h1>Ubuntu Store</h1>
        </header>

        <div class="container">

            <div class="card">

                <img src="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=1000&auto=format&fit=crop">

                <h2>Smartphone</h2>

                <p>Latest Android smartphone with amazing features.</p>

                <button>Buy Now</button>

            </div>

        </div>

    </body>

    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

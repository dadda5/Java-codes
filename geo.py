from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>World Geography Explorer</title>
        <style>
            body{
                margin:0;
                font-family:Arial;
                background:#eef5ff;
            }
            header{
                background:#003366;
                color:white;
                text-align:center;
                padding:20px;
            }
            .banner{
                background:url('https://images.unsplash.com/photo-1521295121783-8a321d551ad2?q=80&w=1200&auto=format&fit=crop');
                height:400px;
                background-size:cover;
                display:flex;
                justify-content:center;
                align-items:center;
                color:white;
                font-size:50px;
                font-weight:bold;
            }
            .country{
                background:white;
                margin:30px;
                border-radius:10px;
                overflow:hidden;
                box-shadow:0 4px 10px rgba(0,0,0,0.2);
            }
            .country img{
                width:100%;
                height:350px;
                object-fit:cover;
            }
            .content{
                padding:20px;
            }
            footer{
                background:#003366;
                color:white;
                text-align:center;
                padding:20px;
            }
        </style>
    </head>
    <body>

    <header>
        <h1>World Geography Explorer</h1>
        <p>Discover Beautiful Countries</p>
    </header>

    <div class="banner">
        Explore The World
    </div>

    <div class="country">
        <img src="https://images.unsplash.com/photo-1524492412937-b28074a5d7da?q=80&w=1200&auto=format&fit=crop">
        <div class="content">
            <h2>India</h2>
            <p>India is famous for the Taj Mahal, culture, Himalayas, and diversity.</p>
        </div>
    </div>

    <div class="country">
        <img src="https://images.unsplash.com/photo-1499856871958-5b9627545d1a?q=80&w=1200&auto=format&fit=crop">
    app.run(host='0.0.0.0', port=5001)

from flask import Flask
                padding:40px;
            }
            .card{
                background:white;
                border-radius:10px;
                overflow:hidden;
                box-shadow:0 4px 10px rgba(0,0,0,0.2);
            }
            .card img{
                width:100%;
                height:250px;
                object-fit:cover;
            }
            .card h2, .card p{
                padding:10px;
            }
            button{
                margin:10px;
                padding:10px 20px;
                background:orange;
                color:white;
                border:none;
                border-radius:5px;
            }
            footer{
                background:#111;
                color:white;
                text-align:center;
                padding:20px;
            }
        </style>
    </head>
    <body>

    <header>
        <h1>Ubuntu Store</h1>
        <p>Modern Shopping Website</p>
    </header>

    <div class="banner">
        Welcome to Ubuntu Store
    </div>

    <div class="products">

        <div class="card">
            <img src="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=1000&auto=format&fit=crop">
            <h2>Smartphone</h2>
            <p>Latest Android smartphone.</p>
            <button>Buy Now</button>
        </div>

        <div class="card">
            <img src="https://images.unsplash.com/photo-1496181133206-80ce9b88a853?q=80&w=1000&auto=format&fit=crop">
            <h2>Laptop</h2>
            <p>Best laptop for coding and gaming.</p>
            <button>Buy Now</button>
        </div>

        <div class="card">
            <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=1000&auto=format&fit=crop">
            <h2>Headphones</h2>
            <p>Premium wireless sound quality.</p>
            <button>Buy Now</button>
        </div>

    </div>

    <footer>
        <p>© 2026 Ubuntu Store DevOps Project</p>
    </footer>

    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

import java.io.IOException;
import java.io.PrintWriter;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet("/")

public class IndiaWebsite extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");

        PrintWriter out = response.getWriter();

        out.println("""
        <!DOCTYPE html>

        <html>

        <head>

            <title>India Tourism</title>

            <style>

                body {
                    font-family: Arial;
                    background-color: #f4f4f4;
                    text-align: center;
                    margin: 0;
                    padding: 0;
                }

                header {
                    background-color: orange;
                    color: white;
                    padding: 20px;
                }

                .container {
                    margin-top: 40px;
                }

                .card {
                    background: white;
                    width: 400px;
                    margin: auto;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px gray;
                }

                img {
                    width: 100%;
                    border-radius: 10px;
                }

            </style>

        </head>

        <body>

            <header>
                <h1>Welcome to India</h1>
            </header>

            <div class="container">

                <div class="card">

                    <img src="https://upload.wikimedia.org/wikipedia/commons/d/da/Taj-Mahal.jpg">

                    <h2>India Tourism</h2>

                    <p>
                        India is famous for culture, history, food, Himalayas, and the Taj Mahal.
                    </p>

                </div>

            </div>

        </body>

        </html>
        """);
    }
}

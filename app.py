from flask import Flask, request, render_template
import google.generativeai as palm

palm.configure(api_key="AIzaSyAHA0JwVpNAUBXX9wVF28RTu5JqO7byRd4")
model = {"model": "models/chat-bison-001"}

app = Flask(__name__)   # sign the contract: the app belongs to me

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        print(q)
        r = palm.chat(
            **model,
            messages=q
        )
        return(render_template("index.html", result=r.last))
    else:
        return(render_template("index.html", result="waiting for question ..."))
    
if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=80)
    # If can't work, check the host and port number.
    

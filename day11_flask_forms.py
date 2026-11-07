from flask import Flask, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
     if request.method == "POST":
         prompt = request.form["prompt"]
         length = len(prompt)
         return f"<h1>Твой запрос: {prompt}</h1><p>Символов: {length}</p>"
     
     return """
         <form method="POST">
             <textarea name="prompt"></textarea>
             <button
    type="submit">Рассчитать</button>
        </form>
        """
if __name__ == "__main__":
     app.run(debug=True)

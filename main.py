from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# simple HTML template (inline for simplicity)
template = """
<!doctype html>
<title>Rock Paper Scissors</title>
<h2>Rock Paper Scissors</h2>
<form method="post">
  <button type="submit" name="choice" value="rock">🪨 Rock</button>
  <button type="submit" name="choice" value="paper">📄 Paper</button>
  <button type="submit" name="choice" value="scissors">✂️ Scissors</button>
</form>

{% if user_choice %}
  <p>You chose: <b>{{ user_choice }}</b></p>
  <p>Computer chose: <b>{{ computer_choice }}</b></p>
  <h3>Result: {{ result }}</h3>
{% endif %}
"""

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

@app.route("/", methods=["GET", "POST"])
def index():
    user_choice = None
    computer_choice = None
    result = None

    if request.method == "POST":
        user_choice = request.form["choice"]
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = decide_winner(user_choice, computer_choice)

    return render_template_string(
        template,
        user_choice=user_choice,
        computer_choice=computer_choice,
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)

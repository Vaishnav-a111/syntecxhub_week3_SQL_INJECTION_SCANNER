from flask import Flask, request

app = Flask(__name__)

@app.route('/')

def home():

    user_input = request.args.get('id')

    if user_input:

        # Simulated SQL error
        if "'" in user_input or "OR" in user_input.upper():

            return """
            You have an error in your SQL syntax;
            mysql_fetch_array() expects parameter 1
            """

        return f"User ID: {user_input}"

    return "Welcome"

app.run(debug=True, port=8000)
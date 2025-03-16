from flask import Flask, request

app = Flask(__name__)

# TCPQ-12 questions
QUESTIONS = [
    "1.	F1 - I have broken rules or regulations in order to implement my ideas or proposals",
    "2.	F1 - I skip procedures or rules because of the excitement of doing some work.",
    "3.	F1 - I have developed ideas that involve violation of certain rules.",
    "4.	F1 - I don’t mind breaking the rules to get a better job.",
    "5.	F2 - I think I dare more than the average person.",
    "6.	F2 - I have created original and positive things that are recognized by many people.",
    "7.	F2 - In my projects I am definitely riskier than others.",
    "8.	F2 - I get my ideas to have an impact on others.",
    "9.	F3 - I like to explore what is around me, in my environment.",
    "10. F3 - I tend to see things from different perspectives.",
    "11. F3 - Just for pleasure, I strive to find out how things work.",
    "12. F3 - Faced with a difficult choice, I follow my intuition."
]

@app.route("/", methods=["GET", "POST"])
def do_survey():
    if request.method == "POST":
        
        # Scores
        total_score = 0
        f1_score = 0
        f2_score = 0
        f3_score = 0
        
        # Calculate scores
        for i in range(1, 13):
            val = request.form.get(f"q{i}")
            if val is not None:
                total_score += int(val)
                if i > 0 and i < 5:
                    f1_score += int(val)
                if i > 4 and i < 9:
                    f2_score += int(val)
                if i > 8:
                    f3_score += int(val)

        # Return a simple results page
        return f"""
        <!doctype html>
        <html>
        <head>
            <title>Survey Results</title>
        </head>
        <body>
            <h1>Your total score is: {total_score}</h1>
            <h1>F1 score is: {f1_score}</h1>
            <h1>F2 score is: {f2_score}</h1>
            <h1>F3 score is: {f3_score}</h1>
            <p><a href="/">Go back</a></p>
        </body>
        </html>
        """
    
    else:
        # Build the HTML form for the questions
        question_html = ""
        
        for i, question in enumerate(QUESTIONS, start=1):
            question_html += f"<p>{question}</p>"
            for score in range(1, 8):
                question_html += f"""
                    <label>
                        <input type="radio" name="q{i}" value="{score}" required> {score}
                    </label>
                """
            question_html += "<br><br>"

        # Return the survey page
        return f"""
        <!doctype html>
        <html>
        <head>
            <title>TCPQ-12 Question Survey</title>
        </head>
        <body>
            <h1>TCPQ-12 Question Survey</h1>
            <form method="POST">
                {question_html}
                <input type="submit" value="Submit Survey">
            </form>
        </body>
        </html>
        """

if __name__ == "__main__":
    app.run(debug=True)

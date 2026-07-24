from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def helloMessage():
    name="Sivani"
    habits=["Drawing Practice","Coding Practice","Languages","Dashboard Project","Reading Practice"]
    habit_card_tsk=[i.split(" ")[0] for i in habits]
    progress_tasks={"Dashboard":"40%",
                   "Coding":"1/1",
                   "Drawing":"1/1",
                   "Excel":"0/1"}
    return render_template('index.html',habits=habits,name=name,habit_card_tsk=habit_card_tsk,progress_tasks=progress_tasks)

if __name__=='__main__':
    app.run(debug=True)



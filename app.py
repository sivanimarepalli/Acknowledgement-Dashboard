from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def helloMessage():
    name="Sivani"
    habits=["Drawing Practice","Coding Practice","Languages","Dashboard Project","Reading Practice"]
    habit_card_tsk=["Drawing","Languages","Dashboard","Coding","Excel"]
    return render_template('index.html',habits=habits,name=name,habit_card_tsk=habit_card_tsk)

if __name__=='__main__':
    app.run(debug=True)



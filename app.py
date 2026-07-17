from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def helloMessage():
    name="Sivani"
    habits=["Drawing Practice","Coding Practice","Languages","Dashboard Project","Reading Practice"]
    return render_template('index.html',habits=habits,name=name)

if __name__=='__main__':
    app.run(debug=True)



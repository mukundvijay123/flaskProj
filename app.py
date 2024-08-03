from flask import Flask,render_template

app=Flask(__name__)
Jobs=[
    {
        'id':1,
        'title':"data analyst",
        'location':"Bengaluru,India",
        'salary':"12000$"
    },
    {
        'id':2,
        'title':"data scientist",
        'location':"Bengaluru,India",
        'salary':"13000$"
    },
    {
        'id':3,
        'title':"backend engineer",
        'location':"Pune,India",
        'salary':"14000$"
    }
]

@app.route("/")
def home():
    return render_template("home.html",jobs=Jobs,company_name="RKVCORP")


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)

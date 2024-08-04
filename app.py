from flask import Flask, render_template

# an app is simply an object of the class Flask
app = Flask(__name__)


JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Bengaluru, India',
        'salary' : 'Rs.10,00,000'
    },
    {
        'id' : 2,
        'title' : 'Data Scientist',
        'location' : 'Delhi, India',
        'salary' : 'Rs.15,00,000'
    },
    {
        'id' : 3,
        'title' : 'Backend Engineer',
        'location' : 'Remote',
        'salary' : 'Rs.12,00,000'
    },
    {
        'id' : 4,
        'title' : 'Frontend Engineer',
        'location' : 'San Francisco',
        'salary' : '$120,000'
    }
]


@app.route("/")
def hello_rish():
    return render_template("home.html", 
                           jobs = JOBS, 
                           company_name = "Rish")

if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug=True)
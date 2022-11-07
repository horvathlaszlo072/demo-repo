from flask import Flask, render_template

app = Flask(__name__)

posta = [
    { 
        'author':'Horváth László',
        'title' : 'Blog post 1',
        'content': 'First post content',
        'date_posted': '2022.október 23.'
    },
    { 
        'author':'Máté Edina',
        'title' : 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '2022.október 24.'
    }    
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posta)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

#if __name__ == "__main__":
#        app.run(host='127.0.0.1', port=5000)    

if __name__ == "__main__":
    app.run(debug=True)
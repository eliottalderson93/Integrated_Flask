from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    piece_title = ['king','queen','bishop','knight','rook','pawn']
    return render_template("code.html",piece_title=piece_title)
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/<x>')
def index_2(x):
    piece_title = ['king','queen','bishop','knight','rook','pawn']
    x=int(x)+1
    return render_template("code.html",piece_title=piece_title,max=num)
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # we'll talk about the following two lines after we learn a little more about forms
    name = request.form['name']
    email = request.form['email']
    # redirects back to the '/' route
    return redirect('/')
if __name__=="__main__":
    # run our server
    app.run(debug=True)
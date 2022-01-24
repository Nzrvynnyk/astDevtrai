from flask import Flask, render_template, request, redirect, abort
from models import db, UserModel
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db/docker_practice_v3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/')
def start():
    allUsers = RetrieveUserList()
    return render_template('home.html', users=allUsers)


@app.route('/user/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createUser.html')

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        number = request.form['number']
        user = UserModel(firstname=firstname, lastname=lastname, email=email, number=number)
        db.session.add(user)
        db.session.commit()
        return redirect('/')


def RetrieveUserList():
    users = UserModel.query.all()
    return users


@app.route('/user/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    user = UserModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if user:
            db.session.delete(user)
            db.session.commit()

            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            number = request.form['number']
            user = UserModel(firstname=firstname, lastname=lastname, email=email, number=number)

            db.session.add(user)
            db.session.commit()
            return redirect('/')
        return "user does not exist"

    return render_template('update.html', user=user)


@app.route('/user/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    user = UserModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if user:
            db.session.delete(user)
            db.session.commit()
            return redirect('/')
        abort(404)

    return render_template('delete.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

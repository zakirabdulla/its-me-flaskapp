from app import app
from flask import render_template, redirect, url_for, request
from forms import RegistrationForm, LoginForm,LinkForm
from models import User,Link
from flask_login import login_required,login_user,logout_user,current_user
from werkzeug.security import check_password_hash
from sqlalchemy import or_

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        newUser = User(username=form.username.data,email=form.email.data,password=form.password.data)
        newUser.save()
        return redirect('/')
    return render_template('register.html',form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.form,meta={'csrf':False})
        print(form.EmailOrUsername.data,form.password.data,form.validate(),form.errors)
        if form.validate():
            u = User.query.filter(or_(User.username==form.EmailOrUsername.data,User.email==form.EmailOrUsername.data)).first()
            if u and check_password_hash(u.password,form.password.data):
                login_user(u)
                return redirect('/')
    return render_template('login.html',form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    linkform = LinkForm()
    if linkform.is_submitted():
        if linkform.validate():
            newlink = Link(title=linkform.title.data,address=linkform.adress.data,user_id=current_user.id,type=linkform.type.data)
            newlink.save()
            return redirect('/account')
    return render_template('account.html',linkform=linkform)
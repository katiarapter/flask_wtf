from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect


app = Flask(__name__)


class LoginForm(FlaskForm):
    id_1 = StringField('id астронавта', validators=[DataRequired()])
    password_1 = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_2 = StringField('id капитана', validators=[DataRequired()])
    password_2 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<profession>')
def training(profession):
    if profession in ['строитель', 'инженер']:
        return render_template('training.html', profession='Инженерные тренажеры', ship_image="space2.png")
    else:
        return render_template('training.html', profession='Научные симуляторы', ship_image="space1.png")


@app.route('/list_prof/<list_index>')
def list_prof(list_index):
    return render_template('list_prof.html', list_index=list_index)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('safe.html', title='Аварийный доступ', form=form, image='mars.png', style='style.css')


@app.route('/success')
def success():
    return render_template('success.html', title='Аварийный доступ')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


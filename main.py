from flask import Flask, render_template, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

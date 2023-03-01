from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if prof in ['строитель', 'инженер']:
        return render_template('training.html', prof='Инженерные тренажеры', ship_image="space2.png")
    else:
        return render_template('training.html', prof='Научные симуляторы', ship_image="space1.png")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

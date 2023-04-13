from flask import Flask, render_template, send_file
from flask_login import LoginManager
from random import randint
from data.full import Full
from data import db_session
from Mandelbrot import return_binary

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mandels.db")
    app.run()


@app.route('/')
def start():
    return render_template('start.html')


@app.route("/cube")
@login_manager.user_loader
def index():

    return render_template("cube0.html", size='300', size2='150', size1='149')


@app.route("/mandel/random")
def mandel():
    db_sess = db_session.create_session()
    id = randint(0, 150)
    for full in db_sess.query(Full).filter(Full.id == id):
        d = full.photo
        break
    with open('aaa.png', 'wb') as q:
        q.write(d)
    return send_file('aaa.png', mimetype='image/gif')


@app.route("/mandel/notcash/<int:imgx>/<int:imgy>")
def mandel_notcash(imgx, imgy):
    return_binary(imgx, imgy)
    return send_file('mid.png', mimetype='image/gif')


@app.route("/cube/user/<int:cube_size>/<speed>/<color>")
def cube(cube_size, speed, color):
    color = f'#{color}'
    try:
        float(speed)
    except Exception:
        return 'Неверный формат данных'
    g = color[1:]
    a, b, c = int(g[0:2], base=16), int(g[2:4], base=16), int(g[4:], base=16)
    return render_template("cube0.html", size=str(cube_size),
                           size2=str(cube_size // 2),
                           size1=str(cube_size // 2 - 1),
                           height=str(round(cube_size * 1.25)),
                           speed=str(speed),
                           colorhex=color,
                           color=f'{a},{b},{c}')


@app.route("/cube/random")
@login_manager.user_loader
def cube_random():
    g = f'{f()}{f()}{f()}'
    color = f'#{g}'
    cube_size = randint(100, 600)
    speed = str(randint(1, 100) / 10)
    a, b, c = int(g[0:2], base=16), int(g[2:4], base=16), int(g[4:], base=16)
    return render_template("cube0.html", size=str(cube_size),
                           size2=str(cube_size // 2),
                           size1=str(cube_size // 2 - 1),
                           height=str(round(cube_size * 1.25)),
                           speed=str(speed),
                           colorhex=color,
                           color=f'{a},{b},{c}')


def f():
    return hex(randint(0, 255))[2:].rjust(2, '0')


@app.errorhandler(500)
def bad_error(error):
    return render_template('500.html')


@app.route("/test/500")
@login_manager.user_loader
def test_500():
    1/0


@app.errorhandler(404)
def bad_error(error):
    return render_template('404.html')


if __name__ == '__main__':
    main()

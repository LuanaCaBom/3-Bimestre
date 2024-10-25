from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET'] = 'STRINgqUENINGUémsAbe'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/bim3g2"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLACHEMY_TRACK_MODIFICATIOS'] = False
from database import db
from flask_migrate import Migrate
from models import Usuario, Pizza, Pedido
db.init_app(app)
migrate = Migrate(app, db)
from modulos.usuarios import bp_usuario
app.register_blueprint(bp_usuario, url_prefix='/usuarios')



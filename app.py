from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy()
db.init_app(app)
# migrate = Migrate(app,db)

@app.route("/")
def index():
    return  render_template("login.html")
def home():
    gestante= db.session.query(Gestante).all()
    return render_template("home.html")
   
class Gestante(db.Model):
    __tablename__ = "gestantes"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    peso = db.Column(db.Float, nullable=False)
    altura = db.Column(db.Float, nullable=False)
    inicio_gestacao = db.Column(db.String(10), nullable=False)
    prenatal = db.Column(db.String(3), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

@app.route('/adicionar', methods=['GET','POST'])
def adicionar():
    if request.method == "POST":
        nome= request.form('nomeForm')
        numero= request.form('numeroForm')
        email= request.form('emailForm')
        cpf= request.form('cpfForm')
        idade= request.form('idadeForm')
        peso= request.form('pesoForm')
        altura= request.form('alturaForm')
        inicio_gestacao= request.form('inicio_gestacaoForm')
        prenatal= request.form('prenatalForm')

    gestante= Gestante(
        nome=nome,
        numero=numero,
        email=email,
        cpf=cpf,
        idade=idade,
        peso=peso,
        altura=altura,
        inicio_gestacao= inicio_gestacao,
        prenatal=prenatal
        )
    db.session.add(gestante)
    db.sesion.commit()
    return redirect(url_for("index"))
    return render_template("cadastrar.html")



@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

with app.app_context():
    db.create_all()
    
if __name__ == "__main__":
    app.run(debug=True)
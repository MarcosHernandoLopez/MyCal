from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

db = SQLAlchemy()



class UserModel(db.Model, UserMixin):
    __tablename__ = 'Usuarios'

    id = db.Column(db.String(), primary_key=True)
    email = db.Column(db.String(), nullable = False, unique = True)
    name = db.Column(db.String(), nullable = False, unique = True)
    password = db.Column(db.String(), nullable = False)

    def __init__(self, name, email, password):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<Nombre: {self.name} - Email: {self.email}>"

class EventModel(db.Model):
    __tablename__ = 'Eventos'

    id = db.Column(db.String(), primary_key=True)
    title = db.Column(db.String(), nullable = False)
    start = db.Column(db.DateTime(), nullable = False)
    end = db.Column(db.DateTime(), nullable = False)
    grupo = db.Column(db.String(), nullable = False)
    backgroundColor = db.Column(db.String(), nullable = False)

    def __init__(self, title, start, end, grupo, backgroundColor):
        self.id = grupo + "%" + str(uuid.uuid4())
        self.title = title
        self.start = start
        self.end = end
        self.grupo = grupo
        self.backgroundColor = backgroundColor

    def __repr__(self):
        return f"Título: {self.title}, Inicio: {self.start}, final: {self.end}\n"

class GroupModel(db.Model):
    __tablename__ = "GruposTEMP"

    name = db.Column(db.String(), primary_key = True)
    password = db.Column(db.String(), nullable = False)
    owner = db.Column(db.String(), nullable = False)

    def __init__(self, name, password, owner):
        self.name = name
        self.password = password
        self.owner = owner
        
    def __repr__(self):
        return {self.name}

class GrupoUserRelation(db.Model):
    __tablename__ = "Grupo_User_Relation"

    grupo = db.Column(db.String(), primary_key = True)
    user = db.Column(db.String(), primary_key = True)
    admin = db.Column(db.String(1))
    
    def __init__(self, grupo, user, admin):
        self.grupo = grupo
        self.user = user
        self.admin = admin

    def __repr__(self):
        return f"Grupo: {self.grupo}\n"
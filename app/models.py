## importamos sqlALchemy --> para efinir los atributos de los objetos 
## Pero con tipos trsducibles a sql y mysql 

from app import db
from datetime import datetime

class Medico(db.Model):
    __tablename__='medicos'
    id = db.Column(db.Integer, primary_key = True ) 
    nombres = db.Column(db.String(120), nullable = True )
    apellidos = db.Column(db.String(120), nullable = True)
    tipo_identificacion = db.Column(db.String(4), nullable = True)
    numero_identificacion = db.Column(db.Integer)
    registro_medico = db.Column(db.Integer)
    especialidad = db.Column(db.String(50))
    
    citas = db.relationship('Cita' , backref = 'medico' )

class Paciente(db.Model):
    __tablename__ ='pacientes'
    id = db.Column(db.Integer, primary_key = True ) 
    nombres = db.Column(db.String(120), nullable = True )
    apellidos = db.Column(db.String(120), nullable = True)
    tipo_identificacion = db.Column(db.String(4), nullable = True)
    numero_identificacion = db.Column(db.Integer)
    altura = db.Column(db.Integer)
    tipo_sangre = db.Column(db.String(2))

    citas = db.relationship('Cita' , backref = 'paciente' )
    
class Consultorio(db.Model):
    __tablename__ = 'consultorios'
    id= db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer)

    citas = db.relationship('Cita' , backref = 'consultorio' )

class Cita(db.Model):
    __tablename__ = 'citas'
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'))
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'))
    consultorio_id = db.Column(db.Integer, db.ForeignKey('consultorios.id')) 

'''    
med1 = Medico(nombres = 'gonzalo', apellidos = 'Fernandez', tipo_identificacion = 'CC', numero_identificacion = 123455, registro_medico = 8171635, especialidad ='cardiologo')
med2 = Medico(nombres = 'Sandra', apellidos = 'Vargas', tipo_identificacion = 'CC', numero_identificacion = 4163839, registro_medico = 765456, especialidad ='Urologa')
pac1 = Paciente(nombres = 'Maria', apellidos = 'Martinez', tipo_identificacion = 'CC', numero_identificacion = 234577,altura = 159, tipo_sangre = 'O+' )
pac2 = Paciente(nombres = 'Juan', apellidos = 'Romero', tipo_identificacion = 'CC', numero_identificacion = 876568,altura = 180, tipo_sangre = 'A-' )
pac3 = Paciente(nombres = 'Augusto', apellidos = 'villalba', tipo_identificacion = 'CC', numero_identificacion = 896383,altura = 173, tipo_sangre = 'O+' )
con1 = Consultorio(numero = 102)
con2 = Consultorio(numero = 203)
con3 = Consultorio(numero = 206)
mi_cita = Cita(fecha = '2024-03-05', paciente_id = 1, medico_id = 1, consultorio_id = 1 )
fecha1 = datetime(2024, 03, 05)

for ci in Cita.query.all():        
...     print('fecha: '+str(ci.fecha)+' Paciente identificación: '+ str(ci.paciente.numero_identificacion)+ ',paciente nombre: ' + ci.paciente.nombres+' '+ ci.paciente.apellidos)

'''    
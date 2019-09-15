from flask_script import Manager
from aplicacion.app import app,db
from aplicacion.models import *
from getpass import getpass

manager = Manager(app)
app.config['DEBUG'] = True

@manager.command
def create_tables():
    "Create relational database tables."
    db.create_all()
    categoria=Categorias(id=0,nombre="Todos")
    db.session.add(categoria)
    db.session.commit()

@manager.command
def drop_tables():
    "Drop all project relational database tables. THIS DELETES DATA."
    db.drop_all()

@manager.command
def add_data_tables():
    db.create_all()

    categorias = ("Analgesicos","Antiinflamatorios","Antiepilépticos","Antibacterianos","Antialérgicos")
    for cat in categorias:
    	categoria=Categorias(nombre=cat)
    	db.session.add(categoria)
    	db.session.commit()

    medicamentos=[
    {"nombre":"Paracetamol","precio":500,"descripcion":"El paracetamol es un analgésico y antipirético eficaz para el control del dolor leve o moderado causado por afecciones articulares, otalgias, cefaleas, dolor odontogénico, neuralgias, procedimientos quirúrgicos menores etc. También es eficaz para el tratamiento de la fiebre, como la originada por infecciones virales, la fiebre postvacunación, etcétera.","stock":110,"CategoriaId":1,"image":"paracetamol.jpg"},
    {"nombre":"Ibuprofeno","precio":1000,"descripcion":"El ibuprofeno es un analgésico y antiinflamatorio utilizado para el tratamiento de estados dolorosos, acompañados de inflamación significativa como artritis reumatoide leve y alteraciones musculoesqueléticas (osteoartritis, lumbago, bursitis, tendinitis, hombro doloroso, esguinces, torceduras, etc.). Se utiliza para el tratamiento del dolor moderado en postoperatorio, en dolor dental, postepisiotomía, dismenorrea primaria, dolor de cabeza.","stock":170,"CategoriaId":1,"image":"ibuprofeno.jpg"},
    {"nombre":"Betametasona","precio":2000,"descripcion":"La betametasona tópica se usa para tratar la picazón, enrojecimiento, resequedad, costras, descamación, inflamacióny las molestias ocasionadas por diferentes problemas en la piel incluyendo la psoriasis (una enfermedad de la piel en la cual se forman parches rojos y escamosos en algunas áreas del cuerpo) y eccema (una enfermedad de la piel que hace que la piel se seque y pique y, algunas veces, provoca sarpulllidos rojos y escamosos).","stock":50,"CategoriaId":2,"image":"betametasona.jpg"},
    {"nombre":"Hidrocortisona","precio":3000,"descripcion":"La hidrocortisona alivia la inflamación en varias partes del cuerpo. También para tratar o prevenir reacciones alérgicas. Como tratamiento de determinados tipos de enfermedades autoinmunitarias, afecciones cutáneas, asma y otras afecciones pulmonares.","stock":100,"CategoriaId":2,"image":"hidrocortosina.jpg"},
    {"nombre":"Carbamazepina","precio":4000,"descripcion":"La carbamazepina es un fármaco anticonvulsivo y estabilizador del estado de ánimo utilizado, principalmente, para controlar las crisis epilépticas y el trastorno bipolar. Este fármaco es un anticonvulsivante, relacionado químicamente con los antidepresivos tricíclicos.","stock":150,"CategoriaId":3,"image":"carbamazepina.jpg"},
    {"nombre":"Fenitoína","precio":5000,"descripcion":"La fenitoína se usa para controlar cierto tipo de convulsiones.También para tratar y prevenir las convulsiones que pueden empezar durante o después de la cirugía en el cerebro o en el sistema nervioso. La fenitoína pertenece a una clase de medicamentos llamados anticonvulsivos","stock":200,"CategoriaId":3,"image":"fenitoina.jpg"},
    {"nombre":"Amoxicilina","precio":6000,"descripcion":"La amoxicilina se usa para tratar algunas infecciones provocadas por bacterias como la neumonía; la bronquitis (infección de las vías respiratorias que van a los pulmones); e infecciones de los oídos, nariz, garganta, del tracto urinarioy la piel.","stock":250,"CategoriaId":4,"image":"amoxicilina.jpg"},
    {"nombre":"Bencilpenicilina","precio":7000,"descripcion":"La bencilpenicilina se usa para infecciones causadas por organismos susceptibles a la penicilina, incluyendo las producidas por gérmenes anaerobios. La BENCILPENICILINA está indicada en padecimientos infecciosos como amigdalitis, neumonías, bronconeumonías, meningitis bacte­­riana, abscesos, endocarditis bacteriana, parodon­titis, blenorragia, sífilis y osteomielitis.","stock":300,"CategoriaId":4,"image":"bencilpenicilina.png"},
    {"nombre":"Clorfenamina","precio":8000,"descripcion":"La clorfenamina es un antihistamínico indicado en rinitis alérgica estacional y perenne, conjuntivitis alérgica, alergias cutáneas no complicadas, rinitis vasomotora, urticaria, angioedema (edema angioneurótico), eccema alérgico, dermatitis atópica y de contacto, reacciones de hipersensibilidad a medicamentos, reacciones anafilácticas conjuntamente con epinefrina.","stock":350,"CategoriaId":5,"image":"clorfenamina.jpg"},
    {"nombre":"Dexametasona","precio":9000,"descripcion":"La dexametasona Alivia la inflamación (hinchazón, calor, enrojecimiento y dolor) y se usa para tratar ciertas formas de artritis; trastornos de la piel, la sangre, el riñón, los ojos, la tiroides y los intestinos (por ejemplo, colitis); alergias severas; y asma. La dexametasona también se usa para tratar ciertos tipos de cáncer","stock":400,"CategoriaId":5,"image":"dexametasona.jpg"},
    
    ]
    for med in medicamentos:
       	medicamento=Articulos(**med)
       	db.session.add(medicamento)
       	db.session.commit()

@manager.command
def create_admin():
    usuario={"username":input("Usuario:"),
            "password":getpass("Password:"),
            "nombre":input("Nombre completo:"),
            "email":input("Email:"),
            "admin": True}
    usu=Usuarios(**usuario)
    db.session.add(usu)
    db.session.commit()

if __name__ == '__main__':
	manager.run()

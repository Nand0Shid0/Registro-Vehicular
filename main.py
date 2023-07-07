
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QDialog
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2pacshaq122",
  database = "basecarros"
)

#CREARE DATABASE basecarro;
#CREATE TABLE IF NOT EXISTS domicilio (curp varchar(255) PRIMARY KEY, calle varchar(255) ,colonia varchar(255) , codigopostal varchar(255) , numerocasa varchar(255), color varchar(255));
#CREATE TABLE IF NOT EXISTS automovil (curp varchar(255) PRIMARY KEY, agencia varchar(255) , linea varchar(255)  , modelo varchar(255) , placa varchar (255) ,color varchar(255));
#CREATE TABLE IF NOT exists usuarios (nombre varchar(255), edad varchar(65), correo varchar(255), telefono varchar(255), curp varchar(255)); 


def registrar ():
    print('Entrando a registrar')
    name = w_reg.show()
    w_reg.show()
    main.hide()

    w_reg.registrar.clicked.connect(registrar_db)
    w_reg.salir.clicked.connect(salir)

def buscar():
    print('Buscando....')
    curp = str(w_info.curp.text())
    print(curp)

    mycursor = mydb.cursor()
    sql = "SELECT * FROM usuarios WHERE curp = %s "
    cur = (curp, )
    mycursor.execute(sql,cur)
    myresult = mycursor.fetchall()
    a = list(myresult[0])
    na = a[0]
    eda = a[1]
    ema = a[2]
    tel = a[3]
    dni = a[4]

    mycursor2 = mydb.cursor()
    sql = "SELECT * FROM domicilio WHERE curp = %s "
    cur = (curp, )
    mycursor2.execute(sql,cur)
    myresult2 = mycursor2.fetchall()
    b = list(myresult2[0])
    cal = b[1]
    col = b[2]
    cp = b[3]
    ncasa = b[4]

    mycursor3 = mydb.cursor()
    sql = "SELECT * FROM automovil WHERE curp = %s "
    cur = (curp, )
    mycursor3.execute(sql,cur)
    myresult3 = mycursor3.fetchall()
    c = list(myresult3[0])
    agency = c[1]
    line = c[2]
    model = c[3]
    plac = c[4]

    w_info.i_nombre.setText(na)
    w_info.i_edad.setText(eda)
    w_info.i_correo.setText(ema)
    w_info.i_telefono.setText(tel)
    w_info.i_curp.setText(dni)

    w_info.i_calle.setText(cal)
    w_info.i_colonia.setText(col)
    w_info.i_cp.setText(cp)
    w_info.i_ncasa.setText(ncasa)

    w_info.i_agencia.setText(agency)
    w_info.i_modelo.setText(model)
    w_info.i_placa.setText(plac)
    w_info.i_linea.setText(line)    
 
def salir(name):
    w_reg.hide()
    main.show()

def registrar_db():
    #Datos de Usario
    name = w_reg.nombre.text()
    age = w_reg.edad.text()
    curp = w_reg.curp.text()
    telefono =w_reg.telefono.text()
    correo = w_reg.correo.text()
    
    #Direccion de Usuario
    calle = w_reg.calle.text()
    colonia= w_reg.colonia.text()
    n_casa = w_reg.numero.text()
    cp = w_reg.cp.text()
    color_casa = w_reg.color_casa.text()
    
    #Vehiculo del Usuario
    agencia = w_reg.agencia2.text()
    linea = w_reg.linea.text()
    modelo = w_reg.modelo.text()
    placa = w_reg.placa.text()
    color_carro = w_reg.color.text()

    if name or age or curp or telefono or telefono or correo == "":
        print("Rellene todos los campos")
    else:
        sql = "INSERT INTO usuarios (nombre, edad, correo, telefono, curp) VALUES (%s, %s, %s, %s, %s)"
        val = (name, age,correo, telefono, curp, )
        mycursor = mydb.cursor()
        mycursor.execute(sql,val)
        mydb.commit()

        sql2 = "INSERT INTO domicilio (curp, calle, colonia, codigopostal, numerocasa, color) VALUES (%s, %s, %s, %s, %s,%s)"
        val2 = (curp,calle,colonia,cp,n_casa,color_casa) 
        mycursor = mydb.cursor()
        mycursor.execute(sql2,val2)
        mydb.commit() 

        sql3 = "INSERT INTO automovil (curp, agencia, linea, modelo, placa, color) VALUES (%s, %s, %s ,%s, %s, %s)"
        val3 = (curp, agencia, linea, modelo, placa, color_carro, )
        mycursor = mydb.cursor()
        mycursor.execute(sql3,val3)
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        print('exitoso')
    
def info():
    main.hide()
    w_info.show()
    w_info.buscar.clicked.connect(buscar)
    w_info.salir.clicked.connect(salirex)

def salirex():
    app.exit()

app = QtWidgets.QApplication([])

main = uic.loadUi('main.ui')
w_reg = uic.loadUi('main2.ui')
w_info = uic.loadUi('main3.ui')

main.registrar.clicked.connect(registrar)
main.informacion.clicked.connect(info)
main.salir.clicked.connect(salirex)

main.show()
app.exec()
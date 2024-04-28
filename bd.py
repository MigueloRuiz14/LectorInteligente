import pymysql
import tkinter
from tkinter import *
from  tkinter import messagebox


def login():
    bd = pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        db = "registro"
    )
    cursor = bd.cursor()
    sql = "INSERT INTO login (correo, contraseña) VALUES ('{0}', '{1}')".format("txtusuario", "txtpassword")
    try:
        cursor.execute(sql)
        bd.commit()

        messagebox.showinfo(message = "Registro hecho", title = "Aviso")
    
    except:
        bd.rollback()
        messagebox.showinfo(message = "Registro no hecho", title = "Aviso")
    

    bd.close()


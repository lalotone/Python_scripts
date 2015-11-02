#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb

DB_HOST = ''#ponemos la ip del server TIENE QUE TENER PERMISOS EN MYSQL DESDE ESA IP
DB_USER = ''#El usuario de la base de datos
DB_PASS = ''#La contrasenya
DB_NAME = ''#Y la base de datos

try:
	datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]#Guardamos todos los datos en un array para la conexion
	query = "SELECT * FROM proofs"#Ponemos la sentencia SQL que queremos ejecutar, con la tabla a atacar
	conn = MySQLdb.connect(*datos)#Conectamos con los datos del array que hemos hecho arriba
	if conn.open: #Comprobar si la conexion esta abierta
		print "La conexion esta abierta"
	#Aqui poidria haber un else en caso de que no conectase y nos saltase una excepcion

	cursor = conn.cursor()#Cremos un cursor para poder hacer operaciones sobre la BD
	cursorTwo = conn.cursor()#Creo un segundo cursor para otras sentencias

	cursor.execute(query)#Ejecutamos la consulta que hemos puesto mas arriba
	cursorTwo.execute("""INSERT INTO proofs (dataOne,dataTwo,dataThree) VALUES (%s,%s,%s)""", (40,"NukeProof",30))#Esto se pone así para ejecutar una consulta de ejecutar datos
	data = cursor.fetchall()#Cojemos todos los datos que devuelve la sentencia
	
	for row in data:#Vamos recorriendo con un for los datos que tenemos en la variable data de antes
		print row[0], row[1]#Imprimimos los datos de la primera y segunda columna

	cursor.close()#Cerramos el cursor que hemos empleado para llevar a cabo las operaciones
	conn.commit()#Importante hacer el commit tras la insercion de datos O NO LOS METERA
	conn.close()#Cerramos la conexion que hemos abierto con el server de la BD
	if conn.open:
		print "Peligro, la conexion sigue abierta"
	else:
		print "La conexion ha sido cerrada correctamente"
	print "All right"
except:
	print "Fatal  error"

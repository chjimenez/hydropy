#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 15:36:37 2011
@ author:                  Carlos Jimenez 
@ author's email id:       chjimenez@gmail.com   
"""
# import required modules
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from datetime import datetime, date, timedelta
import math

#path = "C:\WorkSpace\CHJ\CHJ-010-2015\INFO_SEC\IDEAM\ideam"

def abreideam(nombre):

	salto = "\n"
	
	fuente = os.path.join(nombre)
	conte = os.path.join("RESUMEN.CHJ")
	f = open(fuente, "r")
	resu = open(conte, "a")
	list_mes = ["ene","feb","mar","apr", "may", "jun", "jul", "aug", "sep", "octu", "nov", "dec"]
	tr_b = ""
	cod_b = ""
	para_b = ""
	clase_b = ""
	suma = -1
	rango = [0, 8, 9]
	rango = [0]
	
	for i in f:
		j = i
		tr=j[0:1]; cod=j[1:9]; para=j[9:11]; ano=j[11:15]; dia=j[15:17]
		ene=j[17:22]; tipo=j[22:23]
		feb=j[23:28]; tipo=j[28:29]
		mar=j[29:34]; tipo=j[34:35]
		apr=j[35:40]; tipo=j[40:41]
		may=j[41:46]; tipo=j[46:47]
		jun=j[47:52]; tipo=j[52:53]
		jul=j[53:58]; tipo=j[58:59]
		aug=j[59:64]; tipo=j[64:65]
		sep=j[65:70]; tipo=j[70:71]
		octu=j[71:76]; tipo=j[76:77]
		nov=j[77:82]; tipo=j[82:83]
		dec=j[83:88]; clase = j[99:100]

		lista = [ano, dia , ene , feb, mar, apr, may, jun , jul , aug , sep , octu , nov , dec]
		if (tr != tr_b or cod != cod_b or para != para_b or clase != clase_b):
			tr_b = tr
			cod_b = cod
			para_b = para
			clase_b = clase
			nombre_f2 = para + clase + cod + tr
			d = open(nombre_f2 + ".CHJ", "a")
			resu.write(nombre_f2+salto)

		lista = [item.replace("99999","     ") for item in lista]
		s = "\t".join(lista)
		s = s+salto
		s = s.replace(' ','')
		d.write(s)
	f.close()
	d.close()
	resu.close()

if __name__ == "__main__":
    nombre = input('Nombre del archivo (tr5 o tr8): ')
    abreideam(nombre)



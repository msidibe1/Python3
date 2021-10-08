#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:05:17 2020  

@author: moussa
"""
import connexion
class Periode:
    requete=""
    def __init__(self):
        self.typePeriode='disponibilite'
        self.duree=3
    def creerPeriode(self, t , d):
        self.typePeriode=t
        self.duree=d 
        #print("periode1", self.typePeriode, "a une duree de:", self.duree) 
        requete ="insert into Periode(typePeriode, duree) values ('"+t+"', '"+d+"');"
        c2=connexion.connexion()
        c2.creerRequete(requete)
        
   
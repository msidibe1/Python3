#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:47:15 2020

@author: moussa
"""
import connexion  
class Employe:
    requete=" "
    def __init__(self):   
         self.nom='Hien'
         self.prenom='Boris'
         self.coordonnees='hien.boris@gmail.com'
         self.idPeriode='1'
    def creerEmploye(self, n , pr , coord, t, p):
         requete="insert into Employe(nom, prenom, coordonnees, idPeriode, planning) values ('"+n+"', '"+pr+"', '"+coord+"','"+t+"', '"+p+"');"
         self.nom=n
         self.prenom=pr
         self.coordonnees=coord 
         self.idPeriode=t
         c6=connexion.connexion()
         c6.creerRequete(requete)
      
          
    
    
    
    
    
    
    
    
    
    
    
    
    
  
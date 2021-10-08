#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 00:41:47 2020

@author: moussa
"""
import connexion
import Evenement
class Presentation(Evenement.Evenement):
    requete=""
    def __init__(self, Presentateur):
	    Evenement.Evenement.__init__(self)
	    self.Presentateur = Presentateur
    def creerPresentation(self, pr):
        self.Presentateur=pr
        requete="insert into Presentation(presentateur) values ('"+pr+"');"
        c4=connexion.connexion()
        c4.creerRequete(requete)
        
       
        
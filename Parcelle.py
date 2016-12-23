# -*- coding: utf-8 -*-
"""
Created on Fri Oct 07 23:51:56 2016

@author: elie
"""

import pandas as pd
#import os
#from scipy.optimize import minimize
import lxml.etree as ET
import re

        
class Geosvg:
    """
    Permet de changer les couleurs des parcelles dans un fichier svg.
    Associe des couleur a des lots
    Colorise les parcelles d'un lot de la couleur de ce lot
    Colorise plusieurs lot
    Exporte le svg en un fichier bitmap
    """
    
    #def __init__(self,F_carte,F_coul,F_lot):
    def __init__(self,F_coul,F_lot,F_carte):
        """
        Definit les attribue de Lot
        """
        #self.coul=lit_couleurs(F_coul)
        self.couls = pd.read_csv(F_coul, sep=";", encoding="utf8", header=0)
        self.lots  = pd.read_csv(F_lot, sep=";", encoding="utf8", header=0)
        self.C    = ET.parse(F_carte)
        #self.lot=lit_lots(F_lot)
        self.F_out=F_carte+"out.svg"
        self.ns={'svg':"http://www.w3.org/2000/svg"}
    
    def style(self,the_id):
        """
        Find the style attribute of the tag path that contains the attribute
        id="the_id".
        """
        print(the_id)
        s=self.C.xpath('.//svg:path[@id="%s"]/@style'%the_id,namespaces=self.ns)
        if len(s)!= 0:
            return(s[0])
        else:
            print("La parcelle n°",the_id," n'existe pas ou est mal rensegnee")
        # print(s)
        # return(s)
    
    def sub_fill(self,s,new_rgb):
        """
        Substitute rgb color, of the "fill:" sub-attribute of the attribute style
        s, by the new rgb color new_rgb.
        """
        fill2="fill:"+new_rgb
        print(fill2)
        s2 = re.sub("(fill:#\S\S\S\S\S\S|fill:none)", fill2, s)
        return(s2)
        
    def dict_sub_attribut(self,s):
        """
        Return a dict of ";" separated sub-attribute of the attribute s
        Each sub-attribute is composed of a key:value.
        """
        ls=s.split(";")
        d={}
        for i in ls:
            k,v=i.split(":")
            d[k]=v
        return(d)

    def colorie_lot(self):
        """
        A partir de lots, couleurs et de cadastre:
        retrouve les parcelles de chaque lot dans le cadastre
        et lui donne la couleur indiquee dans couleurs.
        """
        for i_lot,lot in enumerate(self.lots.keys()):
            for num_parcelle in self.lots[lot].dropna():
                # print(lot) #+":"+num_parcelle)
                coul=self.couls["RGB"][i_lot]
                id=str(int(num_parcelle))
                print(id)
                s=self.style(id)
                print(s)
                s2=self.sub_fill(s,coul)
                print(s2)
                # for rank in self.C.iter('path'):
                for rank in self.C.xpath('.//svg:path',namespaces=self.ns):
                    if rank.attrib["id"]==id:
                        rank.attrib["style"]=s2
                        # rank.set('style', s2)
                        print(rank.attrib["style"]) 
        # print(self.C.tostring())
        # self.C.write(self.F_out)
        self.C.write(self.F_out)
    
    def svg_to_png(self,the_svg):
        """
        Convert an svg file into a png file
        """
        pass
    
    
# if __name__ == '__main__':
    # Claus=Terrain("parcelles_V8.csv")
    # Nlot=5
    # print Clauspath
#    for i in Claus.CT.loc("numeros"):
#        for j in Nlot:
#            Lots=[Lot(i.at[]),]
#    Terrain=[]
    # pass

#Plan:
#coloration du terrain:
#    lire lot
#    donner une couleur par lot
#    lire cadastre.svg
#    donner une couleur par parcelle correspondant a chaque lot
#    exporter le svg en bitmap    

#class Bareme:
#    """
#    Contient un ensemble de critere permettant d'evaluer une parcelle
#    """
#    
#    def init(self,F_Bareme):
#        """
#        Definit les attribue de Bareme
#        """
#        self.FB=F_Bareme
#        self.CoeffBareme=pd.read_csv(self.F_Bareme)
#    
#    
#class BaremeNorme(Bareme):
#    """
#    Contient un ensemble de criteres permettant d'evaluer une 
#    parcelle en €/m2
#    """
#    
#    def init(self,F_Borne):
#        """
#        Definit les attribue de Bareme
#        """
#        self.FBornes=F_Borne
#        self.CoeffBorne=pd.read_csv(self.F_Borne)
#
#    def norm_barem(self):
#        """
#        Normalise les parametre et les fait passer de point a
#        devise par unite de surface
#        """
#        pass
#    
#    def calc_norm(self):
#        """
#        Determine les valeur de la fonction de passage de point a
#        devise
#        """
#        pass
#    

# class Terrain:
    # """
    # Est constitue de lot et de parcelles
    # Lit les caracteristiques de chaque parcelles qui le compose
    # Verifie que toutes les parcelles sont comprises dans les lots
    # qui le compose
    # Peut ajouter ou retirer une parcelle
    # """
    
    # def __init__(self,F_Caract):
        # """
        # Definit les attribue de Terrain
        # """
        # self.T=pd.read_csv(F_Caract,sep="\t")
            
    
   # def lit_carac_parcelle(self,fichier):
       # """
       # Lit un fichier .csv et en cree un tableau pandas
       # """
       # return)
       # pass
    
    # def ajout_lot(self):
        # """
        # Cree des instances de lot a partir
        # """
        # pass
    
    # def enleve_lot(self):
        # """
        # Enleve un lot d'un terrain
        # """
        # pass
    
    # def cree_parcelle(self):
        # """
        # Cree des instances de parcelle
        # """
        # pass


#class PrixParcelle:
#    """
#    Permet de calculer le prix d'une parcelle en fonction d'un bareme
#    """
#    
#    def init(self,P,BN):
#        """
#        Definit les attribue de Prix
#        """
#        self.P=P   #Parcelle
#        self.BN=BN #Bareme norme
#            
#    def prix_parcelle(self):
#        """
#        Calcul le prix d'une parcelle.
#        """
#        return( self.prix_TCons()+self.prix_TAgr())
#    
#    def prix_TAgr(self):
#        """
#        Calcul le prix d'une parcelle de terre agricole.
#        """
#        return( self.prix_ombre_maras()+
#                self.prix_ensoleillement()+
#                self.prix_deniv()+
#                self.prix_l_L()+
#                self.prix_canal()+
#                self.prix_acces()+
#                self.prix_type())
#        
#    def prix_ombre_maras():
#        """
#        Calcul la valeur liee a l'ombre de la crete du Maras.
#        """
#        if(self.P["Ombre_Maras"]==1):
#            return(self.BN["ombre_Maras"]
#        else:
#            return(self.BN["pas_ombre_Maras"]            
#    
#    def prix_ensoleillement(self):
#        """
#        Calcul la valeur liee a l'ensoleillement.
#        """
#    
#    def prix_deniv(self):
#        """
#        Calcul la valeur liee au denivele.
#        """
#    
#    def prix_l_L(self):
#        """
#        Calcul la valeur liee a la formede la parcelle.
#        """
#    
#    def prix_canal(self):
#        """
#        Calcul la valeur liee a l'irigabilite gravitaire.
#        """
#    
#    def prix_acces(self):
#        """
#        Calcul la valeur liee a l'accessibilite.
#        """
#
#    def prix_type(self):
#        """
#        Calcul la valeur liee au type de terrain.
#        """
#
#    def prix_TCons(self):
#        """
#        Calcul le prix d'une parcelle constructible.
#        """

# class Lot:
    # """
    # Regroupe plusieur parcelles
    # """
    
    # def __init__(self):
        # """
        # Definit les attribue de Lot
        # """
        # self.LP=[]

    # def ajout_p(self,Pn):
        # """
        # Ajoute une parcelle au lot.
        # """
        # self.LP.append(Pn)
    
    # def enleve_p(self):
        # """
        # Enleve une parcelle au lot.
        # """
        # self.LP.pop()
    
    # def prix_lot(self):
        # """
        # Calcul le prix d'une parcelle.
        # """
        # prix=0.
        # for P in self.LP:
            # prix=prix+P.at[p,'prix']
        # return(prix)
        
# class OptimLot:
    # """
    # Permet de determiner la composition des lot de sorte a respecter
    # un objectif et des contraintes.
    # """
    
    # def __init__(self):
        # """
        # Definit les attribue de Lot
        # """
        # pass
    
    
    # def lit_conf():
        # """
        # Lit la configuration de l optimisation dans un .csv.
        # """
        # pass
    
    # def objectif(self):
        # """
        # Permet de determiner l'objectif vise
        # """
        # pass

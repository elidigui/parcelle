# -*- coding: utf-8 -*-
"""
Created on Fri Oct 07 23:51:56 2016

@author: elie
"""
import Parcelle as Par
import unittest as ut
import os

    
class TestGeosvg(ut.TestCase):
    """ Test  Lot's methods """
    def setUp(self):
        """ Set test up """
        self.rep_test  = "test"
        self.TestLot1  = self.rep_test + os.sep + "test_lot1.csv"
        self.TestCoul1 = self.rep_test + os.sep + "test_couleur1.csv"
        self.Testsvg1  = self.rep_test + os.sep + "test_svg1.svg"
        self.Testsvg2  = self.rep_test + os.sep + "test_svg2.svg"
        self.a1 = Par.Geosvg(self.TestCoul1, self.TestLot1, self.Testsvg1)
        self.style="color:#000000;clip-rule:nonzero;display:inline;overflow:visible;visibility:visible;opacity:0.38000039;isolation:auto;mix-blend-mode:normal;color-interpolation:sRGB;color-interpolation-filters:linearRGB;solid-color:#000000;solid-opacity:1;fill:#8cff00;fill-opacity:0;fill-rule:evenodd;stroke:#800000;stroke-width:4.65311146;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1;color-rendering:auto;image-rendering:auto;shape-rendering:auto;text-rendering:auto;enable-background:accumulate"
        self.style2="color:#000000;clip-rule:nonzero;display:inline;overflow:visible;visibility:visible;opacity:0.38000039;isolation:auto;mix-blend-mode:normal;color-interpolation:sRGB;color-interpolation-filters:linearRGB;solid-color:#000000;solid-opacity:1;fill:#123456;fill-opacity:0;fill-rule:evenodd;stroke:#800000;stroke-width:4.65311146;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1;color-rendering:auto;image-rendering:auto;shape-rendering:auto;text-rendering:auto;enable-background:accumulate"
        self.c = "#123456"
        self.id = "ellipse1"
        self.opacity1="0.38000039"
        #     "color:#000000;clip-rule:nonzero;display:inline;\
        # overflow:visible;visibility:visible;opacity:0.38000039;\
        # isolation:auto;mix-blend-mode:normal;color-interpolation:\
        # sRGB;color-interpolation-filters:linearRGB;solid-color:#000000;\
        # solid-opacity:1;fill:#8cff00;fill-opacity:0;fill-rule:evenodd;\
        # stroke:#800000;stroke-width:4.65311146;stroke-linecap:butt;\
        # stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;\
        # stroke-dashoffset:0;stroke-opacity:1;color-rendering:auto;\
        # image-rendering:auto;shape-rendering:auto;text-rendering:auto;\
        # enable-background:accumulate"

    def test_lit_coul_header(self):
        """ Test if the function read the header of the color.csv file """
        self.assertEqual(self.a1.couls.keys()[2], "RGB",
                         "Don't read the write header")

    def test_lit_lot_header(self):
        """ Test if the function read the header of the lot.csv file """
        self.assertEqual(self.a1.lots.keys()[2], "Lot3",
                         "Don't read the write header")

    def test_xpath_ellipse_svg(self):
        """ Test if the function can find cx in ellipse in a simple svg """
        id = "ellipse"
        cx = self.a1.C.xpath('.//ellipse[@id="%s"]/@cx' % id)
        self.assertEqual(cx[0], "301.42856","Don't read the tag")

    def test_xpath_path_style_svg1(self):
        """ Test if the function can find style attribute of the path(id=the_id) 
        in a simple svg """
        s = self.a1.style(self.id)
        self.assertEqual(s, self.style, "Don't read the tag")
        
    def test_xpath_path_style_svg2(self):
        """ Test if the function can find style(color) in path attribut style a simple svg """
        s = self.a1.style(self.id)
        color=s.split(";")[0]
        self.assertEqual(color,"color:#000000", "Don't read the tag")

    def test_dict_sub_attribut_opacity(self):
        """
        Test if the sub_attribute "opacity" of the attribute "style" of the tag
        svg.path(id=ellipse1) matches.
        """
        s = self.a1.style(self.id)
        d = self.a1.dict_sub_attribut(s)
        self.assertEqual(d["opacity"],self.opacity1, "Don't read the tag")        
     
    def test_sub_fill_svg(self):
        """ Test if the function read the header of the color.csv file """
        s = self.a1.style(self.id)
        #print("s=" + s[0])
        s2= self.a1.sub_fill(s,self.c)
        # print("s2="+s2)
        # ds2=dict(s2.split(";"))
        # for it in ds2:
            # print(it)
        # fill = s2.split(";")[0]
        # print("c1="+self.c)
        # print("c2="+color)
        self.assertEqual(s2, self.style2, "Don't read the tag")

    #def sub_fill(self, s, rgb):



#List of TestSuites:
suite1 = ut.TestLoader().loadTestsFromTestCase(TestGeosvg)
alltests = ut.TestSuite([suite1])

#Execution of tests:
for suite_ in alltests:
    ut.TextTestRunner(verbosity=2).run(suite_)

if __name__ == '__main__':
    ut.main()
    
        
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
      
        
# class Geosvg:
    # """
    # Permet de changer les couleurs des parcelles dans un fichier svg.
    # Associe des couleur a des lots
    # Colorise les parcelles d'un lot de la couleur de ce lot
    # Colorise plusieurs lot
    # Exporte le svg en un fichier bitmap
    # """
    
    # def __init__(self,F_carte,F_coul):
        # """
        # Definit les attribue de Lot
        # """
        # self.C=lx.etree.parse(F_carte)
        # self.coul=lit_couleurs(F_coul)
        # self.lot=lit_lot(F_lot)
        # self.F_out=F_carte+"out.svg"
    
    # def lit_couleurs(self,F_couleur)
        # """"
        # Lit un fichier csv avec les lot et les couleurs rgb
        # coul=[111111,222222,333333,...,GGGGGG]
        # len(coul)=n_lot
        # """
        # t_coul=
     
    # def lit_lots(self,F_lot)
        # """
        # Lit les lots dans un tableau csv
        # lot[[p1.1,p1.2,...,p1.n1][p2.1,p2.2,...p2.n2],...]
        # """
        
    # def colorie_lot()
        # """
        # A partir de lots, couleurs et de cadastre:
        # retrouve les parcelles de chaque lot dans le cadastre
        # et lui donne la couleur indiquee dans couleurs.
        # """
        # for lot in lots:
            # for num_parcelle in lot:
                # id=num_parcelle
                # style=self.C.xpath('.//path[@id=%s]/@style',id)
                # style2=re.sub("fill:#\S\S\S\S\S\S","fill:#111111",style[0])
                # for rank in self.C.iter('path'):
                    # if rank.attrib["id"]==id:
                        # rank.set('style', style2)
                        # print(rank.attrib["style"]) 
        # self.C.write(self.F_out)

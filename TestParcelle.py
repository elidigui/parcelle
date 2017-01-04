# -*- coding: utf-8 -*-
"""
Created on Fri Oct 07 23:51:56 2016

@author: elie
"""
import Parcelle as Par
import unittest as ut
import os
import hashlib as h

    
class TestGeosvg(ut.TestCase):
    """ Test  Lot's methods """
    def setUp(self):
        """ Set test up """
        self.rep_test  = "test"

        self.TestLot1  = self.rep_test + os.sep + u"test_lot1.csv"
        self.TestCoul1 = self.rep_test + os.sep + u"test_couleur1.csv"
        self.Testsvg1  = self.rep_test + os.sep + u"test_svg1.svg"
        self.a1 = Par.Geosvg(self.TestCoul1, self.TestLot1, self.Testsvg1)
        
        self.TestLot2  = self.rep_test + os.sep + u"test_lot2.csv"
        self.Testsvg2  = self.rep_test + os.sep + u"test_svg2.svg"
        self.Testsvg2ok = self.rep_test + os.sep + u"test_svg2_ok.svg"
        self.a2 = Par.Geosvg(self.TestCoul1, self.TestLot2, self.Testsvg2)
               
        self.style="color:#000000;clip-rule:nonzero;display:inline;overflow:visible;visibility:visible;opacity:0.38000039;isolation:auto;mix-blend-mode:normal;color-interpolation:sRGB;color-interpolation-filters:linearRGB;solid-color:#000000;solid-opacity:1;fill:#8cff00;fill-opacity:0;fill-rule:evenodd;stroke:#800000;stroke-width:4.65311146;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1;color-rendering:auto;image-rendering:auto;shape-rendering:auto;text-rendering:auto;enable-background:accumulate"
        self.style2="color:#000000;clip-rule:nonzero;display:inline;overflow:visible;visibility:visible;opacity:0.38000039;isolation:auto;mix-blend-mode:normal;color-interpolation:sRGB;color-interpolation-filters:linearRGB;solid-color:#000000;solid-opacity:1;fill:#123456;fill-opacity:0;fill-rule:evenodd;stroke:#800000;stroke-width:4.65311146;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1;color-rendering:auto;image-rendering:auto;shape-rendering:auto;text-rendering:auto;enable-background:accumulate"
        self.c = "#123456"
        self.id = "ellipse1"
        self.id2 = "popo"
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
        cx = self.a1.C.xpath('.//svg:ellipse[@id="%s"]/@cx' % id,namespaces=self.a1.ns)
        self.assertEqual(cx[0], "301.42856","Doesn't read the tag")

    def test_xpath_path_style_svg1(self):
        """ Test if the function can find style attribute of the path(id=the_id) 
        in a simple svg """
        s = self.a1.style(self.id)
        self.assertEqual(s, self.style, "Doesn't match the attribute style")
        
    def test_xpath_path_style_svg2(self):
        """ Test if the function can find style(color) in path attribut style 
        a simple svg """
        s = self.a1.style(self.id)
        color=s.split(";")[0]
        self.assertEqual(color,"color:#000000", "Doesn't match the style.color")
        
    def test_xpath_path_style_svg3(self):
        """ Test if the function style return 0 if there is no path.id=self.id2"""
        s = self.a1.style(self.id2)
        self.assertEqual(s,0, "Doesn't match the 0 if a path(id=the_id) not found")

    def test_dict_sub_attribut_opacity(self):
        """
        Test if the sub_attribute "opacity" of the attribute "style" of the tag
        svg.path(id=ellipse1) matches.
        """
        s = self.a1.style(self.id)
        d = self.a1.dict_sub_attribut(s)
        self.assertEqual(d["opacity"],self.opacity1, "Doesn't match the style.opacity\
        in the dict")        
     
    def test_sub_fill_svg(self):
        """ Test if the function sub_fill changes path(id=self.id)style.color"""
        s = self.a1.style(self.id)
        s2= self.a1.sub_fill(s,self.c)
        self.assertEqual(s2, self.style2, "Don't read the tag")

    def test_colorie_lot1(self):
        """ Change the color of path to write and compare to a test file with
        write path"""
        self.a2.colorie_lot()
        t=TestFile(self.a2.F_out,self.Testsvg2ok)
        self.assertEqual(t.cmp, True, "Two files are different")


class TestFile:
    """ tool for comparing files """
    
    def __init__(self,F1,F2):
        """
        Definit les attribue de Lot
        """
        self.cmp=self.is_contents_same(F1,F2)
        
    def checksum(self,f):
        """ Compute md5 sum of a file"""
        md5 = h.md5()
        # file = open(f,"r",encoding='utf-8')
        with open(f,"rb") as file:
            md5.update(file.read())
            print(file.readlines())
            return md5.hexdigest()

    def is_contents_same(self,f1, f2):
        """return true if the md5 sum of f1 and f2 are
        the same, false ether"""
       # print(self.checksum(f1))
       # print(self.checksum(f2))
        return self.checksum(f1) == self.checksum(f2)

    # def cmp_files(f1,f2):
        # if not is_contents_same('foo.txt', 'bar.txt'):
        # print 'The contents are not the same!'

        
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

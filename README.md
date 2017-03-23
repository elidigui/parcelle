# parcelle
Python programme to color an svg map.
The map is an svg file. It containes zones
that have to be svg path.
The id of that zones have to be an integer.
To color the map, to csv file (table) have to be provoded.
-The table which gathere zones into sets.
-The table that associate a color to each set.

# How to use it.
Open a python terminal into the directory which contain Parcelle.py:
import Parcelle as P
G=P.GeoSvg("color","sets","map")
G.colorie_lot()
## "color"
It is the name of a csv file. 
For example:
Lot1;Lot2;Lot3;Lot4;Lot5
92;;89;18;76
93;63;81;19;62
94;52;84;20;
95;57;85;21;
96;;86;22;
80;;87;34;
79;;88;35;
75;;27;36;
66;;28;37;
72;;29;38;
73;;30;42;
74;;23;43;
49;;24;68;
59;;25;50;
53;;26;14;
54;;31;15
55;;32;2
56;;44;3
;;45;4
;;46;5
;;47;9
;;48;10
;;33;11
;;100;13
;;101;67
;;106;70
;;90;77
;;91;71
;;82;69
;;83;64
;;;65
;;;61
;;;51
;;;60

## "sets"
It is the name of a csv file:

For example:
Lot;Couleur;RGB
1;red;#FF0000
2;fuchsia;#FF00FF
3;green;#008000
4;yellow;#FFFF00
5;blue;#0000FF

## "map"
It is the name of the matching svg file which containe
zones.

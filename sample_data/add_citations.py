
###################################
###connect to database

load("connect.py")

#returns
# my_session - database connection
# my_cursor - cursor to my_session

path_to_log = "/home/ben/dynabase/citations_log.txt"
log_file = open(path_to_log, 'w', 1)

from citations.citations_helper import add_citation

#########################


bibliography=[]
bibliography.append(['Benedetto2009',['Robert Benedetto', 'Ben Dickman', 'Sasha Joseph', 'Ben Krause', 'Dan Rubin', 'Xinwen Zhou'],\
    'Involve', 2009,\
    'Robert Benedetto, Ben Dickman, Sasha Joseph, Ben Krause, Dan Rubin, and Xinwen Zhou. Computing points of small height for cubic polynomials. Involve, 2:37--64, 2009.',\
    'MR2501344'])
bibliography.append(['BFHJY2017', ['Robert L. Benedetto', 'Xander Faber', 'Benjamin Hutz', 'Jamie Juul', 'Yu Yasufuku'],\
    'Res. Number Theory', 2017,\
    'Robert L. Benedetto, Xander Faber, Benjamin Hutz, Jamie Juul, and Yu Yasufuku. A large arboreal Galois representation for a cubic postcritically finite polynomial. Res. Number Theory, 3:Paper No. 29, 21 pp., 2017.',\
    'MR3736808'])
bibliography.append(['BM2012', ['Nils Bruin', 'Alex Molnar'], 'LMS J. Comput. Math.', 2012,\
    'Nils Bruin, Alex Molnar. Minimal models for rational functions in a dynamical setting. LMS J. Comput. Math. 15 (2012) 400--417.',\
    'MR3015733'])
bibliography.append(['Canci2010', ['Jung Kyu Canci'], 'Ann. Inst. Fourier (Grenoble)', 2010,\
    'Jung Kyu Canci. Rational periodic points for quadratic maps. Ann. Inst. Fourier (Grenoble), 60(3):953--985, 2010.',\
    'MR2680821'])
bibliography.append(['Chang2006', ['Jianming Chang'], 'J. Math. Anal. Appl.', 2006,\
    'Jianming Chang. Polynomials without repelling periodic point of given period. J. Math. Anal. Appl., 324:1--13, 2006.',\
    'MR2262451'])
bibliography.append(['Dickson1958', ['Leonard Eugene Dickson'], 'Dover Publications', 1958,\
    'Leonard Eugene Dickson. Linear Groups: With an Exposition of the Galois Field Theory. Dover Publications, New York, 1958.',\
    'MR0104735'])
bibliography.append(['Doyle2014', ['John R. Doyle', 'Xander Faber', 'David Krumm'], 'New York J. Math.', 2014,\
    'John R. Doyle, Xander Faber, and David Krumm. Preperiodic points for quadratic polynomials over quadratic fields. New York J. Math., 20:507--605, 2014.',\
    'MR3218788'])
bibliography.append(['dFH2018', ['Joao Alberto de Faria', 'Benjamin Hutz'], 'J. Algebra Appl.', 2018,\
    'Joao Alberto de Faria and Benjamin Hutz. Automorphism groups and invariant theory on PN. J. Algebra Appl., 17:1850162, 38 pp., 2018.',\
    'MR3846410'])
bibliography.append(['FMV2015', ['Xander Faber', 'Michelle Manes', 'Bianca Viray'], 'J. Algebra', 2015,\
    'Xander Faber, Michelle Manes, and Bianca Viray. Computing conjugating sets and automorphism groups of rational functions. J. Algebra, 423:1161--1190, 2015.',\
    'MR3283753'])
bibliography.append(['GHK2023', ['Thomas Gauthier', 'Benjamin Hutz', 'Scott Kaschner'], 'Conform. Geom. Dyn.', 2023,\
    'Thomas Gauthier, Benjamin Hutz, and Scott Kaschner. Symmetrization of rational maps: arithmetic properties and families of Lattes maps of Pk. Conform. Geom. Dyn., 27:98--117, 2023.',\
    'MR4548508'])
bibliography.append(['Hutz2015', ['Benjamin Hutz'], 'Math. Comp.', 2015,\
    'Benjamin Hutz. Determination of all rational preperiodic points for morphisms of PN. Math. Comp., 84(291):289--308, 2015.',\
    'MR3266961'])
bibliography.append(['Hutz2013', ['Benjamin Hutz', 'Patrick Ingram'], 'Rocky Mountain J. Math.', 2013,\
    "Benjamin Hutz and Patrick Ingram. On Poonen's conjecture concerning rational preperiodic points of quadratic maps. Rocky Mountain J. Math., 43(1):193--204, 2013.",\
    'MR3065461'])
bibliography.append(['Ingram2012', ['Patrick Ingram'], 'Int. Math. Res. Not. IMRN', 2012,\
    'Patrick Ingram. A finiteness result for post-critically finite polynomials. Int. Math. Res. Not. IMRN, 2012(3):524--543, 2012.',\
    'MR2885981'])
bibliography.append(['Jones2008', ['Rafe Jones'], 'J. Lond. Math. Soc. (2)', 2008,\
    'Rafe Jones. The density of prime divisors in the arithmetic dynamics of quadratic polynomials. J. Lond. Math. Soc. (2), 78(2):523--544, 2008.',\
    'MR2439638'])
bibliography.append(['JM2014', ['Rafe Jones', 'Michelle Manes'], 'Comment. Math. Helv.', 2014,\
    'Rafe Jones and Michelle Manes. Galois theory of quadratic rational functions. Comment. Math. Helv., 89(1):173--213, 2014.',\
    'MR3177912'])
bibliography.append(['Lukas2014', ['David Lukas', 'Michelle Manes', 'Diane Yap'], 'LMS J. Comput. Math.', 2014,\
    'David Lukas, Michelle Manes, and Diane Yap. A census of quadratic post-critically finite rational functions defined over Q. LMS J. Comput. Math., 17(A):314--329, 2014.',\
    'MR3240812'])
bibliography.append(['Manes2008', ['Michelle Manes'], 'Proc. Lond. Math. Soc. (3)', 2008,\
    'Michelle Manes. Q-rational cycles for degree-2 rational maps having an automorphism. Proc. Lond. Math. Soc. (3), 96:669--696, 2008.',\
    'MR2407816'])
bibliography.append(['Miasnikov2017', ['Nikita Miasnikov', 'Brian Stout', 'Phillip Williams'], 'Acta Arith.', 2017,\
    'Nikita Miasnikov, Brian Stout, and Phillip Williams. Automorphism loci for the moduli space of rational maps. Acta Arith., 180:267--296, 2017.',\
    'MR3709645'])
bibliography.append(['Poonen1998', ['Bjorn Poonen'], 'Math. Z.', 1998,\
    'Bjorn Poonen. The classificiation of rational preperiodic points of quadratic polynomials over Q: a refined conjecture. Math. Z., 228(1):11--29, 1998.',\
    'MR1617987'])
bibliography.append(['Stoll2008', ['Michael Stoll'], 'LMS J. Comput. Math.', 2008,\
    'Michael Stoll. Rational 6-cycles under iteration of quadratic polynomials. LMS J. Comput. Math., 11:367--380, 2008.',\
    'MR2465796'])
bibliography.append(['WR1994', ['Ralph Walde', 'Paula Russo'], 'Amer. Math. Monthly', 1994,\
    'Ralph Walde and Paula Russo. Rational periodic points of the quadratic function Qc(x) = x^2 + c. Amer. Math. Monthly, 101(4):318--331, 1994.',\
    'MR1270956'])


for row in bibliography:
    label, authors, journal, year, citation, mathscinet = row
    is_new, citation_id = add_citation(label, authors, journal, year, citation, mathscinet,
        my_cursor, log_file=log_file)

my_session.commit()
log_file.close()
my_session.close()

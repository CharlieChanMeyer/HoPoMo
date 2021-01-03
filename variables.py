####### Définitions des variables facteurs (Paramétrisation)
ELRbase0 = 1600
ERLstochrange = 0.02
SUPthreshold = 0.2
CELLShive0 = 250000
x1, x2, x3, x4, x5 = 385, 30, 36, 155, 30
LIFESPANegg = 3
LIFESPANlarva = 5
LIFESPANpupa = 12
MORTALITYeggs = 0.03
MORTALITYlarvae = 0.01
MORTALITYpupae = 0.001
CANNIBALISMhungerbase = [0.23, 0.3, 0.58, 0.06, 0] # for i in [1,2,...,5]
MORTALITYbase = 0.01
MORTALITYnursing = 0.005
MORTALITYprocessing = 0.005
MORTALITYforaging = 0.035
LOADpollenforager = 0.06
LOADnectarforager = 0.04
TURNSnectarforager = 15
TURNSpollenforager = 10
FACTORforagingsuccess = 0.8
FACTORminpollenforagers = 0.01
FACTORforagingmax = 0.33
FACTORothertasks = 0.2
ProcessorsPerCell = 2
FACTORpollenstorage = 6
FACTORpollensavingmax = 0.3
RATIOnectar_to_honey = 0.4 # 20/50
w_nectar = 0.43
w_pollen = 0.23
w_cellsbase = 0.037
w_honey = 0.5
w_egg = 0.0001
w_pupa = 0.16
w_adult = 0.1
w_larva = [0.0002,0.00059, 0.00331, 0.0644, 0.160] # for i in [1,...,5]
w_hivebase = 14000 #("14,000g")

####### VARIABLE INITIALE
INITpollen = 0
INITnectar = 0
INIThoney = 5000
INITBEESadult = 15000
INITCELLSbrood = 0
INITWEIGHTcolony = 50

####### Définitions des variables "inconnues" par lecture graphique approximative 
#Après série de test, les graphs semble cohérent avec ces paramètres
POLLENNEEDadult = 0.005 
POLLENNEEDnurse = 0.001 
NECTARNEEDactiveforager = 0.1 
NECTARNEEDadult = 0.1 
NECTARNEEDnurse = 0.2 
NEEDnurses_per_larva = [0.2,0.45,0.75,1.7,3] #REF p231 graph d
NEEDnurses_per_egg = 0.5
NEEDnurses_per_pupa = 0.5
MORTALITYadultbase = 0.01
NECTARNEEDlarva = [0.02,0.03,0.05,0.09,0.2] #REF p231 graph b
POLLENNEEDlarva = [0.001,0.003,0.006,0.013,0.027] #REF p231 graph b

####### Parameter swarming day
swd = 140


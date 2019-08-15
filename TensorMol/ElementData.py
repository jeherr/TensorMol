#
# This is a tentative set of atomic identity data.
# Anyone got an opinion about a better spot for this?
#

from __future__ import absolute_import
import numpy as np

AtomFields = ['symbol','name','atomicnum','mass','ns','np','nd','elecneg','radius','ione','elecaff','polariz']
AtomData = [['X','Nullium', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
['H','Hydrogen', 1.0, 1.00794, 1.0, 0.0, 0.0, 2.3, 53.0, 1312.0, 0.754195, 4.4923955],
['He','Helium', 2.0, 4.002602, 2.0, 0.0, 0.0, 4.16, 31.0, 2372.3, -0.52, 1.383191],
['Li','Lithium', 3.0, 6.941, 1.0, 0.0, 0.0, 0.912, 167.0, 520.2, 0.618049, 164.0],
['Be','Beryllium', 4.0, 9.012182, 2.0, 0.0, 0.0, 1.576, 112.0, 899.5, -0.52, 37.71],
['B','Boron', 5.0, 10.811, 2.0, 1.0, 0.0, 2.051, 87.0, 800.6, 0.279723, 20.53],
['C','Carbon', 6.0, 12.0107, 2.0, 2.0, 0.0, 2.544, 67.0, 1086.5, 1.2621226, 11.26],
['N','Nitrogen', 7.0, 14.0067, 2.0, 3.0, 0.0, 3.066, 56.0, 1402.3, -0.000725, 7.26],
['O','Oxygen', 8.0, 15.9994, 2.0, 4.0, 0.0, 3.61, 48.0, 1313.9, 1.4611136, 5.24],
['F','Fluorine', 9.0, 18.9984032, 2.0, 5.0, 0.0, 4.193, 42.0, 1681.0, 3.4011898, 3.7],
['Ne','Neon', 10.0, 20.1797, 2.0, 6.0, 0.0, 4.787, 38.0, 2081.0, -1.2, 2.67],
['Na','Sodium', 11.0, 22.98976928, 1.0, 0.0, 0.0, 0.869, 190.0, 496.0, 0.547926, 162.7],
['Mg','Magnesium', 12.0, 24.305, 2.0, 0.0, 0.0, 1.293, 145.0, 738.0, -0.415, 70.89],
['Al','Aluminum', 13.0, 26.9815386, 2.0, 1.0, 0.0, 1.613, 118.0, 578.0, 0.43283, 55.4],
['Si','Silicon', 14.0, 28.0855, 2.0, 2.0, 0.0, 1.916, 111.0, 787.0, 1.3895212, 37.31],
['P','Phosphorus', 15.0, 30.973762, 2.0, 3.0, 0.0, 2.253, 98.0, 1012.0, 0.746607, 24.93],
['S','Sulfur', 16.0, 32.065, 2.0, 4.0, 0.0, 2.589, 88.0, 1000.0, 2.0771042, 19.37],
['Cl','Chlorine', 17.0, 35.453, 2.0, 5.0, 0.0, 2.869, 79.0, 1251.0, 3.612724, 14.57],
['Ar','Argon', 18.0, 39.948, 2.0, 6.0, 0.0, 3.242, 71.0, 1521.0, -1.0, 11.07],
['K','Potassium', 19.0, 39.0983, 1.0, 0.0, 0.0, 0.734, 243.0, 419.0, 0.501459, 290.6],
['Ca','Calcium', 20.0, 40.078, 2.0, 0.0, 0.0, 1.034, 194.0, 590.0, 0.02455, 155.9],
['Sc','Scandium', 21.0, 44.955912, 2.0, 0.0, 1.0, 1.19, 184.0, 633.0, 0.188, 142.28],
['Ti','Titanium', 22.0, 47.867, 2.0, 0.0, 2.0, 1.38, 176.0, 659.0, 0.084, 114.34],
['V','Vanadium', 23.0, 50.9415, 2.0, 0.0, 3.0, 1.53, 171.0, 651.0, 0.52766, 97.34],
['Cr','Chromium', 24.0, 51.9961, 1.0, 0.0, 5.0, 1.65, 166.0, 653.0, 0.67584, 78.4],
['Mn','Manganese', 25.0, 54.938045, 2.0, 0.0, 5.0, 1.75, 161.0, 717.0, -0.52, 66.8],
['Fe','Iron', 26.0, 55.845, 2.0, 0.0, 6.0, 1.8, 156.0, 763.0, 0.153236, 62.65],
['Co','Cobalt', 27.0, 58.933195, 2.0, 0.0, 7.0, 1.84, 152.0, 760.0, 0.66226, 57.71],
['Ni','Nickel', 28.0, 58.6934, 2.0, 0.0, 8.0, 1.88, 149.0, 737.0, 1.15716, 51.1],
['Cu','Copper', 29.0, 63.546, 1.0, 0.0, 10.0, 1.85, 145.0, 746.0, 1.2357, 40.7],
['Zn','Zinc', 30.0, 65.38, 2.0, 0.0, 10.0, 1.59, 142.0, 906.0, -0.62, 38.8],
['Ga','Gallium', 31.0, 69.723, 2.0, 1.0, 10.0, 1.756, 136.0, 579.0, 0.43, 51.4],
['Ge','Germanium', 32.0, 72.64, 2.0, 2.0, 10.0, 1.994, 125.0, 762.0, 1.23676, 39.43],
['As','Arsenic', 33.0, 74.9216, 2.0, 3.0, 10.0, 2.211, 114.0, 947.0, 0.8048, 29.8],
['Se','Selenium', 34.0, 78.96, 2.0, 4.0, 10.0, 2.424, 103.0, 941.0, 2.0206047, 26.24],
['Br','Bromine', 35.0, 79.904, 2.0, 5.0, 10.0, 2.685, 94.0, 1139.9, 3.363588, 21.03],
['Kr','Krypton', 36.0, 83.798, 2.0, 6.0, 10.0, 2.966, 88.0, 1350.8, -0.62, 17.075],
['Rb','Rubidium', 37.0, 85.4678, 1.0, 0.0, 0.0, 0.706, 265.0, 403.0, 0.485916, 318.8],
['Sr','Strontium', 38.0, 87.62, 2.0, 0.0, 0.0, 0.963, 219.0, 549.5, 0.05206, 186.0],
['Y','Yttrium', 39.0, 88.90585, 2.0, 0.0, 1.0, 1.12, 212.0, 600.0, 0.307, 153.0],
['Zr','Zirconium', 40.0, 91.224, 2.0, 0.0, 2.0, 1.32, 206.0, 640.1, 0.4333, 121.0],
['Nb','Niobium', 41.0, 92.90638, 1.0, 0.0, 4.0, 1.41, 198.0, 652.1, 0.91740, 106.0],
['Mo','Molybdenum', 42.0, 95.96, 1.0, 0.0, 5.0, 1.47, 190.0, 684.3, 0.7473, 72.5],
['Tc','Technetium', 43.0, 98.0, 2.0, 0.0, 5.0, 1.51, 183.0, 702.0, 0.55, 80.4],
['Ru','Ruthenium', 44.0, 101.07, 1.0, 0.0, 7.0, 1.54, 178.0, 710.2, 1.04638, 65.0],
['Rh','Rhodium', 45.0, 102.9055, 1.0, 0.0, 8.0, 1.56, 173.0, 719.7, 1.14289, 58.0],
['Pd','Palladium', 46.0, 106.42, 0.0, 0.0, 10.0, 1.58, 169.0, 804.4, 0.56214, 32.0],
['Ag','Silver', 47.0, 107.8682, 1.0, 0.0, 10.0, 1.87, 165.0, 731.0, 1.30447, 52.5],
['Cd','Cadmium', 48.0, 112.411, 2.0, 0.0, 10.0, 1.52, 161.0, 867.8, -0.725, 46.9],
['In','Indium', 49.0, 114.818, 2.0, 1.0, 10.0, 1.656, 156.0, 558.3, 0.3, 68.7],
['Sn','Tin', 50.0, 118.71, 2.0, 2.0, 10.0, 1.824, 145.0, 708.6, 1.112070, 42.4],
['Sb','Antimony', 51.0, 121.76, 2.0, 3.0, 10.0, 1.984, 133.0, 834.0, 1.047401, 42.55],
['Te','Tellurium', 52.0, 127.6, 2.0, 4.0, 10.0, 2.158, 123.0, 869.3, 1.970875, 37.0],
['I','Iodine', 53.0, 126.90447, 2.0, 5.0, 10.0, 2.359, 115.0, 1008.4, 3.0590465, 34.6],
['Xe','Xenon', 54.0, 131.293, 2.0, 6.0, 10.0, 2.582, 108.0, 1170.4, -0.83, 27.815],
['Cs','Cesium', 55.0, 132.90545196, 1.0, 0.0, 0.0, 0.659, 298.0, 375.7, 0.471630, 401.0],
['Ba','Barium', 56.0, 137.327, 2.0, 0.0, 0.0, 0.881, 253.0, 502.9, 0.14462, 268.0],
['Lu','Lutetium', 71.0, 174.9668, 2.0, 0.0, 1.0, 1.09, 217.0, 523.5, 0.346, 148.0],
['Hf','Hafnium', 72.0, 178.49, 2.0, 0.0, 2.0, 1.16, 208.0, 658.5, 0.017, 109.0],
['Ta','Tantalum', 73.0, 180.94788, 2.0, 0.0, 3.0, 1.34, 200.0, 761.0, 0.323, 88.0],
['W','Tungsten', 74.0, 183.84, 2.0, 0.0, 4.0, 1.47, 193.0, 770.0, 0.81626, 75.0],
['Re','Rhenium', 75.0, 186.207, 2.0, 0.0, 5.0, 1.60, 188.0, 760.0, 0.060396, 65.0],
['Os','Osmium', 76.0, 190.23, 2.0, 0.0, 6.0, 1.65, 185.0, 840.0, 1.1, 57.0],
['Ir','Iridium', 77.0, 192.217, 2.0, 0.0, 7.0, 1.68, 180.0, 880.0, 1.56436, 51.0],
['Pt','Platinum', 78.0, 195.084, 1.0, 0.0, 9.0, 1.72, 177.0, 870.0, 2.12510, 44.0],
['Au','Gold', 79.0, 196.966569, 1.0, 0.0, 10.0, 1.92, 174.0, 890.1, 2.308610, 36.1],
['Hg','Mercury', 80.0, 200.592, 2.0, 0.0, 10.0, 1.76, 171.0, 1007.1, -0.52, 34.15],
['Tl','Thallium', 81.0, 204.382, 2.0, 1.0, 10.0, 1.789, 156.0, 589.4, 0.377, 52.3],
['Pb','Lead', 82.0, 207.2, 2.0, 2.0, 10.0, 1.854, 154.0, 715.6, 0.356743, 46.96],
['Bi','Bismuth', 83.0, 208.98040, 2.0, 3.0, 10.0, 2.01, 143.0, 703.0, 0.942362, 50.0]]

atoi = {sym:an for (sym,an) in [(x[0],int(x[2])) for x in AtomData]}
itoa = {an:sym for (sym,an) in [(x[0],int(x[2])) for x in AtomData]}
def AtomicNumber(Symb):
	try:
		return atoi[Symb]
	except Exception as Ex:
		raise Exception("Unknown Atom")
	return 0
def AtomicSymbol(number):
	try:
		return itoa[number]
	except Exception as Ex:
		raise Exception("Unknown Atom")
	return 0


def ReadAtomCodeString():
	tmp = []
	for line in ATOMCODELINES.split('\n'):
		tmp.append(list(map(float,line.split(" "))))
	return np.array(tmp)
#ELEMENTCODES = ReadAtomCodeString()
ELEMENTCODES = np.array([[ 0.00000000, 0.00000000, 0.00000000, 0.00000000],
 [-0.36692033, 1.04046142, 0.02580811,-1.12459213],
 [-1.17544310, 2.10155991,-0.16349854, 0.15236642],
 [-0.26468585,-1.32148294, 0.23793422,-0.90989965],
 [-0.76192498,-0.10880161,-0.52418634, 0.53806060],
 [-0.60880640, 0.37563686,-0.70667835, 0.48159885],
 [-0.13983438, 0.82819340,-0.50433149, 0.35255710],
 [-0.63622809, 1.27839120,-0.60050589, 0.51749279],
 [-0.22140335, 1.36488596,-0.35328700, 0.45160462],
 [ 0.39218243, 1.80761458, 0.27345513,-0.09654261],
 [-1.24291191, 1.99047820,-0.59396003, 1.14034548],
 [-0.02648899,-1.44251370, 0.54291518,-0.96379444],
 [-0.59012367,-0.91730780,-0.56601951, 0.59188414],
 [-0.38478455,-0.44871968,-0.50900899, 0.40418466],
 [ 0.05328652, 0.23477859,-0.26191422, 0.40368815],
 [-0.18393185, 0.68167569,-0.37546470, 0.52667162],
 [ 0.48846389, 1.05184594,-0.01993939, 0.33959963],
 [ 0.86630927, 1.39620832, 0.54025307,-0.25443531],
 [-1.00299564, 1.76087677,-0.54277870, 1.37693205],
 [ 0.07866484,-1.69045910, 1.08982946,-0.82995289],
 [-0.23979013,-1.50916090,-0.11841062, 0.45925854],
 [-0.16881587,-1.34517134,-0.13996095, 0.39549192],
 [-0.23079699,-1.26922649,-0.35115835, 0.62743906],
 [ 0.02875169,-1.14002765,-0.31680403, 0.42990417],
 [ 0.09415013,-0.98593191, 0.24079536,-1.02284055],
 [-0.61747451,-0.95191636,-0.68863684, 1.08796644],
 [-0.21331827,-0.89146272,-0.50523728, 0.86707594],
 [ 0.19469208,-0.81057006,-0.37727183, 0.72585305],
 [ 0.37374592,-0.71159614,-0.32143524, 0.47711705],
 [ 0.33350733,-0.33174160, 0.12287428,-1.10000563],
 [-0.36624295,-0.16064743,-0.94014230, 1.11085571],
 [ 0.12338038,-0.50866443,-0.48903437, 0.92138844],
 [ 0.65240528, 0.13407737,-0.38350747, 0.62769279],
 [ 0.41983944, 0.55262742,-0.61579357, 0.77609730],
 [ 0.79632552, 0.98973879,-0.22425551, 0.38082681],
 [ 0.92691224, 1.04197528, 0.31184173, 0.09278129],
 [-0.40862446, 1.16088549,-0.91535076, 1.54538900],
 [ 0.15339622,-1.61507630, 1.29950731,-0.84740150],
 [-0.23566970,-1.38083261, 0.13502276, 0.46141261],
 [-0.09418296,-1.30760258, 0.05765451, 0.41158249],
 [ 0.02749385,-1.20229050,-0.05946386, 0.44595832],
 [ 0.33206215,-1.08694535, 0.42785824,-1.16029961],
 [ 0.29669297,-0.80483785, 0.30918388,-1.13331716],
 [ 0.21094019,-0.78711377,-0.32131427, 0.28133597],
 [ 0.48983907,-0.61521347, 0.30619372,-1.20695156],
 [ 0.53611579,-0.48666715, 0.31122971,-1.21428027],
 [ 0.36503790,-0.09221583, 0.57123687,-1.51496318],
 [ 0.55414296,-0.36537389, 0.22322466,-1.13311883],
 [-0.03791524,-0.08187290,-0.73911051, 0.61015779],
 [ 0.29341768,-0.19362820,-0.40275498, 0.45294985],
 [ 0.62793230, 0.59489150,-0.28177015, 0.14615516],
 [ 0.61970629, 0.87476446,-0.37568990, 0.22273577],
 [ 0.92542217, 1.17163272,-0.02235719,-0.07609650],
 [ 1.14820560, 1.32619854, 0.23661147,-0.50749876],
 [-0.34942323, 1.17553673,-0.86947573, 1.19181219]],dtype=np.float64)

ELEMENTCODES3 = np.array([[ 0.00000000,  0.00000000,  0.00000000],
[ 0.54503504, -0.58790961,  1.13472599],
[ 0.49498670, -1.50471363, -0.45032393],
[ 0.34544460,  1.08643739,  1.64153302],
[ 0.02815721, -0.98418217,  0.31839056],
[-0.25585028, -0.73541069,  0.53094526],
[-0.13327620, -0.84081555,  0.53063329],
[-0.10768406, -1.18246092,  0.80940919],
[-0.28850318, -0.98334907,  0.89868061],
[-0.11811683, -0.91777281,  0.73348282],
[ 0.17141154, -1.19676166,  0.60681170],
[ 0.21338074,  1.03561627,  1.58545165],
[-0.07473498, -0.65137304,  0.32861959],
[-0.46782751,  0.01916748,  0.58378658],
[-0.13509699, -0.10476134,  0.61322983],
[-0.07579338, -0.68132130,  0.94957010],
[-0.23639414, -0.08090801,  1.01063572],
[-0.37505753, -0.04361362,  0.93134489],
[ 0.02648481, -0.86314324,  1.32545023],
[ 0.13226140,  1.46751393,  1.45973520],
[-0.16753976,  0.25848224,  0.36928094],
[-0.21459061,  0.18164552,  0.14425506],
[-0.31456303, -0.12343208, -0.03271151],
[-0.44736269, -0.11309971, -0.32733164],
[ 0.05451204,  0.47392377,  0.84442676],
[-0.32754512, -0.57432446, -0.39011331],
[-0.32794590, -0.58342403, -0.58274900],
[-0.35269396, -0.45088961, -0.70369965],
[-0.31720610, -0.40620421, -0.67339764],
[ 0.04270090,  0.15513308,  0.41647090],
[-0.02835019, -0.93780107, -0.65041152],
[-0.56591509, -0.07513987, -0.56488931],
[-0.40205001,  0.03523371, -0.27660902],
[-0.45330783, -0.16205921,  0.06282289],
[-0.42528499,  0.18695898,  0.32048265],
[-0.34119493,  0.12227882,  0.50017255],
[-0.24798171, -0.53072417,  1.10009185],
[ 0.01600097,  1.60263183,  1.41413088],
[-0.35920139,  0.66851941,  0.20951987],
[-0.43686220,  0.47824505, -0.01640691],
[-0.56355451,  0.22984838, -0.27422186],
[-0.11480191,  0.75410426,  0.69760381],
[-0.10369357,  0.48699169,  0.53258588],
[-0.70376457,  0.00494375, -0.54833734],
[ 0.00034745,  0.53469227,  0.38288394],
[ 0.02136009,  0.52297795,  0.32140540],
[ 0.50920265,  0.57660501,  1.00014530],
[-0.15722945,  0.50279027,  0.16299042],
[-0.56795361, -0.59993513, -0.73460910],
[-0.91515656,  0.25931446, -0.50028062],
[-0.80506370,  0.25818456, -0.39760280],
[-0.68654137,  0.26787079, -0.06730019],
[-0.71121556,  0.46811478,  0.09342037],
[-0.70590287,  0.45189995,  0.15530242],
[-0.35728880, -0.31119433,  0.78115336]],dtype=np.float64)

ELEMENTCODES6= np.array([
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000],
[-0.11941919,  1.66981229, -0.34078133,  3.07054603,  0.02805921,  1.39920098],
[-1.22523230,  0.87273110, -1.53652129,  3.06183707, -0.42268029,  1.15310964],
[-1.08144024,  0.36881344,  0.51654715,  1.19690060,  1.96353767,  0.76873811],
[-1.48361943,  1.46319443, -0.36683392,  1.09550549,  1.53600656,  0.35843163],
[-1.28282031,  1.44948855, -0.18620608,  1.47348346,  0.88606995,  0.30806226],
[-1.32602464,  1.29334867, -0.48786704,  1.94155212,  0.12416053,  0.35994118],
[-1.24627748,  0.85176992, -0.86048699,  2.07662325, -0.32963371,  0.67388868],
[-1.26197000,  0.52469700, -0.77799536,  2.23070478, -1.07025594,  0.75675877],
[-1.44555641,  0.14201532, -1.02444457,  2.31127814, -1.35007258,  0.75662509],
[-1.07409059, -0.75848375, -1.23234814,  1.91492439, -1.17689240,  1.42592260],
[-0.89174750,  0.04866856,  0.69632391,  0.54834641,  1.82084858,  0.71265217],
[-1.40926497,  0.96637200,  0.01948199,  0.21756316,  1.78647874,  0.06625974],
[-1.22867459,  0.94889604,  0.21322550,  0.37090578,  1.19632899,  0.02584965],
[-1.31696296,  0.94352216,  0.34373420,  0.85461569,  0.73722552, -0.02207823],
[-1.26800514,  0.72245921,  0.18126118,  1.03435144,  0.18100415,  0.24566097],
[-1.33957939,  0.44617381,  0.36737751,  1.23793216, -0.70774286,  0.24559946],
[-1.45739180,  0.18906758,  0.11855672,  1.44431478, -1.06015369,  0.27184731],
[-1.07034783, -0.73747370, -0.49106563,  0.90635500, -0.91970411,  0.90417849],
[-1.05082894, -0.96993987,  0.34818567, -0.60255502,  2.08274706,  0.46502396],
[-1.38112443,  0.25809336,  0.17876422, -0.86303816,  2.08446436, -0.29648057],
[-1.32953139,  0.31621456,  0.04980333, -0.77242287,  1.81703866, -0.38247993],
[-1.22285161,  0.36523514, -0.03902504, -0.68072438,  1.56369304, -0.33404530],
[-1.12424562,  0.52599123, -0.08785047, -0.56058980,  1.28007601, -0.46706335],
[ 0.82452399,  0.07000171,  0.69663644,  0.47994512,  0.38088827,  0.77255935],
[-0.67139874,  0.28889090, -0.57186355, -0.73534654,  0.63821079, -0.15108892],
[-0.69769452,  0.45421013, -0.55131923, -0.51601097,  0.33346457, -0.44930740],
[-0.57831174,  0.50699971, -0.53749858, -0.46609951,  0.10330152, -0.67344622],
[-0.51582172,  0.58198002, -0.36257679, -0.42741363, -0.03784290, -0.78027978],
[ 1.47651859,  0.08767746,  0.50529571,  0.44078370, -0.85766235,  0.49140343],
[-0.36527786,  0.33677277, -0.68117395, -0.68922989, -0.31267565, -0.60739562],
[ 0.13536733,  0.04911647, -0.28155821, -0.81738167, -0.78655357, -0.72640802],
[ 0.05418953,  0.02538001, -0.16096230, -0.45016164, -1.20167957, -0.80317889],
[-0.14845072, -0.39336528, -0.30053651, -0.36256235, -1.32479994, -0.48837978],
[-0.01317050, -0.44180772,  0.16161190, -0.16295739, -1.42129365, -0.69127442],
[-0.54807180, -0.35482947,  0.21304333,  0.23918110, -1.46101066, -0.58201421],
[ 0.00987678, -1.11316377, -0.12258884, -0.34097611, -1.50414648,  0.29373636],
[-0.45816513, -1.40104706,  0.28408371, -1.36838131,  1.70132990,  0.26153434],
[-0.93344833, -0.66151015,  0.16332018, -1.45454317,  1.66092869, -0.69774224],
[-0.80301444, -0.53567771,  0.26829590, -1.43255520,  1.37281557, -0.81163049],
[-0.56221300, -0.48905773,  0.34678205, -1.41494204,  1.05299410, -0.86323493],
[ 1.40551689, -0.82275222,  0.96655743, -1.05721223,  0.12534844,  0.17536111],
[ 1.66921535, -0.72419677,  0.97691002, -0.99485472, -0.19193264,  0.26234157],
[ 0.12255616, -0.50950482,  0.08816805, -1.41779258,  0.25406344, -0.89868639],
[ 1.95097505, -0.79510863,  0.80839689, -0.89902946, -0.76678460,  0.19859921],
[ 2.06269453, -0.77025854,  0.74063848, -0.86592198, -0.90989472,  0.14700808],
[ 3.38341300, -0.92921276,  1.23238821,  0.11407094, -1.19440889,  1.12355939],
[ 2.33947754, -0.78862141,  0.46005261, -0.76805435, -1.17741500,  0.10740355],
[ 0.81778547, -0.92866698, -0.61667271, -1.42956137, -0.91914703, -0.78753132],
[ 1.11011003, -1.12882849, -0.21861259, -1.47483145, -1.11245106, -0.97030831],
[ 0.97747886, -1.00757022,  0.15639726, -1.38686250, -1.32278989, -1.09184710],
[ 0.89588423, -1.08787452,  0.08730448, -1.33624534, -1.42822180, -0.97174486],
[ 0.89734094, -0.98847328,  0.34129403, -1.26888969, -1.47359725, -1.12649551],
[ 0.64245285, -0.82784346,  0.53033982, -1.08988835, -1.48541206, -1.18831787],
[ 0.84743619, -1.40274205,  0.05205911, -1.25776575, -1.57183589,  0.11982884]], dtype=np.float64)



ELEMENTCODES2 =  np.array([[ 0.00000000,  0.00000000],
       [ 0.71085673, -0.79332923],
       [ 2.39953519, -1.56964986],
       [-1.17713528,  1.36482797],
       [ 1.34008862, -0.60448391],
       [ 1.38737123, -0.63269106],
       [ 1.53413748, -0.83511535],
       [ 2.34582444, -1.26787597],
       [ 1.95975616, -1.11866275],
       [ 1.98890529, -0.88657389],
       [ 3.47623612, -1.47465154],
       [-1.34615838,  1.65369806],
       [ 0.56994397,  0.05374043],
       [ 0.65207368,  0.27225887],
       [ 0.88499258,  0.17814247],
       [ 1.47613349, -0.39817571],
       [ 1.26176347, -0.12885618],
       [ 1.36800652,  0.14383224],
       [ 2.75012878, -1.14117720],
       [-1.58153715,  1.88298295],
       [-0.78249905,  0.85275507],
       [-0.64256401,  0.67557254],
       [-0.44155386,  0.37618481],
       [-0.53200742,  0.30814481],
       [-1.33551468,  0.73584646],
       [-0.07830985, -0.80833103],
       [-0.26160306, -0.81153918],
       [-0.38610374, -0.81911574],
       [-0.47745947, -0.75275485],
       [-1.37188670,  0.10333268],
       [-0.08959502, -1.08403003],
       [-0.50407450, -0.80669604],
       [ 0.01611934, -0.78175725],
       [ 0.50574058, -0.90369427],
       [ 0.48760115, -0.65692061],
       [ 0.50445794, -0.20205941],
       [ 1.65384507, -1.17681867],
       [-1.64554688,  2.15769673],
       [-1.21322386,  1.16337940],
       [-1.16111218,  1.00945238],
       [-1.10644870,  0.78482784],
       [-1.54963987,  1.31288998],
       [-1.52175151,  1.05904169],
       [-1.08322473,  0.35191339],
       [-1.52161122,  0.82160009],
       [-1.52857659,  0.67603078],
       [-1.63069537,  0.83893412],
       [-1.53088048,  0.30838808],
       [-0.73411122, -0.61012901],
       [-1.05368871, -0.12618754],
       [-0.85908161,  0.06718419],
       [-0.60069441,  0.02237130],
       [-0.56342308,  0.20486819],
       [-0.44261576,  0.28199300],
       [ 0.64107443, -0.70189783]], dtype=np.float64)

ELEMENT_CODES2 = np.array([[ 0.00000000,  0.00000000],
		[5.5182376, 0.75741386],
		[12.989592, -0.0328572],
		[-6.991251, -0.8788967],
		[0.48788768, 0.05988966],
		[1.6732875, -0.48146194],
		[3.687188, -1.1813266],
		[6.105563, -0.21926637],
		[7.320023, -1.8572379],
		[14.339844, -4.7674365],
		[14.563954, -7.3427587],
		[-6.743684, -1.4147816],
		[0.4971933, -0.35540056],
		[1.158971, -0.626655],
		[1.8930136, -1.3232611],
		[3.2053733, -1.6808133],
		[3.4792695, -2.4893658],
		[4.6130905, -5.0699444],
		[8.082435, -4.929978],
		[-10.476722, -2.4531298],
		[-6.116904, -2.0689394],
		[-5.376958, -2.0249956],
		[-4.515292, -1.9711212],
		[-3.5547879, -2.137192],
		[-1.2092505, -1.8508813],
		[-2.110009, -1.7932681],
		[0.47312582, -0.9724194],
		[0.7193984, -1.1344361],
		[0.14216375, -1.5639048],
		[-0.3309995, -1.9958937],
		[0.47803196, -1.7428908],
		[0.14953683, -2.809793],
		[1.5394602, -2.5617726],
		[1.6365567, -3.7310448],
		[2.2447143, -4.957342],
		[5.3240347, -10.120497],
		[6.5203476, -16.627775],
		[-11.846228, -3.6285458],
		[-7.438974, -3.3411343],
		[-6.0673504, -3.413674],
		[-4.8856087, -3.4588053],
		[-1.8935322, -3.4116118],
		[-1.7030648, -4.10565],
		[-3.3521378, -4.130525],
		[-1.8304689, -5.2245317],
		[-1.8800075, -5.707389],
		[-1.245935, -5.1824293],
		[-0.80342084, -6.0175066],
		[-3.5095222, -6.4054155],
		[0.16761307, -5.266091],
		[1.3129086, -5.903992],
		[1.7627504, -5.6283283],
		[2.4881933, -6.37519],
		[4.745271, -10.784818],
		[4.43119, -15.5599375],
		[-18.122364, -5.9345183],
		[-11.620712, -5.204393],
		[-10.079584, -6.7038846],
		[-8.209142, -6.6033816],
		[-7.7836843, -7.4592752],
		[-8.275529, -8.971534],
		[-9.411714, -9.327853],
		[-8.274366, -10.86517],
		[-4.4321456, -13.122757],
		[-3.2879798, -13.687775],
		[-2.68543, -14.3160305],
		[-7.6964874, -13.270931],
		[-1.7991023, -16.269772],
		[-0.71300733, -17.802244],
		[0.0994991, -18.003664]], dtype=np.float64)

ELEMENT_CODES4 = np.array([[ 0.00000000, 0.00000000, 0.00000000,  0.00000000],
		[-2.5513804, -5.7592616, -1.570019, 0.9597991],
		[-6.5345106, -3.9986, -3.7074566, -2.3658702],
		[4.8333983, -6.2240086, -1.249202, 2.0486069],
		[0.4186223, -6.4531493, -4.4682946, 1.8849711],
		[-0.15123788, -5.800419, -3.2940047, 1.1801078],
		[-1.6375434, -5.0062633, -1.9952934, 0.09541747],
		[-2.6509132, -4.8054466, -2.034238, -0.29223832],
		[-2.7602823, -3.929046, -2.438075, -1.407692],
		[-2.9046147, -2.915192, -2.8870792, -2.6655185],
		[-6.717644, -2.0450015, -4.569536, -4.7079797],
		[7.8395, -6.936753, -1.7457044, 2.894855],
		[2.0202854, -7.6684084, -3.818847, 0.70305276],
		[1.1409408, -5.037931, -2.8132944, 0.47489643],
		[0.5356181, -6.216391, -3.0519676, -0.158249],
		[-0.1490499, -4.4558043, -3.7785914, 0.43537363],
		[-0.30983448, -4.256329, -2.8944316, -0.51772],
		[-0.41789976, -3.4629006, -2.7958343, -1.5882387],
		[-3.0685222, -1.2776725, -3.5703053, -4.6152663],
		[7.193855, -7.6691976, 0.12255091, -0.42516446],
		[6.2503614, -7.6132236, -3.0708182, 0.9849971],
		[4.856036, -6.2476296, -3.094816, 1.3026085],
		[3.4549632, -4.974286, -3.0995164, 1.3669995],
		[3.4353325, -4.2819266, -3.1526618, 1.3151109],
		[3.5385675, -2.9535408, -3.0437193, 2.0817711],
		[2.3185253, -4.131144, -3.7341363, 1.2516202],
		[2.2928872, -3.5851743, -3.8784347, 0.9306658],
		[2.189301, -2.4109309, -4.183955, 0.39043185],
		[2.1007168, -1.7268834, -4.7283397, 0.7649392],
		[1.9699631, -0.20511246, -5.9426737, 1.8239678],
		[3.3188124, -2.4396393, -7.4300914, 0.2110966],
		[2.1510346, -1.6788414, -4.224724, -0.16901238],
		[1.5373038, -1.2211224, -5.2692485, -0.027606336],
		[1.4919189, -2.3792672, -6.103144, -0.6932203],
		[0.74700624, -1.7150668, -4.8752184, -0.87878937],
		[0.043626294, -1.5817119, -4.5046287, -1.6363539],
		[-0.73498917, 1.1539364, -5.798006, -5.0569677],
		[7.8886905, -6.6397185, 0.5447978, -1.1868057],
		[6.7827973, -6.5068374, -2.2858627, -1.3052325],
		[6.3289514, -5.159576, -2.5104373, -0.37375],
		[6.126114, -4.421404, -2.9824169, 0.2491598],
		[6.0238175, -2.3379898, -2.8541102, 1.5343702],
		[4.908068, -0.8018897, -3.6160288, 1.3200582],
		[4.410344, -2.3260436, -3.815118, 0.29119706],
		[3.6250403, 0.090955615, -4.029447, 1.0440168],
		[3.2576375, 0.2631651, -4.2128134, 1.0686506],
		[2.9761908, 1.5848755, -5.985635, 3.0179186],
		[2.849603, 0.81420475, -4.84298, 1.0887735],
		[3.9495804, -1.3493524, -7.1853623, -0.41072518],
		[2.5785937, -1.062681, -3.946417, -0.712771],
		[2.2148595, -0.05350085, -4.8197865, -0.7984139],
		[2.434557, -2.326516, -4.7613482, -2.3392107],
		[2.3947463, -0.9634739, -5.3536787, -3.7211952],
		[1.4822152, -0.22049338, -5.5291495, -4.9492083],
		[0.8468896, 2.3932886, -6.90869, -7.023838],
		[9.346741, -7.415296, 2.2813776, -3.3387027],
		[8.314072, -7.4214783, -1.6558774, -3.8060603],
		[8.014477, -3.045358, -2.7494197, -2.6347556],
		[7.20436, -2.4130063, -3.817134, -2.4804966],
		[6.4285126, -1.4230547, -4.279484, -1.7311608],
		[7.0993123, -0.65722454, -4.505959, -2.0563915],
		[7.172266, 1.0047804, -5.3870664, -4.0892243],
		[7.4730906, 2.3568654, -5.492267, -3.8459082],
		[7.457717, 2.9055762, -5.7015367, -3.6160223],
		[6.4028955, 5.323797, -7.3247213, -2.356566],
		[6.0816326, 5.6498637, -7.9215975, -2.1431234],
		[6.001079, 2.5042822, -8.102415, -3.8793695],
		[5.222268, 3.1952038, -5.6475205, -4.695193],
		[4.7440853, 2.7182384, -6.2739787, -4.8635745],
		[4.289927, 3.443812, -5.8423595, -5.493875]], dtype=np.float64)

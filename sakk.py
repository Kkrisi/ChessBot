

import chess
import tkinter as tk
import cv2 as cv
import numpy as np
from PIL import ImageGrab
import time
import os




def KepernyoKeszites():

	global formatted_timestamp
	
	save_folder = r'C:\Users\kadar\OneDrive\Desktop\programozas\sakk'

	screenshot = ImageGrab.grab()

	current_struct_time = time.gmtime(time.time())
	day = current_struct_time.tm_mday
	hour = current_struct_time.tm_hour
	minute = current_struct_time.tm_min

	formatted_timestamp = time.strftime('%d_%H_%M', current_struct_time)

	filename = f'screenshot_{formatted_timestamp}.png'

	screenshot.save(os.path.join(save_folder, filename))



	





def FiguraFelismeres(figura, threshold, readMethod1, readMethod2):
	haystack_img = cv.imread(f'screenshot_{formatted_timestamp}.png', readMethod1)
	needle_img = cv.imread(f'{figura}', readMethod2)

	# TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
	result = cv.matchTemplate(haystack_img, needle_img, cv.TM_SQDIFF_NORMED)

	global locations

	locations = np.where(result <= threshold)
	locations = list(zip(*locations[::-1]))

	
	if locations:
		print(f'Found needle: {figura}')


		needle_w = needle_img.shape[1]
		needle_h = needle_img.shape[0]
		line_color = (0, 255, 0)
		line_type = cv.LINE_4

		for loc in locations:
			top_left = loc
			bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
			cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)

		#cv.imshow('Matches', result)
		#cv.waitKey()
		#cv.imshow('Matches', haystack_img)
		#cv.waitKey()
	else:
	    print(f'Needle not found: {figura}')

	






def Elhelyezkedes():

	a_column = [(293, 833), (288, 739), (291, 643), (295, 553), (289, 453), (296, 369), (297, 277), (292, 168)]
		# 			a1			a2			a3			a4			a5			a6			a7			a8
	b_column = [(382, 829), (386, 735), (390, 638), (384, 548), (480, 459), (383, 362), (383, 266), (389, 175)]
		#			b1			b2			b3			b4			b5			b6			b7			b8		
	c_column = [(480, 833), (476, 731), (473, 633), (474, 541), (476, 452), (476, 357), (475, 260), (473, 162)]		
		#			c1			c2			c3			c4			c5			c6			c7			c8
	d_column = [(578, 834), (570, 729), (570, 639), (569, 541), (566, 451), (569, 356), (571, 266), (568, 161)]		
		#			d1			d2			d3			d4			d5			d6			d7			d8

	chessboard = [
	    a_column,
	    b_column,
	    c_column,
	    d_column
	]


	print(f"\nTablaKoardinatak: {TablaKoardinatak} \n")

	
	babuSzamlalo = 0
	eltaroltSzam = 0
	pozicioLista = []
	SorSzamLista = []


	for babu in TablaKoardinatak:
		legkisebbKulonbseg = 600
		for column in chessboard:
			SorSzam = 0
			for number in column:
				ertek1 = abs(babu[0] - number[0])
				ertek2 = abs(babu[1] - number[1])
				if ertek1 + ertek2 < legkisebbKulonbseg:
					legkisebbKulonbseg = ertek1 + ertek2
					eltaroltSzam = number[0]

				SorSzam += 1


			for i in range(len(column)):
				if eltaroltSzam in column[i]:
					print(f"column[1]: {column[i]}, index: {column.index(column[i])+1}")


		if any(x[0] == eltaroltSzam for x in a_column):
			pozicioLista.append('A' + str())
		elif any(x[0] == eltaroltSzam for x in b_column):
			pozicioLista.append('B' + str())
		elif any(x[0] == eltaroltSzam for x in c_column):
			pozicioLista.append('C' + str())
		elif any(x[0] == eltaroltSzam for x in d_column):
			pozicioLista.append('D' + str())



		babuSzamlalo += 1
		print("babuSzamlalo:-----------------",babuSzamlalo)
		print("pozicioLista:",pozicioLista)








# SakkBot indítása!

KepernyoKeszites()

idoReszek = formatted_timestamp.split("_")
ora = int(idoReszek[1])

if ora < 15:
	print("nappali")
	Figurak = [	
		# Nappali
	    ('white_king.png', 0.2, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
		('white_queen.png', 0.2, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('white_bishop.png', 0.2, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('white_knight.png', 0.2, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('white_rook.png', 0.2, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('white_pawn.png', 0.2, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),


	    ('black_king.png', 0.2, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('black_queen.png', 0.2, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('black_bishop.png', 0.2, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('black_knight.png', 0.2, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('black_rook.png', 0.2, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('black_pawn.png', 0.2, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE)
	]

else:
	Figurak = [
		# Esti
		('white_king.png', 0.3, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
		('white_queen.png', 0.3, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('white_bishop.png', 0.28, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('white_knight.png', 0.3, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('white_rook.png', 0.28, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('white_pawn.png', 0.3, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),


	    ('black_king.png', 0.3, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('black_queen.png', 0.34, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('black_bishop.png', 0.3, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('black_knight.png', 0.3, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('black_rook.png', 0.34, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE),
	    ('black_pawn.png', 0.3, cv.COLOR_BGR2GRAY, cv.IMREAD_GRAYSCALE)
	]

TablaKoardinatak = []

for figura, threshold, readMethod1, readMethod2 in Figurak:
	FiguraFelismeres(figura, threshold, readMethod1, readMethod1)
	for location in locations:
		if not (locations[:1]):	# ha a lista üres akkor pass
			pass
		else:
			if (locations[:1])[0] not in TablaKoardinatak: 
				TablaKoardinatak.append((locations[:1])[0])


Elhelyezkedes()







def LepesKalkulalas(negyzet, figuranev, szin):

	board = chess.Board()

	#Position the pieces: Use the set_piece() method to place pieces on the board
	#board.set_piece(chess.A3, chess.King(chess.WHITE))
	board.set_piece(chess.negyzet, chess.figuranev(chess.szin))


	print(board)

	#Use an engine like Stockfish to calculate the best next moves.
	engine = chess.engine.StockfishEngine()

 	#A higher depth will result in more accurate but slower calculations.
	engine.depth = 10

	#Analyze the board position
	moves = engine.analyze(board)

	#Print the best next moves:
	for move in moves:
	    print(move)




#def LezerPont():







# MEGOLDANDO PROBLEMAK::::

	# képernyőkepeket kulon mappábol olvassa, és mindig torolje ha tobb van mint 3 az elso 2-t

	# A tábla betűk és számok pl A2, C3 változnak attol fuggoen hogy melyik színnel vagy, EZT IS KELL FIGYELNI!

	# Különböző színek a különböző figurák felismeréséhez? tűzpiros, világoskék, ibolyalila 










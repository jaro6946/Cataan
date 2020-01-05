
from graphics import *
from random import *
import math
import time

 

class Geom(object):
	
	def __init__(self, inscibedDiameter, window):

		self.iR=inscibedDiameter/2 #iR = Inscribed Radius

		self.hexSide=math.tan(math.radians(30))*self.iR #hexSide is one side of the hexagon divided by two
		self.cR=math.sqrt(math.pow(self.hexSide, 2)+pow(self.iR, 2)) # Circumscribed radius
		self.window=window
		self.yOffset=math.sqrt(-math.pow(self.iR,2)+math.pow(2*self.hexSide,2))		#sqrt=iR^2-(hexSide*2)^2


		self.nodes= {1 : [2, 9],
				2 : [1, 3],
				3 : [2, 11, 4],
				4 : [3, 5],
				5 : [4, 6, 13],
				6 : [5, 7],
				7 : [6, 15],
				8 : [18, 9],
				9 : [1, 8 ,10],
				10: [9, 11, 20],
				11: [10,12,3],
				12: [11, 13, 22],
				13: [5, 12, 14],
				14: [13, 15, 24],
				15: [14, 16, 7],
				16: [15, 26],
				17: [28, 18],
				18: [17,19, 8],
				19: [18, 20, 30],
				20: [10, 19, 21],
				21: [20, 22, 31],
				22: [21, 12, 23],
				23: [22, 24, 33],
				24: [14, 23, 25],
				25: [35, 24, 26],
				26: [16, 25, 27],
				27: [26, 37],
				28: [17, 29],
				29: [38, 28, 30],
				30: [19, 29, 31],
				31: [21, 30, 32],
				32: [42, 31, 33],
				33: [23, 32, 34],
				34: [44, 33, 35],
				35: [34, 36, 25],
				36: [46, 35, 37],
				37: [36, 27],
				38: [29, 39],
				39: [47, 38, 39],
				40: [31, 39, 41],
				41: [49, 40, 42],
				42: [32, 41, 43],
				43: [51, 42,44],
				44: [34, 43, 45],
				45: [53, 44, 46],
				46: [36, 45],
				47: [39, 48],
				48: [47, 49],
				49: [41, 48,50],
				50: [49, 51],
				51: [43, 50, 52],
				52: [51, 53],
				53: [45, 52]
				}

		a=((1, 'Desert'),)

		locations=(list(itertools.product(range(1,5),['Field']))+
				list(itertools.product(range(1,5),['Pasture']))+
				list(itertools.product(range(1,5),['Forest']))+
				list(itertools.product(range(1,4),['Mounain']))+
				list(itertools.product(range(1,4),['Hills'])))

		chits=(list(itertools.product(range(1,2),['1']))+
			list(itertools.product(range(1,3),['2']))+
			list(itertools.product(range(1,3),['3']))+
			list(itertools.product(range(1,3),['4']))+
			list(itertools.product(range(1,3),['5']))+
			list(itertools.product(range(1,3),['6']))+
			list(itertools.product(range(1,3),['7']))+
			list(itertools.product(range(1,3),['8']))+
			list(itertools.product(range(1,3),['9']))+
			list(itertools.product(range(1,3),['10']))+
			list(itertools.product(range(1,3),['11']))+
			list(itertools.product(range(1,2),['12'])))

		shuffle(chits)
		shuffle(locations)

	def drw (self, centerLoc, tileType):

		pt1=Point(centerLoc[0], centerLoc[1]+self.cR)
		pt2=Point(centerLoc[0]+self.iR, centerLoc[1]+self.hexSide)
		pt3=Point(centerLoc[0]+self.iR, centerLoc[1]-self.hexSide)
		pt4=Point(centerLoc[0], centerLoc[1]-self.cR)
		pt6=Point(centerLoc[0]-self.iR, centerLoc[1]+self.hexSide)
		pt5=Point(centerLoc[0]-self.iR, centerLoc[1]-self.hexSide)

		vertices=[pt1, pt2, pt3, pt4, pt5, pt6]

		hexa=Polygon(vertices)

		if tileType=='brick':
			hexa.setFill('red')
		elif tileType=='sheep':
			hexa.setFill('green')
		elif tileType=='wheat':
			hexa.setFill('tan')
		elif tileType=='stone':
			hexa.setFill('gray')
		elif tileType=='wood':
			hexa.setFill('brown')

		hexa.draw(self.window)

	
	def hexRow(self,startingLoc,num):
		

		for i in range(num):
			self.drw([startingLoc[0]+2*i*self.iR, startingLoc[1]],'brick')

	def board(self,middle):
		
		row1=[middle[0]-self.iR*2, middle[1]-2*(self.hexSide*2+self.yOffset)]
		row2=[middle[0]-self.iR*3, middle[1]-(self.hexSide*2+self.yOffset)]
		row3=[middle[0]-self.iR*4, middle[1]]
		row4=[middle[0]-self.iR*3, middle[1]+(self.hexSide*2+self.yOffset)]
		row5=[middle[0]-self.iR*2, middle[1]+2*(self.hexSide*2+self.yOffset)]

		rows=[row1, row2, row3, row4, row5]
		tileAmt=[3,4,5,4,3]
		j=-1
		for i in rows:
			j=j+1
			self.hexRow(i,tileAmt[j])


		



		






def main():

	win = GraphWin('Game Board', 401, 401)
	 # right side up coordinates

	l=[201, 201]
	Hexagons=Geom(50, win)
	Hexagons.board(l)
	time.sleep(1)
	print(Hexagons.nodes[2])


	

	



main()



	
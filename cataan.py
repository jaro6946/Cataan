
"""Need to make function to track mouse and return hex location and node location"""


import math
from graphics import *
import time
from random import seed
from random import random
from time import clock

winX=800
winY=800
win = GraphWin('Game Board', winX, winY)

def drwNodes(nodeDict, window):
    for count, node in enumerate(nodeDict):
        point=nodeDict[count+1].nodeCoordinate
        text=str(nodeDict[count+1].nodeID)

        writing=Text(Point(point[0],point[1]), text)
        writing.setSize(15)
        writing.setTextColor("black")

        writing.draw(window)

def drwHex (points, hexID, centerPoint, tileType, pip,window):
        
        writing=Text(Point(centerPoint[0],centerPoint[1]), hexID+" "+str(pip))
        writing.setSize(15)
        writing.setTextColor("white")

        p=[Point(i,j) for i,j in points]
        hexa=Polygon(p)

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
        elif tileType=='dessert':
            hexa.setFill('black')
        else :
            pass

        hexa.draw(window)
        writing.draw(window)


 
class node(object):
    nodePositions=[[],[]] ;"[[nodeID1, nodeID2, etc],[coordinate1, coordinate2, etc]]"
    nodeAmmount=0

    def __init__(self, hexAdjoining, nodeCoordinate):
        self.dupicate=False
        self.nodeCoordinate=nodeCoordinate
        self.nodeID=node.nodeAmmount+1
        self.hexesAdjoining=[hexAdjoining]
        
        "print( self.nodeCoordinate)"

        """Checking for duplicates"""
        if node.nodePositions[1].count(nodeCoordinate)>0: 
            self.dupicate=True
            i=node.nodePositions[1].index(nodeCoordinate)
            self.nodeID2Change=node.nodePositions[0][i]
            hexagon.nodeDict[self.nodeID2Change].hexesAdjoining+=[hexAdjoining]
            self.nodeID=str(self.nodeID2Change)+"D" """D for dupicate"""
            node.nodePositions[0]+=[self.nodeID]
            """print(self.nodeID)
            print("\n")"""
            node.nodePositions[1]+=[self.nodeCoordinate]

            return

        "If it is not a duplicate, add to list"
        
        
        node.nodePositions[0]+=[node.nodeAmmount+1]
        node.nodePositions[1]+=[self.nodeCoordinate]
        node.nodeAmmount+=1

class edge(object):

    
    def __init__(self,nodeID, nodeID1,nodeID2):
        
        self.coordinates=coordinates
        self.nodeID=nodeID
        self.nodePosition=nodePosition
        self.pieceStatus=[0,0]

    
        
    
class hexagon(object):
    centerPositions=[]
    inscribedRadius=.5
    circumscribedRadius=.5/math.cos(math.radians(30))
    halfSideLength=.5*math.tan(math.radians(30))
    nodes=[]
    vertexesGroupedByHexagon=[[None],[None]]
    vertexes=[]
    scale=80
    nodeDict={}

    

    def __init__(self,hexID, centerCoordinates, tileType, pipNumber):
        self.hexID=hexID
        self.centerCoordinates=[centerCoordinates[0],centerCoordinates[1]]
        self.tileType=tileType
        self.pipNumber=pipNumber
        hexagon.centerPositions.append(self.centerCoordinates)
        
        """nw=north west, n=north etc"""


        self.nNodeCoordinates=[self.centerCoordinates[0], self.centerCoordinates[1]+hexagon.circumscribedRadius*hexagon.scale]
        self.neNodeCoordinates=[self.centerCoordinates[0]+hexagon.inscribedRadius*hexagon.scale, self.centerCoordinates[1]+hexagon.halfSideLength*hexagon.scale]
        self.seNodeCoordinates=[self.centerCoordinates[0]+hexagon.inscribedRadius*hexagon.scale, self.centerCoordinates[1]-hexagon.halfSideLength*hexagon.scale]
        self.sNodeCoordinates=[self.centerCoordinates[0], self.centerCoordinates[1]-hexagon.circumscribedRadius*hexagon.scale]
        self.swNodeCoordinates=[self.centerCoordinates[0]-hexagon.inscribedRadius*hexagon.scale, self.centerCoordinates[1]-hexagon.halfSideLength*hexagon.scale]
        self.nwNodeCoordinates=[self.centerCoordinates[0]-hexagon.inscribedRadius*hexagon.scale, self.centerCoordinates[1]+hexagon.halfSideLength*hexagon.scale]
    
        self.instanceVertexLocations=[self.nNodeCoordinates,self.neNodeCoordinates,self.seNodeCoordinates,self.sNodeCoordinates,self.swNodeCoordinates,self.nwNodeCoordinates]
        
        drwHex(self.instanceVertexLocations, self.hexID, self.centerCoordinates,tileType,pipNumber, win)
        
        for vertex in self.instanceVertexLocations:
            hexagon.vertexesGroupedByHexagon[0].append([self.hexID])
            hexagon.vertexesGroupedByHexagon[1].append([vertex])
            hexagon.nodeDict[len(hexagon.nodeDict)+1]=node(self.hexID, vertex)
            """delete duplicate entries"""
            if hexagon.nodeDict[len(hexagon.nodeDict)].dupicate is True:
                del hexagon.nodeDict[len(hexagon.nodeDict)]

            


        


def tileColorAndPips(ammountTiles=[3,4,4,3,4,1], pips=[2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12]):
    
    def rand(arg):
        pass
        return random() 
    
    seed(clock)
    pips.sort(key=rand)
    randomizedPips=pips
    randomizedPips+=[0]
    colors=['brick','sheep', 'wheat', 'stone', 'wood','dessert']
    randomizedColors=[]
    
    for count, ammount in enumerate(ammountTiles):
        randomizedColors=randomizedColors+[colors[count]]*ammount

    randomizedColors.sort(key=rand)

    colorsAndPips=[]
    i=0

    for color in randomizedColors:
        
        if color is not 'dessert':
            colorsAndPips+=[[color,randomizedPips[i]]]
            i+=1
        else:
            colorsAndPips+=[[color,0]]
            
    print(colorsAndPips)    
    colorsAndPips=[[i for i,j in colorsAndPips],[j for i,j in colorsAndPips]]

    return colorsAndPips





class board(hexagon):
   
    centerLocationDict={}

    lowerHexAmmount=3
    midHexAmmount=5
   
    

    
    rows=(midHexAmmount-lowerHexAmmount)*2+1
    height=hexagon.circumscribedRadius*hexagon.scale+hexagon.halfSideLength*hexagon.scale*rows+hexagon.circumscribedRadius*hexagon.scale
    width=midHexAmmount*hexagon.inscribedRadius*2*hexagon.scale

    yCenter2CenterDistance=2*hexagon.inscribedRadius*math.sin(math.radians(60))*hexagon.scale
    xCenter2CenterDistance=2*hexagon.inscribedRadius*hexagon.scale

    def __init__(self):
        board.xWindowSize=winX
        board.yWindowSize=winY
        board.xMiddle=board.xWindowSize//2
        board.yMiddle=board.yWindowSize//2

    def neighborCenter(self,startLocation, xDir,yDir):
        """xDir 1 for the right and -1 for left, yDir 1 for up and -1 for down"""
        self.startLocation=startLocation
        self.neighborCoordinates=[0,0]
        
        self.neighborCoordinates[1]=self.startLocation[1]+board.yCenter2CenterDistance*yDir
        self.neighborCoordinates[0]=self.startLocation[0]+board.xCenter2CenterDistance*xDir-yDir*.5*board.xCenter2CenterDistance

        return self.neighborCoordinates


    def makeBoard(self):
        """Find all the hexagon locations and create hexagon classes for each"""

        """Check to make sure the board will fit in the window"""
        if board.height>board.yWindowSize and board.width>board.xWindowSize:
            raise ValueError("your board is too wide and tall")

        elif board.height>board.yWindowSize:
            raise ValueError("your board is too tall")

        elif board.width>board.xWindowSize:
            raise ValueError("your board is too wide")

        """Find top left hex location - it will be our starting point for finding the rest"""
        self.startingCoordinates=[board.xMiddle,board.yMiddle]

        self.topLeftCoordinate=[self.startingCoordinates[0]-self.lowerHexAmmount*board.scale*board.inscribedRadius,\
            self.startingCoordinates[1]+((board.rows-1)/2)*(board.yCenter2CenterDistance/2)]

        """Find all the center locations of the tiles and save them to a dictonary"""
        self.column = self.lowerHexAmmount
        self.startPoint=self.topLeftCoordinate
        self.yDir=0
        self.xDir=1
        self.hexLocations=[]
        [self.tileColorList, self.pipList]=tileColorAndPips()

        abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for i in range(self.rows):
            
            for p in range(self.column):
                self.startPoint=self.neighborCenter(self.startPoint, self.xDir,self.yDir)
                self.hexLocations+=[self.startPoint]
                self.yDir=0
                self.xDir=1

            self.yDir=-1

            if i < self.rows//2:
                self.xDir=-self.column
                self.column=self.column+1
                
            else:
                self.column=self.column-1
                self.xDir=-self.column

            print("\n"*2)
        for i,j in enumerate(self.hexLocations):
            
            board.centerLocationDict[i+1]=hexagon(abc[i],j,self.tileColorList[i], self.pipList[i])

        drwNodes(hexagon.nodeDict,win)

'''def updateBoardImage
    a=hexagon(1, [50,50])
    d=a.instanceNodePositions()
    b=a.returnNodes()
    c=a.centerCoordinates
    e=[Point(k[0],k[1]) for k in a.instanceNodePositions()]

    drwHex(e, "pass",win)
        


    time.sleep(5)    
    win.close'''

        
print("\n"*12)
a=board()
a.makeBoard()
for i in hexagon.nodeDict:
    print(hexagon.nodeDict[i].hexesAdjoining)

time.sleep(60)

    
    
    


print("\n"*6)

print("\n")


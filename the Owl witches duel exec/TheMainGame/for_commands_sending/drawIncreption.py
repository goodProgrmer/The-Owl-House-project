def init(): # initial drawStrings
    global drawStrings
    drawStrings=["",""] # drawStrings[0] for player 1 and drawStrings[2] for player 2


"""incription ruls:
1. every incripted comand that draw somesing on the screen will be in new line
2. comand blit can get incription of some comand that return image instid of its text argument
3. every command that return image will sturt with the prefics ".re " and after that the other command incription
4. every drawing command incription start with its code and "|" and after that the nececery arguments the divided by "|"
5. every returning value command incription start with its code and "|" and after that the nececery arguments the divided by "|"
"""

def drawFilledArcIncription(color,r,center,stA,endA,isForP1=True,isForP2=True):
    """append command of drawing filled arc to drawStrings[0] and/or drawStrings[1] (acording to paramiters) according to the protocol
    :param color: filling color
    :param r: arc rudios
    :param center: arc center
    :param stA: the start angle of the arc according to x axis
    :param endA: the start angle of the arc according to x axis
    :type color: RGB
    :type r: float
    :type center: (int,int)
    :type stA: float
    :type endA: float
    :param isForP1: does it supposed to write the command in drawStrings[0]
    :param isForP2: does it supposed to write the command in drawStrings[1]
    :type isForP1: bool
    :type isForP2: bool"""
    if isForP1:
        drawStrings[0]+="DFA|"+str(color)+"|"+str(r)+"|"+str(center)+"|"+str(round(stA,2))+"|"+str(round(endA,2))+"\n"
    if isForP2:
        drawStrings[1]+="DFA|"+str(color)+"|"+str(r)+"|"+str(center)+"|"+str(round(stA,2))+"|"+str(round(endA,2))+"\n"

def imegedClockImgIncription(r,prosents,imageName):
    """return command of drawing clock img according to the protocol
    :param r: clock rudios: (resize the image to fit the radios)
    :param prosents: the prosent of circle that the clock hand need to sow. 50% will be when prosent=0.5
    :param imageName: path to the image from wich the clock will be made
    :type r: float
    :type prosents: float
    :type imageName: string
    :return: command of drawing clock img according to the protocol
    :rtype: string"""
    return ".re ICI:"+str(r)+":"+str(prosents)+":"+imageName

def prosentRestIncription(prosent,width,hight,color):
    """return command of creating prosent rect according to the protocol
    :param prosent: the prosent of the inside rect that will be filled. 50% will be when prosent=50.
    :param width: width of the surface
    :param hight: hight of the surface
    :param color: filling color of the prosent rect
    :type prosent: float
    :type width: float
    :type hight: float
    :type color: (int,int,int)
    :param isForP1: does it supposed to write the command in drawStrings[0]
    :param isForP2: does it supposed to write the command in drawStrings[1]
    :type isForP1: bool
    :type isForP2: bool
    :return: command of creating prosent rect according to the protocol
    :rtype: string"""
    return ".re PR:"+str(prosent)+":"+str(width)+":"+str(hight)+":"+str(color)

def rectDrewIncription(color,rectTuple,width=0,isForP1=True,isForP2=True):
    """append command of drawing rect to drawStrings[0] and/or drawStrings[1] (acording to paramiters) according to the protocol
    :param color: rect color
    :param rectTuple: (x,y,width,hight)
    :param width: bording width (if 0, the rect will be filled inside)
    :type color: (int,int,int)
    :type rectTuple: (float,float,float,float)
    :type width: float
    :param isForP1: does it supposed to write the command in drawStrings[0]
    :param isForP2: does it supposed to write the command in drawStrings[1]
    :type isForP1: bool
    :type isForP2: bool"""
    rectTuple= (int(rectTuple[0]),int(rectTuple[1]),int(rectTuple[2]),int(rectTuple[3]))
    if isForP1:
        drawStrings[0]+="RD|"+str(color)+"|"+str(rectTuple)+"|"+str(width)+"\n"
    if isForP2:
        drawStrings[1]+="RD|"+str(color)+"|"+str(rectTuple)+"|"+str(width)+"\n"

def circleDrewIncription(color,r,center,isForP1=True,isForP2=True):
    """append command of drawing circle to drawStrings[0] and/or drawStrings[1] (acording to paramiters) according to the protocol
    :param color: circle color
    :param r: radius
    :param center: circle center
    :type color: (int,int,int)
    :type r: float
    :type center: (float,float)
    :param isForP1: does it supposed to write the command in drawStrings[0]
    :param isForP2: does it supposed to write the command in drawStrings[1]
    :type isForP1: bool
    :type isForP2: bool"""
    if isForP1:
        drawStrings[0]+="CD|"+str(color)+"|"+str(r)+"|"+str(center)+"\n"
    if isForP2:
        drawStrings[1]+="CD|"+str(color)+"|"+str(r)+"|"+str(center)+"\n"

def lineDrewIncription(color, start_pos, end_pos, width=1,isForP1=True,isForP2=True):
    """append command of drawing circle to drawStrings[0] and/or drawStrings[1] (acording to paramiters) according to the protocol
    :param color: line color
    :param start_pos: start point of the line
    :param end_pos: end point of the line
    :param width: the width of the line
    :type color: (int,int,int)
    :type start_pos: (float,float)
    :type end_pos: (float,float)
    :type width: float
    :param isForP1: does it supposed to write the command in drawStrings[0]
    :param isForP2: does it supposed to write the command in drawStrings[1]
    :type isForP1: bool
    :type isForP2: bool"""
    if isForP1:
        drawStrings[0]+="LD|"+str(color)+"|"+str(start_pos)+"|"+str(end_pos)+"|"+str(width)+"\n"
    if isForP2:
        drawStrings[1]+="LD|"+str(color)+"|"+str(start_pos)+"|"+str(end_pos)+"|"+str(width)+"\n"

def blitIncription(imageSrc,pos,isForP1=True,isForP2=True):
    """append command of blit to drawStrings[0] and/or drawStrings[1] (acording to paramiters) according to the protocol
    :param imageSrc: the thing that it need to drew. imageSrc can be the name of the file or returning value command incription.
    :param pos: the point to blit (top left corner)
    :type imageSrc: string
    :type pos: (float,float)
    :param isForP1: does it supposed to write the command in drawStrings[0]
    :param isForP2: does it supposed to write the command in drawStrings[1]
    :type isForP1: bool
    :type isForP2: bool"""
    if isForP1:
        appendStr= "B|"+imageSrc+"|"+str(pos)+"\n"
        drawStrings[0]+= appendStr
        #drawStrings[0]+="B|"+imageSrc+"|"+str(pos)+"\n"
    if isForP2:
        drawStrings[1]+="B|"+imageSrc+"|"+str(pos)+"\n"

def polygonIncription(color, points, width=0,isForP1=True,isForP2=True):
    """append command of palygon (described in pygame tutorial) to drawStrings[0] and/or drawStrings[1] (acording to paramiters) according to the protocol
    :param color: drawn object color
    :param points: the points to pass to palygon function
    :param width: bording width (if 0, the shape will be filled inside)
    :type color: (int,int,int)
    :type points: list of points of type (float,float)
    :type width: float
    :param isForP1: does it supposed to write the command in drawStrings[0]
    :param isForP2: does it supposed to write the command in drawStrings[1]
    :type isForP1: bool
    :type isForP2: bool"""
    if isForP1:
        drawStrings[0]+="P|"+str(color)+"|"+str(points)+"|"+str(width)+"\n"
    if isForP2:
        drawStrings[1]+="P|"+str(color)+"|"+str(points)+"|"+str(width)+"\n"

def textDrawIncription(fontName, fontNum, text, color):
    """return the command of creating text according to the protocol
    :param fontName:the name of the font
    :param fontNum: the size of the font
    :param text: the text
    :param color: its color
    :type fontName: string
    :type fontNum: int
    :type text: string
    :type color: (int,int,int)
    :return: the command of creating text according to the protocol
    :rtype: string"""
    return ".re TD:"+str(fontName)+":"+str(fontNum)+":"+str(text)+":"+str(color)

def rotatedfilledSurfaseCreateIncription(size,color,a):
    """return the command of creating surface, filling it and rotating it according to the protocol"""
    return ".re RFSC:"+str(size)+":"+str(color)+":"+str(a)

def rotatedResizedImageIncription(img,size_multiples,a):
    """return the command of creating surface, filling it and rotating it according to the protocol
    :param img: the image to rotate
    :param size_multiples: the multiple of the size in x and y
    :param a: the angle to rotate the image"""
    return ".re RRI:"+str(img)+":"+str(size_multiples)+":"+str(a)

#low level incription
def getIncriptionStr(placeNum):
    """return the incription string in drawStrings[placeNum].
    :param placeNum: the index of the string to return
    :type placeNum: int (0 or 1)
    :return: drawStrings[placeNum]
    :rtype: string"""
    return drawStrings[placeNum]

def setIncriptionStr(placeNum,string):
    """set the incription string drawStrings[placeNum] to the parameter string
    :param placeNum: the index of the string to cheng it value
    :param string: new incription string
    :type placeNum: int (0 or 1)
    :type string: string"""
    drawStrings[placeNum]= string

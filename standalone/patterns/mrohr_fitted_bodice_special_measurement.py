# !/usr/bin/python
#
# mrohr_fitted_bodice_special_measurement.py
# Inkscape extension - Effects - Sewing Patterns - Shirt Waist Allington
# Copyright (C) 2010, 2011, 2012 Susan Spencer, Steve Conklin <www.taumeta.org>

'''
Licensing paragraph :

1. CODE LICENSE :  GPL 2.0 +
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT FNY WARRFNTY; without even the implied warranty of
MERCHFNTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111 - 1307  USA

2. PATTERN LICENSE :  CC BY - NC 3.0
The output of this code is a pattern and is considered a
visual artwork. The pattern is licensed under
Attribution - NonCommercial 3.0 (CC BY - NC 3.0)
<http : //creativecommons.org/licenses/by - nc/3.0/>
Items made from the pattern may be sold;
the pattern may not be sold.

End of Licensing paragraph.
'''

from tmtpl.designbase import *
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.patternmath import *
from tmtpl.constants import *
from tmtpl.utils import *

class Design(designBase):

    def pattern(self) :
        """
        Method defining a pattern design. This is where the designer places
        all elements of the design definition
        """

        # The designer must supply certain information to allow
        #   tracking and searching of patterns
        #
        # This group is all mandatory
        #
        self.setInfo('patternNumber', 'MR_B1')
        self.setInfo('patternTitle', 'MRohr Fitted Bodice Special Measurement Method')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'M.Rohr')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """This is a test pattern for Seamly Patterns. Adapted from Sara May Allington's 'Dressmaking', 1917""")
        self.setInfo('category', 'Shirt/TShirt/Blouse')
        self.setInfo('type', 'Historical')
        #
        # The next group are all optional
        #
        self.setInfo('gender', 'F') # 'M',  'F',  or ''
        self.setInfo('yearstart', '1900')
        self.setInfo('yearend', '')
        self.setInfo('culture', 'European')
        self.setInfo('wearer', '')
        self.setInfo('source', '')
        self.setInfo('characterName', '')
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')

        #get client data
        CD = self.CD #client data is prefaced with CD

        #create a pattern named 'bodice'
        bodice = self.addPattern('bodice')

        #create pattern pieces,  assign an id lettercd ..
        A = bodice.addPiece('Bodice Front', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = bodice.addPiece('Bodice Back', 'B', fabric = 2, interfacing = 0, lining = 0)
        #C = bodice.addPiece('Sleeve', 'C', fabric = 2, interfacing = 0, lining = 0)

        #pattern points
        # x, y coordinates are always passed as a two-item list like this: (23.6, 67.0)
        # points are always in the 'reference' group, and always have style='point_style'

        #---Front A---#
        FNC = A.addPoint('FNC', (0.0, 0.0)) #front neck center
        FWC = A.addPoint('FWC', down(FNC, CD.front_waist_length)) #front waist center
        FSH = A.addPoint('FSH', up(FWC, CD.front_shoulder_height)) #front shoulder height
        FSW = A.addPoint('FSW', right(FSH, 0.5 * CD.front_shoulder_width)) #front shoulder width
        FSP = A.addPoint('FSP', highestP(onCircleAtX(FWC, CD.front_shoulder_balance, FSW.x))) #front shoulder point
        FNS = A.addPoint('FNS', leftmostP(onCircleAtY(FSP, CD.shoulder, FSH.y))) #front neck side
        FAP2 = A.addPoint('FAP2', rightmostP(onCircleAtX(FNS, CD.front_underarm_balance, 0.5 * CD.across_chest))) #front armscye point 2
        FUC = A.addPoint('FUC', (FNC.x, FAP2.y)) #front underarm center
        FUS3 = A.addPoint('FUS3', right(FUC, 0.5 * CD.front_underarm)) #front underarm side 2 - inline with front underarm center & front armscye

        FBP = A.addPoint('FBP', rightmostP(onCircleAtX(FNS, CD.bust_balance, 0.5 * CD.bust_distance))) #bust point
        FBC = A.addPoint('FBC', (FNC.x, FBP.y)) #bust center
        FBS = A.addPoint('FBS', rightmostP(onCircleTangentFromOutsidePoint(FBP, (0.5 * CD.front_bust) - distance(FBC, FBP), FUS3))) #front bust side

        side_ease = 0.04 * CD.bust/4.0
        FUS2 = A.addPoint('FUS2', polar(FAP2, CD.front_underarm/2.0 - distance(FUC, FAP2), angleOfLine(FBP, FBS))) #front underarmside 3 - parallel to bustline
        FAP = A.addPoint('FAP', polar(FAP2, side_ease, angleOfLine(FBP, FBS))) #front armscye point - 2.5% ease
        FUS = A.addPoint('FUS', polar(FUS3, side_ease, angleOfLine(FBP, FBS))) # front underarm side - incl. side ease
        FWS2 = A.addPoint('FWS2', onLineAtLength(FUS3, FBS, CD.side - distance(FUS2, FUS3))) #front waist side 2
        FWS = A.addPoint('FWS', polar(FWS2, side_ease, angleOfLine(FBP, FBS))) #front waist side - incl. side_ease

        #front waist dart 1
        full_bust = 'false'
        FD1 = A.addPoint('FD1', FBP) #front dart point
        FD1.i = A.addPoint('FD1.i', right(FWC, 0.4 * CD.bust_distance)) #dart inside leg
        FD1.o = A.addPoint('FD1.o', lowestP(intersectCircles(FBP, distance(FBP, FD1.i), FWS, 0.5 * CD.front_waist - distance(FWC, FD1.i)))) #dart outside leg
        updatePoint(FD1, polar(FBP, 0.15 * distance(FBP, FD1.i), angleOfLine(FBP, FD1.i) - 0.5 * angleOfVector(FD1.o, FBP, FD1.i))) #lower front waist dart 1 point

        #create front waist dart 2 if full bust
        total_dart_angle = angleOfVector(FD1.i, FBP, FD1.o)
        total_dart_width = distance(FD1.i, FD1.o)
        max_dart_width = CD.front_bust/6.0 #1/3 of half front bust
        if total_dart_width > max_dart_width: #if waist dart width > 1/3 of half front bust
            full_bust = 'true'
            #change 1st bust dart width to 2/3 total_dart_width
            updatePoint(FD1.o, polar(FBP, distance(FBP, FD1.i), angleOfLine(FBP, FD1.i) - 2/3.0 * total_dart_angle))
            updatePoint(FD1, polar(FBP, 0.15 * distance(FBP, FD1.i), angleOfLine(FBP, FD1.i) - 0.5 * angleOfVector(FD1.o, FBP, FD1.i))) #lower front waist dart 1 point
            #add second bust dart
            FBP2 = A.addPoint('FBP2', onLineAtLength(FBP, FBS, 2 * distance(FBP, FD1))) #2nd bust point
            FD2 = A.addPoint('FD2', FBP2) #2nd dart point
            pnt_m = intersectLineRay(FD1.o, FWS, FD2, angleOfLine(FBP, FBS) + ANGLE90)
            FD2.i = A.addPoint('FD2.i', intersectLineRay(FD1.o, FWS, FD2, angleOfLine(FD2, pnt_m) + total_dart_angle/6.0)) #2nd dart inside leg is parallel to 1st dart outside leg
            FD2.o = A.addPoint('FD2.o', polar(FD2, distance(FD2, FD2.i), angleOfLine(FD2, FD2.i) - total_dart_angle/3.0))
            updatePoint(FD2, polar(FBP2, distance(FBP, FD1), angleOfLine(FD2, FD2.i) - total_dart_angle/6.0)) #lower 2nd dart point


        #front control points
        #b/w FNS & FNC
        FNC.addInpoint(right(FNC, 0.6 * abs(FNC.x - FNS.x)))
        FNS.addOutpoint(polar(FNS, 0.5 * abs(FNC.y - FNS.y), angleOfLine(FNS, FNC.inpoint)))
        #b/w FUS & FAP
        FUS.addOutpoint(polar(FUS, 0.4 * distance(FUS, FAP), angleOfLine(FBS, FBP)))
        FAP.addInpoint(polar(FAP, 0.33 * distance(FUS, FAP), angleOfLine(FNS, FAP)))
        #b/w FAP & FSP
        FAP.addOutpoint(polar(FAP, 0.3 * distance(FAP, FSP), angleOfLine(FAP, FNS)))
        FSP.addInpoint(polar(FSP, 0.15 * distance(FAP, FSP), angleOfLine(FSP, FNS) - ANGLE90))
        #b/w FWC & FD1.i
        FWC.addOutpoint(right(FWC, 0.33 * distance(FWC, FD1.i)))
        FD1.i.addInpoint(left(FD1.i, 0.33 * distance(FWC, FD1.i)))
        #b/w FD1.o & FWS ... or FD1.o & FD2.i
        if full_bust == 'true':
            #b/w FD1.o & FD2.i
            FD1.o.addOutpoint(onLineAtLength(FD1.o, FD2.i, 0.33 * distance(FD1.o, FD2.i)))
            FD2.i.addInpoint(onLineAtLength(FD2.i, FD1.o, 0.33 * distance(FD1.o, FD2.i)))
            #b/w FD2.o & FWS
            FD2.o.addOutpoint(onLineAtLength(FD2.o, FWS, 0.33 * distance(FD2.o, FWS)))
            FWS.addInpoint(polar(FWS, 0.33 * distance(FD2.i, FWS), angleOfLine(FWS, FD2.o)))
        else:
            #b/w FD1.o & FWS
            FD1.o.addOutpoint(onLineAtLength(FD1.o, FWS, 0.33 * distance(FD1.o, FWS)))
            FWS.addInpoint(polar(FWS, 0.33 * distance(FD1.o, FWS), angleOfLine(FWS, FD1.o)))
        #extend front waist dart 1 for smoother waistline
        theta = angleOfVector(FD1.i.inpoint, FD1.i, FD1) - ANGLE90
        r = distance(FD1.i.inpoint, FD1.i)
        updatePoint(FD1.i, dPnt(extendLine(FD1, FD1.i, r * sin(theta))))
        updatePoint(FD1.o, dPnt(extendLine(FD1, FD1.o, r * sin(theta))))
        #extend fold length to meet seamline when folded toward front waist center
        foldDart(FD1, FWC) #creates BD1.m for seamline, BD1.ic & BD1.oc for dartline
        if full_bust == 'true':
            #extend front waist dart 2 for smoother waistline
            theta = angleOfVector(FD2.i.inpoint, FD2.i, FD2) - ANGLE90
            r = distance(FD2.i.inpoint, FD2.i)
            updatePoint(FD2.i, dPnt(extendLine(FD2, FD2.i, r * sin(theta))))
            updatePoint(FD2.o, dPnt(extendLine(FD2, FD2.o, r * sin(theta))))
            #extend dart fold length to meet seamline when folded toward FWC front waist center
            foldDart(FD2, FD1.o) #creates BD1.m for seamline, BD1.ic & BD1.oc for dartline

        #---Back B---#
        BNC = B.addPoint('BNC', (0.0, 0.0)) #back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.back_waist_length)) #back waist center
        BWO = B.addPoint('BWO', left(BWC, 0.03 * CD.back_waist)) #back waist offset - 3% of back waist
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height)) #back shoulder height
        BSW = B.addPoint('BSW', left(BSH, 0.5 * CD.back_shoulder_width)) #back shoulder width
        BSP2 = B.addPoint('BSP2', highestP(onCircleAtX(BWO, CD.back_shoulder_balance, BSW.x))) #back shoulder point
        BNS = B.addPoint('BNS', rightmostP(onCircleAtY(BSP2, CD.shoulder, BSH.y))) #back neck side
        BSP = B.addPoint('BSP', extendLine(BNS, BSP2, 0.065 * CD.shoulder))# add 6.5% ease for shoulder dart
        BAP2 = B.addPoint('BAP2', lowestP(onCircleAtX(BNS, CD.back_underarm_balance, BNC.x - 0.5 * CD.across_back))) #back armscye point 2
        BAP = B.addPoint('BAP', left(BAP2, side_ease)) #back armscye point - incl. ease
        BUC = B.addPoint('BUC', (BNC.x, BAP.y)) #back underarm center
        BUS3 = B.addPoint('BUS3', left(BUC, 0.5 * CD.back_underarm)) #back underarm side 3
        BUS2 = B.addPoint('BUS2', down(BUS3, distance(FUS2, FUS3))) #back underarm side 2 - lowered same as front
        BUS = B.addPoint('BUS', left(BUS2, side_ease)) #back underarm side (6% ease)
        #back waist dart
        pnt1 = intersectLines(BWO, BSP, BUC, BUS)
        pnt2 = intersectLines(BWO, BSP, BAP, BNS)
        BD1 = B.addPoint('BD1', up(pnt1, 0.5 * distance(pnt1, pnt2))) #back waist dart point
        pnt_m = (BD1.x, BWC.y) #dart midpoint at waist
        BD1.i = B.addPoint('BD1.i', right(pnt_m, 0.15 * distance(pnt_m, BWC))) #dart inside point on waistline
        BD1.o = B.addPoint('BD1.o', left(pnt_m, distance(pnt_m, BD1.i))) #dart outside point on waistline
        BWS2 = B.addPoint('BWS2', lowestP(intersectCircles(BUS, distance(FUS, FWS), BD1.o, 0.5 * CD.back_waist - distance(BWC, BD1.i)))) #back waist side
        BWS = B.addPoint('BWS', left(BWS2, side_ease)) #back underarm side - incl. side_ease
        #back shoulder dart
        dart_width = distance(BSP, BNS) - distance(FSP, FNS)
        pnt_m = midPoint(BSP, BNS) #midpoint of shoulder dart at shoulder seam
        pnt_p = intersectLineRay(BNS, BAP, pnt_m, angleOfLine(BSP, BNS) + ANGLE90)
        BD2 = B.addPoint('BD2', onLineAtLength(pnt_m, pnt_p, 0.75 * distance(pnt_m, pnt_p))) #back shoulder dart point
        BD2.i = B.addPoint('BD2.i', onLineAtLength(pnt_m, BNS, 0.5 * dart_width)) #back shoulder dart inside leg
        BD2.o = B.addPoint('BD2.o', onLineAtLength(pnt_m, BSP, 0.5 * dart_width)) #back shoulder dart outside leg
        extendDart(BSP, BD2, BNS) #smooth shoulder seam at dart
        foldDart(BD2, BNS) #fold dart toward BNS

        #back control points
        #b/w BNS & BNC
        BNC.addInpoint(left(BNC, 0.75 * abs(BNC.x - BNS.x)))
        BNS.addOutpoint(polar(BNS, 0.5 * abs(BNC.y - BNS.y), angleOfLine(BNS, BNC.inpoint)))
        #b/w BUS & BAP
        BUS.addOutpoint(polar(BUS, 0.5 * distance(BUS, BAP), angleOfLine(BWS, BUS) + ANGLE90))
        BAP.addInpoint(polar(BAP, 0.5 * distance(BUS.outpoint, BAP), angleOfLine(BNS, BAP)))
        #b/w BAP & BSP
        BAP.addOutpoint(polar(BAP, 0.33 * distance(BAP, BSP), angleOfLine(BAP, BNS)))
        BSP.addInpoint(polar(BSP, 0.15 * distance(BAP, BSP), angleOfLine(BSP, BNS) + ANGLE90))
        #b/w FWC & FD1.i
        BWC.addOutpoint(left(BWC, 0.33 * distance(BWC, BD1.i)))
        BD1.i.addInpoint(right(BD1.i, 0.33 * distance(BWC, BD1.i)))
        #b/w FD1.o & FWS
        BD1.o.addOutpoint(onLineAtLength(BD1.o, BWS, distance(BD1.i, BD1.i.inpoint)))
        BWS.addInpoint(polar(BWS, 0.33 * distance(BD1.o, BWS), angleOfLine(BWS, BD1.o)))
        #extend front waist dart legs for smoother waistline
        theta = angleOfVector(BD1.i.inpoint, BD1.i, BD1) - ANGLE90
        r = distance(BD1.i.inpoint, BD1.i)
        updatePoint(BD1.i, dPnt(extendLine(BD1, BD1.i, r * sin(theta))))
        updatePoint(BD1.o, dPnt(extendLine(BD1, BD1.o, r * sin(theta))))
        #extend dart fold length to meet seamline when folded toward BWC back waist center
        foldDart(BD1, BWC) #creates BD1.m for seamline, BD1.ic & BD1.oc for dartline

        #Bodice Front A
        pnt1 = dPnt((FNC.x + abs(FNC.x - FSP.x)/2.0, FNC.y + abs(FUC.y - FNC.y)/2.0))
        A.setLabelPosition(pnt1)
        pnt2 = up(pnt1, 0.5*IN)
        A.setLetter(pnt2, scaleby = 10.0)
        AG1 = dPnt((FNC.x + abs(FNS.x - FNC.x)/2.0, abs(FUC.y - FNC.y)/2.0))
        AG2 = down(AG1, 0.75 * CD.back_waist_length)
        A.addGrainLine(AG1, AG2)
        A.addGridLine(['M', FSP, 'L', FSW, 'L', FSH, 'L', FWC, 'M', FAP2, 'L', FNS, 'L', FBP, 'M', FBC, 'L', FBP, 'L', FBS, 'M', FUC, 'L', FUS3, 'L', FUS,'M', FAP2,'L', FUS2, 'M', FWC, 'L', FSP])

        if full_bust == 'true':
            A.addDartLine(['M', FD1.oc, 'L', FD1, 'L', FD1.ic, 'M', FD2.oc, 'L', FD2, 'L', FD2.ic])
            pth = (['M', FNC, 'L', FWC, 'C', FD1.i, 'L', FD1.m, 'L', FD1.o, 'C', FD2.i, 'L', FD2.m, 'L', FD2.o, 'C', FWS, 'L', FUS, 'C', FAP, 'C', FSP, 'L', FNS, 'C', FNC])
            A.addSeamLine(pth)
            A.addCuttingLine(pth)
        else:
            A.addDartLine(['M', FD1.oc, 'L', FD1, 'L', FD1.ic])
            pth = (['M', FNC, 'L', FWC, 'C', FD1.i, 'L', FD1.m, 'L', FD1.o, 'C', FWS, 'L', FUS, 'C', FAP, 'C', FSP, 'L', FNS, 'C', FNC])
            A.addSeamLine(pth)
            A.addCuttingLine(pth)

        #Bodice Back B
        pnt1 = dPnt((BNC.x - abs(BNC.x - BSP.x)/2.0, BNC.y + abs(BUC.y - BNC.y)/2.0))
        B.setLabelPosition(pnt1)
        pnt2 = up(pnt1, 0.5*IN)
        B.setLetter(pnt2, scaleby = 10.0)
        BG1 = dPnt((BNC.x - abs(BNS.x - BNC.x)/2.0, abs(BUC.y - BNC.y)/3.0))
        BG2 = down(BG1, 0.75 * CD.back_waist_length)
        B.addGrainLine(BG1, BG2)
        B.addGridLine(['M', BSP2, 'L', BSW, 'L', BSH, 'L', BUC, 'L', BUS3, 'L', BUS2, 'M', BNS, 'L', BAP2, 'M', BWO, 'L', BSP2])
        B.addDartLine(['M', BD1.oc, 'L', BD1, 'L', BD1.ic, 'M', BD2.oc, 'L', BD2, 'L', BD2.ic])
        pth = (['M', BNC, 'L', BWC, 'C', BD1.i, 'L', BD1.m, 'L', BD1.o, 'C', BWS, 'L', BUS, 'C', BAP, 'C', BSP, 'L', BD2.o, 'L', BD2.m, 'L', BD2.i, 'L', BNS, 'C', BNC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #call draw() to generate svg file
        self.draw()

        return

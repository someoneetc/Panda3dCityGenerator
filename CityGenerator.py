import os
import random
import yaml
from panda3d.core import PNMImage, PNMPainter

import numpy as np
from scipy.spatial import Voronoi

def generateRoadMap(heightMap,n_crossroads):
    roadMap = PNMImage(heightMap.getReadXSize(),heightMap.getReadYSize())
    roadMap.fill(255,255,255)
    painter = PNMPainter(roadMap)
    crossroads = [] 
    for c in range(n_crossroads):
        crossroads += [[random.randrange(0,heightMap.getReadXSize()),
                       random.randrange(0,heightMap.getReadYSize())]]
    crossroads = np.array(crossroads)
    voronoi = Voronoi(crossroads)
    voronoi_verts = voronoi.vertices
    for region in voronoi.regions:
        for i in range(1,len(region)):
            if (region[i] > -1 and region[i-1] > -1):
                pt0 = voronoi_verts[region[i-1]]
                pt1 = voronoi_verts[region[i]]
                painter.drawLine(pt0[0],pt0[1],pt1[0],pt1[1])
            

    return roadMap 
        

def generateCity(cityGeneratorPath,heightMapPath):
    #TODO generate density map
    #TODO call roadmap generator


    hmap = PNMImage()
    hmap.read(heightMapPath)

    roadmap = generateRoadMap(hmap,50)
    roadmap.write('testrmap.pnm')
    exit(0)
    


    return 0

    roadmap = PNMImage()
    roadmap.read('test.png')
    for i in range(roadmap.getReadXSize()):
        for j in range(roadmap.getReadYSize()):
            x= roadmap.getXelVal(i,j)

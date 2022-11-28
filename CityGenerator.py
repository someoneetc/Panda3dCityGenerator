from panda3d.core import PNMImage

def generateCity():
    #TODO generate density map
    #TODO call roadmap generator
    
    roadmap = PNMImage()
    roadmap.read('test.png')
    for i in range(roadmap.getReadXSize()):
        for j in range(roadmap.getReadYSize()):
            if roadmap.getXelVal(i,j)

from direct.showbase.ShowBase import ShowBase

from Panda3dTerrainGenerator import TerrainGenerator
import CityGenerator 

class Test(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        #Generate terrain
        shape = (1025,1025)

        #textures should be put in the following order according with
        #their role(for the time being only 3 textures are supported)
        texture_paths = [
                    'Panda3dTerrainGenerator/example_textures/dirt/Ground042_1K_Color.jpg',
                    'Panda3dTerrainGenerator/example_textures/grass/Grass003_1K_Color.jpg',
                    'Panda3dTerrainGenerator/example_textures/rock/Rock050_1K_Color.jpg',
                    'Panda3dTerrainGenerator/example_textures/snow/Snow006_1K_Color.jpg',
                ]

        #the relative scale factors
        texture_scale_factors = [
                    10,
                    10,
                    10,
                    10
                ]

        #Path to a folder which contains nature objects
        nature_path = 'Panda3dTerrainGenerator/example_nature'

        TerrainGenerator.generateTerrain(
                                         'Panda3dTerrainGenerator',
                                         TerrainGenerator.GENERATORS['FractalCellNoise'],
                                         [TerrainGenerator.MODIFIERS,TerrainGenerator.MODIFIERS['Smooth']],
                                         TerrainGenerator.FINALIZERS['Playability'],
                                         shape,
                                         texture_paths,
                                         texture_scale_factors,
                                         nature_path,
                                         10,
                                         "test", 
                                         force=True
                                        )

        

        CityGenerator.generateCity('.','test/heightmap.pnm')


test = Test()
test.run()

from direct.showbase.ShowBase import ShowBase

import CityGenerator 

class Test(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        CityGenerator.generateCity()


test = Test()
test.run()

"""FishBrowser module: comtains the FishBrowser class"""

from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from panda3d.core import *
from toontown.toonbase import TTLocalizer
from toontown.estate import FlowerSpeciesPanel
from toontown.estate import GardenGlobals

class FlowerBrowser(DirectScrolledList):
    """
    This is the class that handles the photoalbum view of
    the kinds of flowers the toon has collected.  The tab on
    the GardenPage is "Album".
    """
    notify = DirectNotifyGlobal.directNotify.newCategory("FlowerBrowser")

    def __init__(self, parent = aspect2d, **kw):
        self._parent = parent
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        optiondefs = (('parent', self._parent, None),
         ('relief', None, None),
         ('incButton_image', (gui.find('**/FndsLst_ScrollUp'),
           gui.find('**/FndsLst_ScrollDN'),
           gui.find('**/FndsLst_ScrollUp_Rllvr'),
           gui.find('**/FndsLst_ScrollUp')), None),
         ('incButton_relief', None, None),
         ('incButton_scale', (1.3, 1.3, -1.3), None),
         ('incButton_pos', (0, 0, -0.525), None),
         ('incButton_image3_color', Vec4(0.8, 0.8, 0.8, 0.5), None),
         ('decButton_image', (gui.find('**/FndsLst_ScrollUp'),
           gui.find('**/FndsLst_ScrollDN'),
           gui.find('**/FndsLst_ScrollUp_Rllvr'),
           gui.find('**/FndsLst_ScrollUp')), None),
         ('decButton_relief', None, None),
         ('decButton_scale', (1.3, 1.3, 1.3), None),
         ('decButton_pos', (0, 0, 0.525), None),
         ('decButton_image3_color', Vec4(0.8, 0.8, 0.8, 0.5), None),
         ('numItemsVisible', 1, None),
         ('items', map(str, GardenGlobals.getFlowerSpecies()), None),
         ('scrollSpeed', 4, None),
         ('itemMakeFunction', FlowerSpeciesPanel.FlowerSpeciesPanel, None),
         ('itemMakeExtraArgs', base.localAvatar.flowerCollection, None))
        gui.removeNode()
        # Merge keyword options with default options
        self.defineoptions(kw, optiondefs)
        # Initialize superclasses
        DirectScrolledList.__init__(self, parent)
        self.initialiseoptions(FlowerBrowser)

    def destroy(self):
        assert self.notify.debugStateCall(self)
        DirectScrolledList.destroy(self)
        self._parent = None

    #def load(self):
    #    assert self.notify.debugStateCall(self)
    #    pass

    def update(self):
        assert self.notify.debugStateCall(self)
        # removed redundant update call -grw
        pass

    def show(self):
        assert self.notify.debugStateCall(self)
        self['items'][self.index].show()        
        DirectScrolledList.show(self)                

    def hide(self):
        assert self.notify.debugStateCall(self)
        self['items'][self.index].hide()
        DirectScrolledList.hide(self)        


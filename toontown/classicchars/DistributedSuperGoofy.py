"""DistributedSuperGoofy module: contains the DistributedSuperGoofy class"""

from panda3d.core import *
from . import DistributedCCharBase
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from toontown.classicchars import DistributedToontropolisStadium
from . import CharStateDatas
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from . import DistributedCCharBase

class DistributedSuperGoofy(DistributedToontropolisStadium.DistributedToontropolisStadium):
    """DistributedSuperGoofy class"""

    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedSuperGoofy")

    def __init__(self, cr):
        try:
            self.DistributedToontropolisStadium_initialized
        except:
            self.DistributedToontropolisStadium_initialized = 1
            DistributedCCharBase.DistributedCCharBase.__init__(self, cr,
                                                               TTLocalizer.SuperGoofy,
                                                               'sg')
            self.fsm = ClassicFSM.ClassicFSM(self.getName(),
                            [State.State('Off',
                                         self.enterOff,
                                         self.exitOff,
                                         ['Neutral']),
                             State.State('Neutral',
                                         self.enterNeutral,
                                         self.exitNeutral,
                                         ['Walk']),
                             State.State('Walk',
                                         self.enterWalk,
                                         self.exitWalk,
                                         ['Neutral']),
                             ],
                             # Initial State
                             'Off',
                             # Final State
                             'Off',
                             )

            self.fsm.enterInitialState()
            
            # We want him to show up as Goofy
            self.nametag.setName(TTLocalizer.Goofy)
            
    def walkSpeed(self):
        return ToontownGlobals.SuperGoofySpeed

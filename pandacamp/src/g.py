
# Globals are defined here.  Every module should have an
#  import g

# Many of these duplicate top level names ("world", "cam") but the top level
# name shouldn't be used with the library to avoid initialization problems

currentTime = 0      # The current global time
world = None         # The world object, exported to the user variable world
cam = None           # The camera object, exported to the user variable cam
directObj = None     # This is a DirectObject that accepts events from Panda3D
panda3dCamera = None # The original Panda3d camera
objectNames = None   # Hands out unique name to every panda object
eventSignals = {}
newEvents = {}       # Events that are being sensed but not reacted to yet
events = {}          # This is a dictionary of all events posted in the previous tick interval
reactEvents = []     # Reactions that are not part of an object
eventSignals = None  # This is a dictionary of event values received since the last tick
newModels = []       # The new list of active models assembled at every tick
thunks = []
tracking = False
nextNE2dY = .95      # Positioning for 2-D controls
nextNW2dY = .95
tccontext = None
initMousePos = None  # True on the first tick when there is no prior location
mousePos = None      # Last location of the mouse

# Global GUI signals

mouse =       None  # Current mouse position
lbp =         None  # Left button press
lbr =         None  # Left button release
rbp =         None  # Right button press
rbr =         None  # Right button release
lbutton =     None  # Left button state
rbutton =     None  # Right button state
rbuttonPull = None  # "Pulled" 2-D Point for the right button
lbuttonPull = None  # "Pulled" 2-D point for the left button

# Math functions

add = None
sub = None
mul = None
abs = None

# Used to identify signals

nextSignalRef = 0

# Configuration stuff

pandaPath = "/c/panda/lib"
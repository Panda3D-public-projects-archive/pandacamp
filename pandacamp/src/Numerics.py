from Signal import *
from StaticNumerics import *
from Interp import *
import math
from Color import Color
from Control import *
import random

# Basic constructors

P2        = lift(SP2, "P2", numType2, P2Type)
P2Polar   = lift(SP2Polar, 'P2Polar', numType2, P2Type)
P3        = lift(SP3, "P3", numType3, P3Type)
P3C       = lift(SP3C, 'P3C', numType3, P3Type)
HPR       = lift(SHPR, "HPR", numType3, HPRType)

getX      = lift(lambda v:v.x, "getX", [hasXYType], numType)
getY      = lift(lambda v:v.y, "getY", [hasXYType], numType)
getZ      = lift(lambda v:v.z, "getZ", [P3Type], numType)

getH      = lift(lambda v:v.h, "getH", [HPRType], numType)
getP      = lift(lambda v:v.p, "getP", [HPRType], numType)
getR      = lift(lambda v:v.r, "getR", [HPRType], numType)

radians   = lift(math.radians, "radians", numType1, numType)
degrees   = lift(math.degrees, "degrees", numType1, numType)
sin       = lift(math.sin, "sin", numType1, numType)
cos       = lift(math.cos, "cos", numType1, numType)
tan       = lift(math.tan, "tan", numType1, numType)
atan2     = lift(math.atan2, 'atan2', numType2, numType)
sqrt      = lift(math.sqrt, 'sqrt', numType1, numType)
exp       = lift(math.exp, "exp", numType1, numType)
pow       = lift(math.pow, "pow", numType2, numType)
log       = lift(math.log, "log", numType1, numType)

ceiling   = lift(sCeiling, "ceiling", numType1, numType)
floor     = lift(sFloor, "floor", numType1, numType)
fraction  = lift(sFraction, "fraction", numType1, numType)
# sections
add       = lift(lambda x: lambda y: x+y, "add", numType1, fnType)
sub       = lift(lambda x: lambda y: y-x, "sub", numType1, fnType)
times     = lift(lambda x: lambda y: x*y, "times", numType1, fnType)
div       = lift(lambda x: lambda y: x/y, "div", numType1, fnType)

dot       = lift(lambda x,y: genDot(x,y), "dot", infer="dot")
const     = lift(lambda x: lambda y: x, "const", [anyType], fnType)

color     = lift(Color, "color", [numType, numType, numType], ColorType)
colora    = lift(Color, "color", [numType, numType, numType, numType], ColorType)

string    = lift(str, 'string', [anyType], stringType)

norm      = lift(normP3, 'norm', [P3Type], P3Type)

# Interpolation stuff

lerp = lift(lerpStatic, "lerp", infer='interpolate')
interpolate = lift(interpolateStatic, "interpolate", infer='interpolate')
to = lift(toS, "to", infer = "interpolate")
at = lift(atS, "at", infer = "interpolate")
move = lift(moveS, "move", infer = "interpolate")
repeat = lift(repeatS, "repeat", infer = "interpolate")
reverse = lift(reverseS, "reverse", infer = "interpolate")
forever = lift(lambda i: repeatS(-1, i), "forever", infer = "interpolate")
    
P3toHPR = lift(sP3toHPR, "P3toHPR", [P3Type], HPRType)
HPRtoP3 = lift(sHPRtoP3, "HPRtoP3", [HPRType], P3Type)
normA = lift(sNormA, "normA", [numType], numType)

def dist(x,y):
    return abs(x-y)


format    = lift(lambda str, *a: str % a, "format", infer = 'format')

# Lifted conditional

def staticIf(test, x, y):
    if test:
        return x
    return y

choose = lift(staticIf, "choose", infer = "choose")

emptyControl = scEmptyControl
addVal = lift(scAddVal, "addVal", [stringType, anyType, controlType], controlType)
hasVal = lift(scHasVal, "hasVal", [stringType, controlType], boolType)
getVal = lift(scGetVal, "getVal", [stringType, controlType], anyType)
eraseVal = lift(scEraseVal, "eraseVal", [stringType, controlType], controlType)
control = lift(scControl, "control", [stringType, anyType], controlType)

# Non-reactive stuff

def rand(i = None):
    if i is None:
        return random.random()
    if type(i) is type([]):
        return random.choice(i)
    return random.randint(0, i)


step = lift(sStep, "step", numType1, numType)
smoothStep = lift(sSmoothStep, "step", numType1, numType)
import PEffect
#!/usr/bin/env python
#HappyDoc:# These variables should be discovered.
#HappyDoc:TestInt=1
#HappyDoc:TestString="String"
#HappyDoc:TestStringModule=string.strip(' this has spaces in front and back ')
#HappyDoc:url=urlencode({'a':'A', 'b':'B'})
#HappyDoc:docStringFormat='StructuredText'
#
import g
from Handle import *
from pandac.PandaModules import *
from direct.particles.Particles import *
from direct.particles.ParticleEffect import *
#import direct.directbase.DirectStart
#from direct.directbase.TestStart import *
from Numerics import *
from Handle import *
#from Time import uniqueName
from pandac.PandaModules import *
from Color import *

##In future, we should add a duration parameter to these particle effects to
##make it easier to set more useful particle effects.
##Kendric June09
def explosion(color = yellow, endColor = red, size = 1,poolSize = 4000,
              birthRate = 1.000, litterSize = 1000, lifeSpanBase = 1.00,
              terminalVelocityBase = 1.000, emissionType = "ETCUSTOM",
              amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = None, **args):
  return PEffect(colorType = "startEnd", particleFile = 'Explosion.py', color=color,
                 endColor = endColor,size = size, poolSize = poolSize, birthRate = birthRate,
                 litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                 terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
                 amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)

def intervalRings(color = yellow, endColor = red, size = 1,poolSize = 30000,
                  birthRate = 0.0200, litterSize = 500, lifeSpanBase = 6.000,
                  terminalVelocityBase = 400.000, emissionType = "ETCUSTOM",
                  amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 1.00,**args):
  return PEffect(colorType = "startEnd", particleFile = 'IntervalRings.ptf', color=color,
                 endColor = endColor,size = size, poolSize = poolSize, birthRate = birthRate,
                 litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                 terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
                 amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)

def likeFountainWater(color = blue, endColor = green, size = 1, poolSize = 100000,
                      birthRate = 0.0200, litterSize = 10, lifeSpanBase = 3.00,
                      terminalVelocityBase = 400.000, emissionType = "ETRADIATE",
                      amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 7.00,**args):
  return PEffect(colorType = "headTail", particleFile = 'LikeFountainWater.ptf', color=color,
                      endColor = endColor,size = size, poolSize = poolSize,
                      birthRate = birthRate, litterSize = litterSize,
                      lifeSpanBase = lifeSpanBase, terminalVelocityBase = terminalVelocityBase,
                      emissionType = emissionType, amplitude = amplitude,
                      amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)

def shakenSparkles(size = 1, poolSize = 20000, birthRate = 0.0200, litterSize = 10, 
                   lifeSpanBase = 3.00, terminalVelocityBase = 400.000, emissionType = "ETRADIATE",
                   amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 7.00, **args):
  return PEffect(particleFile = 'ShakenSparkles.ptf',size = size, poolSize = poolSize, 
                 colorType = "image", birthRate = birthRate, litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                 terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
                 amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)

def warpSpeed(color = yellow, endColor = red, size = 1, poolSize = 20000,
              birthRate = 0.0200, litterSize = 50, lifeSpanBase = 1.00,
              terminalVelocityBase = 4000.000, emissionType = "ETRADIATE",
              amplitude = 6.00, amplitudeSpread = 0.00, lineScaleFactor = 1.00,**args):
  return PEffect(colorType = "startEnd", particleFile = 'Warpspeed.ptf', color=color,
              endColor = endColor,size = size, poolSize = poolSize, birthRate = birthRate,
              litterSize = litterSize, lifeSpanBase = lifeSpanBase,
              terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
              amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)

def fireish(size = 1,poolSize = 1024, birthRate = 0.0200, litterSize = 10, 
            lifeSpanBase = 0.50, terminalVelocityBase = 4000.000, emissionType = "ETRADIATE",
            amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 1.00, **args):
  return PEffect(colorType = "image", particleFile = 'fireish.ptf', size = size,
                 poolSize = poolSize, birthRate = birthRate, litterSize = litterSize,
                 lifeSpanBase = lifeSpanBase, terminalVelocityBase = terminalVelocityBase,
                 emissionType = emissionType, amplitude = amplitude, amplitudeSpread = amplitudeSpread,
                 lineScaleFactor = lineScaleFactor, **args)

def heavySnow(color = white, endColor = white, size = 1, poolSize = 60000,
              birthRate = 0.0200, litterSize = 100, lifeSpanBase = 6.00,
              terminalVelocityBase = 400.000, emissionType = "ETRADIATE",
              amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 1.00,**args):
  return PEffect(colorType = "startEnd", particleFile = 'heavySnow.ptf', color=color,
                 endColor = endColor, size = size, poolSize = poolSize, birthRate = birthRate,
                 litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                 terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
                 amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)

def lightSnow(color = white, endColor = white, size = 1, poolSize = 60000,
              birthRate = 0.0200, litterSize = 3, lifeSpanBase = 6.00,
              terminalVelocityBase = 400.000, emissionType = "ETRADIATE",
              amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 1.00,**args):
  return PEffect(colorType = "startEnd", particleFile = 'lightSnow.ptf',
                 color=color, endColor = endColor, size = size, poolSize = poolSize,
                 birthRate = birthRate, litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                 terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
                 amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)


class PEffect(Handle):
    """
    PEffect(Handle):
    """
    pid = 1
    def __init__(self, name = None, particleFile = "LikeFountainWater.py",
                defaultPath = True, parent = render, hpr = None, position = None,
                colorType = None, color = gray, endColor = None,
                size = None, birthRate = None, poolSize = None, litterSize = None,
                lineScaleFactor = None, lifeSpanBase = None, terminalVelocityBase = None,
                amplitude = None, amplitudeSpread = None, emissionType = "ETRADIATE"):
        """
        PEffect __init__(self,
                        name = 'PEffect',
                        particleFile = "LikeFountainWater.py",
                        defaultPath = True,
                        parent = render,
                        hpr = None,
                        position = None,
                        color = gray,
                        startColor = None ,
                        endColor = None,
                        headColor = None,
                        tailColor = None,
                        birthRate = None,
                        poolSize = None,
                        litterSize = None,
                        lineScaleFactor = None,
                        lifeSpanBase = None,
                        terminalVelocityBase = None,
                        amplitude = None,
                        amplitudeSpread = None
                        ):
        """
        if name is None:
            name = 'PEffect-%d' % PEffect.pid
            PEffect.pid += 1

        Handle.__init__(self, name = name)
        self.d.colorType = colorType

        #pathname = "/lib/panda/lib/lib-original/particles/"
        base.enableParticles()
        p = ParticleEffect()

        self.__dict__[name] = p
        self.particleName = name

        if defaultPath:
            p.loadConfig(Filename(g.pandaPath+"/particles/"+ particleFile))
        else:
            p.loadConfig(Filename(particleFile))

        pd = p.particlesDict["particles-1"]

        if emissionType is not None:
            if emissionType is "ETRADIATE":
                pd.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)  #emitter type ETEXPICIT ETCUSTOM, ETRADIATE
            elif emissionType is "ETCUSTOM":
                pd.emitter.setEmissionType(BaseParticleEmitter.ETCUSTOM)

        checkKeyType('PEffect', name, stringType, 'name')
        self.__dict__['position'] = newSignalRef(self, 'position', P3Type)
#        self.__dict__['color'] = newSignalRefd(self, 'color', ColorType,color)
        
        self.__dict__['hpr'] = newSignalRefd(self, 'hpr', HPRType, HPR(0,0,0))
        self.__dict__['size'] = newSignalRefd(self, 'size', numType, 1)
        if size is not None:
             self.size.setBehavior(size)
        self.__dict__['color'] = newSignalRefd(self,'color',ColorType,color)# color at which the effect will start
        if endColor is None:
            endColor = color
        self.__dict__['endColor'] = newSignalRefd(self,'endColor',ColorType,endColor)# color at which the effect will end at
        self.color.setBehavior(color)
        if lineScaleFactor is not None:
            self.__dict__['LineScaleFactor'] = newSignalRefd(self,'LineScaleFactor',numType,lineScaleFactor) #how long a particle is
        if poolSize is not None:
            self.__dict__['PoolSize'] = newSignalRefd(self,'PoolSize',numType,poolSize) #Number of particles avaiable for the entire effect
        if birthRate is not None:
            self.__dict__['BirthRate'] = newSignalRefd(self,'BirthRate',numType,birthRate) #The rate in which the particle effect occurs
        if litterSize is not None:
            self.__dict__['LitterSize'] = newSignalRefd(self,'LitterSize',numType,litterSize) #Number of particles per effect occcurance
        if lifeSpanBase is not None:
            self.__dict__['LifeSpanBase']  = newSignalRefd(self,'LIfeSpanBase',numType,lifeSpanBase) #How long the particle effect stays on screen
        if terminalVelocityBase is not None:
            self.__dict__['TerminalVelocityBase'] = newSignalRefd(self,'TerminalVelocityBase',numType,terminalVelocityBase) #how fast the particles move
        if amplitude is not None:
            self.__dict__['Amplitude'] = newSignalRefd(self,'Amplitude', numType, amplitude)#amplitude is the spreading out of particles
        if amplitudeSpread is not None:
            self.__dict__['AmplitudeSpread'] = newSignalRefd(self,'AmplitudeSpread',numType,amplitudeSpread)#amplitude multiplier spreadings of particles.

        if position is not None:
            self.position.setBehavior(position)
        if hpr is not None:
            self.hpr.setBehavior(hpr)
        if color is not None:
            self.color.setBehavior(color)
        if endColor is not None:
            self.endColor.setBehavior(endColor)
        if parent is not render:
            self.__dict__['parent'] = parent.d.model

        g.models.append(self)
        p.reparentTo(render)
        p.start()
        #Had to use this hack because the refresh function kept restarting the particle effects.
        self.__dict__["started"] = True

    def refresh(self):
        """
        refresh(self):
            refreshes the variables in the effect
        """
        name = self.name
        p = self.__dict__[name]#particle effect on our level
        Handle.refresh(self)
        if self.__dict__["started"]:
            p0 = p.particlesDict["particles-1"] #particle effect on panda 3d level
            pr = p0.renderer# renderer settings use this prefix
            pf = p0.factory# factory settings use this prefix
            pe = p0.emitter# emitter settings use this prefix
            #renderer based settings
            if self.d.colorType == "startEnd":
              pr.setStartColor(self.__dict__['color'].now().toVBase4())
              pr.setEndColor(self.__dict__['endColor'].now().toVBase4())
            elif self.d.colorType == "headTail":
              pr.setHeadColor(self.__dict__['color'].now().toVBase4())
              pr.setTailColor(self.__dict__['endColor'].now().toVBase4())
    #        if self.lineScaleFactor is not None:
    #            pr.setLineScaleFactor(self.__dict__['LineScaleFactor'].now())
    #        if self.headColor is not None:
    #            pr.setHeadColor(self.__dict__['HeadColor'].now().toVBase4())
    #        if self.tailColor is not None:
    #            pr.setTailColor(self.__dict__['TailColor'].now().toVBase4())
            #basic particle settings
            #had to comment this one out because it would randomly cause incredible slowdown
            #p0.setPoolSize(self.__dict__['PoolSize'].now())
            p0.setBirthRate(self.__dict__['BirthRate'].now())
            p0.setLitterSize(self.__dict__['LitterSize'] .now())
            #factory based settings
            pf.setLifespanBase(self.__dict__['LifeSpanBase'] .now())
            pf.setTerminalVelocityBase(self.__dict__['TerminalVelocityBase'].now())
            #emitter based settings
            pe.setAmplitude(self.__dict__['Amplitude'].now())
            pe.setAmplitudeSpread(self.__dict__['AmplitudeSpread'].now())

        position = self.__dict__['position'].now()
        x = getX(position)
        y = getY(position)
        z = getZ(position)
        p.setPos(x,y,z)
        hpr = self.__dict__['hpr'].now()
        h = getH(hpr)
        pit = getP(hpr)
        r = getR(hpr)
        p.setHpr(degrees(h), degrees(pit), degrees(r))
        s = self.size.now()
        p.setScale(s)
#        p.particlesDict["particles-1"].emitter.setRadiateOrgin(Point3(x,y,z))
    def exit(self):
        self.__dict__["started"]= False
        name = self.particleName.now()
        p = self.__dict__[name]
        p.disable()
    def stop(self):
        """
        stopP(self):
            stops the emitter from emitting new particles and lets it finish
            the effect on the particles left on screen.
        """
        self.__dict__["started"]= False
        name = self.particleName.now()
        p = self.__dict__[name]
        p.softStop()

    def start(self):
        """
        startP(self):
            starts the Particle effect.
        """
        self.__dict__["started"] = True
        name = self.pid
        p = self.__dict__[self.particleName.now()]
        p.softStart()
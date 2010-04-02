
self.reset()
self.setPos(0.000, 0.000, 0.000)
self.setHpr(0.000, 0.000, 0.000)
self.setScale(1.000, 1.000, 1.000)
p0 = Particles.Particles('particles-1')
# Particles parameters
p0.setFactory("PointParticleFactory")
p0.setRenderer("PointParticleRenderer")
p0.setEmitter("SphereVolumeEmitter")
p0.setPoolSize(20000)
p0.setBirthRate(0.0200)
p0.setLitterSize(50)
p0.setLitterSpread(654)
p0.setSystemLifespan(0.0000)
p0.setLocalVelocityFlag(1)
p0.setSystemGrowsOlderFlag(0)
# Factory parameters
p0.factory.setLifespanBase(1.0000)
p0.factory.setLifespanSpread(2.0000)
p0.factory.setMassBase(6.0000)
p0.factory.setMassSpread(4.0000)
p0.factory.setTerminalVelocityBase(4000.0000)
p0.factory.setTerminalVelocitySpread(0.0000)
# Point factory parameters
# Renderer parameters
p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
p0.renderer.setUserAlpha(1.00)
# Point parameters
#p0.renderer.setPointSize(1.00)
#p0.renderer.setStartColor(Vec4(0.61, 0.59, 1.00, 1.00))
#p0.renderer.setEndColor(Vec4(1.00, 1.00, 1.00, 1.00))
#p0.renderer.setBlendType(PointParticleRenderer.PPONECOLOR)
#p0.renderer.setBlendMethod(BaseParticleRenderer.PPNOBLEND)
# Emitter parameters
p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
p0.emitter.setAmplitude(6.0000)
p0.emitter.setAmplitudeSpread(0.0000)
p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
# Sphere Volume parameters
p0.emitter.setRadius(1.0000)
self.addParticles(p0)

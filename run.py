from toy_model.three_D import Effusion
import pylab

eff = Effusion('dump.crack')
eff.run()
pylab.plot(eff.effusion)
pylab.savefig('trial.png')
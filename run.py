from toy_model.three_D import Effusion
import pylab

eff = Effusion('dump.crack')
eff.run()
pylab.plot(eff.channel_width[20:])
pylab.savefig('channel_width.png')
#print(eff.channel_width)
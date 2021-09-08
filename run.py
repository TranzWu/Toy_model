from toy_model.three_D import Effusion
import pylab

eff = Effusion('dump.crack')
eff.run()
print(eff.avg_channel_width)
pylab.plot(eff.channel_width[20:])
pylab.savefig('channel_width.png')
#print(eff.channel_width)
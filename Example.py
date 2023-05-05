import sys
import matplotlib
#matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()

#---------------------#

#import matplotlib.pyplot as plt
#import numpy as np

#xpoints = np.array([0, 6])
#ypoints = np.array([0, 250])

#plt.plot(xpoints, ypoints)
#plt.show()

#---------------------#

#import sys
#import matplotlib
#matplotlib.use('Agg')

#import matplotlib.pyplot as plt
#import numpy as np

#xpoints = np.array([1, 8])
#ypoints = np.array([3, 10])

#plt.plot(xpoints, ypoints)
#plt.show()

#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()

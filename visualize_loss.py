import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



epochs = []
iterations = []
d_a = []
g_a = []
c_a = []
d_b = []
g_b = []
c_b = []

with open('loss_Log.txt','r') as f:
	lines = f.readlines()
	for l in lines:
		line = l.split(' ')
		epochs.append(int(line[1].replace(',','')))
		iterations.append(int(line[3].replace(',','')))
		d_a.append(float(line[9]))
		g_a.append(float(line[11]))
		c_a.append(float(line[13]))
		d_b.append(float(line[17]))
		g_b.append(float(line[19]))
		c_b.append(float(line[21]))

all_loss = np.array(g_a) + np.array(d_a) + np.array(c_a)
plt.plot(np.array(epochs)[:6000:30], np.array(g_a)[:6000:30], 'g', label='Generator loss')
plt.plot(np.array(epochs)[:6000:30], np.array(d_a)[:6000:30], 'b', label='Discriminator loss')
#plt.plot(np.array(epochs)[:6000:30], all_loss[:6000:30], 'r', label='combiened loss')
plt.title('Generator ($G$) and Discriminator ($D_X$) Training Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
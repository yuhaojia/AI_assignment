import numpy as np
from matplotlib import pyplot as plt
import math

def wei_vis(w):
	w_len = int(math.sqrt(w.shape[0]))
	if w_len*w_len != w.shape[0]:
		w_temp = w[:-1]
	else:
		w_temp = w.copy()
	w_mat = np.reshape(w_temp, (w_len, w_len))
	plt.imshow(w_mat)
	plt.colorbar()
	plt.show()
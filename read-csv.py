import numpy as np
import torch
def load_data(filename, size=None, skip=0):
    u = np.loadtxt(filename, dtype=int, delimiter=',',skiprows=skip, max_rows=size)
    v = torch.from_numpy(u).to(torch.int64)
    return v

"""
Sometimes we want only a small part of a big tensor T and we would like to use tensor like 
torch.Tensor([[0,1],[0,2],[1,0]])
as index (which means we want T[0,1], T[0,2] and T[1,0]).

"""
import torch
import numpy as np

tensor = torch.arange(15).view(5,3)
index = torch.Tensor([[0,1],[0,2],[1,0]])

# Using np.narray as index of torch.Tensor requires x axis and y axis as dim 0 and dim 1, which is the transpose of our array
index_np = index.numpy().T      

print(tensor)
print(tensor[index_np])
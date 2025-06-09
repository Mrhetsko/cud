import torch
from icecream import ic

# Set manual seed
torch.manual_seed(7)
tensor_D = torch.rand(1, 1, 1, 10)
ic(tensor_D)

ic(tensor_D.squeeze())
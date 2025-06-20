import numpy as np
import torch
from icecream import ic


# ic(torch.__version__)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
scalar = torch.tensor(7)
# ic(scalar)
# ic(scalar.ndim)

# ic(scalar.item())

vector = torch.tensor((7,7))
# ic(vector)
# ic(vector.ndim)
# ic(vector.shape)

MATRIX = torch.tensor([
    [7, 8],
    [9, 10]
]).cpu()
# ic(MATRIX)
# ic(MATRIX.shape)
# ic(MATRIX.ndim)
# ic(MATRIX[0])

TENSOR = torch.tensor([[[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]],
                       [[88, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]
                       ])
# ic(TENSOR.ndim)
# ic(TENSOR.shape)
# ic(TENSOR[0].ndim)
# ic(TENSOR[0])
# ic(TENSOR[1])
# ic(TENSOR.size())
# 1h 37m


# Random tensors

random_tensors = torch.rand(3, 4)
# ic(random_tensors)
# ic(random_tensors.shape)
# ic(random_tensors.ndim)


rand_image_size_tensor = torch.rand(size=(5, 10, 10))

# ic(rand_image_size_tensor)
# ic(rand_image_size_tensor.shape)

# ic(rand_image_size_tensor.ndim)

zeros = torch.zeros(3, 4)
# ic(zeros)
# ic(zeros * random_tensors)

ones = torch.ones(3, 4)
# ic(ones)
# ic(ones.dtype)

## RANGE OF TENSORS

one_to_ten = torch.arange(start=1, end=11, step=1)
# ic(one_to_ten)

ten_zeroes = torch.zeros_like(one_to_ten)
# ic(ten_zeroes)

# Float32

float32_tensor = torch.tensor([3.0, 6.0, 9.0],
                              dtype=None,
                              device=device,
                              requires_grad=False)
# ic(float32_tensor)
# ic(float32_tensor.dtype)
# ic(torch.cuda.is_available())
# ic(float32_tensor.device)
# 2h 03m

float16_tensor = float32_tensor.type(torch.float16)
# ic(float16_tensor)

# ic(float16_tensor * float32_tensor)


int32_tensor = torch.tensor([3, 6, 9], dtype=torch.long, device=device)
# ic(int32_tensor)
# ic(int32_tensor.device)


sone_tensor = torch.rand((3, 4), dtype=torch.float16, device=device)
# ic(sone_tensor.dtype)
# ic(sone_tensor.size())
# ic(sone_tensor.shape)
# ic(sone_tensor.device)

# Manipulating tensors

tensor = torch.tensor([1, 2, 3])
tensor += 10


# ic(tensor)
# ic(tensor * 10)
# 2h 35m

# ic(torch.matmul(torch.rand(4, 4), torch.rand(4, 3)))


tensor_A = torch.tensor([[1, 2],
                         [3, 4],
                         [5, 6]])
tensor_B = torch.tensor([[7, 10],
                         [8, 11],
                          [9, 12]
                         ])

resab = torch.mm(tensor_A, tensor_B.T)
# ic(resab)
# ic(tensor_B.shape)
# ic(tensor_B.T.shape)
# 2h 51main


x = torch.arange(0, 100, 10)

# ic(torch.min(x))
# ic(x.min())
#
# ic(x.max())
#
# ic(x.dtype)
# y = x.type(torch.float32)
# ic(y.dtype)
y = x.type(torch.float32)
# ic(y.mean())

# ic(y.argmax())
# ic(y.argmin())
# ic(y[4])

# 3h 06m

x = torch.arange(1., 10.)
# x = torch.arange(1., 13.)
# ic(x)

x_reshaped = x.reshape(1, 9)
# ic(x_reshaped, x_reshaped.shape)

# 3h 11m
# Change the view

z = x.view(1, 9)
# ic(z)

# z[:, 0] = 5

# ic(z)
# ic(x)


# Stack

x_stacked = torch.stack([x, x, x, x], dim=0)

# Squeeze
x_squeezed = x_reshaped.squeeze()

# ic(x_squeezed)
# ic(x_squeezed.shape)

# Permute

a = torch.rand(2, 3, 5)
# ic(a)
# ic(a.size())

b = torch.permute(a, (2, 0, 1))
# ic(b)
# ic(b.size())

# c = torch.rand(5, 3, 2)
# ic(c)
# d = torch.permute(c, (1, 0, 2)) # size 352
# ic(d.size())

x = torch.arange(1, 10)
xx = x.reshape(1, 3, 3)
# ic(x, x.shape)
# ic(xx)

# ic(xx[0])
# ic(xx[0][0])
# ic(xx[0][2])
# ic(xx[0, 2])
# ic(xx[0, 2, 2])

# print(xx[0, 2, 2])
# ic(xx[0, 2, -1:])
# ic(xx[0, :, -1])
# ic(xx[0, :, 2])

# 3h 38 Numpy

array = np.arange(1.0, 8.0)
tensor = torch.from_numpy(array)
# ic(array, tensor)

# 3h 46m

RAND_SEED = 3
torch.manual_seed(RAND_SEED)
random_ta = torch.rand(3, 3)

# torch.manual_seed(RAND_SEED)
# random_tb = torch.rand(3, 3)
# ic(random_ta)
# ic(random_tb)
#
ic(torch.cuda.device_count())
ten = torch.tensor(2, device=device)
ic(ten.device)






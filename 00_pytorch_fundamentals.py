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


ic(tensor)
ic(tensor * 10)
# 2h 35m
import torch

# Створюємо тензор на GPU
x = torch.rand(10000, 10000).to("cuda")
y = torch.mm(x, x)

print("Memory allocated (MB):", torch.cuda.memory_allocated() / 1024**2)
print("Memory reserved (MB):", torch.cuda.memory_reserved() / 1024**2)

import torch
import numpy as np
x = torch.tensor([[1.,0.],[-1.,1.]], requires_grad=True)

z = x.pow(2).sum()
z.backward()
print(z)
x.grad
print(x)
print(z)
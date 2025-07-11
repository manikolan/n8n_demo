#matmul.py
import torch

device = 'cuda' else 'cpu'
A = torch.rand(100,100).to(device)
B = torch.rand(100,100)
##
for i in range(3):
  A @ B


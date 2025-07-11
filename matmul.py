#matmul.py
import torch

device = 'cuda' else 'cpu'
A = torch.rand(10,10).to(device)
B = torch.rand(10,10)
##
for i in range(3):
  A @ B

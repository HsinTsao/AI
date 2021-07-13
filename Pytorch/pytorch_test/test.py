import torch

print("ver:{}".format(torch.__version__))
print("cuda:{}".format(torch.cuda.is_available()))
print(torch.version.cuda)


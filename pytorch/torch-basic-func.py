import torch
import time

def intro():
    a = torch.arange(24).view(2,3,4)
    # tensor.items() turns an 0-d tensor to a Python built-in type (int, float)
    print(a[0,1,2].items()]
    # Note that "view" doesn't change how the tensor is stored, only change how it is used.
    # tensor.view(*args)     view tensor in shape [*args] following the stored order
    print(a.view(3,4,2))
    # tensor.permute(*args)       view tensor in shape [u,v,w] following the dimension order
    # for a 2-d tensor, tensor.permute(1,0) returns its transpose.
    print(a.permute(1,2,0))

    b = torch.arange(12).view(3,1,-1)
    # tensor.expand(...) only expand to a new dimension or expand a dimension whose size=1
    print(b.expand(-1,2,-1))
    print(b.expand(2,-1,-1,-1))
    # tensor.repeat(...) repeat a tensor certain times on certain dimension
    print(b.repeat(3,1,2))

    c = torch.arange(12).view(3,4)
    d = torch.arange(12).view(4,3)
    # torch.einsum("sum->result",a,b)       calculate sum in Einstein notation, 
    print(torch.einsum("ijk,jlk->il",a,b))
    print(torch.einsum("ij,ji->ij",c,d))

    # .view(*args) is equal to .view(*args) or .contiguous().view(*args), depending on whether the tensor is contiguous.
    e = torch.arange(6).reshape(2,3)
    f = torch.arange(20,26).view(2,3)

    # torch.stack() creates a new dimension corresponding to the index of input tuple
    print(torch.stack((e,f)))
    # torch.cat() concatenate input tuple in respect to a dimension within.
    print(torch.cat((e,f),dim=0))
    print(torch.cat((e,f),dim=1))

    g = torch.arange(12).view(3,4,1)
    h = torch.arange(45, 57).view(3,1,4)
    # bmm means batch matrix-matrix product
    print(torch.bmm(g,h))
    # An example of dot product in batches
    print(torch.bmm(h,g))
    

def shuffle_tensor(input):
    shuffle = torch.randperm(len(input))
    output = input[shuffle].view(input.size())
    return output


def compete(func1, args1, func2, args2):
    """
    usage:
    a = torch.rand(12300,23400)
    b = torch.rand(23400,12300)
    compete(torch.einsum, ["ij,jk->ik",a,b], a.mm, [b])
    # torch.einsum() should be slightly slower than tensor.mm()
    """
    start=time.time()
    func1(*args1)
    end=time.time()
    print(f"funtion {func1.__name__} takes {end-start} seconds")

    start=time.time()
    func2(*args2)
    end=time.time()
    print(f"funtion {func2.__name__} takes {end-start} seconds")


if __name__ == "__main__":
    intro()

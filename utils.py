import torch 
import torchvision.transforms as transforms 
from PIL import Image 

def print_examples(model,device,dataset):
    
    transform=transforms.Compose([
        transforms.Resize((299,299)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
    ])
    
    pass 


def save_checkpoint(state,filename="my_checkpoint.pth.tar"):
    print("=> saving checkpoint")
    
    torch.save(state,filename)
    
    
def load_checkpoint(checkpoint,model,optimizer):
    print("=> loading checkpoint")
    
    model.load_state_dict(checkpoint["state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer"])
    step=checkpoint["step"]
    
    return step 
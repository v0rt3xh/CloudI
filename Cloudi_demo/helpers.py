import torch
import numpy as np
import torchvision.transforms as T
from torch.utils.data.dataset import Dataset
from torch.utils.data import DataLoader
import torchvision.utils as vutils
from torchvision import models
import torch.nn as nn
import torch.nn.functional as F

label_names = ['Altocumulus or Cirrocumulus', 'Altostratus or Cirrostratus', 
'Cumulonimbus', 'Cirrus', 'Contrails', 'Cumulus', 
'Nimbostratus or Stratus', 'Stratocumulus']
label_acronym = ['AcCc', 'AsCs', 'Cb', 'Ci', 'Ct', 'Cu', 'NsSt', 'Sc']
model_ft = models.resnet18(pretrained=True)
num_classes = 8
num_ftrs = model_ft.fc.in_features
model_ft.fc = nn.Linear(num_ftrs, num_classes)
path = os.path.dirname(__file__)
themodel = path + "/ResNet_In390_Rotated_83_1.pt"
model_ft.load_state_dict(torch.load(themodel))
model_ft.eval()
CROP_SIZE = 390

def tensorTransform(theCloud):
    transforms = T.Compose([T.Resize(CROP_SIZE), 
    T.ToTensor(),
    T.Normalize((0.485, 0.456, 0.406),(0.229, 0.224, 0.225))])
    outCloud = torch.unsqueeze(transforms(theCloud), 0)
    return outCloud



def Cloud_Predictor(theCloud):
    inCloud = tensorTransform(theCloud)
    with torch.no_grad():    
        preds = model_ft(inCloud)
        # Also need a score for our prediction.
        # In other words, we need the output of the last fully connected layer.
        score = F.softmax(preds, dim = 1)
        top_p, _ = score.topk(1, dim = 1)
        top_p = top_p.item()
        _,predLabel = torch.max(preds, 1)
        labelndex = predLabel.item()
        predLabel = label_names[labelndex]
        description_dir = "Descriptions/" + label_acronym[labelndex] + ".txt"
    return top_p, predLabel, description_dir

""" Pytorch Models for Machine Learning """
""" These Models will be used to recognize the various gestures in images/video that will be 
fed into the model. The model will then output the gesture that it thinks it is. That data will
later be worked on to activate various functions in a smart home automation system. I will first
begin by training the models on dummy data of gestures, then moving on to real data when I can 
properly itegrate the images/video into the model."""

# Imports
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torch import nn, optim

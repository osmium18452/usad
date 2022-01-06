import tensorflow as tf
from dataloader import dataloader
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--epochs", default=50, type=int)
parser.add_argument("-b", "--batch_size", default=50, type=int)
parser.add_argument("-l", "--lr", default=0.001, type=float)
parser.add_argument("-g", "--gpu", default="0")
parser.add_argument("-r", "--ratio", default=0.1, type=float)
parser.add_argument("-m", "--model", default=0, type=int)
parser.add_argument("-f", "--file_name", default="norm.npy", type=str)
args = parser.parse_args()

EPOCHS = args.epochs
BATCH_SIZE = args.batch_size
LEARNING_RATE = args.lr
GPU = args.gpu
TRAIN_SIZE = args.ratio
MODEL = args.model
FILE_NAME = args.file_name

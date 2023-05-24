from datasets import load_dataset, Dataset

dataset = load_dataset("conv_ai")
print(dataset['train'][0])
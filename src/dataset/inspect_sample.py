from src.dataset.loader import load_nih_stream

dataset = load_nih_stream()

# Print dataset feature information
print("Dataset features:")
print(dataset.features)

# Inspect one sample
sample = next(iter(dataset))

print("\nSample:")
print(sample)
label_id = sample["labels"][0]
label_name = dataset.features["labels"].feature.names[label_id]

print("Label ID:", label_id)
print("Disease name:", label_name)

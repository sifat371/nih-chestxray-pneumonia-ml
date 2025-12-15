from datasets import load_dataset

def load_nih_stream(split="train"):
    """
    Loads the NIH ChestX-ray14 dataset using streaming
    (image classification config).
    """
    dataset = load_dataset(
        "alkzar90/NIH-Chest-X-ray-dataset",
        "image-classification",          # ✅ REQUIRED CONFIG
        split=split,
        streaming=True,
        trust_remote_code=True           # ✅ REQUIRED FOR CUSTOM SCRIPT
    )
    return dataset

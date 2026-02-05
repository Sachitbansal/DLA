import os
import shutil

# Paths
SRC_VAL_IMG = "tiny-imagenet-200/val/images"
ANNOT_FILE  = "tiny-imagenet-200/val/val_annotations.txt"
DST_VAL     = "tiny-imagenet-10/val"

# Your chosen 10 classes (must match train)
selected_wnids = [
    "n02124075",
    "n04067472",
    "n04540053",
    "n04099969",
    "n07749582",
    "n01641577",
    "n02802426",
    "n09246464",
    "n07920052",
    "n03970156"
]

os.makedirs(DST_VAL, exist_ok=True)

# Create class folders
for wnid in selected_wnids:
    os.makedirs(os.path.join(DST_VAL, wnid), exist_ok=True)

# Read annotations
with open(ANNOT_FILE, "r") as f:
    for line in f:
        img, wnid, *_ = line.strip().split()

        if wnid in selected_wnids:
            src = os.path.join(SRC_VAL_IMG, img)
            dst = os.path.join(DST_VAL, wnid, img)
            shutil.copy(src, dst)

print("✅ Validation set for 10 classes created successfully.")

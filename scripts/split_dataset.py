import os, shutil, random
from pathlib import Path

images_dir = Path(r"E:\Assignment\images")  
labels_dir = Path(r"E:\Assignment\labels")   
out_dir = Path("dataset_split")

images = [f for f in images_dir.glob("*.jpg") if (labels_dir / (f.stem + ".txt")).exists()]
random.shuffle(images)

n = len(images)
train_split = int(0.8 * n)
val_split = int(0.1 * n)

splits = {
    "train": images[:train_split],
    "val": images[train_split:train_split+val_split],
    "test": images[train_split+val_split:]
}

for split, files in splits.items():
    img_out = out_dir / split / "images"
    lbl_out = out_dir / split / "labels"
    img_out.mkdir(parents=True, exist_ok=True)
    lbl_out.mkdir(parents=True, exist_ok=True)

    for img in files:
        lbl = labels_dir / (img.stem + ".txt")
        shutil.copy(img, img_out / img.name)
        shutil.copy(lbl, lbl_out / lbl.name)

print("Split counts:", {k: len(v) for k,v in splits.items()})

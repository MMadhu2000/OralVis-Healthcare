import os
import yaml

train_path = r"E:\Assignment\dataset_split\train"
val_path = r"E:\Assignment\dataset_split\val"

classes = [
    "Tooth_11", "Tooth_12", "Tooth_13", "Tooth_14", "Tooth_15", "Tooth_16", "Tooth_17", "Tooth_18",
    "Tooth_21", "Tooth_22", "Tooth_23", "Tooth_24", "Tooth_25", "Tooth_26", "Tooth_27", "Tooth_28",
    "Tooth_31", "Tooth_32", "Tooth_33", "Tooth_34", "Tooth_35", "Tooth_36", "Tooth_37", "Tooth_38",
    "Tooth_41", "Tooth_42", "Tooth_43", "Tooth_44", "Tooth_45", "Tooth_46", "Tooth_47", "Tooth_48"
]

data_yaml = {
    'train': train_path,
    'val': val_path,
    'nc': len(classes),
    'names': classes
}

with open("data.yaml", "w") as f:
    yaml.dump(data_yaml, f, default_flow_style=False)

print("✅ data.yaml file created successfully!")

🦷 Tooth Detection Using YOLO
📌 Project Overview

This project focuses on automatic tooth detection and localization using the YOLO (You Only Look Once) object detection framework.
Our goal is to create a robust model capable of identifying individual teeth in dental X-rays, assisting in dental analysis, diagnosis, and treatment planning.

📂 Dataset

Source: Custom dental X-ray dataset.

Annotations: Tooth bounding boxes labeled according to FDI Tooth Numbering System.

Data Split:

70% → Training

20% → Validation

10% → Testing

The dataset was preprocessed, rectified, and structured into train/, val/, and test/ folders with YOLO-compatible .yaml files.

⚙️ Model Training

Framework: YOLOv8 / YOLO11

Hardware: Kaggle GPU

Training Command:

yolo detect train data=data.yaml model=yolov8n.pt epochs=100 imgsz=640


Optimization:

Image augmentation (flip, scale, brightness)

Hyperparameter tuning

Rectification of annotation errors

The model was trained on 100 epochs with a batch size of 16, achieving stable convergence.

📊 Model Evaluation

After training, the model was tested on the test split to evaluate performance.
Evaluation metrics included:

Precision (P)

Recall (R)

mAP@0.5 (Mean Average Precision at IoU 0.5)

mAP@0.5:0.95

Results Summary:

Precision: 0.92

Recall: 0.89

mAP@0.5: 0.91

mAP@0.5:0.95: 0.83

📌 These results show that the model generalizes well across unseen data.

📷 Results & Visualizations
1. Confusion Matrix

(Insert confusion matrix image here)

2. PR Curve (Precision-Recall Curve)

(Insert PR Curve image here)

3. mAP Curve

(Insert mAP curve image here)

4. Example Predictions

(Insert prediction results from test set here — before/after images)

🚀 Usage
Inference

To run detection on new images:

yolo detect predict model=best.pt source="images/"

Validation

To validate model performance:

yolo detect val model=best.pt data=data.yaml

Testing
yolo detect test model=best.pt data=data.yaml

📌 Key Contributions

Curated and rectified a high-quality dental X-ray dataset.

Trained and evaluated a YOLO-based model for tooth detection.

Achieved strong performance metrics (mAP > 0.9).

Provided visual performance analysis (confusion matrix, PR curve, mAP curve).

🔮 Future Work

Tooth classification by type (incisors, canines, premolars, molars).

Detection of dental pathologies (caries, root canal, fillings).

Integration into a clinical decision support system for dentists.

🙌 Acknowledgements

Dataset annotation & preprocessing team.

Open-source YOLO community.

Kaggle GPU resources."# OralVis-Healthcare" 

**🦷 Tooth Detection Using YOLO
📌 Project Overview**

This project focuses on automatic tooth detection and localization using the YOLO (You Only Look Once) object detection framework.
Our goal is to create a robust model capable of identifying individual teeth in dental X-rays, assisting in dental analysis, diagnosis, and treatment planning.

**📂 Dataset
**
Source: Custom dental X-ray dataset.

Annotations: Tooth bounding boxes labeled according to FDI Tooth Numbering System.

**🏷️ Label Validation & Rectification
**

During dataset validation, some annotation files contained BAD_LINE errors (not in the expected YOLO 5-column format: class x_center y_center width height).
To ensure compatibility with YOLOv8, the labels were checked, corrected, and saved back.

**🔎 Steps Performed:**

Checked error lines flagged in label_validation_report.csv.

Converted polygons → bounding boxes using the formulas:

**x_center = (xmin + xmax) / 2

y_center = (ymin + ymax) / 2

width = xmax - xmin

height = ymax - ymin
**
Normalized values to [0,1] relative to image width/height.

Removed unfixable lines (extra/missing values).

Re-saved corrected .txt files into the dataset directory.

**Fixes:
**
1) File: cate2-00029... (original polygon line → fixed YOLO)

Polygon → bbox:

xmin = 0.160156, ymin = 0.568359, xmax = 0.250000, ymax = 0.741211

Converted to YOLO (class 5):

5 0.205078 0.654785 0.089844 0.172852

(center_x=0.205078, center_y=0.654785, width=0.089844, height=0.172852)

2) File: cate2-00109... (line 31)

Polygon → bbox:

xmin=0.616365, ymin=0.387109, xmax=0.629297, ymax=0.485996

YOLO (class 17):

17 0.622831 0.436553 0.012932 0.098886

(center_x=0.622831, center_y=0.436553, width=0.012932, height=0.098886)

3) File: cate2-00109... (line 32)

Polygon → bbox:

xmin=0.602522, ymin=0.526697, xmax=0.611042, ymax=0.579906

YOLO (class 17):

17 0.606782 0.553302 0.008521 0.053210

(center_x=0.606782, center_y=0.553302, width=0.008521, height=0.053210)

4) File: cate5-00030... (line 1)

Polygon → bbox:

xmin=0.104348, ymin=0.486957, xmax=0.186957, ymax=0.640217

YOLO (class 31):

31 0.145652 0.563587 0.082609 0.153261

(center_x=0.145652, center_y=0.563587, width=0.082609, height=0.153261)

**Data Split:**

80% → Training

10% → Validation

10% → Testing

The dataset was preprocessed, rectified, and structured into train/, val/, and test/ folders with YOLO-compatible .yaml files.

⚙️ Model Training

Framework: YOLOv8

Hardware: Kaggle GPU

Training Command:

yolo detect train data=data.yaml model=yolov8n.pt epochs=50 imgsz=640

The model was trained on 50 epochs with a batch size of 16, achieving stable convergence.
**
📊 Model Evaluation
**
After training, the model was tested on the test split to evaluate performance.
Evaluation metrics included:

Precision (P)
<img width="2250" height="1500" alt="BoxP_curve" src="https://github.com/user-attachments/assets/b515e886-6eac-49bc-a84a-221c9a35494f" />

Recall (R)
<img width="2250" height="1500" alt="BoxR_curve" src="https://github.com/user-attachments/assets/f90786ad-eb70-47f0-9e6b-c9b644f4aea0" />

mAP@0.5 (Mean Average Precision at IoU 0.5)

mAP@0.5:0.95

Results Summary:

Precision: 0.92

Recall: 0.89

mAP@0.5: 0.91

mAP@0.5:0.95: 0.83

📌 These results show that the model generalizes well across unseen data.

**📷 Results & Visualizations**

1. Confusion Matrix
<img width="3000" height="2250" alt="confusion_matrix" src="https://github.com/user-attachments/assets/84781e9c-2161-4e19-a3dc-3c4f40632a30" />

2. PR Curve (Precision-Recall Curve)
<img width="2250" height="1500" alt="BoxPR_curve" src="https://github.com/user-attachments/assets/7e4f07ee-90cb-405c-bf75-599774ffce2a" />

3. mAP Curve
<img width="2250" height="1500" alt="BoxF1_curve" src="https://github.com/user-attachments/assets/c5eb41a6-d7fe-4ca7-ba79-2b8b5382e9c3" />


4. Example Predictions:

Lable: ![val_batch0_labels](https://github.com/user-attachments/assets/38672a12-cdd7-41a6-a1d0-21acdd2ab426)

Prediction: ![val_batch0_pred](https://github.com/user-attachments/assets/970e6c2d-e885-4ac1-a716-7ee2ba6ad792)

Lable:![val_batch1_labels](https://github.com/user-attachments/assets/5cbd0689-5441-4899-aaea-1bd3fb6567e5)

Prediction:![val_batch1_pred](https://github.com/user-attachments/assets/3dc9655a-90ee-4b2b-939d-e6b68fe21ceb)


Lable:![val_batch2_labels](https://github.com/user-attachments/assets/e4821e65-416b-459c-987e-37db691fb86b)

Prediction:![val_batch2_pred](https://github.com/user-attachments/assets/4a02eb3e-bbaf-401e-810f-3f118fc53881)


**🚀 Usage
Inference**

To run detection on new images:

yolo detect predict model=best.pt source="images/"

Validation

To validate model performance:

yolo detect val model=best.pt data=data.yaml

Testing
yolo detect test model=best.pt data=data.yaml

**📌 Key Contributions
**
Curated and rectified a high-quality dental X-ray dataset.

Trained and evaluated a YOLO-based model for tooth detection.

Achieved strong performance metrics (mAP > 0.9).

Provided visual performance analysis (confusion matrix, PR curve, mAP curve).
**
🔮 Future Work
**
Tooth classification by type (incisors, canines, premolars, molars).

Detection of dental pathologies (caries, root canal, fillings).

Integration into a clinical decision support system for dentists.

**🙌 Acknowledgements**

Dataset annotation & preprocessing team.

Open-source YOLO community.

Kaggle GPU resources."# OralVis-Healthcare" 

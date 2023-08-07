# Walmart_Hackathon_Team34
Team Name: Fraudsters
Team Captain: Samruddhi Rajole (BTech IT)
Team Member :Manisha Suryawanshi (Btech Comp)
Team Member: Neha Vaidya(BTech IT)
![image](https://github.com/Neha-Vaidya/Walmart_Hackathon_Team34/assets/88196713/67aae032-169e-485c-aeb4-b0b982830888)

 
 References:
 Image Data Set:https://drive.google.com/drive/folders/1Caose_BlGZapeSAUw2w0ExnW3dwR6KTv?usp=drive_link
 DataSet after OCR Extraction: https://docs.google.com/spreadsheets/d/18SWQMFhymNTRr0Dk9mvXasEisRDT1QshU_IWbH_g1fg/edit?usp=drive_link
                               https://drive.google.com/file/d/1-2Q-h1GyUfeD_zJvQP0hsoPc5Se-XRCE/view?usp=drive_link
 



<b>Problem Statement:</b>

<b>SecureClaim - Empowering HR's Fraud-Free Reimbursement Process</b>

Managing employee reimbursement of expenses is a critical task for HR departments. The risk of fraudulent activities related to employee reimbursements poses a significant concern. To address these challenges, we seek an Innovative solution that leverages technology to streamline the entire employee reimbursement 
process, empowering HR departments to efficiently detect fraudulent bills, enhance employee satisfaction,ensure policy compliance, and prevent fraudulent 
activities.Thus, the idea of SecureClaim aligns perfectly with the chosen theme of a machine learning-based fraud detection system.

<b>Architecture:</b>

The streamlined architecture allows us to deliver a functional and reliable fraud detection system
![image](https://github.com/Neha-Vaidya/Walmart_Hackathon_Team34/assets/91827825/599575d1-5393-4f84-a2f9-b5ce6521bb08)

<b>Technologies and Development Tools Used:</b>
Front-end: HTML, CSS, JavaScript
Back-end: Django (Python-based web framework)
Database: SQLite
Machine Learning: Logistic Regression, Naive Bayes
OCR: Tesseract (OCR library)
Model Training: Joblib (for model persistence)
Google Colab (for initial model training and 
experimentation)

The architecture above illustrates the flow of our SecureClaim system. Data collection involves using publicly available bill images or a small dataset, manually labelled as "fraud" or "legitimate." Preprocessing and feature engineering include applying OCR with Tesseract, extracting text, and deriving basic features like total amount, items purchased, and store information.

<b>Implementation Plan </b>

We will begin by collecting publicly available bill images or creating a small dataset for training purposes. By labelling some bills as "fraud" and others as 
"legitimate," using Isolation Forest Algorithm we will create a labelled dataset for model training.Next, we will employ OCR with the Tesseract library to 
convert bill images into text. This extracted text will undergo preprocessing to ensure data quality and relevance. We will extract essential features, such as 
total amount, items purchased, and store information, to form the basis of our model.For model training, we will select a simple classification algorithm like Logistic Regression, Random Forest, Naive Bayes, known for their quick implementation, training times and accuracy. The small labelled dataset will be split into a training set and a validation set for evaluation.

In the real-time prediction phase, we will deploy the trained model in a user-friendly web interface. Users can upload a bill image, and the system will use OCR to extract text and classify the bill as "fraud" or "legitimate." The prediction result will be promptly displayed. At real time we are providing option to user for uploading updated dataset to retrain the model to improve performance and adapt emerging fraud patterns. Our approach is not only innovative but also highly practical, focusing on the critical aspects of data preprocessing, feature engineering, and model selection

<b>
  UI
</b>

![image](https://github.com/Neha-Vaidya/Walmart_Hackathon_Team34/assets/91827825/82a356f4-bfe3-441f-b164-2883e081ec4b)

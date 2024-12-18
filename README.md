Hybrid Expert System for Customer Support Using Rules and Machine Learning
1. Abstract
In this paper, we propose a hybrid expert system for automating customer support queries,
leveraging a combination of rule-based classification and machine learning (ML) for intent
detection. The system is implemented on a large-scale dataset containing 1,041,179 user
queries, manually labeled into nine intent categories. A dual-tier approach was applied: rules
identify predefined intents using expanded keyword-based and regular expression (regex)
patterns, while a TF-IDF + Logistic Regression model serves as a fallback for ambiguous
cases.
Challenges related to data imbalance were addressed through downsampling majority classes
and upsampling minority classes, ensuring balanced performance. The final balanced dataset
contained 135,000 samples, distributed uniformly across intents. Experimental results revealed
82.58% accuracy and high precision across critical categories, demonstrating the robustness
of our hybrid system for real-world deployment.
2. Introduction
Automated customer support has become essential in modern industries to handle the high
volume of inquiries, reduce operational costs, and ensure 24/7 availability. Traditional rule-
based systems offer clear and interpretable outputs but fail in handling nuanced or unseen
queries. Conversely, machine learning (ML)-based approaches provide greater
generalization but suffer from dataset imbalances, overfitting, and computational complexity
(Liu et al., 2018).
This paper introduces a hybrid expert system that integrates:
 A Rule-Based Module for predictable, frequent intents with regex patterns and
expanded keywords.
 A Machine Learning Fallback for ambiguous inputs using TF-IDF vectorization and
Logistic Regression.
The system addresses practical challenges, including:
1. Data Imbalance: Skewed datasets with underrepresented categories like
'refund_request.'
CS-52400-01 Expert System
Hybrid Expert System for Customer Support Using Rules and Machine Learning
Sai Rishi Kiran Mannava(manns02@pfw.edu)
2. Efficiency vs. Accuracy: Ensuring real-time responses while maintaining high
accuracy.
3. Scalability: Handling large-scale user queries in production environments.
3. System Architecture
3.1 System Design
The architecture is divided into three core modules:
1. Preprocessing and Rule-Based Classification:
o Cleans and tokenizes the input text.
o Applies regex patterns and WordNet-based keyword expansion to classify
known intents.
o Outputs an intent if matched; otherwise, it passes the query to the ML fallback.
2. Machine Learning Fallback:
o Uses a TF-IDF vectorizer to represent textual data numerically.
o Employs a Logistic Regression model with class balancing to predict
ambiguous queries.
3. Response Mapping:
o Maps predicted intents to predefined template responses, ensuring clarity and
consistency.
3.2 Rule-Based Module
The rule-based system prioritizes frequent and well-defined intents, reducing computational
overhead. It relies on:
 Regex Patterns: Example for refund requests:
python
Copy code
CS-52400-01 Expert System
Hybrid Expert System for Customer Support Using Rules and Machine Learning
Sai Rishi Kiran Mannava(manns02@pfw.edu)
'refund_request': r"(cancel.*payment|refund|stop.*transaction)"
 Keyword Expansion: Leveraged WordNet (Miller, 1995) to include synonyms like:
o "Refund" → "reimbursement," "money back."
o "Technical issue" → "error," "malfunction," "crash."
3.3 Machine Learning Module
The fallback ML classifier uses:
 TF-IDF Vectorization: N-gram range (1,2) to capture phrases and keywords.
 Logistic Regression: Chosen for its:
o Scalability on large datasets.
o Interpretability and speed in production.
o Effective handling of class imbalances using class_weight='balanced'.
The hybrid flow ensures low latency by routing predictable queries through the rule-based
system, while ambiguous inputs are processed via ML.
4. Dataset
4.1 Dataset Description
The dataset contained over 1,041,179 queries, categorized into intents:
1. account_help
2. complaint
3. delivery_inquiry
4. general_query
5. positive_feedback
6. product_inquiry
7. refund_request
CS-52400-01 Expert System
Hybrid Expert System for Customer Support Using Rules and Machine Learning
Sai Rishi Kiran Mannava(manns02@pfw.edu)
8. support_contact
9. technical_issue
Each row includes:
 Dialogue ID (Unique identifier)
 Text (User query)
 Intent (Manually labeled intent)
4.2 Addressing Imbalanced Data
The dataset was heavily skewed toward the ‘unknown’ class (~65%). To address this:
 Downsampling: Reduced ‘unknown’ samples to 50,000.
 Upsampling: Used bootstrapped resampling to increase minority class samples to
15,000.
Class Initial Count Final Count
Unknown 675,438 50,000
Refund Request 1,067 15,000
Positive Feedback 4,759 15,000
... ... ...
4.3 Synthetic Data
To improve coverage, 900 synthetic queries were generated using templates with
placeholders, e.g.:
 Delivery Inquiry: “Where is my package?” → “Track order #1234.”
5. Implementation
5.1 Preprocessing
Text cleaning involved:
CS-52400-01 Expert System
Hybrid Expert System for Customer Support Using Rules and Machine Learning
Sai Rishi Kiran Mannava(manns02@pfw.edu)
1. Lowercasing and stopword removal.
2. Regex normalization to strip URLs, mentions, and special characters.
5.2 Model Training
 Vectorization: TF-IDF (max_features=5000).
 Classifier: Logistic Regression with balanced class weights.
 Training/Evaluation Split: 80-20.
5.3 Balancing Techniques
Resampling ensured an equal distribution of all intent categories:
python
Copy code
upsampled = resample(minority_class, n_samples=15000, replace=True, random_state=42)
5.4 System Integration
The system prioritizes rules for computational efficiency. If no rule matches:
python
Copy code
intent, method = hybrid_classifier.predict_intent(user_input)
6. Results
The hybrid system was evaluated on the balanced test set:
Metric Value
Accuracy 82.58%
Precision 86.41%
Recall 82.58%
CS-52400-01 Expert System
Hybrid Expert System for Customer Support Using Rules and Machine Learning
Sai Rishi Kiran Mannava(manns02@pfw.edu)
F1 Score 82.70%
6.1 Confusion Matrix
Key insights:
 ‘Refund Request’ and ‘Product Inquiry’ had near-perfect precision and recall.
 ‘General Query’ had high recall (1.00) but lower precision due to overlap.
6.2 Analysis
 Rule vs ML Split: 70% of queries were handled by rules, reducing ML overhead.
 Ambiguity Handling: ML achieved balanced accuracy across minority classes.
7. Discussion
The hybrid architecture presents several advantages:
1. Efficiency: Rules reduce computational costs, making the system scalable.
2. Robustness: ML fallback improves generalization for unseen inputs.
3. Balancing: Downsampling and upsampling techniques ensure fairness across
categories.
Challenges Addressed:
 Imbalanced Data: Class balancing significantly improved recall.
 Ambiguous Queries: ML integration addressed rule limitations.
Limitations:
 Complex intents with multiple sentences may require deep learning models.
8. Conclusion
This hybrid expert system successfully integrates rule-based classification with machine
learning for intent detection, achieving robust and efficient customer support automation.
Future improvements include:
1. Integrating Transformer-based models for higher accuracy.
CS-52400-01 Expert System
Hybrid Expert System for Customer Support Using Rules and Machine Learning
Sai Rishi Kiran Mannava(manns02@pfw.edu)
2. Expanding the intent catalog to handle emerging queries.
9. References
1. Liu, Z., Chen, H., & Huang, J. (2018). A Survey of Automated Customer Support
Systems. Journal of AI Research, 45(1), 110-126.
2. Miller, G. A. (1995). WordNet: A Lexical Database for English. Communications of the
ACM, 38(11), 39-41.
3. Jiang, M., & Huang, S. (2020). Handling Imbalanced Datasets in Text Classification.
IEEE Transactions on Knowledge Engineering, 62(3), 290-298.

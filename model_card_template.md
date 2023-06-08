# Model Card

 - Author: Eduardo Aviles

## Model Details
This model is a Random Forest Classifier trained on the Census Income Dataset from UCI Machine Learning Repository. The model is used to predict whether a person makes over 50K a year based on census data. The model was trained with Python using the Scikit-Learn library.


## Intended Use
The intended use of this model is to predict a person's income bracket based on features such as their education, occupation, and marital status. This could be used for a variety of applications, such as targeted advertising, or to inform public policy decisions.

## Training Data
The training data is the Census Income Dataset, which contains 48,842 instances and 14 attributes including age, workclass, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country, and income. The data was split into a train set and a test set, with 80% of the data used for training and 20% used for testing.

## Evaluation Data
The evaluation data is the test split from the Census Income Dataset. This dataset was used to evaluate the performance of the model after training, and to compute the metrics reported below.


## Metrics
The model was evaluated using precision, recall, and F-beta score. These metrics were calculated for each slice of the categorical features in the dataset as well.

- Precision: 0.7320211960635882,
- Recall: 0.6279220779220779
- Fbeta: 0.6759874169870674

## Ethical Considerations
The model is based on the U.S. Census data, which is a representative sampling of the population, but there may be biases inherent in the data. For example, there may be systematic differences in the way certain demographic groups are represented in the census. Also, the model makes a binary prediction of whether a person makes over or under 50K a year, which is a simplification of the complexity of people's financial situations.

## Caveats and Recommendations
The model is trained on data from the United States, and may not perform well when applied to data from other countries. The model should be used with care when making decisions that could have a significant impact on individuals, and it is recommended to incorporate other sources of information when possible.

## Additional Information
Detailed performance metrics for each slice of the categorical features are as follows:

- Workclass: The model showed the highest precision, recall, and fbeta for individuals who have never worked or without pay, with all scores being 1. The lowest scores were for individuals who are self-employed (not incorporated), with precision, recall, and fbeta scores being around 0.95, 0.91, and 0.93 respectively.
- Education: The model performed best for individuals with preschool education, with a precision of 0 and recall and fbeta of 1. The model performed worst for individuals with HS-grad education, with precision, recall, and fbeta scores being around 0.95, 0.87, and 0.91 respectively.
- Marital-status: The model showed the highest precision, recall, and fbeta for individuals who are married spouse absent, separated, and married AF-spouse, with all scores being 1. The lowest scores were for individuals who are divorced, with precision, recall, and fbeta scores being around 0.97, 0.87, and 0.92 respectively.
- Occupation: The model showed the highest precision, recall, and fbeta for individuals who are in armed forces and private house service, with all scores being 1. The lowest scores were for individuals who are in other-service, with precision, recall, and fbeta scores being around 0.98, 0.83

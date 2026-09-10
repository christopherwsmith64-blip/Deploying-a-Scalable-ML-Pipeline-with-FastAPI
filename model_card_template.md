# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model is a Random Forest classifier used to predict whether a person's
annual salary is greater than $50,000 or less than or equal to $50,000. The
model was built using scikit-learn with a random state of 42. Categorical
features were processed using one-hot encoding before training.

## Intended Use

This model is intended to demonstrate a machine learning pipeline that predicts
whether a person's annual salary is greater than $50,000 based on Census
data. It is intended for educational purposes and should not be used to make
real-world employment, financial, or other decisions about individuals.

## Training Data

The training data comes from the provided Census dataset, which contains 32,561
records. The data includes demographic and employment-related features such as
age, education, occupation, workclass, marital status, and hours worked per
week. The dataset was split into training and test sets, with 80% of the data
used for training. Categorical features were processed using one-hot encoding.

## Evaluation Data

The evaluation data consists of the remaining 20% of the Census dataset that
was held out from model training. The test data was processed using the same
encoder that was fitted to the training data. Model performance was evaluated
on the full test set and separately across each unique value of every
categorical feature.

## Metrics

The model was evaluated using precision, recall, and F1 score. On the test
dataset, the model achieved a precision of 0.7353, recall of 0.6378, and an
F1 score of 0.6831. Performance was also calculated for each unique value
within every categorical feature to identify differences in model performance
across data slices.

## Ethical Considerations

The dataset includes sensitive demographic features such as race and sex, which
could contribute to biased predictions if the model were used in a real-world
setting. Differences in model performance across demographic groups should be
reviewed carefully. The model should not be used to make decisions that could
affect employment, financial opportunities, or access to services.

## Caveats and Recommendations

The model was trained on the provided Census dataset and may not represent
current population or income patterns. Some categories also contain relatively
few records, which can make their individual performance metrics less reliable.
Future improvements could include additional data cleaning, model tuning, and
further analysis of performance differences across demographic groups.
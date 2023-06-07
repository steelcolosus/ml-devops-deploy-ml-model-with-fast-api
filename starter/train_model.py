""" Script to train machine learning model. """
import os
import time
import logging
from sklearn.model_selection import train_test_split
from starter.ml.data import process_data, clean_data
from starter.ml.model import (
    train_model,
    compute_model_metrics,
    inference,
    save
)
from starter.ml.performance_slices import compute_metrics_per_slice
# Add the necessary imports for the starter code.
log_path = os.path.join(
    "logs",
    f"deploy_model_{time.strftime('%b_%d_%Y_%H_%M_%S')}.log"
)

logging.basicConfig(
    level=logging.DEBUG
)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler(log_path)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)


log = logging.getLogger("[TRAIN_MODEL]")
log.propagate = False

log.addHandler(stream_handler)
log.addHandler(file_handler)


# Add code to load in the data.
path = os.path.join(os.path.dirname(__file__), "..", "data", "census.csv")
log.debug("Loading data from %s", path)
data = clean_data(path)
log.debug("splitting data into train and test sets")
train, test = train_test_split(data, test_size=0.20)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

log.debug("Processing train data")
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features,
    label="salary", training=True)

# Process the test data with the process_data function.
log.debug("Processing test data")
X_test, y_test, _, _ = process_data(
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb,
)

# Train and save a model.
log.debug("Training model")
model = train_model(X_train, y_train)

# calculate predictions
log.debug("Calculating predictions")
preds = inference(model, X_test)

# calculate model metrics
log.debug("Calculating model metrics")
precision, recall, fbeta = compute_model_metrics(y_test, preds)
log.debug("Precision: %s, Recall: %s, Fbeta: %s", precision, recall, fbeta)
# save model
BASE_PATH = "model"
log.debug("Saving model, encoder and lb to %s", BASE_PATH)
save(model, os.path.join(BASE_PATH, "model.joblib"))
save(encoder, os.path.join(BASE_PATH, "encoder.joblib"))
save(lb, os.path.join(BASE_PATH, "lb.joblib"))

# compute metrics per slice, and save pandas data frame in  slice_output.txt.
output_file = os.path.join(BASE_PATH, "slice_output.txt")
log.debug("Computing metrics per slice and saving to %s", output_file)
with open(output_file, "w", encoding="utf-8") as f:
    for feature in cat_features:
        df_results = compute_metrics_per_slice(
            model,
            data, cat_features,
            feature,
            encoder,
            lb
        )
        f.write(f'\nResults for feature: {feature}\n')
        f.write(df_results.to_string())
        f.write("\n" + "="*50 + "\n")
log.debug("Done!")

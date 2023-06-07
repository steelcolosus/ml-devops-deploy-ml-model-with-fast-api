
'''
Output the performance of the model on slices of the categorical features.
'''

import pandas as pd
from starter.ml.model import compute_model_metrics, inference
from starter.ml.data import process_data


def compute_metrics_per_slice(model, data, cat_features, feature, encoder, lb):
    '''
    Compute the model metrics for each slice of the feature.
    '''

    unique_values = data[feature].unique()
    results = []

    for value in unique_values:
        # Filter the test data for the current feature value
        sliced_data = data[data[feature] == value]

        # Split the data into X and y
        X_slice, y_slice, _, _ = process_data(
            sliced_data,
            categorical_features=cat_features,
            label='salary',
            encoder=encoder,
            lb=lb,
            training=False
        )

        # Make predictions
        preds = inference(model, X_slice)

        # Compute performance metrics
        precision, recall, fbeta = compute_model_metrics(y_slice, preds)

        results.append({
            'feature_value': value,
            'precision': precision,
            'recall': recall,
            'fbeta': fbeta
        })

    # Save to a dataframe
    df_results = pd.DataFrame(results)

    return df_results

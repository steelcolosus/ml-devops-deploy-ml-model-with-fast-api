''' This file contains the fixtures used in the tests. '''''
import os
import tempfile
import pytest

from starter.ml.model import save, train_model
from starter.ml.data import clean_data, process_data


@pytest.fixture(scope="session")
def user_data_path():
    """
    Returns the path to the user data file.
    """
    path = os.path.join(os.path.dirname(__file__), "..", "data", "census.csv")
    return path


@pytest.fixture(scope="session")  # type: ignore
def cleaned_data(user_data_path):
    """
    Returns the cleaned data from the user data file.
    """
    return clean_data(user_data_path)


@pytest.fixture(scope="session")
def categorical_features(cleaned_data):
    """
    Returns the categorical features from the cleaned data.
    """
    return [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]


@pytest.fixture(scope="session")
def data(cleaned_data, categorical_features):
    """
    Returns the processed data from the cleaned data.
    """

    return process_data(
        cleaned_data,
        categorical_features,
        label="salary",
        training=True
    )


@pytest.fixture(scope="session")
def model(data):
    """
    Trains a machine learning model using the loaded data.
    """
    X, y, _, _ = data
    _model = train_model(X, y)
    return _model


@pytest.fixture(scope="session")
def tmp_path(request):
    """
    Returns a temporary directory unique to the test invocation.
    """
    return tempfile.mkdtemp()


@pytest.fixture(scope="session")
def saved_model_path(tmp_path, model):
    """
    Saves a trained machine learning model to a temporary file.
    """
    model_path = os.path.join(tmp_path, "model.joblib")
    save(model, model_path)
    return model_path

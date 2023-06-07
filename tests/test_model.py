""" Tests for the model module. """
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from starter.ml.model import (
    train_model, compute_model_metrics, inference, load)


def test_train_model(data):
    """
    Tests the train_model function using the loaded data.
    """
    X, y, _, _ = data
    model = train_model(X, y)
    assert model is not None


def test_compute_model_metrics(data, model):
    """
    Tests the compute_model_metrics function using the loaded data and model.
    """
    X, y, _, _ = data
    preds = inference(model, X)
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)


def test_inference(data, model):
    """
    Tests the inference function using the loaded data and trained model.
    """
    X, y, _, _ = data
    preds = inference(model, X)
    assert isinstance(preds, np.ndarray)


def test_save_and_load_model(data, saved_model_path):
    """
    Tests the save_model and load_model functions.
    """
    X, y, _, _ = data
    model = load(saved_model_path)
    preds = inference(model, X)
    assert isinstance(model, RandomForestClassifier)
    assert isinstance(preds, np.ndarray)

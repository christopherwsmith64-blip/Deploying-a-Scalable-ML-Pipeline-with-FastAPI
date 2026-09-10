import pytest
from sklearn.ensemble import RandomForestClassifier

from ml.data import apply_label
from ml.model import compute_model_metrics, train_model


# TODO: implement the first test. Change the function name and input as needed
def test_apply_label():
    """
    Tests that binary predictions are converted to the expected salary labels.
    """
    assert apply_label([1]) == ">50K"
    assert apply_label([0]) == "<=50K"


# TODO: implement the second test. Change the function name and input as needed
def test_train_model():
    """
    Tests that train_model returns a RandomForestClassifier.
    """
    X = [[25, 0], [45, 1], [30, 0], [50, 1]]
    y = [0, 1, 0, 1]

    model = train_model(X, y)

    assert isinstance(model, RandomForestClassifier)


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Tests that compute_model_metrics returns the expected metric values.
    """
    y = [0, 1, 1, 0]
    preds = [0, 1, 1, 0]

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert precision == pytest.approx(1.0)
    assert recall == pytest.approx(1.0)
    assert fbeta == pytest.approx(1.0)

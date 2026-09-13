import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    # activities is mutated in-place by signup/unregister, so restore it after each test
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original)

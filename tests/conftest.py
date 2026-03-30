from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

INITIAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities before each test for deterministic behavior."""
    activities.clear()
    activities.update(deepcopy(INITIAL_ACTIVITIES))
    yield


@pytest.fixture
def client():
    return TestClient(app)

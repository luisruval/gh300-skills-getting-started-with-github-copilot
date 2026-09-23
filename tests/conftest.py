from copy import deepcopy
from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def restore_activities() -> Generator[None, None, None]:
    original_activities = deepcopy(activities)

    yield

    activities.clear()
    activities.update(original_activities)

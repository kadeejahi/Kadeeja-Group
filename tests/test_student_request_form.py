
"""
CampusConnect - T-01 Student Request Form Tests

These tests verify the student submission interface.
They *do not* verify authentication, database storage,
or full input validation.
"""

import sys
from pathlib import Path

# Allow pytest to import the application from src/.
sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from student_request_form import app


def test_request_form_loads():
    """Verify that the submission page loads successfully."""
    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    assert b"Submit a Support Request" in response.data


def test_request_form_displays_fields():
    """Verify that the expected form fields are present."""
    with app.test_client() as client:
        response = client.get("/")

    assert b'name="category"' in response.data
    assert b'name="description"' in response.data
    assert b"Submit Request" in response.data


def test_request_form_receives_submission():
    """Verify that the backend receives sample form data."""
    with app.test_client() as client:
        response = client.post(
            "/",
            data={
                "category": "IT Support",
                "description": "Campus Wi-Fi is not working.",
            },
        )

    assert response.status_code == 200
    assert b"IT Support" in response.data
    assert b"Campus Wi-Fi is not working." in response.data


def test_submission_is_identified_as_preview():
    """Verify that the page does not claim data was saved."""
    with app.test_client() as client:
        response = client.post(
            "/",
            data={
                "category": "Academic",
                "description": "Sample academic request.",
            },
        )

    assert b"Request Preview" in response.data
    assert b"It has not been saved." in response.data

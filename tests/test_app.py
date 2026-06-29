from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_removes_student_from_activity():
    activity_name = "Chess Club"
    participant_email = "michael@mergington.edu"

    response = client.delete(
        f"/activities/{activity_name}/unregister?email={participant_email}"
    )

    assert response.status_code == 200
    assert participant_email not in activities[activity_name]["participants"]

    # Restore the participant for subsequent tests.
    activities[activity_name]["participants"].append(participant_email)

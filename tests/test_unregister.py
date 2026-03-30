def test_unregister_success_removes_participant(client):
    response = client.delete(
        "/activities/Chess%20Club/participants",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Unregistered michael@mergington.edu from Chess Club"

    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]
    assert "michael@mergington.edu" not in participants


def test_unregister_returns_404_for_unknown_activity(client):
    response = client.delete(
        "/activities/Unknown%20Club/participants",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_for_missing_participant(client):
    response = client.delete(
        "/activities/Chess%20Club/participants",
        params={"email": "not-registered@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"

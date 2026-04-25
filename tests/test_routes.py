from app import create_app


def build_client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_home_route():
    client = build_client()
    response = client.get("/")

    assert response.status_code == 200
    data = response.get_json()
    assert data["app"] == "ACEest Fitness & Gym"


def test_workouts_route():
    client = build_client()
    response = client.get("/workouts")

    assert response.status_code == 200
    data = response.get_json()
    assert "workouts" in data
    assert len(data["workouts"]) == 3


def test_members_route():
    client = build_client()
    response = client.get("/members")

    assert response.status_code == 200
    data = response.get_json()
    assert "members" in data
    assert data["members"][0]["name"] == "Rahul"


def test_plans_route():
    client = build_client()
    response = client.get("/plans")

    assert response.status_code == 200
    data = response.get_json()
    assert "plans" in data
    assert data["plans"][1]["plan"] == "Silver"

from locust import HttpUser, task, between

class FlaskAppUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def homepage(self):
        self.client.get("/")

    @task(1)
    def prediction(self):
        with open("tests/Sign2.jpeg", "rb") as image:
            files = {"file": image}
            self.client.post("/prediction", files=files)

    @task(2)
    def static_css(self):
        self.client.get("/static/css/custom.css")

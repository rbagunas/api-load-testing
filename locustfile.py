from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_home(self):
        self.client.get("/")

    @task
    def get_status(self):
        self.client.get("/status")

    @task
    def post_data(self):
        self.client.post("/data", json={"key": "value"})

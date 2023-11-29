from locust import task, FastHttpUser

class TargetURL:
    ROOT = "/"
    STRING = "/string"
    JSON = "/json"
    CALC = "/calc"

class LocustImpl(FastHttpUser):

    @task
    def root(self):
        self.client.get(TargetURL.ROOT)

    @task
    def string(self):
        self.client.get(TargetURL.STRING)

    @task
    def json(self):
        self.client.get(TargetURL.JSON)

    @task
    def calc(self):
        self.client.get(TargetURL.CALC)
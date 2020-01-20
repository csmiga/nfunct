from locust import HttpLocust, TaskSet, task

class Login(TaskSet):
    @task(1)
    def index(self):
        # Support for tests that use multiple hosts
        # https://github.com/locustio/locust/issues/150
        self.client.get("", name="")

class MyLocust(HttpLocust):
    #host = "https://pluto.tv"
    task_set = Login
    min_wait = 5000
    max_wait = 15000

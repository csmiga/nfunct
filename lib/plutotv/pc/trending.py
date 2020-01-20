from locust import HttpLocust, TaskSet, task

class Trending(TaskSet):
    @task(1)
    def index(self):
        # Support for tests that use multiple hosts
        # https://github.com/locustio/locust/issues/150
        self.client.get("https://pluto.tv/trending", name="trending")
        self.client.get("https://pluto.tv/runtime.css", name="runtime.css")
        self.client.get("https://pluto.tv/vendor.css", name="vendor.css")
        self.client.get("https://pluto.tv/main.css", name="main.css")
        self.client.get("https://pluto.tv/runtime.bundle.js", name="runtime.bundle.js")
        self.client.get("https://pluto.tv/vendor.7a6a6f7ac0eb215d4695.js", name="vendor.7a6a6f7ac0eb215d4695.js")
        self.client.get("https://pluto.tv/main.594537fd94900c8964eb.js", name="main.594537fd94900c8964eb.js")
        self.client.get("https://pluto.tv/assets/images/favicons/favicon-large.png", name="favicon-large.png")
        self.client.get("https://pluto.tv/assets/images/favicons/favicon.png", name="favicon.png")
        self.client.get("https://pluto.tv/assets/images/logo.svg", name="logo.svg")
        self.client.get("https://pluto.tv/assets/16x9.png", name="16x9.png")
        self.client.get("https://pluto.tv/pages/Trending.1361a947bba82d2cbcde.js", name="Trending.1361a947bba82d2cbcde.js")

class MyLocust(HttpLocust):
    host = "https://pluto.tv"
    task_set = Trending
    min_wait = 5000
    max_wait = 15000

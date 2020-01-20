from locust import HttpLocust, TaskSet, task

class Ondemand(TaskSet):
    @task(1)
    def index(self):
        # Support for tests that use multiple hosts
        # https://github.com/locustio/locust/issues/150
        self.client.get("https://pluto.tv/on-demand", name="on-demand")
        self.client.get("https://pluto.tv/runtime.css", name="runtime.css")
        self.client.get("https://pluto.tv/vendor.css", name="vendor.css")
        self.client.get("https://pluto.tv/main.css", name="main.css")
        self.client.get("https://pluto.tv/assets/images/favicons/favicon-large.png", name="favicon-large.png")
        self.client.get("https://pluto.tv/assets/images/favicons/favicon.png", name="favicon.png")
        self.client.get("https://api.pluto.tv/v3/vod/categories?includeItems=true&deviceId=1b9654d3-87e7-4aad-ba99-84cbe4354fde&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=bce71bee-a100-40bc-94bc-33525decc686&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="vod/categories")

class MyLocust(HttpLocust):
    #host = "https://pluto.tv"
    task_set = Ondemand
    min_wait = 5000
    max_wait = 15000

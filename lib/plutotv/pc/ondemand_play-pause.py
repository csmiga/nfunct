from locust import HttpLocust, TaskSet, task

class OndemandPlayPause(TaskSet):
    @task(1)
    def index(self):
        # Support for tests that use multiple hosts
        # https://github.com/locustio/locust/issues/150
        self.client.get("https://pluto.tv/on-demand", name="on-demand")
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
        self.client.get("https://pluto.tv/vendors~pages/ChatOnly~pages/ChatOnly-Layout~pages/Vod~pages/Watch~pages/Watch-Layout.9e1d331ed70460da1a6e.js", name="Watch-Layout.9e1d331ed70460da1a6e.js")
        self.client.get("https://pluto.tv/pages/Vod.41b672b4fd577db843bb.js", name="Vod.41b672b4fd577db843bb.js")
        self.client.options("https://api.pluto.tv/v3/vod/categories?includeItems=true&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="vod/categories")
        self.client.get("https://api.pluto.tv/v3/vod/categories?includeItems=true&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="vod/categories")
        self.client.get("https://pluto.tv/vendors~clappr.117b3331d1956bfab199.js", name="vendors~clappr.117b3331d1956bfab199.js")
        self.client.get("https://pluto.tv/assets/images/darkPlaceHolder.png", name="darkPlaceHolder.png")
        self.client.get("https://pluto.tv/38861cba61c66739c1452c3a71e39852.ttf", name="38861cba61c66739c1452c3a71e39852.ttf")
        self.client.options("https://service-stitcher.clusters.pluto.tv/session/063e5ced-3056-4c9a-8e91-f0d3e7ec006c.json?clientTime=1573996332&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="session-opt")
        self.client.get("https://service-stitcher.clusters.pluto.tv/session/063e5ced-3056-4c9a-8e91-f0d3e7ec006c.json?clientTime=1573996332&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="session-get")
        self.client.options("https://service-stitcher.clusters.pluto.tv/session/063e5ced-3056-4c9a-8e91-f0d3e7ec006c.json?clientTime=1573996332&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="session-opt")
        self.client.get("https://service-stitcher.clusters.pluto.tv/session/063e5ced-3056-4c9a-8e91-f0d3e7ec006c.json?clientTime=1573996332&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="session-get")
        self.client.options("https://service-stitcher.clusters.pluto.tv/session/063e5ced-3056-4c9a-8e91-f0d3e7ec006c.json?clientTime=1573996332&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="session-opt")
        self.client.get("https://service-stitcher.clusters.pluto.tv/session/063e5ced-3056-4c9a-8e91-f0d3e7ec006c.json?clientTime=1573996332&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="session-get")
        self.client.options("https://service-stitcher.clusters.pluto.tv/session/063e5ced-3056-4c9a-8e91-f0d3e7ec006c.json?clientTime=1573996332&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="session-opt")
        self.client.get("https://service-stitcher.clusters.pluto.tv/session/063e5ced-3056-4c9a-8e91-f0d3e7ec006c.json?clientTime=1573996332&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="session-get")
        self.client.options("https://service-stitcher.clusters.pluto.tv/session/063e5ced-3056-4c9a-8e91-f0d3e7ec006c.json?clientTime=1573996332&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="session-opt")
        self.client.get("https://service-stitcher.clusters.pluto.tv/session/063e5ced-3056-4c9a-8e91-f0d3e7ec006c.json?clientTime=1573996332&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="session-get")
        self.client.options("https://service-stitcher.clusters.pluto.tv/session/063e5ced-3056-4c9a-8e91-f0d3e7ec006c.json?clientTime=1573996332&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="session-opt")
        self.client.get("https://service-stitcher.clusters.pluto.tv/session/063e5ced-3056-4c9a-8e91-f0d3e7ec006c.json?clientTime=1573996332&deviceId=9ffcc5ed-770c-4059-9990-deb4070eced7&deviceMake=Firefox&deviceType=web&deviceVersion=68.0&DNT=0&sid=063e5ced-3056-4c9a-8e91-f0d3e7ec006c&appName=web&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b", name="session-get")

class MyLocust(HttpLocust):
    #host = "https://pluto.tv"
    task_set = OndemandPlayPause
    min_wait = 5000
    max_wait = 15000

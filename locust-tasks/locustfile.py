from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        headers = {
            "Host": "fesk-plp-prod.fesk.engineering.platform.mnscorp.net",
        }

        self.client.get('/l/beauty/skincare', headers=headers)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior

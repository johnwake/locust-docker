from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get('/')

class WebsiteUser(HttpLocust):
    task_set = UserBehavior

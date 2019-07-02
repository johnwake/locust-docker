# Locust Docker
Docker image for the [Locust](http://locust.io/) load testing tool to be used as apart of CI.

## Usage
The Docker image can be run standalone by passing a URL to your locustfile:

### Configure locustfile
To be able to run locust you need to create a locustfile and enter in your test condictions. Here's a simple example below.

```py
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get('/')

class WebsiteUser(HttpLocust):
    task_set = UserBehavior

```

### Build the Docker image
```bash
docker build --tag locust-docker .
```

### Run using local image
```bash
docker run -p 8089:8089 \      
-e LOCUST_TARGET_HOST='https://www.google.com' \
--name locust locust-docker:latest
```
Then point your web browser to [http://localhost:8089/](http://localhost:8089/)

### Run with no web passing in number or requests and time
```bash
docker run -p 8089:8089 \
-e LOCUST_TARGET_HOST='https://www.google.com' \
-e LOCUST_NO_WEB='true' \
-e LOCUST_USERS_SPAWN='1000' \
-e LOCUST_HATCH_RATE='10' \
-e LOCUST_RUN_TIME='1m' \
--name locust locust-docker:latest
```

#### Run in detached mode
```bash
docker run -d -p 8089:8089 \
...
```

### Pass in custom locustfile from a url
```bash
-e LOCUST_LOCUSTFILE_PATH='https://github.com/johnwake/locust-docker/blob/master/locust-tasks/locustfile.py'
```

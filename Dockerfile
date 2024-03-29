FROM python:3.7.3

# Install packages
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

# Add tasks directory
COPY locust-tasks /locust-tasks

# Set the entrypoint
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5557 5558 8089
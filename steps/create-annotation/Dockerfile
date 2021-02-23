FROM relaysh/core:latest-python
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Create Grafana Annotation"
LABEL "org.opencontainers.image.description"="This step posts an annotation to a Grafana dashboard"
LABEL "com.puppet.nebula.sdk.version"="v1"

To build docker image locally:
```
docker buildx build -f Dockerfile --tag bdirks/pytrace:latest --load .
```

To push to docker hub:
```
docker push bdirks/pytrace:latest
```

FROM alpine:latest

WORKDIR /app

COPY . /app

# Install Python using pyp
RUN apk add --no-cache python3 py3-pip


ENTRYPOINT [ "python3", "/app/app.py" ]








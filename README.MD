Build:
```
docker build -t flask-server:v0.1 .
```
Run:
```
docker run -d -p 5000:5000 --restart=always flask-server:v0.1
```

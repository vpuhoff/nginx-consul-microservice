FROM python:3
EXPOSE 80
CMD sleep 5 && python3 -m http.server --cgi
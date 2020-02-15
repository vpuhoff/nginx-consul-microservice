FROM python:3
EXPOSE 80
COPY ./app /app
WORKDIR /app
RUN python3 -m pip install -r reqs.txt
CMD sleep 5 && python3 -m flask run --host 0.0.0.0
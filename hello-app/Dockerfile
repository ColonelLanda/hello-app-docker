FROM python:3.6-slim
WORKDIR /app
ADD requirements.txt /app/
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ADD . /app
EXPOSE 5000
ENV NAME World
CMD ["python", "app.py"]

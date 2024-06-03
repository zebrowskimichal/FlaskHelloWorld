FROM python:3.9
WORKDIR /app
COPY app.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
#port aplikacji
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

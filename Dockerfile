FROM python:3

WORKDIR /usr/src/body_measures_api

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /usr/src/body_measures_api/api

EXPOSE 5000

CMD ["python",  "app.py"]
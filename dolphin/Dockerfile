FROM python:3.12-alpine

WORKDIR /dolphin-jo.ru

COPY . /dolphin-jo.ru/

RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8026

CMD ["gunicorn", "--bind", "0.0.0.0:8026", "dolphin.wsgi:application"]
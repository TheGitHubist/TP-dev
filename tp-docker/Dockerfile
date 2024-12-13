FROM python

WORKDIR /app

COPY ./app/requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./app/main.py ./main.py

ENTRYPOINT python main.py
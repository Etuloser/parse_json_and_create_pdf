FROM python:3.11

WORKDIR /opt/parse_json_and_create_pdf

COPY . /opt/parse_json_and_create_pdf/

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install -r requirements.txt

EXPOSE 30000

CMD ["uvicorn","--host","0.0.0.0","--port","30000","main:app"]
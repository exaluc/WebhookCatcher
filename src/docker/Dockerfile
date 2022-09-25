FROM python:3.10-slim-buster as builder

LABEL fr.erz.image.authors="Lucian BLETAN"

COPY app/requirements.txt /tmp

RUN \
    pip install --upgrade pip && \
    pip wheel --wheel-dir /wheels -r /tmp/requirements.txt

COPY app /opt/webhookcatcher/
RUN rm -rf /opt/webhookcatcher/.git

FROM python:3.10-slim-buster
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /opt/webhookcatcher

COPY --from=builder /wheels /wheels

RUN pip install --no-cache /wheels/*
COPY --from=builder /opt/webhookcatcher/ /opt/webhookcatcher/
COPY data /opt/datawebhook/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]


FROM python:3.12-slim
RUN useradd -m svc && pip install --no-cache-dir scikit-learn
COPY model/model.pkl /srv/model.pkl
USER svc
CMD ["python", "-c", "print('model server placeholder')"]

FROM public.ecr.aws/bitnami/python:3.8

# Install app
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT []
CMD ["python", "app/main.py"]

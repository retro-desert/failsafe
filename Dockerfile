FROM python:3.12-alpine
ENV Home=/failsafe
ENV Reqs=requirements.txt

WORKDIR $Home

COPY $Reqs $Home
RUN pip install --no-cache-dir -r $Reqs

ADD . $Home

CMD ["python", "-m", "app.main"]
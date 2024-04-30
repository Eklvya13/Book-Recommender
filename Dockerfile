FROM python:latest

WORKDIR /BOOK-RECOMMENDER

COPY . /BOOK-RECOMMENDER/

RUN pip install -r requirements.txt

EXPOSE 8501

CMD [ "streamlit", "run", "app.py" ]
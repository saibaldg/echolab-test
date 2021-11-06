#base image for code
FROM python:3.6

ARG TRAIN_DATA

RUN pip install --upgrade pip
COPY requirements.txt model.py runmodel.py savemodel.py train.csv ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python savemodel.py $TRAIN_DATA
#RUN  pip uninstall pystan;pip install pystan==2.18;pip uninstall holidays;pip install holidays==0.9.12

# command to execute when image loads
ENTRYPOINT ["python","runmodel.py"]
CMD ["forecast"]
#CMD [ "python", "runmodel.py"]

# to rm image: docker rmi --force [id]
# to build:  docker build -t naive-time-series .
# to run: docker run naive-time-series

# TODO: 编写本文件
FROM ufoym/deepo:pytorch-py36-cpu
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install . --no-cache-dir
CMD [ "simplelayout", "-h" ]
MAINTAINER ZYY


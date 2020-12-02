# TODO: 编写本文件
FROM deepo-ssh
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install . --no-cache-dir
CMD [ "simplelayout", "-h" ]
MAINTAINER ZYY


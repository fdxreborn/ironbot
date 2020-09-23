FROM alpine:latest


RUN sed -e 's;^#http\(.*\)/edge/community;http\1/edge/community;g' -i /etc/apk/repositories

#
# Installing Packages
#
RUN apk add freetype-dev --no-cache=true --update \
    coreutils \
    bash \
    build-base \
    bzip2-dev \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    sudo \
    aria2 \
    util-linux \
    libevent \
    jpeg-dev \
    libffi-dev \
    libpq \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    linux-headers \
    musl \
    neofetch \
    openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-dev \
    openssl \
    pv \
    jq \
    wget \
    w3m \
    #python \
    #python-dev \
    python3 \
    python3-dev \
    readline-dev \
    sqlite \
    ffmpeg \
    libjpeg-turbo-dev \
    sqlite-dev \
    libc-dev \
    sudo \
    chromium \
    chromium-chromedriver \
    zlib-dev \
    jpeg 
    
     
    #

RUN curl https://cli-assets.heroku.com/install.sh


RUN python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools \
    && pip3 install wheel \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache




RUN git clone https://github.com/tesbot07/ironbot /root/userbot
RUN mkdir /root/userbot/.bin
WORKDIR /root/userbot/
ENV PATH="/root/userbot/.bin:$PATH"
WORKDIR /root/userbot/

RUN pip3 install -r requirements.txt
CMD ["python3","-m","userbot"]

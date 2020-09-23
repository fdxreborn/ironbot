FROM alpine:latest


RUN git clone https://github.com/tesbot07/ironbot /root/userbot
RUN mkdir /root/userbot/.bin
WORKDIR /root/userbot/
ENV PATH="/root/userbot/.bin:$PATH"
WORKDIR /root/userbot/

RUN pip3 install -r requirements.txt

CMD ["python3","-m","userbot"]
FROM alpine:latest

COPY fonts.conf /root/.fonts.conf
COPY JKG-L_3.ttf /root/.local/share/fonts/

RUN apk update && apk add python3 xvfb firefox dbus && rm -rf /var/cache/apk/*
RUN python3 -m ensurepip
RUN pip3 install --upgrade pip selenium xvfbwrapper

RUN fc-cache -fv

CMD ["python3", "/host/example.py"]

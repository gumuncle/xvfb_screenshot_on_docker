FROM alpine:latest

COPY fonts.conf /root/.config/fontconfig/
# Please override your favorite font file path
COPY JKG-L_3.ttf /root/.local/share/fonts/
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
RUN apk update 
#RUN apk add python3 firefox xvfb dbus jpeg
RUN apk add python3 firefox xvfb dbus jpeg
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev && rm -rf /var/cache/apk/*
ENV LIBRARY_PATH=/lib:/usr/lib
RUN apk upgrade
RUN python -m ensurepip
RUN pip install --upgrade pip selenium xvfbwrapper Pillow

RUN fc-cache -fv
CMD ["python", "/host/cal.py"]

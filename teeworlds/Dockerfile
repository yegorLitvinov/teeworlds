FROM alpine:3.4

env USER teeworlds
env HOME /teeworlds

RUN apk add --no-cache --update teeworlds-server
RUN mkdir $HOME
RUN adduser -u 1020 -h $HOME -D -s /bin/sh $USER
ADD ctf.conf $HOME
RUN chown -R $USER:$USER $HOME

USER $USER
WORKDIR $HOME
EXPOSE 8303:8303/udp
ENTRYPOINT /usr/bin/teeworlds_srv -f $HOME/ctf.conf

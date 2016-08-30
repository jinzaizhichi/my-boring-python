FROM golang:alpine
MAINTAINER NeterOster <neteroster@gmail.com>
ADD . $GOPATH/src/app
RUN go get app
RUN go build app
RUN cp -r $GOPATH/src/app/templates .
EXPOSE 8033
ENTRYPOINT ./app

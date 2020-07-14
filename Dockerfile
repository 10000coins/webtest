FROM alpine/socat:latest

EXPOSE 8080
CMD ["-d", "-d", "TCP-LISTEN:8080,crlf,reuseaddr,fork", "SYSTEM:echo HTTP/1.1 200 OK;"]

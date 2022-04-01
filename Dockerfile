FROM alpine:latest

COPY entrypoint.sh /entrypoint.sh

# change permission to execute the script and
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
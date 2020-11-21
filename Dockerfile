FROM openresty/openresty:1.19.3.1-1-buster

LABEL maintainer="kazu0716"

COPY ./nginx.conf /usr/local/openresty/nginx/conf/nginx.conf
COPY ./conf.d/openrestry.conf /etc/nginx/conf.d/default.conf

RUN apt-get update && apt-get upgrade -y && apt-get install lua-cjson -y

CMD ["/usr/local/openresty/bin/openresty", "-g", "daemon off;"]
FROM nginx:1.25.5
COPY ./Docker/Nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8000
CMD ["nginx", "-g", "daemon off;"]

LABEL description="Image of Nginx application. Install packages and run Nginx server"

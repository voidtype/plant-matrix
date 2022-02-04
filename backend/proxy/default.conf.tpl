server {
    listen ${LISTEN_PORT};
    server_name teraharvest.com

    location / {
        return 301 https://$host$request_uri;
    }

    location /.well-known/acme-challenge/ {
    root /var/www/certbot;
    }
}

server {
    listen 443 ssl;
    server_name teraharvest.com

    ssl_certificate /etc/letsencrypt/live/example.org/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.org/privkey.pem;

    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}

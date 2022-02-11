server {
    listen ${LISTEN_PORT} default_server;
#    server_name _;

    location /.well-known/acme-challenge/ {
    root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl default_server;
    server_name teraharvest.com;

    ssl_certificate /etc/letsencrypt/live/teraharvest.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/teraharvest.com/privkey.pem;

    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location /static {
        alias /vol/static;
    }

    location /api {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
        proxy_set_header X-Forwarded-Proto $scheme;

    }

    location / {
        alias /build/;
    }
}

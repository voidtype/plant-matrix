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
        try_files /vol/$uri @react;
    }

    location /api {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
        proxy_set_header X-Forwarded-Proto $scheme;

    }

    location = /api/users/current {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
        proxy_set_header X-Forwarded-Proto $scheme;

    }

    location @react{
        root /build/;
    }

    location / {
        root /build/;
	try_files $uri $uri/ /index.html;
    }
}

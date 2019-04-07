# nginx_proxy

## What is this?
This is a minimal Rest API built in Flask running on python3.x.

## What does it do?
Initially it now allows just three features:
### /
This is just a welcome message.  
### /config
This route responds two methods: GET and POST. 
- GET will return a json object containing nginx.conf content.
- POST will receive a json object containing nginx.conf content, will replace current nginx.conf file, perform an Nginx config check, reload config and return updated nginx.conf content.
### /stats
Last route will return a json object with Nginx statistic information obtained via Nginx VTS module (https://github.com/vozlt/nginx-module-vts).

## How is it installed?
- Clone this repo.
- Run nginx.sh script.
  - what it does? Installs the following packages: git wget gcc openssl-devel libssl-dev pcre-devel and of course, Nginx.
  - and then what? It compiles VTS module.

## How is it run?
- Run api.py with python3.x (tested with 3.6) as a service or in stdout, I prefer doing it using a screen session, but whatever works for you.
  - quick note: api.py has Flask's app running port, so you can edit it to fit your environment.
- Run Nginx.
- Point your preferred tool to Flask's host/port (in my case Postman, or a browser will do), perform a GET request to `/config` and obtain current Nginx's config, which you can use to POST your editions and apply new stuff.
- Point your browser to Nginx's listening host/port and start playing around.

## Footer
- I've run this solution using Vagrant (CentOS7 box and a few port forwarding).
- This's been tested with the following:
  - CentOS v7.
  - Nginx v1.14.1.
  - Python v3.6.
- I've used a pretty good tool to convert nginx conf to JSON and backwards: https://github.com/nginxinc/crossplane

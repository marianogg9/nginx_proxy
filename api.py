import subprocess, json, crossplane
from flask import Flask, request

conf_file = '/etc/nginx/nginx.conf'                                             # setting up a custom path for nginx.conf file

api = Flask('flaskshell')

# some other useful functions, TODO:
#
# def get_servers():
#     payload = crossplane.parse('nginx.conf')['config'][0]['parsed']
#     output = [x['block'] for x in payload if x['directive'] == 'http']
#
#     ...

@api.route('/')
def api_root():
    return 'Welcome to Nginx API!'

@api.route('/stats/', methods=['GET'])
def get_stats():
    status = 'curl -s http://localhost/status/format/json'
    try:
        return json.dumps(subprocess.getoutput(status),indent=4)
    except subprocess.CalledProcessError as exception:
        return 'An error ocurred while trying to fetch stats. More info: %s' % exception

@api.route('/config/', methods = ['GET', 'POST'])
def config():
    if request.method == 'GET':
        if 'format=text' in request.args:
            try:
                payload = crossplane.parse(conf_file)['config'][0]['parsed']    # fetch nginx config from nginx.conf file
                return crossplane.build(payload)                                # get nginx config as a string
            except Exception as e:
                return 'Error: cannot fetch config. More info: %e' % e
        else:
            try:
                payload = crossplane.parse(conf_file)['config'][0]['parsed']    # fetch nginx config from nginx.conf file
                return json.dumps(payload)
            except Exception as e:
                return 'Error: cannot fetch config. More info: %e' % e
    else:
        try:
            json_data = json.loads(str(request.data, encoding='utf-8'))         # convert POST body into JSON
            payload = crossplane.build(json_data)                               # convert JSON from POST body into nginx conf type

            with open(conf_file,'w+') as f:
                f.write(payload)
                f.close()
            try:
                subprocess.check_output('nginx -t', shell=True)
                subprocess.call('/bin/systemctl reload nginx', shell=True)
            except subprocess.CalledProcessError as proc_error:
                return 'Nginx config failed. More info: %s' % proc_error

            return "Successfully updated Nginx conf!. Here's the new one: \n\n%s" % payload
        except Exception as e:
            return "Something went wrong. More info: %" % e

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8001)

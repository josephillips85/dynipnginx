# dynipnginx
Dynamic IP Upstream and Reverse Proxy Nginx

use this script if you have a upsetram server with a dynamic ip address
And using nginx as reverse Proxy

Modify the Script file
Domain: The Url that have the dynamic IP make sure you are using the same url on proxy_pass directive on nginx configuration
nginxBIN: the path where nginx binary is located
logFile: Path where the logfile will be stored

To install you can add this script on your init.d or systemd

Requiered:Python 3

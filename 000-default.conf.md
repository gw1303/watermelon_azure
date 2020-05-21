# 000-default.conf

```bash
<VirtualHost *:80>
    # The ServerName directive sets the request scheme, hostname and port that
    # the server uses to identify itself. This is used when creating
    # redirection URLs. In the context of virtual hosts, the ServerName
    # specifies what hostname must appear in the request's Host: header to
    # match this virtual host. For the default virtual host (this file) this
    # value is not decisive as it is used as a last resort host regardless.
    # However, you must set it for any further virtual host explicitly.
    #ServerName www.example.com

    WSGIDaemonProcess watermelon_project python-home=/home/gw1303/watermelon/watermelon_venv python-path=/home/gw1303/watermelon/watermelon_project/watermelon_project

    # 주석 몇 줄
    ServerAdmin webmaster@localhost
    WSGIScriptAlias / /home/gw1303/watermelon/watermelon_project/watermelon_project/wsgi.py

    <Directory /home/gw1303/watermelon/watermelon_project/watermelon_project>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    <Directory />
        AllowOverride None
        Require all granted
    </Directory>

    DocumentRoot /var/www/html

    # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
    # error, crit, alert, emerg.
    # It is also possible to configure the loglevel for particular
    # modules, e.g.
    #LogLevel info ssl:warn

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    # For most configuration files from conf-available/, which are
    # enabled or disabled at a global level, it is possible to
    # include a line for only one particular virtual host. For example the
    # following line enables the CGI configuration for this host only
    # after it has been globally disabled with "a2disconf".
    #Include conf-available/serve-cgi-bin.conf
    #nclude conf-available/serve-cgi-bin.conf
</VirtualHost>

```


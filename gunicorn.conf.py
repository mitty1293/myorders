# See: https://docs.gunicorn.org/en/stable/settings.html

debug = False
# bind = '0.0.0.0:8000'
bind = "unix:/var/run/gunicorn/gunicorn.sock"
wsgi_app = "myorders.wsgi"

# Worker Processes
workers = 2
worker_class = "sync"

# Logging
accesslog = "/app/myorders/logs/app_access.log"
errorlog = "/app/myorders/logs/app_error.log"
loglevel = "info"
logconfig = None

# Process Name
proc_name = "gunicorn_myorders_django"

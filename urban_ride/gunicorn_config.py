import gunicorn
import multiprocessing

# Get the workers by CPU
workers = multiprocessing.cpu_count() * 2 + 1

# Bind gunicorn to Port
bind = "0.0.0.0:5000"
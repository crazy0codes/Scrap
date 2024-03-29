import psutil

def check_cpu_usage(threshold=80):
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > threshold:
        return True
    else:
        return False
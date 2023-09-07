import requests
from datadog import initialize, statsd

URL = "https://api.github.com"

options = {'statsd_host':'localhost',
           'statsd_port':8125}

try:
    response = requests.head(URL)
    statsd.gauge('app.http.response.code', response.status_code, sample_rate=1, tags=["env:dev","app:pythonapp"])

except Exception as e:
    print(f"NOT OK: {str(e)}")
else:
    if response.status_code == 200:
        print("OK")
    else:
        print(f"NOT OK: HTTP response code {response.status_code}")


if __name__ == "__main__":
    initialize(**options)

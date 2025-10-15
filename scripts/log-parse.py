
import sys, json, re
for line in sys.stdin:
    m = re.search(r'JOB (?P<name>\S+) STATUS=(?P<status>\w+) DURATION=(?P<sec>\d+)', line)
    if m:
        print(json.dumps({"job": m.group("name"), "status": m.group("status"), "seconds": int(m.group("sec"))}))

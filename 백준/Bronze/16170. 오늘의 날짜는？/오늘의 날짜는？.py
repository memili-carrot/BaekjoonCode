from datetime import datetime, timezone
utc_now = datetime.now(timezone.utc)

print(utc_now.year)
print(utc_now.strftime("%m"))
print(utc_now.strftime("%d"))
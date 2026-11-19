import sys

header = sys.stdin.read().lower()

checks = {
    "spf=fail": "SPF failed: sender server not allowed",
    "dkim=fail": "DKIM failed: signature doesn't match",
    "dmarc=fail": "DMARC failed: domain policy not met",
}

found = [msg for key, msg in checks.items() if key in header]

if found:
    print("SUSPICIOUS")
    for msg in found:
        print("-", msg)
else:
    print("No red flags found")
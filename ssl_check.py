import ssl, socket, json, urllib.request
from datetime import datetime

domains = ["google.com", "github.com", "facebook.com"]
webhook_url = "http://localhost:5678/webhook/ssl-check"

for domain in domains:
    try:
        ctx = ssl.create_default_context()
        conn = ctx.wrap_socket(socket.socket(), server_hostname=domain)
        conn.settimeout(10)
        conn.connect((domain, 443))
        cert = conn.getpeercert()
        conn.close()

        expiry = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
        issuer = dict(x[0] for x in cert['issuer']).get('organizationName', 'Unknown')

        data = json.dumps({
            "domain": domain,
            "valid_to": expiry.isoformat(),
            "issuer": issuer
        }).encode()

        req = urllib.request.Request(webhook_url, data=data,
              headers={'Content-Type': 'application/json'}, method='POST')
        urllib.request.urlopen(req)
        print(f"✅ {domain} sent — expires {expiry.date()}")

    except Exception as e:
        print(f"❌ {domain}: {e}")
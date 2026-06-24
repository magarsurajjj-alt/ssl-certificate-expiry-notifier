# SSL Certificate Expiry Notifier

Automatically monitors SSL certificates and sends 
phone notifications before they expire.

## What it does
- Checks SSL certificates for multiple domains daily
- Calculates days until expiration
- Sends push notifications via ntfy.sh
- Alerts when certificates expire within 30 days

## Tech Stack
- n8n (automation workflow)
- Python 3
- Docker
- ntfy.sh (push notifications)
- Windows Task Scheduler

## How it works
1. Python script checks real SSL certificates
2. Sends data to n8n via Webhook
3. n8n analyzes certificate health
4. Sends notification to your phone

## Setup
1. Install n8n in Docker
2. Import workflow.json into n8n
3. Install ntfy app on phone
4. Subscribe to your topic
5. Run ssl_check.py daily via Task Scheduler

## Notification Types
- HEALTHY — more than 30 days remaining
- WARNING — less than 30 days remaining  
- CRITICAL — less than 14 days remaining
- EXPIRED — certificate has expired

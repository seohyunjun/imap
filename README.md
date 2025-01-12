# IMAP

 To send email using smtplib, you need to have an email account that supports SMTP. If you don't have one, you can create a free account on [Gmail](https://mail.google.com/).

---

#### main.py
``` bash
python main.py --title "test message" --content "this is a test message"
```

#### Output
``` plain
2025-01-12 16:18:30,315 - INFO - SMTP Connection established
2025-01-12 16:18:30,950 - INFO - SMTP Connection secured
2025-01-12 16:18:31,780 - INFO - SMTP xxxxx@gmail.com Login successful
2025-01-12 16:18:35,744 - INFO - Email send to xxxx@gmail.com
2025-01-12 16:18:36,008 - INFO - SMTP Connection closed
```

#### environment variables
``` bash
SMTP_EMAIL="smtp.gmail.com"
EMAIL="xxx@gmail.com"
SMTP_EMAIL_PASSWORD="xxxx xxxx xxxx"
# SSL: 465, TLS: 587
SMTP_PORT=587
```
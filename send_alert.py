ALERT_THRESHOLD = 0.8

def send_alert(risk_score):

    if risk_score >= ALERT_THRESHOLD:
        print("HIGH RISK DETECTED! Alert Triggered!")
        return "Alert Sent"
    else:
        return "Safe"

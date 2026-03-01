import cv2
from detect import detect_crowd
from predict import predict_risk
from send_alert import send_alert

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    crowd_count, results = detect_crowd(frame)
    risk_score = predict_risk(crowd_count)
    alert_status = send_alert(risk_score)

    print(f"Crowd Count: {crowd_count}")
    print(f"Risk Score: {risk_score:.2f}")
    print(f"Status: {alert_status}")

    cv2.imshow("ASTRA - Crowd Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

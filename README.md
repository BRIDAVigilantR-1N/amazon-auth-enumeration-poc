# PoC: Account Enumeration on Buy with Prime Console

## Overview
This repository contains a Proof-of-Concept (PoC) demonstrating an **Account Enumeration** vulnerability within the `console.buywithprime.amazon.com` sign-in flow. The system returns distinct responses for registered versus non-registered email addresses, allowing an attacker to programmatically verify the existence of merchant accounts.

## Vulnerability Detail
- **Target URL:** `https://console.buywithprime.amazon.com`
- **Type:** Account Enumeration
- **Impact:** Attackers can harvest valid merchant email addresses for targeted phishing, credential stuffing, or social engineering attacks.

## Proof of Concept
The provided script `amz_enumv2.py` automates the checking process. It utilizes:
1. **User-Agent Rotation:** To bypass basic browser fingerprinting.
2. **Dynamic Delay:** To mimic human behavior and evade simple rate-limiting.
3. **Response Analysis:** Distinguishes between "Account not found" and "Password prompt/OTP" states.

### Execution
1. Add target emails to `list.txt`.
2. Run the script: `python amz_enumv2.py`.

## Evidence
Refer to the `/evidence` folder for screenshots showing:
- **LIVE ✅**: Valid account detection.
- **GAK ADA ❌**: Non-existent account detection.
- **Anomalous Behavior**: System response changes under high-frequency requests, indicating a bypassable security threshold.

## Remediation
- Implement **Generic Error Messages** that do not reveal whether an account exists.
- Apply stricter **IP-based Rate Limiting**.
- Integrate mandatory CAPTCHAs for repeated failed lookups.
- 

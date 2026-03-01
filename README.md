# PoC: Amazon Buy With Prime Account Enumeration

## Executive Summary
This repository contains a Proof of Concept (PoC) for an Account Enumeration vulnerability found on the `console.buywithprime.amazon.com` login endpoint. The application reveals the existence of registered merchant accounts through distinct error messages.

## Vulnerability Details
- **Endpoint:** `https://console.buywithprime.amazon.com/login`
- **Behavior:** The system returns "Tidak ditemukan akun dengan alamat email tersebut" for non-registered emails, while showing a password prompt for registered ones.

## Potential Impact
An attacker can automate this process to:
1. Identify high-value partner/merchant emails.
2. Facilitate targeted phishing and credential stuffing campaigns.
3. Map out Amazon's B2B ecosystem.

## Usage
Run the provided `amz_enum.py` script to test specific email batches.

## Disclaimer
This research is conducted under the Amazon Vulnerability Research Program. Use only for authorized testing.

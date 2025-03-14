# 3dos-ref
auto refferal 3dos network with proxy support
# Referral Automation Script

## Overview
This script automates the process of creating referrals using temporary emails and proxies. It registers new accounts, verifies emails, and tracks successful and failed referrals.

## Requirements
- Python 3.x
- Required libraries: `requests`, `beautifulsoup4`, `colorama`
## Installation

1. **Clone Repo**

```
git clone https://github.com/adhe222/3dos-ref.git
cd 3dos-ref
```
2. **Install Required Libraries**
   Create a `requirements.txt` file with the following content:
   ```
   requests
   beautifulsoup4
   colorama
   ```

   Then, install the libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Proxy List**
   Create a `proxy.txt` file containing your proxy list, one per line. Example:
   ```
   http://proxy1.example.com:8080
   http://proxy2.example.com:8080
   http://proxy3.example.com:8080
   ```

## Usage
1. **Run the Script**
   After setting up the environment and configuration, run the script using the following command:
   ```bash
   python kontl.py
   ```

2. **Follow Prompts**
   The script will prompt you to enter the number of referrals you want to create and the referral code (if any). Follow the instructions displayed on the screen.

   Example:
   ```
   Masukkan jumlah referral yang diinginkan: 5
   Masukkan Referral Code (jika ada): ABC123
   ```

## Features
- **Generate Random Passwords**: Automatically generates strong, random passwords for each account.
- **Temporary Emails**: Uses the Temp-Mail44 API to generate temporary emails for registration.
- **Proxy Support**: Supports the use of proxies to handle multiple requests and avoid IP blocking.
- **Email Verification**: Automatically checks for verification emails, extracts verification links, and completes the verification process.
- **Track Success and Failures**: Displays a summary of successful and failed referrals at the end of the process.

## Example Output
```
Masukkan jumlah referral yang diinginkan: 5
Masukkan Referral Code (jika ada): ABC123
=== Proses Referral #1 ===
Menggunakan proxy: http://proxy1.example.com:8080
Email Sementara: tempemail1@example.com
Password Otomatis: P@ssw0rd123
Status Code: 200
Response Body: {"success": true, "message": "Registration successful"}
Memeriksa pesan yang masuk...
Pesan yang diterima:
- Dari: no-reply@example.com
  Tanggal: 2023-10-01T12:00:00Z
Tautan verifikasi ditemukan: https://example.com/verify?token=abc123
Verifikasi email berhasil!
...
Ringkasan:
Referral Berhasil: 4
 - tempemail1@example.com
 - tempemail2@example.com
 - tempemail3@example.com
 - tempemail4@example.com
Referral Gagal: 1
 - tempemail5@example.com
```

## Notes
- Ensure you have a stable internet connection.
- Verify that the proxies listed in `proxy.txt` are functional.
- The script assumes that the verification link is contained in an email with the subject "Verify Your Email".
- If you encounter issues, check the logs and ensure all configurations are correct.

## Troubleshooting
- **No Proxy**: If you do not have proxies, the script will still work but may be limited by rate limits or IP blocking.
- **API Key Issues**: Ensure your Temp-Mail44 API key is correct and has sufficient credits.
- **Network Errors**: Check your internet connection and proxy settings.
- **Rate Limiting**: If you receive rate limit errors, consider using more proxies or waiting before retrying.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

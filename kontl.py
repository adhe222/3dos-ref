import requests
import string
import random
import time
import re
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

# Inisialisasi Colorama
init(autoreset=True)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def get_temp_email(proxy=None):
    url = "https://temp-mail44.p.rapidapi.com/api/v3/email/new"
    headers = {
        "authority": "temp-mail44.p.rapidapi.com",
        "method": "POST",
        "path": "/api/v3/email/new",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "0",
        "origin": "https://flexmail.vercel.app",
        "priority": "u=1, i",
        "referer": "https://flexmail.vercel.app/",
        "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "x-rapidapi-host": "temp-mail44.p.rapidapi.com",
        "x-rapidapi-key": "a95ba4ea57mshef963564ef6be07p161285jsn3de0eeae2ee7"
    }
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None
        response = requests.post(url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            data = response.json()
            if 'email' in data:
                return data['email']
            else:
                raise Exception("Gagal mendapatkan email sementara dari Temp-Mail44.")
        else:
            raise Exception(f"Gagal terhubung ke Temp-Mail44 API. Status Code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error saat menghubungi Temp-Mail44 API: {e}")

def check_email_messages(email, proxy=None):
    url = f"https://temp-mail44.p.rapidapi.com/api/v3/email/{email}/messages"
    headers = {
        "authority": "temp-mail44.p.rapidapi.com",
        "method": "GET",
        "path": f"/api/v3/email/{email}/messages",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://flexmail.vercel.app",
        "priority": "u=1, i",
        "referer": "https://flexmail.vercel.app/",
        "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "x-rapidapi-host": "temp-mail44.p.rapidapi.com",
        "x-rapidapi-key": "a95ba4ea57mshef963564ef6be07p161285jsn3de0eeae2ee7"
    }
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None
        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            messages = response.json()
            if isinstance(messages, list) and len(messages) > 0:
                for message in messages:
                    body = message.get('body_html') or message.get('body_text')
                    if body:
                        message['body'] = body
                return messages
            else:
                raise Exception("Tidak ada pesan yang ditemukan.")
        else:
            raise Exception(f"Gagal terhubung ke Temp-Mail44 API. Status Code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error saat menghubungi Temp-Mail44 API: {e}")

def follow_redirect_and_get_final_url(url, proxy=None):
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None
        response = requests.get(url, allow_redirects=True, proxies=proxies)
        return response.url
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error saat mengikuti redirect: {e}")

def extract_link_from_subject(subject):
    url_pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    matches = re.findall(url_pattern, subject)
    if matches:
        return matches[0]
    else:
        raise Exception("Tidak ada tautan verifikasi yang ditemukan dalam subjek email.")

def extract_verification_link_from_html(body, subject):
    if body:
        soup = BeautifulSoup(body, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        if links:
            tracking_link = links[0]
            final_url = follow_redirect_and_get_final_url(tracking_link)
            return final_url
    if subject:
        return extract_link_from_subject(subject)
    raise Exception("Tidak ada tautan verifikasi yang ditemukan dalam pesan.")

def verify_email(verification_link, proxy=None):
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None
        response = requests.get(verification_link, proxies=proxies)
        if response.status_code == 200:
            print(Fore.GREEN + "Verifikasi email berhasil!")
        else:
            raise Exception(f"Gagal melakukan verifikasi email. Status Code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error saat melakukan verifikasi email: {e}")

def main():
    url = "https://api.dashboard.3dos.io/api/auth/register"
    headers = {
        "authority": "api.dashboard.3dos.io",
        "method": "POST",
        "path": "/api/auth/register",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "expires": "0",
        "origin": "https://dashboard.3dos.io",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://dashboard.3dos.io/",
        "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    }
    referral_count = int(input(Fore.YELLOW + "Masukkan jumlah referral yang diinginkan: "))
    referral_code = input(Fore.YELLOW + "Masukkan Referral Code (jika ada): ").strip()
    if not referral_code:
        print(Fore.RED + "Referral Code kosong. Melanjutkan tanpa referral code.")
    with open("proxy.txt", "r") as file:
        proxies = [line.strip() for line in file if line.strip()]
    successful_referrals = []
    failed_referrals = []

    for i in range(referral_count):
        print(Fore.MAGENTA + f"=== Proses Referral #{i+1} ===")
        proxy = proxies[i % len(proxies)] if proxies else None
        print(Fore.CYAN + f"Menggunakan proxy: {proxy}" if proxy else "Tidak menggunakan proxy")
        try:
            email = get_temp_email(proxy)
            password = generate_password()
            print(Fore.GREEN + f"Email Sementara: {email}")
            print(Fore.GREEN + f"Password Otomatis: {password}")
            payload = {
                "email": email,
                "password": password,
                "referral_code": referral_code if referral_code else None,
                "referred_by": referral_code if referral_code else None,
                "country_id": 1
            }
            response = requests.post(url, headers=headers, json=payload, proxies={"http": proxy, "https": proxy} if proxy else None)
            print(Fore.YELLOW + f"Status Code: {response.status_code}")
            print(Fore.YELLOW + f"Response Body: {response.text}")
            if response.status_code == 200:
                print(Fore.CYAN + "Memeriksa pesan yang masuk...")
                time.sleep(10)
                messages = check_email_messages(email, proxy)
                if messages:
                    print(Fore.GREEN + "Pesan yang diterima:")
                    for message in messages:
                        print(Fore.CYAN + f"- Dari: {message.get('from')}")
                        print(Fore.CYAN + f"  Tanggal: {message.get('created_at')}")
                        if "Verify Your Email" in message.get('subject', ''):
                            body = message.get('body', '')
                            subject = message.get('subject', '')
                            verification_link = extract_verification_link_from_html(body, subject)
                            print(Fore.GREEN + f"Tautan verifikasi ditemukan: {verification_link}")
                            verify_email(verification_link, proxy)
                            successful_referrals.append(email)
                else:
                    print(Fore.RED + "Tidak ada pesan yang diterima.")
                    failed_referrals.append(email)
            else:
                print(Fore.RED + "Gagal mendaftar. Silakan coba lagi.")
                failed_referrals.append(email)
        except Exception as e:
            print(Fore.RED + f"Error: {e}")
            failed_referrals.append(email)

    print(Fore.CYAN + "\nRingkasan:")
    print(Fore.GREEN + f"Referral Berhasil: {len(successful_referrals)}")
    for email in successful_referrals:
        print(Fore.GREEN + f" - {email}")
    print(Fore.RED + f"Referral Gagal: {len(failed_referrals)}")
    for email in failed_referrals:
        print(Fore.RED + f" - {email}")

if __name__ == "__main__":
    main()

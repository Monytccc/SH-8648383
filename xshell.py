import requests
import time

def main():
    # Prompt user for the required values
    cookie = input("Masukkan cookie: ")
    channel = input("Masukkan Channel: ")
    xsrf_token = input("Masukkan X-Xsrf-Token: ")

    url = "https://www.xshellz.com/ajax/shell/keep"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Channel": channel,
        "Content-Length": "17",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": cookie,
        "Origin": "https://www.xshellz.com",
        "Priority": "u=1, i",
        "Referer": "https://www.xshellz.com/xpanel/shell/143758",
        "Sec-Ch-Ua": '"Chromium";v="125", "Not.A/Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "X-Xsrf-Token": xsrf_token
    }

    data = {"opid": "143758"}  # Data yang akan dikirim

    while True:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            print("Permintaan berhasil")
            print(response.text)  # Cetak respons dari server jika perlu
        else:
            print(f"Error: {response.status_code}")

        time.sleep(1000)  # Tunggu 1 detik sebelum mengulang permintaan

if __name__ == "__main__":
    main()

import requests

def check_https(url):
    if not url.startswith('http'):
        url = 'http://' + url  # Add http if not present

    try:
        response = requests.get(url, timeout=5)
        if response.url.startswith('https://'):
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def humorous_analysis(is_https):
    if is_https:
        return "This site is as secure as a vault with a password of '1234'!"
    else:
        return "This site is about as secure as a paper bag in a rainstorm!"

def main():
    url = input("Enter the URL of the website to check: ")
    is_https = check_https(url)
    analysis = humorous_analysis(is_https)
    
    if is_https:
        print(f"✅ {url} uses HTTPS! {analysis}")
    else:
        print(f"❌ {url} does not use HTTPS! {analysis}")

if __name__ == "__main__":
    main()

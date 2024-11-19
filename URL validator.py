import validators

def is_valid_url(url):
    return validators.url(url)

url = input("Enter a URL: ")
if is_valid_url(url):
    print(f"{url} is a valid URL.")
else:
    print(f"{url} is an invalid URL.")

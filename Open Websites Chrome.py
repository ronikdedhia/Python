import webbrowser as wb

def webauto():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLS = ("stackoverflow.com", "github.com", "gmail.com",
            "google.co.in", "youtube.com")
    for url in URLS:
        print("Opening: " + url)
        wb.get(chrome_path).open(url)
webauto()

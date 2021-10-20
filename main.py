from SpotifyScraper.scraper import Request, Scraper

request = Request().request()
scraper = Scraper(session=request)
playlist_information = scraper.get_playlist_url_info(url="https://open.spotify.com/playlist/6mZs5jRMpKF31qGSVpI3LF?si=752abcf27f504e0a")
print(playlist_information)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import httpx
from selectolax.parser import HTMLParser


def get_data(store, url, selector):
    resp = httpx.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Brave/701.0.3626.121Safari/537.36"
        },
    )
    html = HTMLParser(resp.text)
    price = html.css_first(selector).text().strip().replace('\xa0', '')
    return{"store": store, "price": price}

def main():
    results = [
        get_data(
            "Amazon", "https://www.amazon.pl/dp/B09Y2MYL5C?th=1", "span.a-offscreen"
        ),
        get_data(
            "x-kom", "https://www.x-kom.pl/p/747460-sluchawki-bezprzewodowe-sony-wh-1000xm5-czarne.html", "div.jwVRpW"
        ),
        get_data(
            "x-kom", "https://www.x-kom.pl/p/747460-sluchawki-bezprzewodowe-sony-wh-1000xm5-czarne.html", "div.jwVRpW"
        ),
        get_data(
            "morele", "https://www.morele.net/sluchawki-sony-wh-1000xm5-czarne-10818330/", "div.product-price"
        )
    ]
    print(results)

if __name__ == "__main__":
    main()

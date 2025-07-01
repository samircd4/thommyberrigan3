import requests
from rich import print
from selectolax.parser import HTMLParser
import pandas as pd


COOKIES = {
    'domain-mixpanel-id_67d13458c807c1abb6f39429756d3810': '$device:19780bfe36266a-06791b905715348-26011e51-1fa400-19780bfe36266a',
    'CreSessionId': '7032bd7e-54b8-402d-8cfc-524f041d1aae',
    '_gcl_au': '1.1.328052599.1750211749',
    '_hjSessionUser_3086717': 'eyJpZCI6ImYwMGIwNzQzLWQyMzMtNWQ4Yy04OGQ4LTVhYTk0MTc4NGI2ZSIsImNyZWF0ZWQiOjE3NTAyMTE3NTAzNTksImV4aXN0aW5nIjp0cnVlfQ==',
    '_gid': 'GA1.3.520720394.1750841186',
    '_lr_env_src_ats': 'false',
    '_lr_geo_location_state': 'C',
    '_lr_geo_location': 'BD',
    '_clck': 'szx4vg%7C2%7Cfx2%7C0%7C1995',
    'ppid': '0000000000000000000000002ecd60ed',
    '_lr_retry_request': 'true',
    'ak_bmsc': '0EB5720C16E3D94F6BE54211E82C1DCE~000000000000000000000000000000~YAAQxKTUF7JbMmWXAQAAAZ2RpxwvoA7/vODriP1E8m46S+kIPRDbAArVZQYtsF06DOdw/cOZ0zfUGEPtGqfLv67WY+n8QGfDN5+NnjQcvxgfbkCUlEa5XMTdUxLJgp7mJ7y+xNcjETpVlQ0T6stCcNckqZc8/T1C+ati1XLy7j3XpJORFHmhKTlJLHXh51+EoRI2zUL0xUxCckZQ3Do+YSaMe2fTcwm0R23LpyWqbcx58X1JQJVty1/vjuJu7WA8jHY//f/+rIIQuXoSz9NCl23HkSSm8IIbAiDLjaaSIFFEHtvinQ0Qlm6g+Vj7m+LrFhzLnRfq7Pzlf9nvzO9kbYrXcE0IQrWEuv5Jx20BzoG03WeJHr3SoY+MVUeMGHR9ApnxJti+BEjHSXl8sufcKuoyrKRxVioye70T19dAQTy7A1GlRLshXIOsk5VszqXatYLgX7w/NU2nSURlG8l+qzxXKsmNhUP5pI4Z59gTWw==',
    '_hjSession_3086717': 'eyJpZCI6IjRiM2UwYjQ3LTJmMjMtNDBiMi04N2RiLWRhMGRmNzdmNTIyMyIsImMiOjE3NTA4NjMwMjc0MTEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    'DM_SitId1457': '1',
    'DM_SitId1457SecId12674': '1',
    'LastSearchSeoUrl': '/for-sale/?kw=Liquidation',
    '_ga_Y1P6W8L5GD': 'GS2.1.s1750863027$o7$g1$t1750863141$j13$l0$h0',
    '_ga': 'GA1.1.1889506923.1750211749',
    '_ga_5EJ2ZSEPWX': 'GS2.1.s1750863027$o6$g1$t1750863141$j13$l0$h0',
    'TEAL': 'v:519780bfe70684781466198913685576f9228672bb8$t:1750864941943$sn:5$en:6$s:1750863026946%3Bexp-sess',
    '_uetsid': 'e19dfdf051a011f09ef7fd19356daf8d',
    '_uetvid': '5c3538e04be711f083a341829d965d92',
    'cto_bundle': 'oXO4f19QSzV0TW05QlFpZzdzOTg4QlhZUTVvdVNVemRIJTJCbE1tM2ZPRUVCMzQlMkZlOEc4RTBCZTRsV1NrZDhGYWhUbTQzeGw0cVoyS2ZOR3Yxa2FBY1RVeWM3U2J3MFp6bWtUbHNFQXdvTFNZRWZKUnBTTFhCMzVha0V2YVVhaGEwMUV4MU9GRm9haXNraEdNQkZia1olMkZnUU1MY3F0MDlCT1NHOWwlMkIwVENSJTJGcDBtclladnJYbFo1TEJtTUlvNUNaYm0yRDclMkYyamF6UmJkazJTeXVZZ3l1NWIwSVNaaHVKSEhwS2hOQ2ZzMnlXVSUyQmFDYyUyRml0NGpCRFBxdzVrVXZURXZyR1clMkJrSmpBaCUyRmE1Z0hYZXdUSUVJVEtDVkZnJTNEJTNE',
    'nol_fpid': 'hmthtvfdxvtqghl0z3mn6nn19zgoj1750211749|1750211749633|1750863142128|1750863142152',
    '_clsk': 'wseb5r%7C1750863762277%7C7%7C1%7Cy.clarity.ms%2Fcollect',
    'bm_sv': 'B3B85477457CB43109B4BDAE9B5B172B~YAAQ7aTUFxVRwJiXAQAAKnyfpxx8sRar5h/7cNn2sVakplD3tOVMZFNR3LxFZUCzgAtfkTN6tT8CGv8o1W43xfuIDE4bg5K4gi49g01M5TiydrBBd5z78wUjNltGnU25aUXDuMqsayGj7xxC9wKO3aN/3Qb6/fd0Hv9dmbKZJ7OoJruU+B+BIie0P7erB6CUVuyOvWdGp1GoxZ4HSP0XNJfPV9QTssFqeqAbMlge48Szr63jef5hKLqsy6218N0sS+7YusL1532EQQQLvaegZwOw~1',
}

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': 'domain-mixpanel-id_67d13458c807c1abb6f39429756d3810=$device:19780bfe36266a-06791b905715348-26011e51-1fa400-19780bfe36266a; CreSessionId=7032bd7e-54b8-402d-8cfc-524f041d1aae; _gcl_au=1.1.328052599.1750211749; _hjSessionUser_3086717=eyJpZCI6ImYwMGIwNzQzLWQyMzMtNWQ4Yy04OGQ4LTVhYTk0MTc4NGI2ZSIsImNyZWF0ZWQiOjE3NTAyMTE3NTAzNTksImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.3.520720394.1750841186; _lr_env_src_ats=false; _lr_geo_location_state=C; _lr_geo_location=BD; _clck=szx4vg%7C2%7Cfx2%7C0%7C1995; ppid=0000000000000000000000002ecd60ed; _lr_retry_request=true; ak_bmsc=0EB5720C16E3D94F6BE54211E82C1DCE~000000000000000000000000000000~YAAQxKTUF7JbMmWXAQAAAZ2RpxwvoA7/vODriP1E8m46S+kIPRDbAArVZQYtsF06DOdw/cOZ0zfUGEPtGqfLv67WY+n8QGfDN5+NnjQcvxgfbkCUlEa5XMTdUxLJgp7mJ7y+xNcjETpVlQ0T6stCcNckqZc8/T1C+ati1XLy7j3XpJORFHmhKTlJLHXh51+EoRI2zUL0xUxCckZQ3Do+YSaMe2fTcwm0R23LpyWqbcx58X1JQJVty1/vjuJu7WA8jHY//f/+rIIQuXoSz9NCl23HkSSm8IIbAiDLjaaSIFFEHtvinQ0Qlm6g+Vj7m+LrFhzLnRfq7Pzlf9nvzO9kbYrXcE0IQrWEuv5Jx20BzoG03WeJHr3SoY+MVUeMGHR9ApnxJti+BEjHSXl8sufcKuoyrKRxVioye70T19dAQTy7A1GlRLshXIOsk5VszqXatYLgX7w/NU2nSURlG8l+qzxXKsmNhUP5pI4Z59gTWw==; _hjSession_3086717=eyJpZCI6IjRiM2UwYjQ3LTJmMjMtNDBiMi04N2RiLWRhMGRmNzdmNTIyMyIsImMiOjE3NTA4NjMwMjc0MTEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; DM_SitId1457=1; DM_SitId1457SecId12674=1; LastSearchSeoUrl=/for-sale/?kw=Liquidation; _ga_Y1P6W8L5GD=GS2.1.s1750863027$o7$g1$t1750863141$j13$l0$h0; _ga=GA1.1.1889506923.1750211749; _ga_5EJ2ZSEPWX=GS2.1.s1750863027$o6$g1$t1750863141$j13$l0$h0; TEAL=v:519780bfe70684781466198913685576f9228672bb8$t:1750864941943$sn:5$en:6$s:1750863026946%3Bexp-sess; _uetsid=e19dfdf051a011f09ef7fd19356daf8d; _uetvid=5c3538e04be711f083a341829d965d92; cto_bundle=oXO4f19QSzV0TW05QlFpZzdzOTg4QlhZUTVvdVNVemRIJTJCbE1tM2ZPRUVCMzQlMkZlOEc4RTBCZTRsV1NrZDhGYWhUbTQzeGw0cVoyS2ZOR3Yxa2FBY1RVeWM3U2J3MFp6bWtUbHNFQXdvTFNZRWZKUnBTTFhCMzVha0V2YVVhaGEwMUV4MU9GRm9haXNraEdNQkZia1olMkZnUU1MY3F0MDlCT1NHOWwlMkIwVENSJTJGcDBtclladnJYbFo1TEJtTUlvNUNaYm0yRDclMkYyamF6UmJkazJTeXVZZ3l1NWIwSVNaaHVKSEhwS2hOQ2ZzMnlXVSUyQmFDYyUyRml0NGpCRFBxdzVrVXZURXZyR1clMkJrSmpBaCUyRmE1Z0hYZXdUSUVJVEtDVkZnJTNEJTNE; nol_fpid=hmthtvfdxvtqghl0z3mn6nn19zgoj1750211749|1750211749633|1750863142128|1750863142152; _clsk=wseb5r%7C1750863762277%7C7%7C1%7Cy.clarity.ms%2Fcollect; bm_sv=B3B85477457CB43109B4BDAE9B5B172B~YAAQ7aTUFxVRwJiXAQAAKnyfpxx8sRar5h/7cNn2sVakplD3tOVMZFNR3LxFZUCzgAtfkTN6tT8CGv8o1W43xfuIDE4bg5K4gi49g01M5TiydrBBd5z78wUjNltGnU25aUXDuMqsayGj7xxC9wKO3aN/3Qb6/fd0Hv9dmbKZJ7OoJruU+B+BIie0P7erB6CUVuyOvWdGp1GoxZ4HSP0XNJfPV9QTssFqeqAbMlge48Szr63jef5hKLqsy6218N0sS+7YusL1532EQQQLvaegZwOw~1',
}




def search(query):
    params = {
        'kw': query,
    }

    response = requests.get('https://www.commercialrealestate.com.au/for-sale/', params=params, cookies=COOKIES, headers=HEADERS)
    ads = []
    if response.status_code == 200:
        html = HTMLParser(response.text)
        ads_ele = html.css('ul.css-l1tire li')
        for ad in ads_ele:
            ad_link = ad.css_first('h2 a').attributes['href']
            print(f"[bold blue]Ad Link:[/bold blue] {ad_link}")
            ads.append(f'https://www.commercialrealestate.com.au{ad_link}')
        return ads
    else:
        print(f"Error: {response.status_code}")
        return None, response.status_code


def get_details(ad_url):
    response = requests.get(ad_url, cookies=COOKIES, headers=HEADERS)
    if response.status_code == 200:
        html = HTMLParser(response.text)
        title = html.css_first('h1.css-1mysost').text(strip=True)
        attr = html.css('ul.css-1pkuoet li')
        ad_type = attr[0].css_first('span.icon-text').text(strip=True) if attr else ''
        squire_metere = attr[1].css_first('span.icon-text').text(strip=True) if len(attr) > 1 else ''
        e_of_i = attr[2].css_first('span.icon-text').text(strip=True) if len(attr) > 2 else ''
        
        description = html.css_first('div.vDetailsDescription').text(strip=True)
        
        return {
            'title': title,
            'ad_type': ad_type,
            'squire_metere': squire_metere,
            'e_of_i': e_of_i,
            'description': description,
            'url': ad_url
        }
    else:
        print(f"Error fetching ad details: {response.status_code}")
        return None

def main():
    query = 'Liquidation'
    print(f"[bold green]Searching for: {query}[/bold green]")
    ads = search(query)
    ads_excel = []
    for ad in ads:
        print(f"[bold yellow]Fetching details for ad:[/bold yellow] {ad}")
        details = get_details(ad)
        if details:
            print(f"[bold cyan]Title:[/bold cyan] {details['title']}")
            print(f"[bold cyan]Ad Type:[/bold cyan] {details['ad_type']}")
            print(f"[bold cyan]Square Meter:[/bold cyan] {details['squire_metere']}")
            print(f"[bold cyan]E of I:[/bold cyan] {details['e_of_i']}")
            print(f"[bold cyan]Description:[/bold cyan] {details['description']}")
            print(f"[bold cyan]URL:[/bold cyan] {details['url']}\n")
            ads_excel.append(details)
        else:
            print("[red]Failed to fetch ad details.[/red]\n")
    
    if ads_excel:
        df = pd.DataFrame(ads_excel)
        df.to_excel('ads_details.xlsx', index=False)
        print("[bold green]Ad details saved to ads_details.xlsx[/bold green]")


if __name__ == "__main__":
    main()
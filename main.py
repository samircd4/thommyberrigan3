import requests
import json
from rich import print
import pandas as pd


def get_list(
        keywords=["Liquidation"],
        page_no=1,
        page_size=200,
        sale_method=None):
    url = "https://www.commercialrealestate.com.au/bf/api/gqlb"
    data = []
    for keyword in keywords:
        variables = {
            "detailsAdId": 0,
            "searchType": 6,
            "saleModeId": 0,
            "pageNo": page_no,
            "pageSize": page_size,
            "sortingOption": 0,
            "categoryIds": [],
            "priceFrom": None,
            "priceTo": None,
            "stateIds": [],
            "regionIds": [],
            "areaIds": [],
            "suburbIds": [],
            "adIds": [],
            "keywords": keyword,
            "agencyIds": [],
            "buildingSizeFrom": None,
            "buildingSizeTo": None,
            "landSizeFrom": None,
            "occupancyStatus": None,
            "carSpaces": None,
            "landSizeTo": None,
            "saleMethod": sale_method if sale_method is not None else [],
            "boundingBox": None,
            "featureFlags": "property-alert-relocation,use-agency-open-search,cre-news-homepage-fy25,prefill-enquiry,featured-properties-homepage-experiment,transport-component,fy25-nbn,listings-copy-seo-experiment,adbridg-ads,static-enquiry-form,related-searches,property-page-bfnew"
        }

        extensions = {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "f8708b9598f15c29e61d58b0a20253fac0b4b54a702864c243e32d5942929d5e"
            }
        }

        params = {
            "operationName": "propertySearchQuery",
            "variables": json.dumps(variables, separators=(',', ':')),
            "extensions": json.dumps(extensions, separators=(',', ':'))
        }

        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,bn;q=0.8",
            "content-type": "application/json",
            "priority": "u=1, i",
            "referer": "https://www.commercialrealestate.com.au",
            "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
        }

        cookies = {
            # You can split the cookie string by '; ' and then by '=' to build this dict
            "domain-mixpanel-id_67d13458c807c1abb6f39429756d3810": "$device:19780bfe36266a-06791b905715348-26011e51-1fa400-19780bfe36266a",
            "_gcl_au": "1.1.328052599.1750211749",
            "_hjSessionUser_3086717": "eyJpZCI6ImYwMGIwNzQzLWQyMzMtNWQ4Yy04OGQ4LTVhYTk0MTc4NGI2ZSIsImNyZWF0ZWQiOjE3NTAyMTE3NTAzNTksImV4aXN0aW5nIjp0cnVlfQ==",
            "_lr_env_src_ats": "false",
            "_gid": "GA1.3.1433061516.1751328620",
            "_lr_geo_location_state": "C",
            "_lr_geo_location": "BD",
            "_clck": "szx4vg%7C2%7Cfx8%7C0%7C1995",
            "DM_SitId1457": "1",
            "DM_SitId1457SecId12674": "1",
            "DEVICE_SESSIONID": "617ea13f-aa53-4a62-b6fe-5b400e8c567b",
            "CreSessionId": "9c33f5ec-8c09-4977-8c67-daebacc180a2",
            "ppid": "000000000000000000000000c6a207d1",
            "_ga": "GA1.1.1889506923.1750211749",
            "_uetsid": "c6988490560f11f0a78d77395e17ac87",
            "_uetvid": "5c3538e04be711f083a341829d965d92",
            "cto_bundle": "swZ-G19PQjU5RlBSZlZOS3lpR3U0ZSUyQjNSbFc3RVNCZUtWOXpLMW5hd2JpRHVOaE9OdmRoQ1JObTkySzBFZ2psaVVVQXElMkJaUUkwQUglMkZ3SW84UUlFc1BzJTJCdmIxd2FwMSUyRnY1NUU1SUtVQWY4aUltY2drRUl2WTBEcTAlMkI3byUyRjExJTJCJTJGRGxUdXRnTFprZlZ1Z2tzNlMlMkJWb2ZCM1lCbCUyQnM1TWJDTjRVM2RqczclMkI1dW93VmlrQWlaSHRkdXg0TXNyViUyQm5lMW1FRTJhcVJ6cndOWGdUQjdiRCUyQmJGV1l4OE1RSFdCdHEzck8wM2c4YlM3enptQVlUYnhKZjA5bmkxUUZRR1ZwVHRMWVclMkJHZlpxeHphTmV6JTJGJTJGNzI0anhqeEx0JTJGcW9OMjNpJTJCWXFONzdCT2FtQTc2R1BSQnhvbm9XcVhZdEZHZlNzcWQwTEp4ZkpXcVZZdjB3MzR3R3R1aWdyQSUzRCUzRA",
            "nol_fpid": "hmthtvfdxvtqghl0z3mn6nn19zgoj1750211749|1750211749633|1751330331878|1751330332046",
            "_hjSession_3086717": "eyJpZCI6ImYxOWIxYTYzLWUxYmQtNDZjOS1iZDlmLWQ1YTJmODZhNjRlZCIsImMiOjE3NTEzNTUyMDMxNDEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=",
            "ak_bmsc": "8EF3D99E17A2ADED46C771F339D9F14F~000000000000000000000000000000~YAAQz6TUF9z7sa2XAQAAj6DnxBxpotaczNCdl+1dURn9MAepS9iBsWJnRv/+HMv04pSvnlY/2WwYjWOuSNIOYyW9D0Medj2YjPu0sS3qsuI5M9SQTnCz/WGmT25ua+JcS+SNGNKSOY/WjwwS1bhg6asOWGfnBJbhtYEGmdZ96CQ/jS9cNIfWoirBhXXS763HeYtpqkPb5XSeTLP7Z6p39D5ZPq59/oG5d2X9ygyI3p+jOeBqbRoCGH7jb9SSefDjA0JYwY3mTPggOT0x6KyDZ9+bMImB8tr6/lBbkl+2y9pCarorndsnDeM2cxxgfK0gZm10vga4nfrZco5wILzLaxJyQo0LRQd8n8CTO6oTP9TDJVDurZN0iRiL4ceBmDBf+CLBxUN5v+Og+/bK8gcoPXOM5HoAtwrR6c+fut8=",
            "LastSearchSeoUrl": "/for-sale/?pn=2&sm=standard",
            "_clsk": "7jbqmw%7C1751355544557%7C7%7C1%7Cy.clarity.ms%2Fcollect",
            "TEAL": "v:519780bfe70684781466198913685576f9228672bb8$t:1751357344741$sn:12$en:6$s:1751355204337%3Bexp-sess",
            "_ga_Y1P6W8L5GD": "GS2.1.s1751355202$o14$g1$t1751355544$j60$l0$h0",
            "_ga_5EJ2ZSEPWX": "GS2.1.s1751355202$o13$g1$t1751355544$j60$l0$h0",
            "bm_sv": "FD8F0927499143C32E4FB8D70DDEBF8B~YAAQ7aTUFyQn46aXAQAAB5ztxByer2uUczu7HrwbRgkb7spEVnHFiyRukqVTMwgTLBJ+hHhUjm/NlqFbDkrHck117352r1iBGwdBthFimr2/++/EsFa69MMC6F/K2e3lTtV7q5H6zW9WM7z8W4my6PccJ+lf2erl8YUZ229+X5RQ00Q4VIVk1hrVCQ7FFB5ps42chkCXjyvxT+h4l1f5w9iws8INdCw5ziazQ99xulnCJBTZqGfpwLXuXbfdi0DHgHK8H5GADIRGuFlCTn0CCF3g~1"
        }

        response = requests.get(url, headers=headers,
                                params=params, timeout=10)
        response.raise_for_status()
        fetched_data = []
        for item in response.json()['data']['searchListings']['pagedSearchResults']:
            item['keyword'] = keyword
            fetched_data.append(item)
            print(item)
        data.extend(fetched_data)

    return data


def get_simplified_list(*args, **kwargs):
    data = get_list(*args, **kwargs)
    print(data)
    simplified = []
    for item in data:
        simplified.append({
            "adid": item.get("adID"),
            "keyword": item.get("keyword"),
            "seoUrl": f'https://www.commercialrealestate.com.au{item.get("seoUrl")}',
            "shortDescription": item.get("shortDescription"),
            "displayableStreet": item.get("displayableStreet"),
            "suburb": item.get("suburb"),
            "state": item.get("state"),
            "postcode": item.get("postcode"),
        })
    
    df = pd.DataFrame(simplified)
    # Remove duplicates by displayableStreet
    df = df.drop_duplicates(subset=["displayableStreet"])
    df.to_excel("commercialrealestate.xlsx", index=False)
    
    return df

def get_secondary_list(keywords=["Liquidation"],*args, **kwargs):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://www.realcommercial.com.au',
        'Referer': 'https://www.realcommercial.com.au/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    }
    results = []
    page = 1
    for keyword in keywords:
        while True:
            json_data = {
                'channel': 'buy',
                'filters': {
                    'keywords': keyword,
                    'within-radius': 'includesurrounding',
                    'surrounding-suburbs': True,
                },
                'page': page,
                'page-size': 100,
            }

            response = requests.post(
                'https://api.realcommercial.com.au/listing-ui/searches?featureFlags=showSoldDisclaimer,lsapiLocations',
                headers=headers,
                json=json_data,
            )
            print(response.status_code)
            data = response.json()['listings']
            
            if len(data) == 0:
                break
            page+=1
            
            for item in data:
                print(item)
                results.append(
                    {"adid": item.get("id"),
                    "keyword": keyword,
                    "seoUrl": f'https://www.realcommercial.com.au{item.get("pdpUrl")}',
                    "shortDescription": item.get("title"),
                    "displayableStreet": item.get("address", {}).get("streetAddress",''),
                    "suburb": item.get("address", {}).get("suburb"),
                    "state": item.get("address", {}).get("state"),
                    "postcode": item.get("address", {}).get("postcode"),
                })
    
    df = pd.DataFrame(results)
    # Remove duplicates by displayableStreet
    df = df.drop_duplicates(subset=["displayableStreet"])
    df.to_excel("realcommercial.xlsx", index=False)
    return df

def get_both_list(*args, **kwargs):
    df_1 = get_simplified_list(*args, **kwargs)
    df_2 = get_secondary_list(*args, **kwargs)
    
    final_df = pd.concat([df_1, df_2])
    final_df = final_df.drop_duplicates(subset=["displayableStreet"])
    final_df.to_excel('final.xlsx', index=False)
    return final_df

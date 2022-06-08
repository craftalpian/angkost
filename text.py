import requests

cookies = {
    'bm_sz': '05ED225E49EF11C9E14D7128FE7D9912~YAAQNZ5hdkZQ/TeBAQAAOwh0QRDabP6ZAHHp86/MnM5AZ3GZ4Ghim21AfP+MRVfsuQz/UYvhWDfDmQdy0R0cy4VqRxU3XNIKzACQIFkf3Or7Mota/hpysZCo0QIdsXGFsbldxCDzV2AP5eHCr5wwZ30Uff3gaa4YYwKQjOLccOZFlQzMYjdPC1klgGpQv1X/Wic/uhsGt2G3d+LhqIEMADbVZR8lhTuZq0TRsBkRP1EUGO5xawm405LKKCScRGlJFGgog8Sla1WDYjMFZMymHQua9gFLfLsVFb/JsVmdxoIvvZP4Kys=~4539449~4471095',
    '_SID_Tokopedia_': 'lpCPVBD7CHZgmA7r7sjXvmF4lpWFbF68i35tBUWKq5zuPmn_zzTPFfpT8MF9iJEJMAY7S8Hf_FUjIrRbP0sxyKlZyoemAdB_TZaeutT38LjfrYpNY_LXLkAz8rM_1P8T',
    'DID': 'bf9a4ffbeaf6b945eeae7ed227cc5f967dae1b8fe3934634a7fbaf219bc3473b4dfdad5061ac5191606333efd4aa0b6e',
    'DID_JS': 'YmY5YTRmZmJlYWY2Yjk0NWVlYWU3ZWQyMjdjYzVmOTY3ZGFlMWI4ZmUzOTM0NjM0YTdmYmFmMjE5YmMzNDczYjRkZmRhZDUwNjFhYzUxOTE2MDYzMzNlZmQ0YWEwYjZl47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=',
    '_UUID_NONLOGIN_': 'f434f749388a123c072f76848bf3ba0d',
    'hfv_banner': 'true',
    'ak_bmsc': '2DAB839B2E9290CB3EE0DA258C6A2EDC~000000000000000000000000000000~YAAQNZ5hdrFQ/TeBAQAA2Q50QRC+b5GsdR4ssal2DhgNJ3EKEo69Iea764YLKxgI/gl9rk8h74UhDraF6+/D3HWDwIb3iZ9cdjhYy6XzQEg3vILQKIa7V6CztnG0wPePt1coJ06tX7LsF9MI1c5eD0MavFjMA2dLb9fzKESNh6ndLFvNTtVsM1qL9ZhMmaslp885LnHt9XFhnQH1DlRC2VHsTLqslJBaN1mscYwMjrtA0+n0gaBwvVNpyuNQ51w9M0qKfKcvEpzU1ShWmLdG6h8PNehsEhh8ncqxYewRQuBlogM11AQ/M4kaiLciflZHuY0FIYi26e3tL/C1T5nyqTidz1lg3qutrJza4S9QwmvF1VvdV2+vMpzw6+w6vRYuwk9ysHxNfRGC95PUJ/a2fh1s+laV/ZR5Ivt5xEJlJfl+lBVaCRIORDRM2TvcBTQgYmJGKFbsIcUkZBRIHYxCn+dYPWDwu7ln5ZIgx1SOVZ32ElmQnmIlyMKnoImUkg==',
    '_abck': '435CBB788F90B990E895E0F85A4D71F7~0~YAAQNZ5hdtpQ/TeBAQAAVhN0QQhKfaCnXyr5HHkU9V5tFJNj7P6xk2UzeuIjBFbeGLb39/Qr4gx4531vn3+xHyI/7QxqZONyXF7TRbVbvnQ0NsbUFXTpkc47bNlsN6o3ZYr55FiTY8g4ZOxYZifo1+CNsGXuJgxefMAUwWNvKrbX5/SKnfvZ/lRgqCRHRqPakPcStfwWQkH6AjbHaRY1OFPuVenqJHLXCKsb+1b21M7WxX8WXtIUJ3PznTbIeJiIKAGnDAdOiLCQ1jDnleylXl+7gdlQe2K47WYIqyIXjnEFbrshAqthOStOXCtcEPfq3L/hhK/jjHot3QDMHpiddAghNsvQzVa6d+M+4aXN+IjpxllAn1aNABFATYbJzqb+ELPwg3spNmJH+CT2DSC1mW6IDNclLMhq1bDY~-1~-1~-1',
    '_gcl_au': '1.1.359000249.1654660536',
    '_gid': 'GA1.2.334109168.1654660537',
    '_ga': 'GA1.2.1429897948.1654660537',
    '_UUID_CAS_': 'a4dd9a42-05f9-4b7f-ae74-6fd021118af5',
    '_CASE_': '277e3815387e666e6e6b68707e3d15387e666c707e303e307e667e163d373d2e283d7c0c292f3d287e707e3f15387e666d6b6a707e3033323b7e667e7e707e303d287e667e7e707e2c1f337e667e7e707e2b15387e666d6e6e6d6c6f6b69707e2f15387e666d6d696f6c696b6f707e2f08252c397e667e6e347e707e2b342f7e667e0727007e2b3d2e393433292f39033538007e666d6e6e6d6c6f6b6970007e2f392e2a353f390328252c39007e66007e6e34007e70007e030328252c39323d3139007e66007e0b3d2e393433292f392f007e217027007e2b3d2e393433292f39033538007e666c70007e2f392e2a353f390328252c39007e66007e6d6931007e70007e030328252c39323d3139007e66007e0b3d2e393433292f392f007e21017e21',
    '__asc': 'c1de698b18141742742da39f0b4',
    '__auc': 'c1de698b18141742742da39f0b4',
    '_dc_gtm_UA-9801603-1': '1',
    '_gat_UA-9801603-1': '1',
    '_ga_70947XW48P': 'GS1.1.1654660536.1.1.1654660662.45',
    '_dc_gtm_UA-126956641-6': '1',
}

headers = {
    'Host': 'gql.tokopedia.com',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'bm_sz=05ED225E49EF11C9E14D7128FE7D9912~YAAQNZ5hdkZQ/TeBAQAAOwh0QRDabP6ZAHHp86/MnM5AZ3GZ4Ghim21AfP+MRVfsuQz/UYvhWDfDmQdy0R0cy4VqRxU3XNIKzACQIFkf3Or7Mota/hpysZCo0QIdsXGFsbldxCDzV2AP5eHCr5wwZ30Uff3gaa4YYwKQjOLccOZFlQzMYjdPC1klgGpQv1X/Wic/uhsGt2G3d+LhqIEMADbVZR8lhTuZq0TRsBkRP1EUGO5xawm405LKKCScRGlJFGgog8Sla1WDYjMFZMymHQua9gFLfLsVFb/JsVmdxoIvvZP4Kys=~4539449~4471095; _SID_Tokopedia_=lpCPVBD7CHZgmA7r7sjXvmF4lpWFbF68i35tBUWKq5zuPmn_zzTPFfpT8MF9iJEJMAY7S8Hf_FUjIrRbP0sxyKlZyoemAdB_TZaeutT38LjfrYpNY_LXLkAz8rM_1P8T; DID=bf9a4ffbeaf6b945eeae7ed227cc5f967dae1b8fe3934634a7fbaf219bc3473b4dfdad5061ac5191606333efd4aa0b6e; DID_JS=YmY5YTRmZmJlYWY2Yjk0NWVlYWU3ZWQyMjdjYzVmOTY3ZGFlMWI4ZmUzOTM0NjM0YTdmYmFmMjE5YmMzNDczYjRkZmRhZDUwNjFhYzUxOTE2MDYzMzNlZmQ0YWEwYjZl47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; _UUID_NONLOGIN_=f434f749388a123c072f76848bf3ba0d; hfv_banner=true; ak_bmsc=2DAB839B2E9290CB3EE0DA258C6A2EDC~000000000000000000000000000000~YAAQNZ5hdrFQ/TeBAQAA2Q50QRC+b5GsdR4ssal2DhgNJ3EKEo69Iea764YLKxgI/gl9rk8h74UhDraF6+/D3HWDwIb3iZ9cdjhYy6XzQEg3vILQKIa7V6CztnG0wPePt1coJ06tX7LsF9MI1c5eD0MavFjMA2dLb9fzKESNh6ndLFvNTtVsM1qL9ZhMmaslp885LnHt9XFhnQH1DlRC2VHsTLqslJBaN1mscYwMjrtA0+n0gaBwvVNpyuNQ51w9M0qKfKcvEpzU1ShWmLdG6h8PNehsEhh8ncqxYewRQuBlogM11AQ/M4kaiLciflZHuY0FIYi26e3tL/C1T5nyqTidz1lg3qutrJza4S9QwmvF1VvdV2+vMpzw6+w6vRYuwk9ysHxNfRGC95PUJ/a2fh1s+laV/ZR5Ivt5xEJlJfl+lBVaCRIORDRM2TvcBTQgYmJGKFbsIcUkZBRIHYxCn+dYPWDwu7ln5ZIgx1SOVZ32ElmQnmIlyMKnoImUkg==; _abck=435CBB788F90B990E895E0F85A4D71F7~0~YAAQNZ5hdtpQ/TeBAQAAVhN0QQhKfaCnXyr5HHkU9V5tFJNj7P6xk2UzeuIjBFbeGLb39/Qr4gx4531vn3+xHyI/7QxqZONyXF7TRbVbvnQ0NsbUFXTpkc47bNlsN6o3ZYr55FiTY8g4ZOxYZifo1+CNsGXuJgxefMAUwWNvKrbX5/SKnfvZ/lRgqCRHRqPakPcStfwWQkH6AjbHaRY1OFPuVenqJHLXCKsb+1b21M7WxX8WXtIUJ3PznTbIeJiIKAGnDAdOiLCQ1jDnleylXl+7gdlQe2K47WYIqyIXjnEFbrshAqthOStOXCtcEPfq3L/hhK/jjHot3QDMHpiddAghNsvQzVa6d+M+4aXN+IjpxllAn1aNABFATYbJzqb+ELPwg3spNmJH+CT2DSC1mW6IDNclLMhq1bDY~-1~-1~-1; _gcl_au=1.1.359000249.1654660536; _gid=GA1.2.334109168.1654660537; _ga=GA1.2.1429897948.1654660537; _UUID_CAS_=a4dd9a42-05f9-4b7f-ae74-6fd021118af5; _CASE_=277e3815387e666e6e6b68707e3d15387e666c707e303e307e667e163d373d2e283d7c0c292f3d287e707e3f15387e666d6b6a707e3033323b7e667e7e707e303d287e667e7e707e2c1f337e667e7e707e2b15387e666d6e6e6d6c6f6b69707e2f15387e666d6d696f6c696b6f707e2f08252c397e667e6e347e707e2b342f7e667e0727007e2b3d2e393433292f39033538007e666d6e6e6d6c6f6b6970007e2f392e2a353f390328252c39007e66007e6e34007e70007e030328252c39323d3139007e66007e0b3d2e393433292f392f007e217027007e2b3d2e393433292f39033538007e666c70007e2f392e2a353f390328252c39007e66007e6d6931007e70007e030328252c39323d3139007e66007e0b3d2e393433292f392f007e21017e21; __asc=c1de698b18141742742da39f0b4; __auc=c1de698b18141742742da39f0b4; _dc_gtm_UA-9801603-1=1; _gat_UA-9801603-1=1; _ga_70947XW48P=GS1.1.1654660536.1.1.1654660662.45; _dc_gtm_UA-126956641-6=1',
    'tkpd-userid': '1',
    'sec-ch-ua-mobile': '?0',
    "User-Agent": "Opera/9.80 (X11; Linux x86_64; U; de) Presto/2.2.15 Version/10.00",
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'accept': '*/*',
    'x-version': 'fcbd00e',
    'x-source': 'tokopedia-lite',
    'x-device': 'desktop-0.0',
    'x-tkpd-lite-service': 'zeus',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://www.tokopedia.com',
    'referer': 'https://www.tokopedia.com/search?st=product&q=kateter&srp_component_id=02.01.00.00&navsource=home',
    'accept-language': 'en-US,en;q=0.9',
}

json_data = [
    {
        'operationName': 'SearchProductQueryV4',
        'variables': {
            'params': 'device=desktop&navsource=home&ob=23&page=1&q=kateter&related=true&rows=60&safe_search=false&scheme=https&shipping=&source=search&srp_component_id=02.01.00.00&st=product&start=0&topads_bucket=true&unique_id=f434f749388a123c072f76848bf3ba0d&user_addressId=&user_cityId=176&user_districtId=2274&user_id=&user_lat=&user_long=&user_postCode=&user_warehouseId=12210375&variants=',
        },
        'query': 'query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      componentId\n      __typename\n    }\n    data {\n      backendFilters\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        componentId\n        trackingOption\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        position\n        trackingOption\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            wishlist\n            shop {\n              city\n              isOfficial\n              isPowerBadge\n              __typename\n            }\n            ads {\n              adsId: id\n              productClickUrl\n              productWishlistUrl\n              shopClickUrl\n              productViewUrl\n              __typename\n            }\n            badges {\n              title\n              imageUrl\n              show\n              __typename\n            }\n            ratingAverage\n            labelGroups {\n              position\n              type\n              title\n              url\n              __typename\n            }\n            componentId\n            __typename\n          }\n          componentId\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        componentId\n        trackingOption\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          adsId: id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        customVideoURL\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          url\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        ratingAverage\n        shop {\n          shopId: id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      violation {\n        headerText\n        descriptionText\n        imageURL\n        ctaURL\n        ctaApplink\n        buttonText\n        buttonType\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
    },
]

response = requests.post('https://gql.tokopedia.com/graphql/SearchProductQueryV4', cookies=cookies, headers=headers, json=json_data)
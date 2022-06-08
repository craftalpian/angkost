import requests

cookies = {
    '_SID_Tokopedia_': 'lpCPVBD7CHZgmA7r7sjXvmF4lpWFbF68i35tBUWKq5zuPmn_zzTPFfpT8MF9iJEJMAY7S8Hf_FUjIrRbP0sxyKlZyoemAdB_TZaeutT38LjfrYpNY_LXLkAz8rM_1P8T',
    'DID': 'bf9a4ffbeaf6b945eeae7ed227cc5f967dae1b8fe3934634a7fbaf219bc3473b4dfdad5061ac5191606333efd4aa0b6e',
    'DID_JS': 'YmY5YTRmZmJlYWY2Yjk0NWVlYWU3ZWQyMjdjYzVmOTY3ZGFlMWI4ZmUzOTM0NjM0YTdmYmFmMjE5YmMzNDczYjRkZmRhZDUwNjFhYzUxOTE2MDYzMzNlZmQ0YWEwYjZl47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=',
    '_UUID_NONLOGIN_': 'f434f749388a123c072f76848bf3ba0d',
    'hfv_banner': 'true',
    '_gcl_au': '1.1.359000249.1654660536',
    '_gid': 'GA1.2.334109168.1654660537',
    '_ga': 'GA1.2.1429897948.1654660537',
    '_UUID_CAS_': 'a4dd9a42-05f9-4b7f-ae74-6fd021118af5',
    '_CASE_': '277e3815387e666e6e6b68707e3d15387e666c707e303e307e667e163d373d2e283d7c0c292f3d287e707e3f15387e666d6b6a707e3033323b7e667e7e707e303d287e667e7e707e2c1f337e667e7e707e2b15387e666d6e6e6d6c6f6b69707e2f15387e666d6d696f6c696b6f707e2f08252c397e667e6e347e707e2b342f7e667e0727007e2b3d2e393433292f39033538007e666d6e6e6d6c6f6b6970007e2f392e2a353f390328252c39007e66007e6e34007e70007e030328252c39323d3139007e66007e0b3d2e393433292f392f007e217027007e2b3d2e393433292f39033538007e666c70007e2f392e2a353f390328252c39007e66007e6d6931007e70007e030328252c39323d3139007e66007e0b3d2e393433292f392f007e21017e21',
    '__auc': 'c1de698b18141742742da39f0b4',
    'bm_sz': '97BA22870EF27ACC37B1FDA791E5A8C9~YAAQ4GjBF/8WVS+BAQAA7u1LQhDZmGEq0UZbuiKZWXgejKn3I8uPkFIxj0PhaBwnpHjhjS7ZJBfJ8yMnrRHjkm41Ihx1bG+UuPcnbs/hm2PrQ6tcUbSEgAx2fkVLSIZ9zBg2PAieJQpNkl1wgWCTQMEnUfjjz/thEothb+EhrpmDyUsGjGMMLaLS15KG06MvLKWTDUYcEtsFa19UjOyrPJBlwUIRyp9YPLJ+LqfmL+nU2d8u/hVEqfalZVgzH498TiZmRplI6JWq+5IWrCSS8WBWJI8b8xkKS9zkTvDN0modCr2nhD/twRqVAak8wOuJNFZXPVXpd0KCP9hxizA=~3748676~3291191',
    '_abck': '435CBB788F90B990E895E0F85A4D71F7~-1~YAAQ9F9idjpZzzeBAQAAkGVOQggQaDMK1wWj8HBC6/p7vaP569T6ajKZiu+VvG8j9NC1WmnAvqkvZ38/mCzOcpvBvjPpruH/kED88gvlk9GfbriFQyFwycaL4qDcH2e4MI1ZT/EoYNvLz3A882kRJiSLlK9XxYdSt7m9rEMInr8pIFDA3Xd1wPsaxQwx6CFeEtMMV/4MHx3vFV3OLFGq5M9y3Ln+rwMVwu47Y2hxxq2DSgI7wSEtISt53Gd2bBXK1sUnggGB5rhLRfdJdSBpdCzad/Kc4RHKVQRgKyy7cplnQ576Tb83LRaSsFjd2Q872xeMNky2P3bk9TTJogWYzVXKyC09+YMwAAJFyED2OeZW/wF9HwckwEte+QLFKUaTkqM=~-1~-1~-1',
    '_gat_UA-9801603-1': '1',
    '_ga_70947XW48P': 'GS1.1.1654674844.2.1.1654674844.60',
    '_dc_gtm_UA-126956641-6': '1',
    '_dc_gtm_UA-9801603-1': '1',
}

headers = {
    'Host': 'gql.tokopedia.com',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_SID_Tokopedia_=lpCPVBD7CHZgmA7r7sjXvmF4lpWFbF68i35tBUWKq5zuPmn_zzTPFfpT8MF9iJEJMAY7S8Hf_FUjIrRbP0sxyKlZyoemAdB_TZaeutT38LjfrYpNY_LXLkAz8rM_1P8T; DID=bf9a4ffbeaf6b945eeae7ed227cc5f967dae1b8fe3934634a7fbaf219bc3473b4dfdad5061ac5191606333efd4aa0b6e; DID_JS=YmY5YTRmZmJlYWY2Yjk0NWVlYWU3ZWQyMjdjYzVmOTY3ZGFlMWI4ZmUzOTM0NjM0YTdmYmFmMjE5YmMzNDczYjRkZmRhZDUwNjFhYzUxOTE2MDYzMzNlZmQ0YWEwYjZl47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; _UUID_NONLOGIN_=f434f749388a123c072f76848bf3ba0d; hfv_banner=true; _gcl_au=1.1.359000249.1654660536; _gid=GA1.2.334109168.1654660537; _ga=GA1.2.1429897948.1654660537; _UUID_CAS_=a4dd9a42-05f9-4b7f-ae74-6fd021118af5; _CASE_=277e3815387e666e6e6b68707e3d15387e666c707e303e307e667e163d373d2e283d7c0c292f3d287e707e3f15387e666d6b6a707e3033323b7e667e7e707e303d287e667e7e707e2c1f337e667e7e707e2b15387e666d6e6e6d6c6f6b69707e2f15387e666d6d696f6c696b6f707e2f08252c397e667e6e347e707e2b342f7e667e0727007e2b3d2e393433292f39033538007e666d6e6e6d6c6f6b6970007e2f392e2a353f390328252c39007e66007e6e34007e70007e030328252c39323d3139007e66007e0b3d2e393433292f392f007e217027007e2b3d2e393433292f39033538007e666c70007e2f392e2a353f390328252c39007e66007e6d6931007e70007e030328252c39323d3139007e66007e0b3d2e393433292f392f007e21017e21; __auc=c1de698b18141742742da39f0b4; bm_sz=97BA22870EF27ACC37B1FDA791E5A8C9~YAAQ4GjBF/8WVS+BAQAA7u1LQhDZmGEq0UZbuiKZWXgejKn3I8uPkFIxj0PhaBwnpHjhjS7ZJBfJ8yMnrRHjkm41Ihx1bG+UuPcnbs/hm2PrQ6tcUbSEgAx2fkVLSIZ9zBg2PAieJQpNkl1wgWCTQMEnUfjjz/thEothb+EhrpmDyUsGjGMMLaLS15KG06MvLKWTDUYcEtsFa19UjOyrPJBlwUIRyp9YPLJ+LqfmL+nU2d8u/hVEqfalZVgzH498TiZmRplI6JWq+5IWrCSS8WBWJI8b8xkKS9zkTvDN0modCr2nhD/twRqVAak8wOuJNFZXPVXpd0KCP9hxizA=~3748676~3291191; _abck=435CBB788F90B990E895E0F85A4D71F7~-1~YAAQ9F9idjpZzzeBAQAAkGVOQggQaDMK1wWj8HBC6/p7vaP569T6ajKZiu+VvG8j9NC1WmnAvqkvZ38/mCzOcpvBvjPpruH/kED88gvlk9GfbriFQyFwycaL4qDcH2e4MI1ZT/EoYNvLz3A882kRJiSLlK9XxYdSt7m9rEMInr8pIFDA3Xd1wPsaxQwx6CFeEtMMV/4MHx3vFV3OLFGq5M9y3Ln+rwMVwu47Y2hxxq2DSgI7wSEtISt53Gd2bBXK1sUnggGB5rhLRfdJdSBpdCzad/Kc4RHKVQRgKyy7cplnQ576Tb83LRaSsFjd2Q872xeMNky2P3bk9TTJogWYzVXKyC09+YMwAAJFyED2OeZW/wF9HwckwEte+QLFKUaTkqM=~-1~-1~-1; _gat_UA-9801603-1=1; _ga_70947XW48P=GS1.1.1654674844.2.1.1654674844.60; _dc_gtm_UA-126956641-6=1; _dc_gtm_UA-9801603-1=1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'tkpd-userid': '0',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'accept': '*/*',
    'x-version': 'fcbd00e',
    'x-source': 'tokopedia-lite',
    'x-device': 'desktop-0.0',
    'x-tkpd-lite-service': 'zeus',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://www.tokopedia.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.tokopedia.com/search?st=product&q=gamis%20pria&srp_component_id=02.01.00.00&navsource=home',
    'accept-language': 'en-US,en;q=0.9',
}

json_data = [
    {
        'operationName': 'SearchProductQueryV4',
        'variables': {
            'params': 'device=desktop&navsource=home&ob=23&page=1&q=gamis%20pria&related=true&rows=60&safe_search=false&scheme=https&shipping=&source=search&srp_component_id=02.01.00.00&st=product&start=0&topads_bucket=true&unique_id=f434f749388a123c072f76848bf3ba0d&user_addressId=&user_cityId=176&user_districtId=2274&user_id=&user_lat=&user_long=&user_postCode=&user_warehouseId=12210375&variants=',
        },
        'query': 'query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      componentId\n      __typename\n    }\n    data {\n      backendFilters\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        componentId\n        trackingOption\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        position\n        trackingOption\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            wishlist\n            shop {\n              city\n              isOfficial\n              isPowerBadge\n              __typename\n            }\n            ads {\n              adsId: id\n              productClickUrl\n              productWishlistUrl\n              shopClickUrl\n              productViewUrl\n              __typename\n            }\n            badges {\n              title\n              imageUrl\n              show\n              __typename\n            }\n            ratingAverage\n            labelGroups {\n              position\n              type\n              title\n              url\n              __typename\n            }\n            componentId\n            __typename\n          }\n          componentId\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        componentId\n        trackingOption\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          adsId: id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        customVideoURL\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          url\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        ratingAverage\n        shop {\n          shopId: id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      violation {\n        headerText\n        descriptionText\n        imageURL\n        ctaURL\n        ctaApplink\n        buttonText\n        buttonType\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
    },
]

response = requests.post('https://gql.tokopedia.com/graphql/SearchProductQueryV4', cookies=cookies, headers=headers, json=json_data)

print(response.json())
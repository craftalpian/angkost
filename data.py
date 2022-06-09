import numpy as np
from tabulate import tabulate
import bitly_api

def shorten_url(url):
    BITLY_ACCESS_TOKEN = "6ec43aa95e89e7ba69286b89992abe0d7587291a"
    
    x = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

    return x.shorten(url)

def format_price(amount) -> int:
    return int(amount.lower().replace('rp', '').replace('.', ''))

def thousand_format(amount) -> str:
    return '{:,}'.format(amount).replace(',', '.')

def scoring_badge(badge):
    if len(badge) < 1:
        return 1
    else:
        title = badge[0]['title']
        if title == "Official Store":
            return 5
        elif title == "Power Merchant Pro Badge":
            return 4
        else:
            return 2


def scoring_product(count_review, rating_average):
    score = float(count_review)*float(rating_average)
    return score


def extract_data(data):
    data_store = []

    for i, j in enumerate(data):
        if i <= 4:
            data_store.append([j['id'], j['name'], j['badges'], scoring_badge(j['badges']), j['countReview'], j['price'], format_price(j['price']), j['ratingAverage'],
                              j['url'], scoring_product(j['countReview'], j['ratingAverage']), scoring_product(j['countReview'], j['ratingAverage'])+scoring_badge(j['badges'])])

    return data_store

def final_result(data, data_result, budget):
    # Count product
    count = len(data)

    # Storage (by price - LOW)
    stored_price_low = {}

    # Storage (by price - HIGH)
    stored_price_high = {}

    # Storage (by score - LOW)
    stored_score_low = {}

    # Storage (by score - HIGH)
    stored_score_high = {}

    # Final result
    result = {}

    for x, y in enumerate(data_result):
        stored_price_low[data[x]] = sorted(y, key=lambda x: x[6], reverse=False)
        stored_price_high[data[x]] = sorted(y, key=lambda x: x[6], reverse=True)
        stored_score_low[data[x]] = sorted(y, key=lambda x: x[10], reverse=False)
        stored_score_high[data[x]] = sorted(y, key=lambda x: x[10], reverse=True)

    # Result
    result = {}

    # Sort by price - low
    sort_by_price_low = []
    # Sort by price - high
    sort_by_price_high = []
    # Sort by score - low
    sort_by_score_low = []
    # Sort by score - high
    sort_by_score_high = []

    for j in data:
        # cheap
        sort_by_price_low.append(stored_price_low[j][0])
        sort_by_price_high.append(stored_price_high[j][0])
        # score recommendation
        sort_by_score_low.append(stored_score_low[j][0])
        sort_by_score_high.append(stored_score_high[j][0])
    
    result["price_low"] = sort_by_price_low
    result["price_high"] = sort_by_price_high
    result["score_low"] = sort_by_score_low
    result["score_high"] = sort_by_score_high

    for i in result:
        table_detail(i, result[i], budget)

    return result

def table_detail(title, data, budget):
    print(f"\n[{title.upper()}]:")
    data_new = [[x+1, y[1], shorten_url(y[1]), y[5], y[4], y[7], y[10]] for x, y in enumerate(data)]
    print(tabulate(data_new, headers=["#", "nama", "url", "harga", "penjualan", "bintang", "skor"]))
    price_total = np.sum(np.array([x[6] for x in data]))
    print(f"\nTotal: Rp{thousand_format(price_total)}\t\tBudget: Rp{thousand_format(budget)}\t\tSelisih: Rp{thousand_format(budget-price_total)}\n")
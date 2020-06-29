import amazonscraper

results = amazonscraper.search("Python programming", max_product_nb=2)

for result in results:
    print("{}".format(result.title))
    print("  - ASIN : {}".format(result.asin))
    print(
        "  - {} out of 5 stars, {} customer reviews".format(
            result.rating, result.review_nb
        )
    )
    print("  - {}".format(result.url))
    print("  - Image : {}".format(result.img))
    print()

print("Number of results : %d" % (len(results)))

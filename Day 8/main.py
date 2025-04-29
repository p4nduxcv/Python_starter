bid_records = {
    # "bid_1": {
    #     "name": "John",
    #     "bid": "$100"
    # },
    # "bid_2": {
    #     "name": "Doe",
    #     "bid": "$101"
    # }
}
bid_count=1
is_next_person = "y"
highest_bid = 0
highest_bidder = ""

while is_next_person == "y":
    bidder_name = input("Enter Name: ")
    bid_value = int(input("Enter Amount: "))
    bid_records[f"bid_{bid_count}"] = {
        "name": bidder_name,
        "bid": f"{bid_value}"
    }
    bid_count += 1
    is_next_person = input("Bid again? (y/n): ").lower()

# print(bid_records)

for key in bid_records:
    # bid_records[key]["bid"]
    bid_amount = int(bid_records[key]["bid"])
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        highest_bidder = bid_records[key]["name"]

print(highest_bidder)
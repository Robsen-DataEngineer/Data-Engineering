# sales = [
#     {"customer": "Abel", "product": "Laptop", "quantity": 2, "price": 800},
#     {"customer": "Sara", "product": "Phone", "quantity": 3, "price": 500},
#     {"customer": "John", "product": "Laptop", "quantity": 1, "price": 800},
#     {"customer": "Abel", "product": "Mouse", "quantity": 5, "price": 25},
#     {"customer": "Sara", "product": "Keyboard", "quantity": 2, "price": 50},
#     {"customer": "Mike", "product": "Monitor", "quantity": 2},
#     {"customer": "David", "product": "Chair", "quantity": "three", "price": 100},
# ]

# def total_revenue_calculator(numbers):
#     revenue = 0
#     valid_transaction = 0
#     for number in numbers:
#         quantity = number.get("quantity")
#         price = number.get("price")
#         if isinstance(quantity, int) and isinstance(price, int):
#             revenue += number["price"] * number["quantity"]
#             valid_transaction += 1
#     return revenue, valid_transaction

# def unique_calculator(sales, name):
#     data = {}
#     for reve in sales:
#         quantity = reve.get("quantity")
#         price = reve.get("price")
#         if isinstance(quantity, int) and isinstance(price, int):
#             if reve[name] not in data:
#                 data[reve[name]] = reve["quantity"] * reve["price"]
#             else:
#                 data[reve[name]] += reve["quantity"] * reve["price"]
#     return data


# # Task 1 Revenue Per Sale
# for sale in sales:
#     quantity = sale.get("quantity")
#     price = sale.get("price")
#     if isinstance(quantity, int) and isinstance(price, int):
#         revenue = sale["price"] * sale["quantity"]
#         print(f"{sale["customer"]} Bouhgt {sale["product"]}: ${revenue}")
#     else:
#        print(f"Warning: Invalid sales for {sale["customer"]}")
  

# # Task  Total Revenue
# print(f"\nTotal Revenue is: ${total_revenue_calculator(sales)[0]}")

# # Task  Average transaction value
# avg = total_revenue_calculator(sales)
# print(f"valid Transactions: {avg[1]} \nAverage Transaction Revenue: ${avg[0] / avg[1]}\n")

# #Task  Top Customer

# customer_data = unique_calculator(sales, "customer")
# top_customer = ""
# reveneu_generated = 0
# for name in customer_data:
#     if customer_data[name] > reveneu_generated:
#         reveneu_generated = customer_data[name]
#         top_customer = name


# print(f"Top Customer: {top_customer}")
# print(f"Revenue: ${reveneu_generated}\n")

# # Task  Product Revenue

# product_data = unique_calculator(sales, "product")
# for item in product_data:
#     print(f"{item}: ${product_data[item]}")
    

# customers = [
#     {"name": "Abel", "age": 23, "country": "Ethiopia", "email": "abel@gmail.com"},
#     {"name": " sara ", "age": "24", "country": "Ethiopia", "email": "sara@gmail.com"},
#     {"name": "JOHN", "age": 31, "country": "Kenya", "email": "john@gmail.com"},
#     {"name": "Abel", "age": 23, "country": "Ethiopia", "email": "abel@gmail.com"},
#     {"name": "", "age": 29, "country": "Uganda", "email": "mike@gmail.com"},
#     {"name": "David", "age": "twenty", "country": "Ethiopia", "email": "david@gmail.com"},
#     {"name": "  Hana  ", "age": 27, "country": "Ethiopia", "email": "hana@gmail.com"},
#     {"name": "Sara", "age": 24, "country": "Ethiopia", "email": "sara@gmail.com"},
# ]

# def cleaned_data(customers):
#     customers = customers.copy()
#     clean_data = []
#     original_size = len(customers)
#     duplicated_data = 0
#     reject_data = 0
#     for customer in customers:
#         try:
#             customer["name"] = customer["name"].strip().capitalize()
#             customer["age"] = int(customer["age"])
#             if not customer["name"]:
#                 reject_data += 1
#                 continue
#             if customer not in clean_data:
#                 clean_data.append(customer)
#             else:
#                 duplicated_data += 1
#         except (KeyError, ValueError, TypeError):
#             reject_data += 1

#     return clean_data, original_size, duplicated_data, reject_data

        

# result = cleaned_data(customers)
# for name in result[0]:
#     print(name["name"])

# print(f"Original records: {result[1]}")
# print(f"Rejected: {result[3]}")
# print(f"Duplicates: {result[2]}")
# print(f"Clean records: {len(result[0])}")

# transactions = [
#     {"id": 101, "customer": "Abel", "product": "Laptop", "quantity": "2", "price": "800"},
#     {"id": 102, "customer": " sara ", "product": "Phone", "quantity": 3, "price": 500},
#     {"id": 103, "customer": "JOHN", "product": "Laptop", "quantity": 1, "price": 800},
#     {"id": 104, "customer": "Abel", "product": "Mouse", "quantity": 5, "price": 25},
#     {"id": 105, "customer": "Sara", "product": "Keyboard", "quantity": 2, "price": 50},
#     {"id": 106, "customer": "Mike", "product": "Monitor", "quantity": 2, "price": None},
#     {"id": 107, "customer": "David", "product": "Chair", "quantity": "three", "price": 100},
#     {"id": 108, "customer": "abel", "product": "Laptop", "quantity": 1, "price": 800},
#     {"id": 109, "customer": "", "product": "Phone", "quantity": 2, "price": 500},
#     {"id": 110, "customer": "Hana", "product": "Desk", "quantity": 2, "price": "150"},
#     {"id": 111, "customer": "Sara", "product": "Phone", "quantity": 1, "price": 500},
#     {"id": 111, "customer": "Sara", "product": "Phone", "quantity": 1, "price": 500},
# ]

# def revenue_calculator(transactions, name):
#     customer_transaction = {}
#     for transaction in transactions:
#         if transaction[name] not in customer_transaction:
#             customer_transaction[transaction[name]] = transaction["quantity"] * transaction["price"]
#         else:
#             customer_transaction[transaction[name]] += (transaction["quantity"] * transaction["price"])
#     return customer_transaction


# def clean_data(transactions):
#     clean_customer_transaction = []
#     rejected = 0
#     vaild_transaction = 0
#     duplicated = 0
#     tran_id = set()

#     for transaction in transactions:
#         try:
#             transaction["customer"] = str(transaction["customer"].strip().capitalize())
#             transaction["quantity"] = int(transaction["quantity"])
#             transaction["price"] = float(transaction["price"])
#             tx_id = transaction["id"]
#         except (ValueError, KeyError, TypeError):
#             rejected += 1
#             continue
#         if not transaction["customer"] or transaction["quantity"] <= 0 or transaction["price"] < 0:
#             rejected += 1
#             continue
#         if tx_id in tran_id:
#             duplicated += 1
#             continue
#         tran_id.add(tx_id)
#         vaild_transaction += 1
#         clean_customer_transaction.append(transaction)

#     return clean_customer_transaction, rejected, vaild_transaction, duplicated

# result = clean_data(transactions)
# total_revenue = 0

# for revenue in result[0]:
#     total_revenue += revenue["quantity"] * revenue["price"]

# customer_revenue = revenue_calculator(result[0], "customer")
# for item in customer_revenue:
#     print(f"{item}: ${customer_revenue[item]}")

# print("\n")
# product_revenue = revenue_calculator(result[0], "product")
# for item in product_revenue:
#     print(f"{item}: ${product_revenue[item]}")
# print('\n')
# average_transaction_revenue = total_revenue / result[2]

# print(f"Total Revenue: {total_revenue}")
# print(f"Average Revenue: {average_transaction_revenue}")
# print(f"Vaild Transaction: {result[2]}")
# print(f"Rejected Transaction: {result[1]}")
# print(f"Duplicated Transaction: {result[3]}")


import csv



def clean_data(data):
    clean_data = []
    rejected_data = []
    data_id = set()
    duplicated_data = 0
    valid_transaction = 0
    total_recored = 0
    for item in data:
        total_recored += 1
        try:
            item["customer"] = item["customer"].strip().capitalize()
            item["quantity"] = int(item["quantity"])
            item["price"] = float(item["price"])
            tx_id = item["id"]
        except (KeyError, ValueError, TypeError) as e:
            if isinstance(e, ValueError):
                item["reason"] = "Missing Data"
            rejected_data.append(item)
            continue
        if not item["customer"]:
            item["reason"] = "Empty Customer"
            rejected_data.append(item)
            continue
        elif item["quantity"] <= 0:
            item["reason"] = "Invalid quantity"
            rejected_data.append(item)
            continue
        elif item["price"] < 0:
            item["reason"] = "Invalid Price"
            rejected_data.append(item)
            continue
        if tx_id in data_id:
            item["reason"] = "Duplicated Data"
            rejected_data.append(item)
            duplicated_data += 1
            continue
        data_id.add(tx_id)
        valid_transaction += 1
        clean_data.append(item)

    return clean_data, rejected_data, valid_transaction, duplicated_data, len(rejected_data), total_recored

list_data = []
with open("sale.csv", mode = 'r') as file:
    raw_data = csv.DictReader(file)
    for item in raw_data:
        list_data.append(item)


cleaned_data = clean_data(list_data)
columns = list(cleaned_data[0][0].keys())


with open("clean_sale.csv", mode="w", newline="") as file:
    data = csv.DictWriter(file, fieldnames=columns)
    data.writeheader()
    data.writerows(cleaned_data[0])



rejected_col = list(cleaned_data[1][0].keys())


with open("rejected_sales.csv", mode="w") as file:
    data = csv.DictWriter(file, fieldnames=rejected_col)
    data.writeheader()
    data.writerows(cleaned_data[1])

print(f"Total Transaction: {cleaned_data[5]}")
print(f"Valid: {cleaned_data[2]}")
print(f"Rejected: {cleaned_data[4]}")
print(f"Duplicated: {cleaned_data[3]}")

print("\n")


total_revenue = 0
for item in cleaned_data[0]:
    total_revenue += item["price"] * item["quantity"]

print(f"Total Reveneu: ${total_revenue}")

print(f"Average Transaction: {total_revenue / cleaned_data[2]}")
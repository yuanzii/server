
import time;
import random;

F2002 = [{"id": 757, "order_id": 20201101113019, "customer_id": "A283", "customer_name": "အားခွင်း ဟောင်လိတ်",
  "total_amount": 35000, "datetime": 1604188800000, "product_id": "AV1501", "product_name": "ဘိလပ်မြေ(ကျား)",
  "product_detal": "Tiger -> ( 50 kg )", "count": 100, "price": 110, "subtotal": 11000},
 {"id": 757, "order_id": 20201101113019, "customer_id": "A283", "customer_name": "အားခွင်း ဟောင်လိတ်",
  "total_amount": 35000, "datetime": 1604332924000, "product_id": "AV1504", "product_name": "ဘိလပ်မြေ(ဆင်)",
  "product_detal": "Elephant -> ( 50 kg )", "count": 200, "price": 120, "subtotal": 24000}]
for F1 in F2002:
    timeStamp = float(F1["datetime"] / 1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)
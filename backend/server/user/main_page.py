from user import user
from flask import render_template, request, jsonify
import pandas as pd
import datetime;
import random;
import  time;


@user.route('/get_customer', methods=["POST", "GET"])
def get_customer():
    import db.psql as con
    import importlib
    importlib.reload(con)
    from db.psql import con

    try:
        post_data = request.json
        customer_id = post_data.get("customer_id")
        print("customer_id ： " + customer_id)
        if request.method == 'POST':
            print("POST")
            A1001 = pd.read_sql(
                "SELECT * from customers where ctm_code_no ILIKE '"+customer_id+"' ", con)
            print("DataFrame")
            print(A1001)
            if A1001.empty:
                print("输入错误！没有该数据！")
                return "输入错误！没有该数据！"
            else:
                A2002 = A1001.to_json(orient="records", lines=True)
                con.close()
                print("DataFrame to_json")
                print(A2002)
                return A2002

    except Exception:
        print("Error:出错啦！！！")
        return jsonify("")


@user.route('/get_product', methods=["POST", "GET"])
def get_product():
    import db.psql as con
    import importlib
    importlib.reload(con)
    from db.psql import con

    try:
        # post_data 是前端发送过来的json数据
        post_data = request.json
        product_id = post_data.get("product_id")
        print("product_id ： " + product_id)

        if request.method == 'POST':
            B1001 = pd.read_sql(
                "SELECT * from goods_detail where idname ILIKE '"+product_id+"' ", con)
            print("DataFrame")
            print(B1001)
            if B1001.empty:
                print("输入错误！没有该数据！")
                return "输入错误！没有该数据！"
            else:
                B2002 = B1001.to_json(orient="records", lines=True)
                con.close()
                print("DataFrame to_json")
                print(B2002)
                return B2002

    except Exception:
        print("Error:出错啦！！！")
        return jsonify("")

@user.route('/orders', methods=["POST", "GET","PUT"])
def all_orders():
    import db.psql as con
    import importlib
    importlib.reload(con)
    from db.psql import con

    try:
        if request.method == 'POST':
            print("POST")
            post_data = request.json
            orders = post_data.get("orders")
            products = post_data.get("products")

            order_no = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

            for product in products:
                product["order_id"] = order_no

            orders["order_id"] = order_no

            cur = con.cursor()

            cur.execute("""INSERT INTO order_head(order_id,customer_id,customer_name,total_amount,
            datetime)VALUES (%(order_id)s,%(customer_id)s, %(customer_name)s, %(total_amount)s,
            %(datetime)s)""", orders)

            cur.executemany("""INSERT INTO order_goods(order_id,product_id,product_name,product_detal,
            count,price,subtotal)VALUES (%(order_id)s,%(product_id)s, %(product_name)s, %(product_detal)s,
            %(count)s, %(price)s, %(subtotal)s)""", products)

            cur.executemany("""INSERT INTO released_waybill(order_id,product_id,product_name,product_detal,
                        count,price)VALUES (%(order_id)s,%(product_id)s, %(product_name)s, %(product_detal)s,
                        %(count)s, %(price)s)""", products)

            con.commit()
            con.close()
            return jsonify("")

        if request.method == 'GET':
            print("GET")
            F1001 = pd.read_sql('SELECT order_head.id,order_head.order_id,\
            order_head.customer_id,order_head.customer_name,order_head.total_amount,\
            order_head.datetime,order_goods.product_id,order_goods.product_name,\
            order_goods.product_detal,order_goods.count,order_goods.price,\
            order_goods.subtotal FROM order_head INNER JOIN order_goods\
            ON order_head.order_id=order_goods.order_id ', con)
            F2002 = F1001.to_json(orient="records")
            con.close()
            return F2002

        if request.method == 'PUT':
            print("PUT")
            post_data = request.json
            order_id = post_data.get("order_id")
            G1001 = pd.read_sql("SELECT order_head.id,order_head.order_id,\
                                order_head.customer_id,order_head.customer_name,order_head.total_amount,\
                                order_head.datetime,order_goods.product_id,order_goods.product_name,\
                                order_goods.product_detal,order_goods.count,order_goods.price,\
                                order_goods.subtotal FROM order_head INNER JOIN order_goods\
                                ON order_head.order_id=order_goods.order_id \
                                WHERE (order_head.order_id='" + order_id + "')", con)
            G2002 = G1001.to_json(orient="records")
            con.close()
            return (G2002)

    except Exception:
        return jsonify("")

# def remove_waybill():

@user.route('/orders/<order_id>', methods=["GET", "PUT"])
def single_order(order_id):
    import db.psql as con
    import importlib
    importlib.reload(con)
    from db.psql import con

    if request.method == 'GET':
        print("GET")
        G1001 = pd.read_sql("SELECT order_head.id,order_head.order_id,\
                    order_head.customer_id,order_head.customer_name,order_head.total_amount,\
                    order_head.datetime,released_waybill.product_id,released_waybill.product_name,\
                    released_waybill.product_detal,released_waybill.count,released_waybill.price,\
                    released_waybill.subtotal FROM order_head INNER JOIN released_waybill\
                    ON order_head.order_id=released_waybill.order_id \
                    WHERE (order_head.order_id='" + order_id + "')", con)
        G2002 = G1001.to_json(orient="records")
        con.close()
        return (G2002)

    if request.method == 'PUT':
        print("PUT")
        post_data = request.json
        released_waybill = post_data.get("released_waybill")

        cur = con.cursor()
        cur.execute("DELETE FROM released_waybill a USING order_head b WHERE a.order_id=b.order_id AND b.order_id = '" + str(order_id) + "'")

        cur.executemany("INSERT INTO released_waybill(order_id,product_id,product_name,product_detal,\
                        count,price)VALUES (%(order_id)s,%(product_id)s, %(product_name)s, %(product_detal)s,\
                        %(count)s, %(price)s)", released_waybill)

        con.commit()
        con.close()
        return jsonify("")

@user.route('/waybill', methods=["POST","GET","PUT"])
def waybill():
    import db.psql as con
    import importlib
    importlib.reload(con)
    from db.psql import con

    # if request.method == 'GET':
    # print("GET")
    # G1001 = pd.read_sql("SELECT order_head.id,order_head.order_id,\
    #             order_head.customer_id,order_head.customer_name,order_head.total_amount,\
    #             order_head.datetime,order_goods.product_id,order_goods.product_name,\
    #             order_goods.product_detal,order_goods.count,order_goods.price,\
    #             order_goods.subtotal FROM order_head INNER JOIN order_goods\
    #             ON order_head.order_id=order_goods.order_id \
    #             WHERE (order_head.order_id='" + order_id + "')", con)
    # G2002 = G1001.to_json(orient="records")
    # con.close()
    # return (G2002)

    # if request.method == 'PUT':
    #     print("PUT")
    #     post_data = request.json
    #     released_waybill = post_data.get("released_waybill")
    #
    #     cur = con.cursor()
    #     cur.executemany("DELETE FROM released_waybill a USING order_head b WHERE a.order_id=b.order_id AND a.order_id = 20200814134312")
    #
    #     cur.executemany("INSERT INTO released_waybill(order_id,product_id,product_name,product_detal,\
    #                     count,price)VALUES (%(order_id)s,%(product_id)s, %(product_name)s, %(product_detal)s,\
    #                     %(count)s, %(price)s)", released_waybill)
    #
    #     con.commit()
    #     con.close()
    #     return jsonify("")

    if request.method == 'POST':
        print("POST")
        post_data = request.json
        waybill = post_data.get("waybill")
        nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # 生成当前时间
        randomNum = random.randint(0, 10000)  # 生成的随机整数n，其中0<=n<=10000
        if randomNum < 10:
            randomNum = str(000) + str(randomNum)
        elif randomNum < 100:
            randomNum = str(00) + str(randomNum)
        elif randomNum < 1000:
            randomNum = str(0) + str(randomNum)
        uniqueNum = str(nowTime) + str(randomNum)
        print(uniqueNum)
        order_create_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        for bill in waybill:
            bill["waybill_id"] = uniqueNum
            bill["order_create_time"] = order_create_time

        cur = con.cursor()
        cur.executemany("""INSERT INTO waybill(waybill_id,customer_id,customer_name,product_id,
            product_name,product_detail,count,order_id,order_create_time) VALUES (%(waybill_id)s,
            %(customer_id)s,%(customer_name)s, %(product_id)s,%(product_name)s,%(product_detal)s,
            %(count)s,%(order_id)s,%(order_create_time)s)""", waybill)

        con.commit()
        con.close()
        return jsonify("")

@user.route('/last_product', methods=["GET"])
def last_product():
    import db.psql as con
    import importlib
    importlib.reload(con)
    from db.psql import con

    A10001 = pd.read_sql('SELECT order_head.id,order_head.order_id,\
        order_head.customer_id,order_head.customer_name,order_head.total_amount,\
        order_head.datetime,order_goods.product_id,order_goods.product_name,\
        order_goods.product_detal,order_goods.count,order_goods.price,\
        order_goods.subtotal FROM order_head INNER JOIN order_goods\
        ON order_head.order_id=order_goods.order_id ', con)
    A10001['g'] = 1
    A10002 = A10001.groupby(['g'])['id'].max().reset_index()
    max_id = A10002.id[0]
    F10001 = A10001.loc[A10001['id'] == max_id]
    F10002 = F10001.to_json(orient="records")

    con.close()

    return F10002

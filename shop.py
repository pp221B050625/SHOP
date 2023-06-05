import mysql.connector as mysql
import re

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="hardex",
    database="shop"
)
cur = db.cursor(buffered=True)


def check_username(name):
    sql = "SELECT * FROM users WHERE username=%s"
    cur.execute(sql, (name,))
    names = cur.fetchone()
    if names is None:
        return True
    else:
        return False


def get_usernames():
    sql = "SELECT username from users"
    l = []
    cur.execute(sql)
    names = cur.fetchall()
    for n in names:
        l.append(n)
    return l


def add_user(name, pas, number):
    sql = "INSERT INTO users(username,password,Phone_number) VALUES(%s,%s,%s)"

    cur.execute(sql, (name, pas, number))
    db.commit()


def login_check(name, pas):
    get_id = "SELECT id from users where username = %s"
    cur.execute(get_id, (name,))
    idd = cur.fetchone()
    check_pass = "SELECT password from users where id = %s"
    try:
        cur.execute(check_pass, (idd[0],))
        pw = cur.fetchone()
        if str(pw[0]) == pas:
            return True
        else:
            return False
    except TypeError:
        return False


def credit_card_check(card):
    if len(card) == 16 or len(card) == 19:
        if re.search("(^[456]\d{15})|(^[456]\d{0,3}[-]\d{4}[-]\d{4}[-]\d{4})", card) and not re.search(
                r'.*(\d).*\1.*\1.*\1',
                card.replace("-", "")):
            return True
        else:
            return False
    else:
        return False


def check_name(name):
    return (re.findall("^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)", name))


def check_date(date):
    if re.match("(0[1-9]|1[0-2])\/?([0-9]{2})$", date):
        return True
    else:
        return False


def add_order(user, card, address, date, total):
    sql = "INSERT INTO orders(user,credit_card,adress,date,total) VALUES(%s,%s,%s,%s,%s)"
    cur.execute(sql, (user, card, address, date, total))
    db.commit()


def add_product_sales(id,name,total):
    sql = "INSERT INTO product_sales(order_id,product_name,total) VALUES(%s,%s,%s)"
    cur.execute(sql,(id,name,total))
    db.commit()


def get_order_id():
    sql = "SELECT LAST_INSERT_ID() from orders"
    cur.execute(sql)
    id = cur.fetchone()
    return id

def get_profits(d1,d2):
    sql = "SELECT total FROM orders where date between %s and %s"
    cur.execute(sql,(d1,d2))
    total = cur.fetchall()
    return total

def get_quantity(name):
    sql = "SELECT quantity_kg from stock where product_name = %s"
    cur.execute(sql,(name,))
    q = cur.fetchone()
    if q:
     return q[0]

def update_stock(qu,name):
    q = get_quantity(name)
    new = q - qu
    sql = "UPDATE stock SET `quantity_kg` =%s WHERE (`product_name` = %s)"
    cur.execute(sql,(new,name))
    db.commit()

def get_price(name):
    sql = "select price from stock where product_name = %s"
    cur.execute(sql,(name,))
    p = cur.fetchone()
    return p


class Shop:
    def __init__(self):
        self.banana = 370
        self.apple = 437
        self.cherry = 1200
        self.strawberry = 3900
        self.orange = 1041
        self.grape = 650
        self.carrot = 391
        self.tomato = 1106
        self.cucumber = 781
        self.onion = 437
        self.pepper = 1951
        self.potato = 325
        self.cheese = 685
        self.curd = 1820
        self.kumys = 2000
        self.milk = 755
        self.sour_cream = 910
        self.yogurt = 230


print(get_price('apple'))

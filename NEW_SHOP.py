from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from shop import *
import mysql.connector as mysql
import re
import datetime


shop = Shop()


def get_pic(our_pic, n, m):
    pic = Image.open(our_pic)
    pic_res = pic.resize((n, m))
    img = ImageTk.PhotoImage((pic_res))
    return img


class register(Tk):
    def __init__(self):
        super().__init__()
        self.title("Registration window")
        self.geometry('500x700+500+50')


    def label1(self):
        self.label_username = Label(self, text="User name *", font=20)
        self.label_username.pack()
        self.e = Entry(self, bd=5, font=20)
        self.e.pack()

    def label2(self):
        self.label_number = Label(self, text="Number *", font=20).pack()
        self.e4 = Entry(self, bd=5, font=20)
        self.e4.pack()

    def label3(self):
        self.label_pass = Label(self, text="password *", font=20).pack()
        self.e2 = Entry(self, bd=5, font=20)
        self.e2.pack()

    def label4(self):
        self.label_pass2 = Label(self, text="one more time(password) *", font=20).pack()
        self.e3 = Entry(self, bd=5, font=20)
        self.e3.pack()

    def reg_name(self):
        user = self.e.get()
        passwrd = self.e2.get()
        number = self.e4.get()
        correct_number = re.sub(r'[^0-9]', '', number)
        passwrd_confirm = self.e3.get()
        if user == "":
            er = Tk()
            er.geometry('300x60+650+340')
            Label(er, text="Заполните логин").pack()
            b = Button(er, text="OKAY", command=er.destroy)
            b.pack()
            er.mainloop()
        elif passwrd == "":
            er = Tk()
            er.geometry('300x60+650+340')
            Label(er, text="Заполните пароль").pack()
            b = Button(er, text="OKAY", command=er.destroy)
            b.pack()
            er.mainloop()
        elif len(passwrd) < 5:
            er = Tk()
            er.geometry('300x60+650+340')
            Label(er, text="Пароль должен быть из 5 или больше символов").pack()
            b = Button(er, text="OKAY", command=er.destroy)
            b.pack()
            er.mainloop()

        elif passwrd_confirm != passwrd:
            er = Tk()
            er.geometry('200x60+650+340')
            Label(er, text="Пароли не совпадают").pack()
            b = Button(er, text="OKAY", command=er.destroy)
            b.pack()
            er.mainloop()

        elif not check_username(user):
            er = Tk()
            er.geometry('200x60+650+340')
            Label(er, text="Логин занят").pack()
            b = Button(er, text="OKAY", command=er.destroy)
            b.pack()
            er.mainloop()
        else:
            add_user(user, passwrd, correct_number)
            self.destroy()

    def Button_register(self):
        self.button = Button(self, text="Register", command=self.reg_name).pack()


class login(Tk):
    def __init__(self):
        super().__init__()
        self.title("Shop App")
        self.geometry('500x700+500+50')
        self.config(bg='white')
        self.img = get_pic("wipwip/unnamed.jpg", 34, 34)
        self.img1 = get_pic("wipwip/passwordd.jpg", 34, 34)
        self.log_in_ = get_pic("wipwip/our_login_button.png", 120, 34)
        self.logo_shop = get_pic("wipwip/logo_new.png", 120, 130)
        self.sum =0

    def login_screen(self):
        self.logo_image = Label(self, image=self.logo_shop).place(x=190, y=90)
        self.user = Entry(self, background='white', foreground='black', font=("Times New Roman", 20), bg="#0694ea")
        self.password = Entry(self, background='white', foreground='black', font=("Times New Roman", 20), show='*',
                              bg="#0694ea")
        self.user.place(x=120, y=250)
        self.password.place(x=120, y=300)
        Label(self, image=self.img).place(x=70, y=251)
        Label(self, image=self.img1).place(x=70, y=300)

    def reg(self, event):
        Register = register()
        Register.label1()
        Register.label2()
        Register.label3()
        Register.label4()
        Register.Button_register()
        Register.mainloop()

    def profits(self):
        format = "%Y-%m-%d"
        try:
            date1 = self.E1.get()
            date2 = self.E2.get()
            date = datetime.datetime.strptime(date1,format)
            date = datetime.datetime.strptime(date2,format)
            for i in get_profits(date1,date2):
                self.sum += i[0]
            self.prf.config(text =f"Profits from {date1} to {date2} = {self.sum} tenge",font=20)
        except ValueError:
            er = Tk()
            er.geometry('200x60+650+340')
            Label(er, text="Неверная дата!!!").pack()
            b = Button(er, text="OKAY", command=er.destroy)
            b.pack()
            er.mainloop()

    def admin_enter(self,event):
        self.name = self.e.get()
        self.pwd = self.e4.get()
        if self.name == 'admin' and self.pwd == 'admin':
            self.w.destroy()
            self.root = Tk()
            self.root.geometry("400x400+100+100")
            Label(self.root,text="DATE 1").pack()
            self.E1 = Entry(self.root,bd=5,font=20)
            self.E1.pack()
            Label(self.root, text="DATE 2").pack()
            self.E2 = Entry(self.root, bd=5, font=20)
            self.E2.pack()
            self.B1 = Button(self.root,text="PROFITS",command=self.profits)
            self.B1.pack()
            self.prf = Label(self.root,text ="")
            self.prf.pack()


            self.root.mainloop()


    def adminmode(self,event):
        self.w = Tk()
        self.w.geometry('500x700+500+50')
        self.l = Label(self.w, text="USERNAME", font=20)
        self.l.pack()  # side=LEFT
        self.e = Entry(self.w, bd=5, font=20)
        self.e.pack()  # )
        Label(self.w, text="PASSWORD", font=20).pack()
        self.e4 = Entry(self.w, bd=5, font=20)
        self.e4.pack()
        self.lgin = Button(self.w,text="ENTER",bd=5)
        self.lgin.bind('<Button-1>', self.admin_enter)
        self.lgin.pack()
        self.w.mainloop()

    def login_button(self):
        self.log_in = Button(self, image=self.log_in_, bd=5)  # bg='#49e040'
        self.log_in.bind('<Button-1>', self.getname)
        self.log_in.place(x=190, y=370)

    def admin_button(self):
        self.admin = Button(self, text="ADMIN MODE", bd=5)  # bg='#49e040'
        self.admin.bind('<Button-1>',self.adminmode)
        self.admin.place(x=190, y = 650)

    def signup_button(self):
        self.signup = Button(self, text="""Don't have an account?
   Sign Up!!!""", bd=0, bg='white', fg='#0694ea')
        self.signup.bind('<Button-1>', self.reg)
        self.signup.place(x=180, y=600)

    def getname(self, event):
        self.username = self.user.get()
        self.passwrd = self.password.get()
        if login_check(self.username, self.passwrd):
            self.destroy()
            App = app()
            App.label(self.username)
            App.Button_checkout()
            App.Func_Button()
            App.mainloop()
        else:
            self.wrong_login()

    def wrong_login(self):
        er = Tk()
        er.geometry('200x60+650+340')
        Label(er, text="Неверный логин или пароль!!!").pack()
        b = Button(er, text="OKAY", command=er.destroy)
        b.pack()
        er.mainloop()


class app(Tk):
    def __init__(self):
        super().__init__()
        self.new_order = {}
        self.order ={}
        self.order['apple'] = 0
        self.order['banana'] = 0
        self.order['cherry'] = 0
        self.order['strawberry'] = 0
        self.order['orange'] = 0
        self.order['grape'] = 0
        self.order['carrot'] = 0
        self.order['tomato'] = 0
        self.order['cucumber'] = 0
        self.order['onion'] = 0
        self.order['pepper'] = 0
        self.order['potato'] = 0
        self.order['cheese'] = 0
        self.order['curd'] = 0
        self.order['kumys'] = 0
        self.order['milk'] = 0
        self.order['sour_cream'] = 0
        self.order['yogurt'] = 0
        self.n = 0
        self.total = 0
        self.check = ""
        self.title("Shop App")
        self.geometry('1530x790+0+0')
        self.img = get_pic('wipwip/board_win.png', 1530, 790)
        self.img_user = get_pic('wipwip/unnamed.jpg', 34, 34)
        self.img_logout = get_pic('wipwip/log_out.png', 32, 32)
        self.korzina = get_pic("wipwip/корзина.jpg", 50, 50)
        # фрукты
        self.banana = get_pic('fruits/banana.jpg', 200, 200)
        self.iphone = get_pic('fruits/iphone.jpg', 200, 200)
        self.grape = get_pic('fruits/grape.jpg', 200, 200)
        self.orange = get_pic('fruits/orange.jpg', 200, 200)
        self.cherry = get_pic('fruits/cherry.jpg', 200, 200)
        self.strawberry = get_pic('fruits/strawberry.jpg', 200, 200)
        # овощи
        self.carrot = get_pic('vegetables/carrot.jpg', 200, 200)
        self.cucumbers = get_pic('vegetables/cucumbers.jpg', 200, 200)
        self.onion = get_pic('vegetables/onion.jpg', 200, 200)
        self.pepper = get_pic('vegetables/pepper.jpg', 200, 200)
        self.potato = get_pic('vegetables/potato1.jpg', 200, 200)
        self.tomato = get_pic('vegetables/tomato.jpg', 200, 200)
        # dairy_products
        self.cheese = get_pic('dairy_products/cheese.jpg', 200, 200)
        self.curd = get_pic('dairy_products/curd.jpg', 200, 200)
        self.kumys = get_pic('dairy_products/kumys1.jpg', 200, 200)
        self.milk = get_pic('dairy_products/milk.jpg', 200, 200)
        self.sour_cream = get_pic('dairy_products/sour_cream.png', 200, 200)
        self.yogurt = get_pic('dairy_products/yogurt.jpg', 200, 200)

    def checkout_func(self, event):
        if self.check != "":
            for i in self.order:
                if self.order[i] != 0:
                    self.new_order[i] = self.order[i]
            self.w = Tk()
            self.w.geometry('500x500+500+50')
            self.l = Label(self.w, text="Name on card", font=20)
            self.l.pack()  # side=LEFT
            self.e = Entry(self.w, bd=5, font=20)
            self.e.pack()  # )
            Label(self.w, text="Card number", font=20).pack()
            self.e4 = Entry(self.w, bd=5, font=20)
            self.e4.pack()
            Label(self.w, text="Expiry date (MM/YY)", font=20).pack()
            self.e2 = Entry(self.w, bd=5, font=20)
            self.e2.pack()
            Label(self.w, text="Security code (3 digit)", font=20).pack()
            self.e3 = Entry(self.w, bd=5, font=20)
            self.e3.pack()
            Label(self.w, text="Address", font=20).pack()
            self.e5 = Entry(self.w, bd=5, font=20)
            self.e5.pack()
            Label(self.w, text="Payment amount: " + str(self.total) + '₸', font=20).pack()
            self.confirm = Button(self.w, text="Confirm purchase", command=self.check_info).pack()
            self.w.mainloop()
        else:
            er = Tk()
            er.geometry('300x60+650+340')
            Label(er, text="Пустая корзина").pack()
            b = Button(er, text="OKAY", command=er.destroy)
            b.pack()
            er.mainloop()

    def check_info(self):
        self.name = self.e.get()
        self.card = self.e4.get()
        self.date = self.e2.get()
        self.code = self.e3.get()
        self.address = self.e5.get()
        if self.name == "" or self.card == "" or self.date == "" or self.code == "" or self.address == "":
            er = Tk()
            er.geometry('300x60+650+340')
            Label(er, text="Заполните всю информацию").pack()
            b = Button(er, text="OKAY", command=er.destroy)
            b.pack()
            er.mainloop()
        elif not credit_card_check(self.card):
            er = Tk()
            er.geometry('300x60+650+340')
            Label(er, text="Номер карты введен неправильно").pack()
            b = Button(er, text="OKAY", command=er.destroy)
            b.pack()
            er.mainloop()
        try:
            if self.name != check_name(self.name)[0][0]:
                er = Tk()
                er.geometry('300x60+650+340')
                Label(er, text="Заполните имя правильно").pack()
                b = Button(er, text="OKAY", command=er.destroy)
                b.pack()
                er.mainloop()
        except IndexError:
            er = Tk()
            er.geometry('300x60+650+340')
            Label(er, text="Заполните имя правильно").pack()
            b = Button(er, text="OKAY", command=er.destroy)
            b.pack()
            er.mainloop()
        if not check_date(self.date):
            er = Tk()
            er.geometry('300x60+650+340')
            Label(er, text="Заполните дату правильно").pack()
            b = Button(er, text="OKAY", command=er.destroy)
            b.pack()
            er.mainloop()
        elif len(self.code) != 3 or not self.code.isdigit():
            er = Tk()
            er.geometry('300x60+650+340')
            Label(er, text="Заполните код безопасности правильно").pack()
            b = Button(er, text="OKAY", command=er.destroy)
            b.pack()
            er.mainloop()
        else:
            self.now = datetime.datetime.now().isoformat(' ', 'seconds')
            check = self.check.replace("₸", "T")
            check += f'''{"-" * 85}
            DATE: {self.now}
            TOTAL :{self.total} T
            '''
            with open('check.txt', 'w') as f:
                f.write(check)
            print(check)
            print(self.new_order)
            add_order(Login.username, self.card, self.address, self.now, self.total)
            order_id = get_order_id()[0]
            for elem in self.new_order:
                add_product_sales(order_id,elem,self.new_order[elem])
                q = self.new_order[elem]/get_price(elem)[0]
                update_stock(q,elem)
            self.w.destroy()
            self.destroy()
            er = Tk()
            er.geometry('300x60+650+340')
            Label(er, text="ORDER MADE SUCCESSFULLY").pack()
            b = Button(er, text="OKAY", command=er.destroy)
            b.pack()
            er.mainloop()

    def Func_Button(self):
        self.choice1 = ttk.Combobox(self, values=["fruits", "vegetables", "dairy products"], state="readonly", width=80)
        self.choice1.place(x=80, y=200)
        self.choice1.bind("<<ComboboxSelected>>", self.callBackFunc)
        self.choice3 = ttk.Entry(self, width=83)
        self.choice3.place(x=80, y=350)

    def price(self, string):
        self.l = Label(self, text=(string), background="white", width=5)
        self.l.config(font=("Courier", 44))
        self.l.place(x=270, y=570)
        self.l2 = Label(self, text="₸", background="white", font=("Courier", 44)).place(x=430, y=570)

    def label(self, username):
        self.l = Label(self, image=self.img).place(x=0, y=0)
        self.username = Label(self, text=username, pady=9, background="White").place(x=36, y=0)
        self.label_user = Label(self, image=self.img_user).place(x=0, y=0)
        self.l2 = Label(self, text="Choose what you want to buy", background="white").place(x=80, y=165)
        self.label_cart = Label(self, text="Shopping Cart", background="white").place(x=1000, y=165)

    def Button_checkout(self):
        self.checkout = Button(self, image=self.korzina)
        self.checkout.place(x=1350, y=445)
        self.checkout.bind('<Button-1>', self.checkout_func)

    def call_1(self, event):
        self.choice_for_fruit = ttk.Combobox(self,
                                             values=["apple", "banana", "cherry", "strawberry", "orange", "grape"],
                                             state='readonly', width=80)
        self.choice_for_fruit.place(x=80, y=250)
        self.choice_for_fruit.bind("<<ComboboxSelected>>", self.getname_fruit)

    def getname_fruit(self, event):

        u = self.choice_for_fruit.get()
        Label(self, text=u, width=71).place(x=80, y=300)
        if self.choice_for_fruit.get() == 'banana':
            Label(self, image=self.banana).place(x=60, y=570)
            self.price2 = str(shop.banana)
            self.price(self.price2)
        elif self.choice_for_fruit.get() == 'apple':
            Label(self, image=self.iphone).place(x=60, y=570)
            self.price2 = str(shop.apple)
            self.price(self.price2)
        elif self.choice_for_fruit.get() == 'cherry':
            Label(self, image=self.cherry).place(x=60, y=570)
            self.price2 = str(shop.cherry)
            self.price(self.price2)
        elif self.choice_for_fruit.get() == 'strawberry':
            Label(self, image=self.strawberry).place(x=60, y=570)
            self.price2 = str(shop.strawberry)
            self.price(self.price2)
        elif self.choice_for_fruit.get() == 'orange':
            Label(self, image=self.orange).place(x=60, y=570)
            self.price2 = str(shop.orange)
            self.price(self.price2)
        elif self.choice_for_fruit.get() == 'grape':
            Label(self, image=self.grape).place(x=60, y=570)
            self.price2 = str(shop.grape)
            self.price(self.price2)
        self.Button_Buy_fruit()

    def okay_fruit(self):
        try:
            b = int(self.choice3.get()) + 1
            if self.choice3.get() == '' or self.choice3.get() == "0":
                Label(self, text="the quantity (weight) was entered incorrectly!", background="white").place(
                    x=451, y=450)
            else:
                if int(self.choice3.get()) < get_quantity(self.choice_for_fruit.get()):
                    print(get_quantity(self.choice_for_fruit.get()))
                    self.n += 25
                    if self.n < 256:
                        self.order[self.choice_for_fruit.get()] += int(self.choice3.get()) * int(self.price2)
                        Label(self, text=self.choice_for_fruit.get() + " x " + self.choice3.get(),
                              background="white").place(
                            x=800, y=200 + self.n)
                        Label(self,
                              text='--------------------------------------------------------------------  ' + str(
                                  (int(self.choice3.get()) * (int(self.price2)))) + '₸', background="white").place(x=900,
                                                                                                                   y=200 + self.n)
                        self.total += int(self.choice3.get()) * (int(self.price2))
                        self.check += self.choice_for_fruit.get() + " x " + self.choice3.get() + '--------------------------------------------------------------------  ' + str(
                            (int(self.choice3.get()) * (int(self.price2)))) + '₸' + "\n"
                        print(self.check)
                        print(self.total)
                        Label(self, text="Total: " + str(self.total) + '₸', background='white').place(x=1000, y=490)
                    else:
                        win = Tk()
                        Label(win, text="exceeded the limit").pack()
                        win.mainloop()
                else:
                    er = Tk()
                    er.geometry('300x60+650+340')
                    Label(er, text="ORDER MORE THAN STOCK").pack()
                    b = Button(er, text="OKAY", command=er.destroy)
                    b.pack()
                    er.mainloop()
        except ValueError:
            Label(self, text="the quantity (weight) was entered incorrectly!", background="white").place(
                x=451, y=450)

    def Button_Buy_fruit(self):
        if self.choice_for_fruit:
            Button(self, text="Buy", command=self.okay_fruit).place(x=80, y=445)

    def call_2(self, event):
        self.choice_for_vegetables = ttk.Combobox(self,
                                                  values=["carrot", "tomato", "cucumber", "onion", "pepper", "potato"],
                                                  state='readonly', width=80)
        self.choice_for_vegetables.place(x=80, y=250)
        self.choice_for_vegetables.bind("<<ComboboxSelected>>", self.getname_veg)

    def getname_veg(self, event):
        u = self.choice_for_vegetables.get()
        Label(self, text=u, width=71).place(x=80, y=300)
        if self.choice_for_vegetables.get() == 'carrot':
            Label(self, image=self.carrot).place(x=60, y=570)
            self.price2 = str(shop.carrot)
            self.price(self.price2)
        elif self.choice_for_vegetables.get() == 'potato':
            Label(self, image=self.potato).place(x=60, y=570)
            self.price2 = str(shop.potato)
            self.price(self.price2)
        elif self.choice_for_vegetables.get() == 'cucumber':
            Label(self, image=self.cucumbers).place(x=60, y=570)
            self.price2 = str(shop.cucumber)
            self.price(self.price2)
        elif self.choice_for_vegetables.get() == 'onion':
            Label(self, image=self.onion).place(x=60, y=570)
            price2 = str(shop.onion)
            self.price(self.price2)
        elif self.choice_for_vegetables.get() == 'pepper':
            Label(self, image=self.pepper).place(x=60, y=570)
            self.price2 = str(shop.pepper)
            self.price(self.price2)
        elif self.choice_for_vegetables.get() == 'tomato':
            Label(self, image=self.tomato).place(x=60, y=570)
            self.price2 = str(shop.tomato)
            self.price(self.price2)
        self.Button_Buy_veg()

    def okay_veg(self):
        try:
            b = int(self.choice3.get()) + 1
            if self.choice3.get() == '' or self.choice3.get() == "0":
                Label(self, text="the quantity (weight) was entered incorrectly!", background="white").place(
                    x=451, y=450)
            else:
                if int(self.choice3.get()) < get_quantity(self.choice_for_vegetables.get()):
                    self.n += 25
                    if self.n < 256:
                        self.order[self.choice_for_vegetables.get()] += int(self.choice3.get()) * int(self.price2)
                        Label(self, text=self.choice_for_vegetables.get() + " x " + self.choice3.get(),
                              background="white").place(x=800, y=200 + self.n)
                        Label(self,
                              text='--------------------------------------------------------------------  ' + str(
                                  (int(self.choice3.get()) * (int(self.price2)))) + '₸', background="white").place(x=900,
                                                                                                                   y=200 + self.n)
                        self.total += int(self.choice3.get()) * (int(self.price2))
                        self.check += self.choice_for_vegetables.get() + " x " + self.choice3.get() + '--------------------------------------------------------------------  ' + str(
                            (int(self.choice3.get()) * (int(self.price2)))) + '₸' + "\n"
                        print(self.total)
                        Label(self, text="Total: " + str(self.total) + '₸', background='white').place(x=1000, y=490)
                    else:
                        win = Tk()
                        Label(win, text="exceeded the limit").pack()
                        win.mainloop()
                else:
                    er = Tk()
                    er.geometry('300x60+650+340')
                    Label(er, text="ORDER MORE THAN STOCK").pack()
                    b = Button(er, text="OKAY", command=er.destroy)
                    b.pack()
                    er.mainloop()
        except ValueError:
            Label(self, text="the quantity (weight) was entered incorrectly!", background="white").place(
                x=451, y=450)

    def Button_Buy_veg(self):
        if self.choice_for_vegetables:
            Button(self, text="Buy", command=self.okay_veg).place(x=80, y=445)

    def call_3(self, event):
        self.choice_for_dairy_products = ttk.Combobox(self, values=["cheese", "curd", "kumys", "milk", "sour_cream",
                                                                    "yogurt"], state='readonly', width=80)
        self.choice_for_dairy_products.place(x=80, y=250)
        self.choice_for_dairy_products.bind("<<ComboboxSelected>>", self.getname_dairy)

    def getname_dairy(self, event):
        u = self.choice_for_dairy_products.get()
        Label(self, text=u, width=71).place(x=80, y=300)
        if self.choice_for_dairy_products.get() == 'cheese':
            Label(self, image=self.cheese).place(x=60, y=570)
            self.price2 = str(shop.cheese)
            self.price(self.price2)
        elif self.choice_for_dairy_products.get() == 'curd':
            Label(self, image=self.curd).place(x=60, y=570)
            self.price2 = str(shop.curd)
            self.price(self.price2)
        elif self.choice_for_dairy_products.get() == 'kumys':
            Label(self, image=self.kumys).place(x=60, y=570)
            self.price2 = str(shop.kumys)
            self.price(self.price2)
        elif self.choice_for_dairy_products.get() == 'milk':
            Label(self, image=self.milk).place(x=60, y=570)
            self.price2 = str(shop.milk)
            self.price(self.price2)
        elif self.choice_for_dairy_products.get() == 'sour_cream':
            Label(self, image=self.sour_cream).place(x=60, y=570)
            self.price2 = str(shop.sour_cream)
            self.price(self.price2)
        elif self.choice_for_dairy_products.get() == 'yogurt':
            Label(self, image=self.yogurt).place(x=60, y=570)
            self.price2 = str(shop.yogurt)
            self.price(self.price2)
        self.Button_Buy_dairy()

    def okay_dairy(self):
        try:
            b = int(self.choice3.get()) + 1
            if self.choice3.get() == '' or self.choice3.get() == "0":
                Label(self, text="the quantity (weight) was entered incorrectly!", background="white").place(
                    x=451, y=450)
            else:
                if int(self.choice3.get()) < get_quantity(self.choice_for_fruit.get()):
                    self.n += 25
                    if self.n < 256:
                        self.order[self.choice_for_dairy_products.get()] += int(self.choice3.get()) * int(self.price2)
                        l1 = Label(self, text=self.choice_for_dairy_products.get() + " x " + self.choice3.get(),
                                   background="white")
                        l1.place(x=800, y=200 + self.n)
                        l2 = Label(self,
                                   text='--------------------------------------------------------------------  ' + str(
                                       (int(self.choice3.get()) * (int(self.price2)))) + '₸', background="white")
                        l2.place(x=900, y=200 + self.n)
                        self.total += int(self.choice3.get()) * (int(self.price2))
                        self.check += self.choice_for_dairy_products.get() + " x " + self.choice3.get() + '--------------------------------------------------------------------  ' + str(
                            (int(self.choice3.get()) * (int(self.price2)))) + '₸' + "\n"
                        print(self.total)
                        Label(self, text="Total: " + str(self.total) + '₸', background='white').place(x=1000, y=490)

                    else:
                        win = Tk()
                        Label(win, text="exceeded the limit").pack()
                        win.mainloop()
                else:
                    er = Tk()
                    er.geometry('300x60+650+340')
                    Label(er, text="ORDER MORE THAN STOCK").pack()
                    b = Button(er, text="OKAY", command=er.destroy)
                    b.pack()
                    er.mainloop()
        except ValueError:
            Label(self, text="the quantity (weight) was entered incorrectly!", background="white").place(
                x=451, y=450)

    def Button_Buy_dairy(self):
        if self.choice_for_dairy_products:
            Button(self, text="Buy", command=self.okay_dairy).place(x=80, y=445)

    def callBackFunc(self, event):
        Label(self, text="Now choose what exactly you want to buy", background="White").place(x=80, y=230)
        Label(self, text="Write the quantity (kg)", background="White").place(x=80, y=320)
        if self.choice1.get() == 'fruits':
            self.call_1(event)
        elif self.choice1.get() == 'vegetables':
            self.call_2(event)
        elif self.choice1.get() == "dairy products":
            self.call_3(event)


Login = login()
Login.login_screen()
Login.login_button()
Login.signup_button()
Login.admin_button()
Login.mainloop()

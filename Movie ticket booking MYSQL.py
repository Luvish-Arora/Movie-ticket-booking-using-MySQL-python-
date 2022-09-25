#FUNCTIONS

def movie_timmings():#THIS FUNCTION IS DEFINED FOR SELECTING MOVIE TIMINGS
    print("Select the movie timmings")
    print("1] 9:30am-12:30pm")
    print("2] 1:30pm-4:30pm")
    print("3] 6:00pm-9:00pm")
    print("4] 9:30pm-12:30am")
    a = int(input("choose the option:- "))#TO SELECT OPTION
    global v_timing#CALLING GLOBAL VALUE
    if a == 1:
       v_timing = "9:30am-12:30"
    if a == 2:
       v_timing = "1:30pm-4:30pm"
    if a == 3:
       v_timing = "6:00pm-9:00pm"
    if a == 4:
       v_timing = "9:30pm-12:30am"
    return [v_timing]#RETURNING VALUE

def Movie():#THIS FUNCTION IS DEFINED FOR SELECTING THE MOVIE
    print("Select movie type :- ")
    print("1] Comedy")
    print("2] Horror")
    print("3] Romance")
    print("4] Action")
    print("5] Drama")
    print("6] Thriller")
    print("7] Science friction")
    print("8] Animated")
    global v_movie#CALLING GLOBAL VALUE
    d = int(input("-->"))#TO SELECT OPTION
    if d == 1:
        print("1]Dhamaal 2]Welcome")
        u = int(input("Movie:- "))
        if u == 1:
            v_movie = "Dhamaal"
        if u == 2:
            v_movie = "Welcome"
    if d == 2:
        print("1]THE CONJURING  2]ANNABELLE")
        u = int(input("Movie:- "))
        if u == 1:
            v_movie = "THE CONJURING "
        if u == 2:
            v_movie = "ANNABELLE"
    if d == 3:
        print("1]HALF GIRLFRIEND  2]AASHIQUI 2")
        u = int(input("Movie:- "))
        if u == 1:
            v_movie = "HALF GIRLFRIEND"
        if u == 2:
            v_movie = "AASHIQUI 2"
    if d == 4:
        print("1]WAR  2]AVENGERS")
        u = int(input("Movie:- "))
        if u == 1:
            v_movie = "WAR"
        if u == 2:
            v_movie = "AVENGERS"
    if d == 5:
        print("1]GOLMAAL  2]DE DANA DAN")
        u = int(input("Movie:- "))
        if u == 1:
            v_movie = "GOLMAAL"
        if u == 2:
            v_movie = "DE DANA DAN"
    if d == 6:
        print("1]PUSHPA  2]KGF2")
        u = int(input("Movie:- "))
        if u == 1:
            v_movie = "PUSHPA"
        if u == 2:
            v_movie = "KGF2"
    if d == 7:
        print("1]SPIDER-MAN  2]AVATAR")
        u = int(input("Movie:- "))
        if u == 1:
            v_movie = "SPIDER-MAN"
        if u == 2:
            v_movie = "AVATAR"
    if d == 8:
        print("1]AVATAR  2]CARS")
        u = int(input("Movie:- "))
        if u == 1:
            v_movie = "AVATAR"
        if u == 2:
            v_movie = "CARS"
    return v_movie#RETURNING VALUE

def class1():#THIS FUNCTION IS DEFINED FOR SELECTING THE CLASS
        print("----1st class or 2nd class seats-----")
        global v_class#CALLING GLOBAL VALUE
        global v_cost#CALLING GLOBAL VALUE
        c = int(input("Please select the class:- "))#TO SELECT OPTION
        if c == 1:
            v_class = 'First class'
            v_cost = int(v_tic) * 400
        if c == 2:
            v_class = 'Second class'
            v_cost = int(v_tic) * 600

def snacks():#THIS FUNCTION IS DEFINED FOR SELECTING SNACKS
    global v_cost#CALLING GLOBAL VALUE
    global v_snacks#CALLING GLOBAL VALUE
    u = input("DO you like to add snacks:- ")#TO SELECT OPTION
    if u == 'yes' or u == 'YES' or u == 'Yes':
        print("CHECK COMBOS")
        print('1]Veg\n2]NON-Veg')
        q = int(input('Select:- '))#TO SELECT OPTION
        if q == 1:
            print('1]Burger=₹100\n2]Pizza=₹350\n3]Hot-Dog=₹80')
            w = int(input('Select:- '))#TO SELECT OPTION
            if w == 1:
                v_cost = v_cost + 100
                v_snacks = 'Veg Burger'
            if w == 2:
                v_cost = v_cost + 350
                v_snacks = 'Veg Pizza'
            if w == 3:
                v_cost = v_cost + 80
                v_snacks = 'Veg Hot-Dog'
        if q == 2:
            print('1]Burger=₹120\n2]Pizza=₹370\n3]Hot-Dog=₹100')
            w = int(input('Select:- '))#TO SELECT OPTION
            if w == 1:
                v_cost = v_cost + 120
                v_snacks = 'NON-Veg Burger'
            if w == 2:
                v_cost = v_cost + 370
                v_snacks = 'NON-Veg Pizza'
            if w == 3:
                v_cost = v_cost + 100
                v_snacks = 'NON-Veg Hot-Dog'
    else:
        v_snacks = 'Nothing'
    return v_snacks#RETURNING VALUE

def ticket():#THIS FUNCTION IS DEFINED FOR CREATING THE MOVIE TICKET
      print("\n \n \n")
      print(": ---------------------------------------- :\n: ---------------------------------------- :")
      print(": **************ABC THREATRE************** :\n: **************MOVIE TICKET************** :\n: ---------------------------------------- :\n: ---------------------------------------- :")
      print(": LOGIN ID----------->", uk)
      print(": NAME--------------->", v_fname, v_lname)
      print(': MOBILE NUMBER------>', f_phno)
      print(": NUMBER OF TICKETS-->", v_tic)
      print(': MOVIE NAME--------->', v_movie)
      print(": MOVIE TIMINGS------>", v_timing)
      print(": SANCKS ORDER------->", v_snacks)
      print(": Payment method----->",v_payment)
      print(": ---------------------------------------- :\n: ---------------------------------------- :")
      print(":       TOTAL COST===", v_cost, '                :')
      print(":        THANK YOU                         :")
      print(": ---------------------------------------- :\n: ---------------------------------------- :\n: ---------------------------------------- :\n: ---------------------------------------- :")

def password():#THIS FUNCTION IS DEFINED FOR CHECKING THE PASSWORD AFTER ENTERING THE USER-ID
    print("----------------------------------------")
    us = input('Enter the password:- ')
    for i in a:
        v_phno, v_tic, v_sex, v_fname, v_lname, v_passwd, v_userID, v_movie, v_timing, v_date, v_class, v_snacks, v_cost,v_payment = i#ENTERING ALL VALUE IN 'i' OF THE ROW OF A PARTICULAR USER-ID
    while us!= v_passwd:
     print("Incorrect password!!")
     print("----------------------------------------")
     us=input('Enter password again:- ')
    if us==v_passwd:
        print("----------------------------------------")
        print('Password is Correct')
        print("----------------------------------------")

def payment():#THIS FUNCTION IS DEFINED FOR SELECTING THE PAYMENT METHOD AND ALSO CHECKING IF THE CRETID CARD IS VALID OR NOT
    global v_payment#CALLING GLOBAL VALUE
    print("----------------------------------------")
    print('Select payment method:- ')
    print('1]Cash\n2]Credit card')
    t=int(input(':- '))#TO SELECT OPTION
    if t==1:
        print('Please pay:- ',v_cost)
        v_payment='Cash'
        print("----------------------------------------")
        return v_payment#RETURNING VALUE
    elif t==2:
        print('total cost:- ',v_cost)
        print("----------------------------------------")
        r=input('Enter credit card number:- ')

        while len(r)!=16:
             print("Please enter a valid card number")
             r=input('Enter again:- ')
        if len(r)==16:
            while not r[1:16].isdigit():
                print("Please enter a valid card number")
                r = input('Enter CVV again:- ')
            if r[1:16].isdigit():
                g=input('Enter Your CVV:- ')
                while len(g)!=3:
                 print("Please enter valid CVV")
                 g=input('Enter CVV again:- ')
                if len(g)==3:
                    while not g[1:3].isdigit():
                        print("Please enter valid CVV")
                        g = input('Enter CVV again:- ')
                    if g[1:3].isdigit:
                        print('Correct CVV')
                        print('Payment successfull')
                        print("----------------------------------------")
                        print("----------------------------------------")
                        v_payment='Credit card'
                        return v_payment#RETURNING VALUE

def select_display_record():#THIS FUNCTION IS DEFINED FOR SELECTING AND DISPLAYING THE DATA USING USER-ID
    v_userID=input("Enter the userID to check the record:- ")
    c1.execute("use luvishdb;")#SELECTING DATABASE
    c1.execute("Select * from movie_ticket_booking;")#EXECUTING IN MYSQL
    a=c1.fetchall()#FETCHING ALL DATA
    for i in a:
     if i[6]==v_userID:
        print("userID found!!\nDetails are as follow")
        print(i)
        print("----------------------------------------")
     conn.commit()



def delete_record():#THIS FUNCTION IS DEFINED FOR DELETING THE DATA OR THE ENTIRE ROW AFTER ENTERING USER-ID
    c1.execute("use luvishdb")  # SELECTING DATABASE
    print("Content of the table")
    c1.execute('select * from movie_ticket_booking;')
    print(c1.fetchall())
    n = input('Enter the userID to delete the record:- ')
    v_delete = "delete from movie_ticket_booking where v_userID='%s'"%(n)
    c1.execute(v_delete)#EXECUTING IN MYSQL
    conn.commit()
    print('Record deleted')
    print("----------------------------------------")
    c1.execute('select * from movie_ticket_booking;')
    print(c1.fetchall())

def phone_number():#THIS FUNCTION IS DEFINED FOR CHECKING IF THE MOBILE NUMBER IS VALID OR NOT
    global v_phno#CALLING GLOBAL VALUE
    v_phno = input("Enter phone number:- ")
    while len(v_phno)!=10:
        print("Please enter a valid Phone number")
        v_phno = input('Enter again:- ')
    if len(v_phno) == 10:
        while not v_phno[1:10].isdigit():
            print("Please enter a valid Phone number")
            v_phno = input('Enter again:- ')
        if v_phno[1:16].isdigit():
            return v_phno

#CREATING THE GLOBAL VALUES FOR FUNCTIONS
v_timing = ''
v_movie = ''
v_class = ''
v_cost = ''
v_snacks = ''
v_payment=''
v_phno=''

#IMPORTING MYSQL AND CHECKING WHEATHER PYTHON CONNECTOR IS WORKING
import mysql.connector as x
conn=x.connect(host = 'localhost',user='root',passwd='ansh03082004')
c1=conn.cursor()
if conn.is_connected():
    print ("Enter your choice as 1 , 2 , 3 , 4 ")
    print ("---------ABC THREATRE--------")
    print ("1] SIGN UP and book tickets ")#DISPLAYING DIFFERENT OPTIONS
    print ("2] LOG IN and book tickets ")
    print ("3] Search and display record ")
    print ("4] Delete a record ")
    con = input ("do you want to continue or not:- ")
    if con=='Yes'or con=='YES'or con=='yes':
        ch=int(input("Enter your choice:- "))
        if ch==1:
         v_fname = input("Enter your first name :- ")
         v_lname = input("Enter your last name :- ")
         v_sex = input("Enter your sex(Male/Female/others) :- ")
         phone_number()#FUNCTION CALLING
         f_phno=v_phno
         v_tic = input("Enter total tickets :- " )
         v_userID = input("Enter your userID :- ")
         uk=v_userID
         v_passwd = input ("Enter your passwd :- ")
         Movie()#FUNCTION CALLING
         print("----------------------------------------")
         movie_timmings()#FUNCTION CALLING
         v_date = input("Enter the date of booking :- ")
         print("----------------------------------------")
         class1()#FUNCTION CALLING
         print("----------------------------------------")
         snacks()#FUNCTION CALLING
         print("----------------------------------------")
         payment()#FUNCTION CALLING
         c1.execute("use luvishdb")#SELECTING DATABASE
         v_ins="insert into movie_ticket_booking \n values( '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(v_phno,v_tic,v_sex,v_fname,v_lname,v_passwd,v_userID,v_movie,v_timing,v_date,v_class,v_snacks,v_cost,v_payment)#FOR INSERTING VALUES IN TABLE
         c1.execute(v_ins)#EXECUTING IN MYSQL
         conn.commit()
         print("----------------------------------------")
         print("----------------------------------------")
         print ("Ticket booked congrats")
         print ("Thank you for visiting ABC theatre")
         print("----------------------------------------")
         ticket()#FUNCTION CALLING
        if ch ==2:
         print("------Please login------")
         v_fname = input("Enter your first name :- ")
         v_lname = input("Enter your last name:- ")
         uk=input('Enter your user-id:- ')
         c1.execute("use luvishdb")#SELECTING DATABASE
         e="select * from movie_ticket_booking where v_userID='{}';"
         c1.execute(e.format(uk))#EXECUTING IN MYSQL
         a=c1.fetchall()#FETCHING ALL DATA
         for i in a:
             v_phno, v_tic, v_sex, v_fname, v_lname, v_passwd, v_userID, v_movie, v_timing, v_date, v_class, v_snacks, v_cost,v_payment = i
             f_phno=v_phno

         if not a:

              print('User-ID not found!!')
              print("----------------------------------------")
         else:
              for i in a:
                 password()#FUNCTION CALLING
                 v_tic = int(input("Enter total tickets :- "))
                 f_tic=v_tic
                 f_date=input("Enter the date:- ")
                 Movie()#FUNCTION CALLING
                 f_movie=v_movie
                 print("----------------------------------------")
                 movie_timmings()#FUNCTION CALLING
                 f_timing=v_timing
                 print("----------------------------------------")
                 class1()#FUNCTION CALLING
                 f_class=v_class
                 print("----------------------------------------")
                 snacks()#FUNCTION CALLING
                 f_snacks=v_snacks
                 f_cost=v_cost
                 print("----------------------------------------")
                 payment()#FUNCTION CALLING
                 print("----------------------------------------")
                 print("********TICKET BOOKED********")
                 print("###########BOOKING CONFIRMED############")
                 print("###########ENJOY YOUR SHOW##########")

                 v_update="update movie_ticket_booking SET v_tic='%s' ,v_movie='%s' ,v_timing='%s' ,v_date='%s' ,v_class='%s' ,v_snacks='%s' ,v_cost='%s',v_payment='%s' where v_userID='%s'"%(f_tic, f_movie, f_timing, f_date, f_class, f_snacks, f_cost,v_payment,uk)#FOR UPDATING DATA IN TABLE AFTER SELECTING A USER-ID

                 c1.execute(v_update)#EXECUTING IN MYSQL
                 conn.commit()
                 ticket()#FUNCTION CALLING
        if ch==3:
            select_display_record()#FUNCTION CALLING

        if ch==4:
            delete_record()#FUNCTION CALLING

    else:
        print("BOOKING CANCLED")
else:
    print("BOOKING CANCLED")

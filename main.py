import eel
import mysql.connector

eel.init("templates")
db = mysql.connector.connect(
    user='root',
    password='2105',
    host='localhost',
    database='data_task')



@eel.expose()
def registration_user(login,pas):
    mycursore = db.cursor()
    conectform=("SELECT * FROM user_id  WHERE email = %s AND password =%s")
    conk = (login,pas,)

    mycursore.execute(conectform, conk)
    myresylt = mycursore.fetchall()

    db.commit()
    if len(myresylt) > 0:
        print(myresylt, "User yest")
        eel.login_yest()

    else :
     mycursore = db.cursor()
     conectform = "INSERT INTO data_task.user_id(email,password) VALUES(%s,%s)"
     conk = (login, pas,)

     mycursore.execute(conectform, conk)
     db.commit()
     print(conk)
     eel.New_user()


@eel.expose()
def recv_data(login,pas):
    mycursore = db.cursor()
    conectform = "SELECT id_user FROM user_id  WHERE email = %s AND password =%s"
    conk = (login,pas)

    mycursore.execute(conectform, conk)
    myresylt = mycursore.fetchall()
    print("Id - - -", mycursore.lastrowid)
    print(myresylt)
    for row in myresylt:
        id_user_name = row[0]

        print("Id User - " + str(id_user_name))

    if int(id_user_name) > 0:
        eel.log_user()
        if eel.log_user():

            @eel.expose

            def compil(name_task, task_text, task_data):
             mycursore = db.cursor()
             new_post = "INSERT INTO data_task.task_id (Task_text,Task_name,id_user,Data_Clock) VALUES (%s,%s,%s,%s);"
             post = (task_text, name_task, id_user_name,task_data,)

             new_res= "Select * From task_id "
             mycursore.execute(new_post, post)
             db.commit()

             mycursore.execute(new_res)
             myresyltpost = mycursore.fetchall()

             for newresult in myresyltpost:
                 print(newresult)


        else:
         print('No resultation')
    else:
     print("-")
    db.commit()


eel.start("Main.html", size=(800, 600))

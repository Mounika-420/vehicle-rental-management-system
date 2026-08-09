from flask import *
import data_base
from werkzeug.utils import secure_filename
import os
import ast
from datetime import date

aa=data_base.data_base()



app=Flask(__name__)
app.config['SECRET_KEY'] = '1'


def _is_logged_in():
    return "user_id" in session or "owner_id" in session


def _chatbot_response(question):
    q = (question or "").strip().lower()

    if not q:
        return "Please enter a question."

    if "help" in q:
        return (
            "You can ask about: table columns, available vehicles, vehicle rates, "
            "bookings, or my profile."
        )

    if "column" in q or "schema" in q or "table" in q:
        return (
            "Database columns:\n"
            "add_vehicle: id, vehicle_type, number, model, rate, image, status\n"
            "add_book: id, vehicle_name, date, duration, user_id, vehicle_id, status, user_name\n"
            "user_details: id, name, number, email, role, username, password, status"
        )

    if "available" in q and "vehicle" in q or "vehicle list" in q:
        vehicles = aa.show("select vehicle_type, model, number, rate from add_vehicle")
        if not vehicles:
            return "No vehicles found."
        lines = ["Available vehicles:"]
        for row in vehicles[:10]:
            lines.append(f"- {row[0]} | model: {row[1]} | no: {row[2]} | rate/day: {row[3]}")
        if len(vehicles) > 10:
            lines.append("...showing first 10 records.")
        return "\n".join(lines)

    if "rate" in q or "price" in q:
        vehicles = aa.show("select vehicle_type, model, rate from add_vehicle")
        if not vehicles:
            return "No rate information found."
        lines = ["Vehicle rates:"]
        for row in vehicles[:10]:
            lines.append(f"- {row[0]} {row[1]}: {row[2]} per day")
        if len(vehicles) > 10:
            lines.append("...showing first 10 records.")
        return "\n".join(lines)

    if "booking" in q or "booked" in q or "history" in q:
        if "user_id" in session:
            bookings = aa.show(
                "select vehicle_name, date, duration, status from add_book where user_id='"
                + str(session["user_id"])
                + "' order by id desc"
            )
        elif "owner_id" in session:
            bookings = aa.show(
                "select add_book.user_name, add_book.vehicle_name, add_book.date, add_book.duration, add_book.status "
                "from add_book inner join add_vehicle on add_book.vehicle_id = add_vehicle.id "
                "where add_vehicle.status='"
                + str(session["owner_id"])
                + "' order by add_book.id desc"
            )
        else:
            bookings = aa.show("select user_name, vehicle_name, date, duration, status from add_book order by id desc")

        if not bookings:
            return "No booking data found."

        lines = ["Booking details:"]
        for row in bookings[:10]:
            if len(row) == 4:
                lines.append(f"- {row[0]} on {row[1]} for {row[2]} day(s), status: {row[3]}")
            else:
                lines.append(f"- {row[0]} booked {row[1]} on {row[2]} for {row[3]} day(s), status: {row[4]}")
        if len(bookings) > 10:
            lines.append("...showing first 10 records.")
        return "\n".join(lines)

    if "profile" in q or "my details" in q:
        if "user_id" in session:
            profile = aa.show(
                "select name, number, email, role, username from user_details where id='"
                + str(session["user_id"])
                + "'"
            )
        elif "owner_id" in session:
            profile = aa.show(
                "select name, number, email, role, username from user_details where id='"
                + str(session["owner_id"])
                + "'"
            )
        else:
            profile = []

        if not profile:
            return "Profile data not found."
        p = profile[0]
        return f"Profile: name={p[0]}, number={p[1]}, email={p[2]}, role={p[3]}, username={p[4]}"

    return (
        "I can help with vehicle rental data. Try: "
        "'show table columns', 'available vehicles', 'vehicle rates', 'my bookings', or 'my profile'."
    )


@app.route("/")
def index():
    return render_template('login.html')

@app.route("/login",methods=['post','get'])
def login():
     if request.method == "POST":
        a=request.form['box1']
        b=request.form['box2']
        data=aa.show("select * from user_details where username='"+a+"' and password='"+b+"'")
        if data:
            if data[0][4]=='owner':
                session['owner_id']=data[0][0]
                return render_template("home.html")
            else:
                session['user_id']=data[0][0]
                session['user_name']=data[0][1]
                return redirect(url_for("user_home"))
        else:
            return render_template("login.html",data="username or password is incorrect")
     else:
            return render_template("login.html")
     



@app.route("/signup",methods=['post','get'])
def signup():
    if request.method == "POST":
        a = request.form['box1']
        b = request.form['box2']
        c = request.form['box3']
        d = request.form['box4']
        e = request.form['box5']
        f = request.form['box6']
        
        data=aa.show("select * from user_details where username='"+e+"' ")
            
        if data:
            return render_template("signup.html", data="Username already exists")
        else:
            aa.register("INSERT INTO user_details(name,number,email,role,username,password) values ('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"')")
            return render_template('signup.html', data="Registration successful")
    else:
        return render_template('signup.html')
    

    

# admin part

@app.route("/admin_home",methods=['post','get'])
def admin_home():
    if request.method == 'POST':
        a = request.form['box1']
        b = request.form['box2']
        c = request.form['box3']
        d = request.form['box4']
        image=request.files['box5']
        filename=secure_filename(image.filename)
        image.save(os.path.join("static/upload/", filename))
        e = session['owner_id']
        
        aa.register("INSERT INTO add_vehicle(vehicle_type,number,model,rate,image,status) values ('"+a+"','"+b+"','"+c+"','"+d+"','"+str(filename)+"','"+str(e)+"')")
        return render_template("home.html")
    else:
        return render_template("home.html")
    
@app.route("/view_request")
def view_request():
    vehicle_id = session['owner_id']
    data = aa.show(
        "select * from add_book inner join add_vehicle "
        "on add_book.vehicle_id = add_vehicle.id "
        "where add_vehicle.status= '"+str(vehicle_id)+"'"
    )
    return render_template("booking-history.html", data=data)

# user part
    
@app.route("/user_home")
def user_home():
    data=aa.show("select * from add_vehicle ")
    return render_template("user.html",data=data)

@app.route("/add_book", methods=['POST'])
def add_book():
    vehicle_id = request.form['id']
    vehicle_name = request.form['box2']
    booking_date = request.form['box3']
    duration = request.form['box4']

    user_id = session['user_id']
    user_name = session['user_name']

    print("Vehicle ID :", vehicle_id)
    print("Vehicle Name :", vehicle_name)
    print("Date :", booking_date)
    print("Duration :", duration)
    print("User :", user_name)

    query = (
        "INSERT INTO add_book(vehicle_name,date,duration,user_id,vehicle_id,user_name,status) "
        f"VALUES('{vehicle_name}','{booking_date}','{duration}','{user_id}','{vehicle_id}','{user_name}','booked')"
    )

    print(query)

    aa.register(query)

    return redirect(url_for("user_home"))


@app.route("/chatbot")
def chatbot_page():
    if not _is_logged_in():
        return redirect(url_for("login"))
    return render_template("chatbot.html")


@app.route("/chatbot/ask", methods=["POST"])
def chatbot_ask():
    if not _is_logged_in():
        return jsonify({"answer": "Please login first."}), 401

    user_message = request.form.get("message", "")
    answer = _chatbot_response(user_message)
    return jsonify({"answer": answer})




if __name__=="__main__":
    app.run(debug=True)

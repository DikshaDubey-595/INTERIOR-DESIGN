from flask import Flask, render_template, request, redirect, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# ======================
# DATABASE INIT
# ======================
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # contacts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            subject TEXT,
            message TEXT
        )
    """)

    # users table (NEW)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    conn.commit()
    conn.close()

# ======================
# PUBLIC ROUTES
# ======================
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/consultation')
def consultation():
    return render_template('consultation.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

# ======================
# LOGIN PAGE
# ======================
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    if username.strip() == "admin" and password.strip() == "1234":
        session['admin'] = True
        return redirect('/admin')
    else:
        flash("Invalid credentials ❌")
        return redirect('/login')

# ======================
# ADMIN (PROTECTED)
# ======================
@app.route('/admin')
def admin():
    if not session.get('admin'):
        return redirect('/login')

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts ORDER BY id DESC")
    data = cursor.fetchall()

    conn.close()

    return render_template('admin.html', messages=data)

# ======================
# LOGOUT
# ======================


@app.route('/logout')
def logout():
    session.pop('user', None)     # user login clear
    session.pop('admin', None)    # admin login bhi clear (safety)

    return redirect('/userlogin') # always safe page
# ======================
# FORM SUBMIT
# ======================
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    subject = request.form.get('subject', '')
    message = request.form['message']

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO contacts (name, email, subject, message)
        VALUES (?, ?, ?, ?)
    """, (name, email, subject, message))

    conn.commit()
    conn.close()

    flash("Message sent successfully ✅")

    return redirect('/contact')



@app.route('/userlogin')
def userlogin():
    return render_template('userlogin.html')

@app.route('/userlogin', methods=['POST'])
def userlogin_post():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (username, password))

    user = cursor.fetchone()
    conn.close()

    if user:
        session['user'] = username
        return redirect('/dashboard')
    else:
        flash("Invalid user credentials ❌")
        return redirect('/userlogin')
@app.route('/dashboard')
def dashboard():
    if not session.get('user'):
        return redirect('/userlogin')

    return render_template('dashboard.html', user=session['user'])

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, password))
        conn.commit()
        flash("Account created successfully ✅")
        return redirect('/userlogin')
    except:
        flash("User already exists ❌")
        return redirect('/register')
init_db()
@app.route("/")
def home():
    return "Website Live 🚀"

if __name__ == '__main__':
    app.run(debug=True)
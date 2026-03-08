from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'scope-india-secret-key-2024'

def get_db():
    conn = sqlite3.connect('database/registrations.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/placements')
def placements():
    return render_template('placements.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        try:
            data = {
                'full_name': request.form.get('full_name'),
                'date_of_birth': request.form.get('date_of_birth'),
                'gender': request.form.get('gender'),
                'educational_qualification': request.form.get('educational_qualification'),
                'mobile_number': request.form.get('mobile_number'),
                'email': request.form.get('email'),
                'guardian_name': request.form.get('guardian_name'),
                'guardian_occupation': request.form.get('guardian_occupation'),
                'guardian_mobile': request.form.get('guardian_mobile'),
                'course': request.form.get('course'),
                'training_mode': request.form.get('training_mode'),
                'location': request.form.get('location'),
                'preferred_timings': ', '.join(request.form.getlist('preferred_timings')),
                'address': request.form.get('address'),
                'country': request.form.get('country'),
                'state': request.form.get('state'),
                'city': request.form.get('city'),
                'pin_code': request.form.get('pin_code')
            }
            
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO registrations (
                    full_name, date_of_birth, gender, educational_qualification,
                    mobile_number, email, guardian_name, guardian_occupation,
                    guardian_mobile, course, training_mode, location,
                    preferred_timings, address, country, state, city, pin_code
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, tuple(data.values()))
            conn.commit()
            conn.close()
            
            flash('Registration successful! We will contact you soon.', 'success')
            return redirect(url_for('registration'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
    return render_template('registration.html')

@app.route('/admin')
def admin():
    conn = get_db()
    registrations = conn.execute('SELECT * FROM registrations ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('admin.html', registrations=registrations)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

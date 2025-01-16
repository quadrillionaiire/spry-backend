from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from ..models import User, School, ClassCode
from .. import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Collect form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        school_id = request.form['school']
        role = request.form.get('role')
        class_year = request.form.get('class_year')
        additional_info = request.form.get('additional_info')
        class_code = request.form.get('class_code')

        # Verify class code
        valid_code = ClassCode.query.filter_by(code=class_code, school_id=school_id, class_year=class_year, is_active=True).first()
        if not valid_code:
            flash("Invalid or inactive class code. Please contact alumni services for assistance.")
            return redirect(url_for('auth.signup'))

        # Create the user with pending status
        new_user = User(
            username=username,
            email=email,
            school_id=school_id,
            role=role,
            class_year=class_year,
            additional_info=additional_info,
            status='pending'
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.pending_approval'))

    # Retrieve schools for the dropdown
    schools = School.query.all()
    roles = ['Alumnus', 'Staff', 'Admin']
    class_years = list(range(1950, 2024))

    return render_template('signup.html', schools=schools, roles=roles, class_years=class_years)

from flask import render_template, redirect, url_for, flash
from . import homepage

@homepage.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('homepage/dashboard.html')

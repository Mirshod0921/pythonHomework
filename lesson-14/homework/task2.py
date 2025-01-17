
import sqlite3
import requests
import csv

from bs4 import BeautifulSoup
from datetime import datetime

def initialize_database():
    with sqlite3.connect("jobs.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs(
Job_Title TEXT,
Company Name TEXT,
Location TEXT,
Job_Description TEXT,
Application Link TEXT
);
""")
        
    conn.commit()

def scrape_jobs(url):
    response = requests.get(url)
    soap = BeautifulSoup(response.text, 'html.parser')
    job_listing = []
    
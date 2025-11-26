from models import get_url_url, create_table, insert_url, update_url, verify_shortCode_url
from flask import jsonify
import string
import random
from datetime import datetime

# Shortener url function
def shorter_url(url):
    short = str(''.join(random.choices(string.ascii_letters + string.digits, k=6))).lower()

    # Verify uniqueness
    while verify_shortCode_url(short):
        short = str(''.join(random.choices(string.ascii_letters + string.digits, k=6))).lower()

    created_at = updated_at = datetime.now()
    insert_url(short, url,created_at, updated_at)
    return jsonify({'short_url': short}), 201


# Retrieve long url function
def retrieve_long_url(short):
    result = get_url_url(short)
    if result:
        return jsonify({'long_url': result}), 200
    else:
        return jsonify({'error': 'Short URL not found'}), 404

# Update short url function
def update_short_url(short, new_long):
    if verify_shortCode_url(short):
        updated_at = datetime.now()
        res = update_url(short, new_long, updated_at)
        return jsonify({'result': res}), 200
    else:
        return jsonify({'error': 'Short URL not found'}), 404


from datetime import datetime, timedelta
import bcrypt


def get_current_time():
    return datetime.utcnow


def get_current_time_plus(days=0, hours=0, minutes=0, seconds=0):
    return get_current_time() + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)


def hash_password(pw):
    return bcrypt.hashpw(pw, bcrypt.gensalt(12))


def check_password(pw, pw_hash):
    return bcrypt.checkpw(pw, pw_hash)

from datetime import timedelta

def duration_to_seconds(**kwargs):
    return int(timedelta(**kwargs).total_seconds())
# Student/status.py

def get_status(avg):
    """Check status: if average is greater than 10, return 'Acc', else 'Fail'."""
    if avg > 10:
        return "Acc"   # Accepted
    else:
        return "Fail"  # Failed
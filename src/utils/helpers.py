def format_currency(amount):
    """Formats a numeric value as currency."""
    return f"₹{amount:,.2f}"

def format_date(date):
    """Formats a date object to a string in the format 'DD-MM-YYYY'."""
    return date.strftime("%d-%m-%Y")
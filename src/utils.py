import calendar
from datetime import date

def month_ranges(start=(2025, 11), end=(2026, 10)):
    y, m = start
    while (y, m) <= end:
        last = calendar.monthrange(y, m)[1]
        yield f"{y}-{m:02d}", date(y, m, 1).isoformat(), date(y, m, last).isoformat()
        m += 1
        if m == 13:
            y, m = y + 1, 1
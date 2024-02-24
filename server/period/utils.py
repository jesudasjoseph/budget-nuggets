from datetime import date, timedelta
from calendar import monthrange
from budget.models import Budget


def last_day_of_month(year: int, month: int):
    return monthrange(year, month)[1]


def get_date_range_from_date(requested_date: date, period_type):
    start_date = None
    end_date = None
    if period_type == Budget.MONTHLY:
        start_date = date(requested_date.year, requested_date.month, 1)
        end_date = date(
            requested_date.year,
            requested_date.month,
            last_day_of_month(requested_date.year, requested_date.month),
        )
    elif period_type == Budget.ANNUAL:
        start_date = date(requested_date.year, 1, 1)
        end_date = date(
            requested_date.year, 12, last_day_of_month(requested_date.year, 12)
        )
    elif period_type == Budget.BI_WEEKLY:
        start_day = 1 if requested_date.day < 15 else 15
        end_day = (
            14
            if start_day == 1
            else last_day_of_month(requested_date.year, requested_date.month)
        )
        start_date = date(requested_date.year, requested_date.month, start_day)
        end_date = date(requested_date.year, requested_date.month, end_day)

    return start_date, end_date


def get_next_date_range(end_date: date, period_type):
    start_date = end_date + timedelta(days=1)
    end_date = None
    if period_type == Budget.MONTHLY:
        end_date = date(
            start_date.year,
            start_date.month,
            last_day_of_month(start_date.year, start_date.month),
        )

    return start_date, end_date

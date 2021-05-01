from app import app, db
from app.models import Price_List, Price_List_Settings, Delete_Price_List
from datetime import datetime, date, timedelta, time
from dateutil.relativedelta import relativedelta

def update_price_list():
    db_price_list = db.session.query(Price_List)
    db_price_list_settings = db.session.query(Price_List_Settings).first()

    active_end_datetime = datetime.today() + timedelta(weeks = db_price_list_settings.active_prices_range)
    future_end_datetime = active_end_datetime + timedelta(weeks = db_price_list_settings.future_prices_range)

    for segment in db_price_list:
        if segment.start_date <= date.today():
            segment.range_type = 'PAST'
        elif segment.start_date < active_end_datetime.date():
            segment.range_type = 'ACTIVE'
        elif segment.start_date < future_end_datetime.date():
            segment.range_type = 'FUTURE'

    first_changeover_date = db_price_list.order_by(Price_List.start_date.asc()).first().start_date
    last_changeover_date = db_price_list.order_by(Price_List.start_date.desc()).first().start_date
    last_changeover_datetime = datetime(last_changeover_date.year, last_changeover_date.month, last_changeover_date.day)

    new_changeover_datetime = last_changeover_datetime + timedelta(days = (db_price_list_settings.default_changeover_day + 7 - last_changeover_date.weekday()) % 7)

    def previous_year_changeover(changeover_datetime):
        previous_year_date = (changeover_datetime - relativedelta(years=1)).date()

        if (previous_year_date >= first_changeover_date):
            closest_segment = min(db_price_list.all(), key=lambda x: abs(x.start_date - previous_year_date))
            return closest_segment

        return None

    if new_changeover_datetime.date() > last_changeover_date:
        if (previous_year_changeover(new_changeover_datetime)):
            previous_year_segment = previous_year_changeover(new_changeover_datetime)
            new_changeover = Price_List(
                start_date = new_changeover_datetime.date(),
                price = previous_year_segment.price,
                price_2_weeks = previous_year_segment.price_2_weeks,
                price_3_weeks = previous_year_segment.price_3_weeks,
                price_4_weeks = previous_year_segment.price_4_weeks,
                range_type = 'FUTURE'
            )
        else:
            new_changeover = Price_List(
                start_date = new_changeover_datetime.date(),
                range_type = 'FUTURE'
            )
        db.session.add(new_changeover)

    next_changeover_datetime = new_changeover_datetime + timedelta(weeks=1)
    while next_changeover_datetime <= future_end_datetime:
        if previous_year_changeover(next_changeover_datetime):
            previous_year_segment = previous_year_changeover(next_changeover_datetime)
            next_changeover = Price_List(
                start_date = next_changeover_datetime.date(),
                price = previous_year_segment.price,
                price_2_weeks = previous_year_segment.price_2_weeks,
                price_3_weeks = previous_year_segment.price_3_weeks,
                price_4_weeks = previous_year_segment.price_4_weeks,
                range_type = 'FUTURE'
            )
        else:
            next_changeover = Price_List(
                start_date = next_changeover_datetime.date(),
                range_type = 'FUTURE'
        )
        db.session.add(next_changeover)
        next_changeover_datetime += timedelta(weeks=1)

    db.session.commit()
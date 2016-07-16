
from datetime import datetime
from pytz import timezone

def google_cal(title,date_from,date_to,description):
    """

    :param title: string
    :param date_from: datetime object in Warsaw tz
    :param date_to: same
    :param description: string
    :return: formatted google calendar link
    """

    base_link = "http://www.google.com/calendar/event?action=TEMPLATE"

    title = title.replace(" ","%20")
    description = description.replace(" ","%20")
    title_link = "&text="+title

    date_from.replace(tzinfo=timezone('UTC'))
    date_to.replace(tzinfo=timezone('UTC'))
    date_from_gmt = date_from.astimezone(timezone('GMT'))
    date_to_gmt = date_to.astimezone(timezone('GMT'))

    dates_link = "&dates="+ date_from_gmt.strftime("%Y%m%dT%H%M%S") + "Z/"  + date_to_gmt.strftime("%Y%m%dT%H%M%S") + "Z"
    details_link = "&details=" + description

    link = base_link + title_link + dates_link + details_link

    return link


#przykład:
#print(google_cal("XDD lolol",datetime.now(timezone('Europe/Warsaw')), datetime.now(timezone('Europe/Warsaw')),"lolololo XDD lolo :p"))
import re
import pandas as pd


def total(data):
    date_formats = [
        '%d/%m/%Y,',
        '%d/%m/%y,',
        '%m/%d/%y,',
        '%d/%m/%Y,'
    ]

    # Initialize empty lists to store data
    users = []
    messages = []
    dates = []

    selected_format = None

    for date_format in date_formats:
        pattern = f'\d{{1,2}}/\d{{1,2}}/\d{{2,4}},'


        if re.search(pattern, data):
            if re.search(pattern, data):
                messages = re.split(pattern, data)[1:]
                dates = re.findall(pattern, data)
            try:
                # Try parsing the dates using the current format
                df = pd.DataFrame({'user_messages': messages, 'message_data': dates})
                df['message_data'] = pd.to_datetime(df['message_data'], format=date_format)
                df.rename(columns={'message_data': 'dates'}, inplace=True)
                selected_format = date_format
                break  # Break the loop if parsing is successful
            except ValueError:
                continue  # Continue to the next format if parsing fails

    if selected_format is None:
        raise ValueError("Unable to parse date format")


    users = []
    messages = []
    for message in df['user_messages']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df['month_num'] = df['dates'].dt.month
    df['year'] = df['dates'].dt.year
    df['month_name'] = df['dates'].dt.month_name()

    df = df.drop(columns=["user_messages","dates"], axis=1)
    return df

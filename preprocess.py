import pandas as pd
import numpy as np
import re


# Function to preprocess the chat data
def prepros(data):
    pattern = r'^(\d{2}/\d{2}/\d{2}), (\d{2}:\d{2}) - ([^:]+): (.+)$'
    matches = re.findall(pattern, data, flags=re.MULTILINE)

    # Create DataFrame
    tabel = pd.DataFrame(matches, columns=["date", "time", "sender", "message"])

    # Convert date to datetime format
    tabel["date"] = pd.to_datetime(tabel['date'], format="%d/%m/%y")
    tabel["month"] = tabel["date"].dt.month_name()

    # Extract year, day from the date
    tabel["year"] = tabel["date"].dt.year
    tabel["day"] = tabel["date"].dt.day
    tabel["time"] = pd.to_datetime(tabel["time"], format="%H:%M")
    tabel["minutes"] = tabel["time"].dt.minute
    tabel["hour"] = tabel["time"].dt.hour
    # Convert time to datetime and extract minutes and hour


    # Return the final DataFrame
    return tabel
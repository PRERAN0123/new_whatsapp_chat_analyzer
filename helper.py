from urlextract import URLExtract
extractor=URLExtract()
from wordcloud import WordCloud
from collections import Counter
english_stop_words = [
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself",
    "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this",
    "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing",
    "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further",
    "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
    "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "d", "ll", "m", "o", "re",
    "ve", "y", "ain", "aren", "couldn", "didn", "doesn", "hadn", "hasn", "haven", "isn", "ma", "mightn", "mustn", "needn", "shan", "shouldn", "wasn",
    "weren", "won", "wouldn"
]
import emoji

import pandas as pd
def help_to_fetch(selected_data, tabel):
    words = []
    if selected_data!="Overall":
        tabel = tabel[tabel["sender"] == selected_data]
    for i in tabel["message"]:
        words.extend(i.split())
    num = tabel.shape[0]
    links = []
    for i in tabel["message"]:
        links.extend(extractor.find_urls(i))

    msg=tabel[tabel["message"]=="<Media omitted>"].shape[0]



    return num, words,msg,len(links)
def most_busy_users(tabel):
    pp = tabel["sender"].value_counts()
    percentage_df = (tabel["sender"].value_counts(normalize=True) * 100).reset_index()
    percentage_df.columns = ["user", "percentage"]

    return pp,percentage_df
def create_word_cloud(selected_data, tabel):
    if selected_data != "Overall":
        tabel = tabel[tabel["sender"] == selected_data]
    max_used_words = []
    for i in tabel["message"]:
        words = i.split()
        filtered_words = [word for word in words if word.lower() not in english_stop_words]
        max_used_words.extend(filtered_words)
    wc=WordCloud(height=500,width=500,min_font_size=10,background_color="white")
    text = ' '.join(max_used_words)
    neww=wc.generate(text)
    return neww
def most_used_words(selected_data, tabel):
    if selected_data!="Overall":
        tabel = tabel[tabel["sender"] == selected_data]
    max_used_words = []
    for i in tabel["message"]:
        words = i.split()
        filtered_words = [word for word in words if word.lower() not in english_stop_words]
        max_used_words.extend(filtered_words)
    word_counts = Counter(max_used_words)
    most_common_words = pd.DataFrame(word_counts.most_common(20), columns=["MOST USED WORDS", "FREQUENCY OF MOST USED WORDS"])


    return most_common_words
def most_cmn_emoji(selected_data, tabel):
    emoji_list = []
    if selected_data!="Overall":
        tabel = tabel[tabel["sender"] == selected_data]
    for i in tabel["message"]:
        emoji_list.extend([a for a in i if a in emoji.EMOJI_DATA])
    emoji_counts = Counter(emoji_list)
    most_comn_emj=pd.DataFrame(emoji_counts.most_common(20),columns=["emoji","frequency"])
    return most_comn_emj
def montly_timeline(selected_data, tabel):
    if selected_data!="Overall":
        tabel = tabel[tabel["sender"] == selected_data]
    month_to_num = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }
    tabel["mon_num"] = tabel["month"].map(month_to_num)
    tabel.head()
    timeline = tabel.groupby(["year", "month", "mon_num"]).count()["message"].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline["month"][i] + "-" + str(timeline["mon_num"][i]))
    timeline["time"] = time
    return timeline
    # plt.plot(timeline["time"], timeline["message"])
    # plt.xticks(rotation="vertical")
def daily_timeline(selected_data, tabel):
    if selected_data!="Overall":
        tabel = tabel[tabel["sender"] == selected_data]
    tabel["new_date"] = tabel["date"].dt.date
    dates_timeline = tabel.groupby("new_date").count()["message"].reset_index()
    return dates_timeline
def weekly_active(selected_data, tabel):
    if selected_data!="Overall":
        tabel = tabel[tabel["sender"] == selected_data]
    tabel["active"] = tabel["date"].dt.day_name()
    active=tabel["active"].value_counts().reset_index()
    return active
def monthly_active(selected_data, tabel):
    if selected_data!="Overall":
        tabel = tabel[tabel["sender"] == selected_data]
    active_month=tabel["month"].value_counts().reset_index()
    return active_month
def heatwave(selected_data, tabel):
    if selected_data!="Overall":
        tabel = tabel[tabel["sender"] == selected_data]
    period = []
    for i in tabel["hour"]:
        if i == 23:
            period.append(str(i) + "-" + str('00'))
        elif i == 0:
            period.append(str(i) + "-" + str(i + 1))
        else:
            period.append(str(i) + "-" + str(i + 1))
    tabel["period"] = period
    period_counts = tabel["period"].value_counts().reset_index()
    period_counts.columns = ["period", "count"]
    pivot_data = tabel.pivot_table(index="year", columns="period", aggfunc="size", fill_value=0)
    return pivot_data


from collections import Counter
import emoji
import pandas as pd
import wordcloud
from wordcloud import WordCloud


def count(selected_user,df):
    if selected_user !='overall':
        df=df[df['user']==selected_user]

    num_messages=df.shape[0]
    media=df[df['message']=='<Media omitted>\n'].shape[0]
    group_messages=df[df['user']=='group notification'].shape[0]
    return num_messages,media,group_messages

def word_cloud(selected_user,df):
    if selected_user !='overall':
        df=df[df['user']==selected_user]

    df['message'] = df['message'].astype(str)

    wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc=wc.generate(df['message'].str.cat(sep=" "))
    return df_wc

"""def emoji(selected_user,df):
    if selected_user !='overall':
        df=df[df['user']==selected_user]

    emojis=[]
    for messages in df['message']:
        emojis.extend(c for c in messages if c in emoji.UNICODE_EMOJI["en"])
    emoji_df=pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df"""


def timeline(selected_user,df):
    if selected_user !='overall':
        df=df[df['user']==selected_user]

    timeline = df.groupby(['year', 'month_name']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month_name'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline









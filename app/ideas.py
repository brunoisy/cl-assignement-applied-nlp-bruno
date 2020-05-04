import pandas as pd
from models.autocomplete_topic import topic_predictor, topics

df = pd.read_csv("data/leuven_ideas.csv", dtype={'topics': str})
df.set_index("id", inplace=True)
df['topics'] = df['topics'].fillna("")


def get_ideas(search):
    if search:
        return df[df['title'].str.contains(search)]
    else:
        return df


def get_topic_suggestions(idea_id, entry):
    idea = df.loc[idea_id]
    idea_text = idea['title'] + ' ' + idea['body']
    predicted_topics = topics[[bool(p) for p in topic_predictor.predict([idea_text])[0]]]
    return predicted_topics.tolist()


def update_topics(idea_id, topics):
    df.at[idea_id, 'topics'] = ','.join(topics)

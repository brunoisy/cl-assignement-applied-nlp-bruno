import pandas as pd

df = pd.read_csv("data/leuven_ideas.csv", dtype={'topics': str})
df.set_index("id", inplace=True)
df['topics']=df['topics'].fillna("")

def get_ideas(search):
	if search:
		return df[df['title'].str.contains(search)]
	else:
		return df;

def get_topic_suggestions(idea_id, entry):
	topics = pd.DataFrame(df.topics.str.split(',').tolist()).stack().unique()
	return topics.tolist()

def update_topics(idea_id, topics):
	df.at[idea_id,'topics']= ','.join(topics)
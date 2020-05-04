import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline

# problem : multilabel text classification with (unknown) missing labels

# data preparation
ideas = pd.read_csv("data/leuven_ideas.csv", dtype={'topics': str})
ideas_with_topic = ideas[~ideas['topics'].isna()]  # all ideas that have at least one encoded topic
ideas_with_multiple_topics = ideas_with_topic[[len(t.split(',')) > 1 for t in ideas_with_topic['topics']]]

topics = pd.DataFrame(ideas_with_multiple_topics.topics.str.split(',').tolist()).stack().unique()

X = [t + ' ' + b for t, b in zip(ideas_with_multiple_topics['title'], ideas_with_multiple_topics['body'])]
y = [[int(t in idea_topics) for t in topics] for idea_topics in ideas_with_multiple_topics['topics']]  # binarizing output

# model
vectorizer = TfidfVectorizer(ngram_range=(1, 2),
                             max_df=0.8,
                             max_features=1000)
classifier = RandomForestClassifier(n_estimators=100,
                                    max_depth=5,
                                    class_weight='balanced',
                                    random_state=2020)
one_vs_rest = OneVsRestClassifier(classifier, n_jobs=8)
topic_predictor = Pipeline([('vectorizer', vectorizer), ('one_vs_rest', one_vs_rest)])
topic_predictor.fit(X, y)

if __name__ == "__main__":
    # train & test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2020)

    topic_predictor.fit(X_train, y_train)
    y_test_pred = topic_predictor.predict(X_test)
    print(classification_report(y_test, y_test_pred, target_names=topics))

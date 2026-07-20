import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from nlp_cleaner import preprocess_text
csv_path = r"C:\Users\HP\Downloads\archive\Resume\Resume.csv"
df = pd.read_csv(csv_path)
df['Clean_Resume'] = df['Resume_str'].apply(preprocess_text)
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['Clean_Resume'])
encoder = LabelEncoder()
y = encoder.fit_transform(df['Category'])
model = LogisticRegression(max_iter=1000)
model.fit(X, y)
vocab_list = list(tfidf.vocabulary_.keys())
classes_list = list(encoder.classes_)
with open("vocab.txt", "w", encoding="utf-8") as f:
    for word in vocab_list:
        f.write(word + "\n")
with open("classes.txt", "w", encoding="utf-8") as f:
    for category in classes_list:
        f.write(category + "\n")

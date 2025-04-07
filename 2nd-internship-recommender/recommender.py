import pandas as pd

# Load and preprocess dataset
df = pd.read_csv("dataset/internships_internshala.csv")
df['skills'] = df['skills'].fillna('')

def recommend_internships(user_skills):
    user_skills_set = set(map(str.strip, user_skills.lower().split(',')))

    def match_score(intern_skills):
        intern_skills_set = set(map(str.strip, intern_skills.lower().split(',')))
        return len(user_skills_set & intern_skills_set)

    df['score'] = df['skills'].apply(match_score)
    top_matches = df[df['score'] > 0].sort_values(by='score', ascending=False)

    return top_matches[['Title', 'Location', 'start_salary', 'max_salary', 'skills']].head(5).to_dict(orient='records')

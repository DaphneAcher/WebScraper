import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://stackoverflow.com/users/22656/jon-skeet?tab=questions"

headers = {
    'User-Agent': 'Mozilla/5.0'
}

# Step 1: Send GET request
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve the page. Status code:", response.status_code)

soup = BeautifulSoup(html_content, "html.parser")

questions = soup.find_all('div', class_='s-post-summary')

# Create empty lists to store data
titles = []
links = []
votes = []

# Loop through each question
for question in questions:
    title = question.find('a', class_='s-link') #class_ is based on the official syntax on beautifulsoup doc
    if title:
        titles.append(title.text.strip())
        links.append("https://stackoverflow.com" + title['href'])
    else:
        titles.append("")
        links.append("")

    vote = question.find('span', class_='s-post-summary--stats-item-number')
    if vote:
        votes.append(int(vote.text.strip()))
    else:
        votes.append(0)


# Create df using pandas
df = pd.DataFrame({
    'Title': titles,
    'Link': links,
    'Votes': votes
})

print(df.head())

mean_votes = df["Votes"].mean()
min_votes = df["Votes"].min()
max_votes = df["Votes"].max()
std_votes = df["Votes"].std()

# normalise using NumPy
#(x - min) / (max - min)
votes_array = np.array(df["Votes"])
votes_normalized = (votes_array - min_votes) / (max_votes - min_votes)

# Add new column to df
df["Votes_Normalized"] = votes_normalized

#filter
greater_mean = df[df["Votes"] > mean_votes]

# title longer than 60 characters
length_title = df[df["Title"].apply(lambda x: len(x) > 60)]

# Display filtered data
print("Questions with votes greater than mean:")
print(greater_mean[["Title", "Votes"]])

print("Questions with title length greater than 60:")
print(length_title[["Title", "Votes"]])

df_sorted = df.sort_values(by="Votes", ascending=False)
top5 = df_sorted.head(5)

# Save to CSV
top5.to_csv("top_questions.csv", index=False)


# Extra Credit
titles = top5["Title"]
votes = top5["Votes"]

plt.figure(figsize=(10, 5))
plt.barh(titles, votes)

plt.xlabel("Vote Count")
plt.ylabel("Question Title")
plt.title("Top 5 Questions by Vote Count")
plt.tight_layout()

plt.savefig("top5_bar_chart.png")

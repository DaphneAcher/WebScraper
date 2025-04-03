# 🧠 Stack Overflow Scraper:

A Python script that scrapes the most recent questions asked by Jon Skeet on Stack Overflow, analyzes vote counts, and visualizes the top 5 highest-voted questions.

## Features

- ✅ Scrapes question titles, URLs, and vote counts  
- 📊 Computes basic statistics (mean, min, max, std)  
- 🔄 Normalizes vote counts using Min-Max scaling  
- 🔎 Filters:
  - Questions with votes above the mean  
  - Questions with titles longer than 60 characters  
- 💾 Exports top 5 questions to CSV  
- 📈 Generates a bar chart of top 5 most upvoted questions  

---

## Requirements

- Python 3.7+
- Install dependencies:

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/jon-skeet-scraper.git
cd jon-skeet-scraper
```

2. Run the script:

```bash
python main.py
```

3. Output files:
- `top_questions.csv`: CSV file of the top 5 questions  
- `top5_bar_chart.png`: Horizontal bar chart visualization 


## Disclaimer

This script is for educational purposes only. Please respect [Stack Overflow’s terms of service](https://stackoverflow.com/legal/terms-of-service) and [robots.txt](https://stackoverflow.com/robots.txt) policies when scraping.

## Contact

Built with ❤️ by Daphne  


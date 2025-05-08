
# 📊 WhatsApp Chat Analyzer

[![Streamlit App](https://img.shields.io/badge/Try%20the%20App-Online-brightgreen?style=for-the-badge&logo=streamlit)](https://whatsappchatanalyzer001.streamlit.app/)

**WhatsApp Chat Analyzer** is a powerful and interactive tool built using Streamlit that lets you upload and explore the data from your exported WhatsApp chats. Get deep insights into your conversations with visualizations, word clouds, emoji analysis, and much more.

## 🚀 Live Demo

👉 Check out the live app here: [https://whatsappchatanalyzer001.streamlit.app/](https://whatsappchatanalyzer001.streamlit.app/)

## 🔍 Features

- 📈 **Message Statistics** – Total messages, media shared, and links sent.
- 🧑‍🤝‍🧑 **Most Active Users** – Identify the most talkative participants.
- ☁️ **Word Cloud** – Visualize the most frequently used words.
- 📊 **Most Common Words** – Filtered out by stop words for better insights.
- 😂 **Emoji Analysis** – Discover the most used emojis in the chat.
- 🗓️ **Daily & Monthly Timelines** – Track message activity over time.
- 🗓️ **Heatmap Visualization** – See activity levels by time of day.
- 🗓️ **Weekly & Monthly Activity Charts** – Spot trends in chat habits.

## 🛠️ How It Works

1. **Export your WhatsApp chat** (without media) from your phone.
2. **Upload the `.txt` file** using the Streamlit interface.
3. Choose a user or select "Overall" to see general stats.
4. Explore detailed breakdowns and visualizations.

## 🧾 Example Output

- Word cloud showing the top words
- Bar charts of top emojis and users
- Line graphs of message frequency over time

## 🏗️ Tech Stack

- **Python**
- **Pandas** – for data handling
- **Streamlit** – for the web app
- **Matplotlib / Seaborn** – for plotting
- **WordCloud** – for word cloud generation
- **urlextract** – for URL extraction
- **emoji** – for emoji analysis

## 📂 File Structure

- `app.py` – Main Streamlit application file.
- `preprocess.py` – Handles text parsing and datetime extraction.
- `helper.py` – Contains functions for analysis and visualization.

## ⚙️ Local Setup

To run the app locally:

```bash
git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
pip install -r requirements.txt
streamlit run app.py
```

### Required Libraries

Ensure the following Python libraries are installed:

```bash
streamlit
pandas
matplotlib
seaborn
wordcloud
emoji
urlextract
```

## 🤝 Contribution

Feel free to fork this repo and submit pull requests. Bug reports and feature suggestions are welcome!

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

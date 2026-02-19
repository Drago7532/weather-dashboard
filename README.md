# Weather Forecast Dashboard

A Python dashboard that shows weather forecasts for the next few days. Includes temperature, humidity, dew point, and sky conditions with interactive charts.

---

## Features

- Forecast temperature for 1–5 days
- Calculate and display dew point
- Show sky conditions with icons (Clear, Clouds, Rain, Snow)
- Interactive charts using Plotly
- User-friendly frontend with Streamlit

---

## Tech Stack

- Python
- Streamlit
- Plotly
- Requests
- OpenWeather API
- Optional: Pandas for data handling

---

## Installation
git clone https://github.com/drago7532/weather-dashboard.git
cd weather-dashboard

### Create virtual environment
python -m venv .venv

Windows:
.venv\Scripts\activate

Mac/Linux:
source .venv/bin/activate

pip install -r requirements.txt

### Running the code
python -m streamlit run main.py


import streamlit as st
import plotly.express as px
from datetime import datetime

from backend import get_data
from pathlib import Path

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


if place:
    # Get the temperature/sky data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            humidities = [dict["main"]["humidity"] for dict in filtered_data]
            dates = [
                datetime.strptime(d["dt_txt"], "%Y-%m-%d %H:%M:%S")
                .strftime("%d %b %H:%M")
                for d in filtered_data
            ]

            Tdew_values = [
                temp - ((100 - hum) / 5)
                for temp, hum in zip(temperatures, humidities)
            ]

            dew_points = [
                temp - tdew
                for temp, tdew in zip(temperatures, Tdew_values)
            ]


            # Create a temperature plot
            figure = px.line(
                x=dates,
                y=temperatures,
                labels={"x": "Date", "y": "Temperature (C)"},
            )

            st.plotly_chart(figure)

            st.header("Additional Weather Details")

            for date, temp, hum, dew in zip(dates, temperatures, humidities, dew_points):
                st.markdown(f"### {date}")
                col1, col2, col3 = st.columns(3)

                col1.metric("Temp", f"{temp:.1f}°C")
                col2.metric("Humidity", f"{hum}%")
                col3.metric("Dew Point", f"{dew:.2f}°C")

        if option == "Sky":
            BASE_DIR = Path(__file__).parent

            images = {
                "Clear": BASE_DIR / "images" / "clear.png",
                "Clouds": BASE_DIR / "images" / "cloud.png",
                "Rain": BASE_DIR / "images" / "rain.png",
                "Snow": BASE_DIR / "images" / "snow.png"
            }

            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images.get(condition) for condition in sky_conditions if condition in images]
            print(sky_conditions)
            st.image(image_paths, width=115)
    except KeyError:
        st.write("That place does not exist.")
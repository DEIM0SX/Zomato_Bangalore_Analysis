# 🍽️ Zomato Bangalore Restaurant Analysis Dashboard

This project presents a comprehensive **data analysis and visualization dashboard** based on Zomato's Bangalore restaurant dataset. Built using **Python**, **Pandas**, **Matplotlib**, **Seaborn**, and **Streamlit**, the dashboard reveals trends in customer preferences, pricing, restaurant types, and online behaviors.

## 📊 Key Features

- **Top Restaurant Locations**  
  Identify Bangalore's most saturated dining areas like BTM, HSR Layout, and Indiranagar.

- **Online Order & Table Booking Availability**  
  Pie charts showing how many restaurants support online orders and table bookings.

- **Most Popular Cuisines**  
  Explore the top 10 most offered cuisines in the city.

- **Average Cost for Two by Location**  
  Bar chart visualizing cost differences across major locations.

- **Most Popular Restaurants by Votes**  
  Highlights restaurants with the highest customer engagement.

- **Restaurant Type Distribution**  
  Pie chart showing prevalence of casual dining, quick bites, cafes, etc.

---

## 📁 Dataset

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants). It includes details such as:

- Restaurant name and location  
- Cuisines offered  
- Online ordering and booking availability  
- Approximate cost for two  
- Number of votes and ratings  
- Type of restaurant  

---

## 🚀 Tech Stack

- **Python**
- **Pandas** – data cleaning and manipulation  
- **Matplotlib & Seaborn** – for plotting and data visualization  
- **Streamlit** – interactive dashboard creation  
- **Jupyter Notebook** – for initial exploration and EDA  

---

## 🧹 Data Cleaning Highlights

- Converted `approx_cost(for two people)` from string to float  
- Handled null values in `rate`, `phone`, `cuisines`, etc.  
- Removed or replaced invalid entries  
- Parsed comma-separated numbers and standardized missing data

---

## 📂 How to Run

### ▶️ Option 1: Run in Streamlit

```bash
streamlit run zomato_dashboard.py

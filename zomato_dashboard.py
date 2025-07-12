import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page setup
st.set_page_config(page_title="Zomato Analysis Dashboard", layout="wide")
st.title("🍽️ Zomato Bangalore Restaurant Data Analysis")
st.markdown("This dashboard explores restaurant trends based on the Zomato dataset.")

# Load data
df = pd.read_csv("zomato.csv")  # Use your cleaned dataset name

# Clean cost column
df['approx_cost(for two people)'] = (
    df['approx_cost(for two people)']
    .astype(str)
    .str.replace(',', '')
    .str.strip()
    .replace('nan', None)
)

df['approx_cost(for two people)'] = pd.to_numeric(df['approx_cost(for two people)'], errors='coerce')

# ------------------------ BAR CHARTS SECTION ------------------------ #

# -- 1. Top 10 Restaurant Locations --
top_locations = df['location'].value_counts().head(10)
fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_locations.index, y=top_locations.values, palette='viridis', ax=ax1)
ax1.set_title('Top 10 Restaurant Locations', fontsize=14, fontweight='bold')
ax1.set_ylabel("Number of Restaurants")
ax1.set_xlabel("Location")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

col1, col2 = st.columns([3, 3])
with col1: st.pyplot(fig1)
with col2:
    st.markdown("### 📍 Top 10 Restaurant Locations")
    st.markdown("""
    - **BTM**, **Indiranagar**, and **HSR** are the most saturated areas.
    - High density = high competition, but also high opportunity.
    """)

# -- 2. Most Popular Cuisines --
popular_cuisines = df['cuisines'].value_counts().head(10)
fig2, ax2 = plt.subplots(figsize=(12, 6))
popular_cuisines.plot(kind='bar', color='steelblue', ax=ax2)
ax2.set_title('Most Popular Cuisines', fontsize=14, fontweight='bold')
ax2.set_xlabel('Cuisines')
ax2.set_ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

col3, col4 = st.columns([3, 3])
with col3: st.pyplot(fig2)
with col4:
    st.markdown("### 🍜 Most Popular Cuisines")
    st.markdown("""
    - **North Indian** and **Chinese** dominate.
    - Reflects both traditional and fast-food preferences.
    """)

# -- 3. Average Cost by Location --
avg_cost_location = df.groupby('location')['approx_cost(for two people)'].mean().sort_values(ascending=False).head(10)
fig3, ax3 = plt.subplots(figsize=(12, 6))
avg_cost_location.plot(kind='bar', color='teal', ax=ax3)
ax3.set_title('Average Cost for Two by Location', fontsize=14, fontweight='bold')
ax3.set_ylabel('Cost (₹)')
ax3.set_xlabel('Location')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

col5, col6 = st.columns([3, 3])
with col5: st.pyplot(fig3)
with col6:
    st.markdown("### 💸 Average Cost by Location")
    st.markdown("""
    - **Koramangala**, **Indiranagar** are more expensive.
    - Cost often reflects ambiance, service level, and cuisine type.
    """)

# -- 4. Most Popular Restaurants by Votes --
top_voted = df[['name', 'votes']].groupby('name').sum().sort_values(by='votes', ascending=False).head(10)
fig4, ax4 = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_voted.votes, y=top_voted.index, palette='crest', ax=ax4)
ax4.set_title('Most Popular Restaurants by Votes', fontsize=14, fontweight='bold')
ax4.set_xlabel('Votes')
ax4.set_ylabel('Restaurant Name')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()

col7, col8 = st.columns([3, 3])
with col7: st.pyplot(fig4)
with col8:
    st.markdown("### 🗳️ Most Voted Restaurants")
    st.markdown("""
    - These names reflect **brand trust** and **repeat visits**.
    - Useful for newcomers to benchmark competition.
    """)

# ------------------------ PIE CHARTS SECTION ------------------------ #

# -- 5. Online Order Availability --
order_type = df['online_order'].value_counts()
fig5, ax5 = plt.subplots(figsize=(5, 5))
order_type.plot(
    kind='pie',
    autopct='%1.1f%%',
    colors=['#90ee90', '#ff6f61'],
    explode=(0.05, 0),
    shadow=False,
    startangle=140,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1},
    ax=ax5
)
ax5.set_title("Online Order Availability", fontsize=14, fontweight='bold')
ax5.set_ylabel('')
plt.tight_layout()

col9, col10 = st.columns([3, 3])
with col9: st.pyplot(fig5)
with col10:
    st.markdown("### 🛒 Online Order Availability")
    st.markdown("""
    - Most restaurants support online delivery.
    - Reflects modern consumer preference for convenience.
    """)

# -- 6. Restaurant Type Distribution --
rest_types = df['rest_type'].value_counts().head(5)
fig6, ax6 = plt.subplots(figsize=(5, 5))
rest_types.plot(
    kind='pie',
    colors=['#40358f', '#584cb0', '#8277cd', '#c51818', '#9b1212'],
    autopct='%1.1f%%',
    shadow=False,
    startangle=140,
    ax=ax6
)
ax6.set_title('Restaurant Type Distribution')
ax6.set_ylabel('')
plt.tight_layout()

col11, col12 = st.columns([3, 3])
with col11: st.pyplot(fig6)
with col12:
    st.markdown("### 🍽️ Restaurant Type Breakdown")
    st.markdown("""
    - **Casual Dining** and **Quick Bites** lead the way.
    - Ideal for budget-conscious and fast-paced lifestyles.
    """)

# -- 7. Table Booking Availability --
booking_availability = df['book_table'].value_counts()
fig7, ax7 = plt.subplots(figsize=(5, 5))
booking_availability.plot(
    kind='pie',
    colors=['#8277cd', '#c51818'],
    autopct='%1.1f%%',
    shadow=False,
    startangle=140,
    ax=ax7
)
ax7.set_title("Table Booking Availability")
ax7.set_ylabel('')
plt.tight_layout()

col13, col14 = st.columns([3, 3])
with col13: st.pyplot(fig7)
with col14:
    st.markdown("### 🪑 Table Booking")
    st.markdown("""
    - Only a minority offer booking.
    - More common in premium and high-end spots.
    """)


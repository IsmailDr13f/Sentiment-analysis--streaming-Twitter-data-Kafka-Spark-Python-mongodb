# run with "streamlit run Dashboard.py"
import streamlit as st
import pandas as pd
import pymongo
from st_circular_progress import CircularProgress
import matplotlib.pyplot as plt
import numpy as np
import altair as alt

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])


client = init_connection()

@st.cache_data(ttl=600)
def get_data():
    db = client.tweet_db
    items = db.tweet_col.find()
    items = list(items)  
    return items

items = get_data()

def fetch_data():
    client = init_connection()
    db = client.tweet_db
    items = db.tweet_col.find()
    items = list(items)
    return items

def process_data(items):
    data = []
    sentiments = {'Positive': 0, 'Neutral': 0, 'Negative': 0, 'Irrelevant': 0}
    for item in items:
        data.append({
            "Client": item["Entity"],
            "Tweet Content": item["tweet_content"],
            "Predicted Sentiment": {
                0: 'Positive',
                1: 'Neutral',
                2: 'Negative',
                3: 'Irrelevant'
            }.get(item["prediction"], 'Unknown')
        })
        prediction = {
            0: 'Positive',
            1: 'Neutral',
            2: 'Negative',
            3: 'Irrelevant'
        }.get(item["prediction"], 'Irrelevant')  # Default to 'Irrelevant' if prediction is not in the mapping
        sentiments[prediction] += 1
    
    df = pd.DataFrame(data)
    sentiments_df = pd.DataFrame.from_dict(sentiments, orient='index', columns=['Count'])
    return df, sentiments_df

data = []
for item in items:
    data.append({
        "Client": item["Entity"],
        "Tweet Content": item["tweet_content"],
        "Predicted Sentiment": {
            0: 'Positive',
            1: 'Neutral',
            2: 'Negative',
            3: 'Irrelevant'
        }.get(item["prediction"], 'Unknown') 
    })

df = pd.DataFrame(data)


# Count sentiment predictions
sentiments = {'Positive': 0, 'Neutral': 0, 'Negative': 0, 'Irrelevant': 0}
for item in items:
        prediction = {
            0: 'Positive',
            1: 'Neutral',
            2: 'Negative',
            3: 'Irrelevant'
        }.get(item["prediction"], 'Irrelevant')  # Default to 'Irrelevant' if prediction is not in the mapping
        sentiments[prediction] += 1

# Convert sentiment counts to a DataFrame
sentiments_df = pd.DataFrame.from_dict(sentiments, orient='index', columns=['Count'])

st.title(":orange[SENTIMENT ANALYSIS JOURNAL 🐦]")
col12, col22= st.columns([0.5, 0.5],gap="large")
with col12:   
    col12_con=st.container(border=True)
    with col12_con:
        st.header("💻Created By:")
        st.markdown(":red-background[|------DRIEF ISMAIL        🪓]")
        st.markdown(":blue-background[|------AMZIL AMMAR         👮🏻‍♂️]")
        st.markdown(":orange-background[|------ARICHI FATIMAZOHRA  👩🏻‍🍳]")
with col22:
     col22_con= st.container(border=True)
     with col22_con:
        st.header("👾Visit us on GitHub:")
        import base64
        with open("gthb.webp", "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data)
        data = "data:image/png;base64," + encoded.decode("utf-8")

        from streamlit_card import card
        hasClicked = card(
            title="",
            text="",
            image=data,
            url="https://github.com/IsmailDr13f",
            styles={
        "card": {
            "width": "400px",
            "height": "100px",
            "border-radius": "60px",
            "box-shadow": "0 0 10px rgba(232, 232, 232, 0.8)",
            "margin":"5px"
        }
        }
        )

        


col1, col2= st.columns([0.5, 0.5],gap="large")

with col1:
    col1_container = st.container(border=True)
    with col1_container:
        col1_con1,col1_con2 = st.columns([0.9, 0.1])
        with col1_con1:
            st.header("🗃️ Data Visualisation ")
        with col1_con2:
            if st.button("🔄"):
                
                with st.spinner("Fetching data..."):
                    items = fetch_data()
                    df, sentiments_df = process_data(items)
                    #st.rerun()
                    #st.success("Data refreshed successfully!")
        num_rows = st.slider("Choose Number of Rows:", 1, len(df), len(df))
        st.dataframe(df.head(num_rows),width=1500,height =670,hide_index=True,)

with col2:
    col2_container = st.container(border=True)
    with col2_container:
                st.header("✅ Predictions accurate by over 89% ")
               # Create a DataFrame with precision, recall, F1-score, and accuracy values
                data = pd.DataFrame({
                    'Metric': ['Precision', 'Recall', 'F1-score', 'Accuracy'],
                    'Value': [0.6, 0.92, 0.727, 0.89]
                })

                # Create an Altair chart
                chart = alt.Chart(data).mark_bar().encode(
                    y='Value',
                    x=alt.Y('Metric', title=None),
                    color=alt.Color('Metric', legend=None)
                )
                st.altair_chart(chart, use_container_width=True)
                

    # Create a Streamlit container with a border
    chart_container = st.container(border=True)
    # Plot horizontal bar chart
    sentiments_dff = pd.DataFrame.from_dict(sentiments, orient='index', columns=['Count']).reset_index()
    chart = alt.Chart(sentiments_dff).mark_bar().encode(
        x=alt.X('Count:Q', axis=alt.Axis(title='Count')),
        y=alt.Y('index:N', axis=alt.Axis(title='Sentiment')),
        color='index:N'
    ).properties(
        width=400,
        height=300
    ).properties(
    width=400,
    height=300,
    padding={"left": 20, "top": 20, "right": 20, "bottom": 20},  # Add padding for border
    )

    with chart_container:
        st.header("📊 SENTIMENT DISTRIBUTION ")
        # Display chart
        st.altair_chart(chart, use_container_width=True)

ciner = st.container(border=True)
with ciner:
    # Streamlit app
    st.header('💡 SENTIMENT DISTRIBUTION BY CLIENT')
    coli1, coli2= st.columns([0.3, 0.7],gap="large")
    # Filter DataFrame based on selected sentiment
    
    with coli1:
        # Selectbox for sentiment
        sentiment_options = ['Positive', 'Neutral', 'Negative', 'Irrelevant']
        selected_sentiment = st.selectbox('Select Sentiment:', sentiment_options)
        filtered_df = df[df['Predicted Sentiment'] == selected_sentiment]
        sous_con=st.container(border=True)
        with sous_con:
             #st.markdown(":orange[Number of", selected_sentiment, "sentiments by client:]")
             st.write(":orange[Number of]", selected_sentiment, ":orange[sentiments by client:]")
             for client, count in filtered_df['Client'].value_counts().items():
                st.write(f"- {client}: {count}")
    with coli2:
        cinero = st.container(border=True)
        with cinero:
            # Group by client and count tweets
            if not filtered_df.empty:
                sentiment_chart = alt.Chart(filtered_df).mark_bar().encode(
                    x='Client',
                    y='count()',
                    color='Client'
                ).properties(
                    width=600,
                    height=400,
                    title=f'Number of {selected_sentiment} Sentiments by Client'
                )
                
                st.altair_chart(sentiment_chart, use_container_width=True)
            else:
                st.write(f"No {selected_sentiment} sentiments found.")

        




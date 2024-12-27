import streamlit as st
import pandas as pd
import altair as alt
from datasets import load_dataset

# Streamlit app title
st.set_page_config(page_title="LLM Model Analytics", layout="wide")
st.title("LLM Model Analytics")

# Load dataset from Hugging Face
@st.cache_data
def fetch_data():
    dataset = load_dataset("burtenshaw/most_used_models", split="train")
    df = pd.DataFrame(dataset)
    df['lastModified'] = pd.to_datetime(df['lastModified'])
    df['likes'] = df['likes'].astype(int)
    return df

# Load data
df = fetch_data()

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("## Choose a Page:")

# Navigation with icons
pages = {
    "Dashboard": "🏠",
    "Raw Data": "📋",
    "Top Models by Likes": "📊",
    "Filtered Visualization": "🔍"
}

selected_page = st.sidebar.radio(
    "",
    options=list(pages.keys()),
    format_func=lambda x: f"{pages[x]} {x}",
    key="navigation"
)

st.sidebar.markdown("---")  # Divider for spacing

# Page 1: Dashboard
if selected_page == "Dashboard":
    st.header("Dashboard Summary")
    st.write(f"Total Models in Dataset: **{len(df)}**")
    st.write(f"Dataset covers years from **{df['lastModified'].dt.year.min()}** to **{df['lastModified'].dt.year.max()}**.")
    
    # Convert numpy.int64 to int
    most_liked_model = df.loc[df['likes'].idxmax(), 'id']
    most_likes = int(df['likes'].max())
    most_active_author = df['author'].value_counts().idxmax()
    most_active_count = int(df['author'].value_counts().max())

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Most Liked Model", most_liked_model, most_likes)
    with col2:
        st.metric("Most Active Author", most_active_author, most_active_count)

    # Likes Over Time
    st.subheader("Likes Over Time")
    time_chart = (
        alt.Chart(df)
        .mark_area(opacity=0.7, color="skyblue")
        .encode(
            x=alt.X("lastModified:T", title="Date"),
            y=alt.Y("likes:Q", title="Likes"),
            tooltip=["id", "author", "likes", "lastModified"],
        )
        .properties(
            width=800,
            height=400,
            title="Likes Distribution Over Time"
        )
    )
    st.altair_chart(time_chart, use_container_width=True)

    # Authors Contribution
    st.subheader("Authors Contribution")
    author_chart = (
        alt.Chart(df)
        .mark_bar(opacity=0.8, color="teal")
        .encode(
            x=alt.X("author:N", sort="-y", title="Author"),
            y=alt.Y("count():Q", title="Number of Models"),
            tooltip=["author", "count()"]
        )
        .properties(
            width=800,
            height=400,
            title="Number of Models by Author"
        )
    )
    st.altair_chart(author_chart, use_container_width=True)

# Page 2: Raw Data
elif selected_page == "Raw Data":
    st.header("Raw Data")
    st.write("Explore the raw dataset below:")
    st.dataframe(df)

# Page 3: Top Models by Likes
elif selected_page == "Top Models by Likes":
    st.header("Top Models by Likes")
    chart = (
        alt.Chart(df)
        .mark_bar(opacity=0.8, color="steelblue")
        .encode(
            x=alt.X("likes:Q", title="Likes"),
            y=alt.Y("id:N", sort="-x", title="Model ID"),
            color=alt.Color("author:N", scale=alt.Scale(scheme="tableau20"), title="Author"),
            tooltip=["id", "author", "likes", "lastModified"],
        )
        .properties(
            width=800,
            height=400,
            title="Top LLM Models by Likes"
        )
    )
    st.altair_chart(chart, use_container_width=True)

    # Additional Visualization: Distribution of Likes
    st.subheader("Distribution of Likes")
    likes_chart = (
        alt.Chart(df)
        .mark_boxplot(color="orange")
        .encode(
            y=alt.Y("likes:Q", title="Likes"),
            tooltip=["id", "author", "likes"]
        )
        .properties(
            width=800,
            height=300,
            title="Likes Distribution"
        )
    )
    st.altair_chart(likes_chart, use_container_width=True)

# Page 4: Filtered Visualization
elif selected_page == "Filtered Visualization":
    st.header("Filtered Visualization")
    st.sidebar.header("Filter Options")
    authors = st.sidebar.multiselect("Select authors", options=df['author'].unique(), default=df['author'].unique())

    # Apply filter
    filtered_df = df[df['author'].isin(authors)]

    # Filtered chart
    filtered_chart = (
        alt.Chart(filtered_df)
        .mark_bar(opacity=0.8)
        .encode(
            x=alt.X("likes:Q", title="Likes"),
            y=alt.Y("id:N", sort="-x", title="Model ID"),
            color=alt.Color("author:N", scale=alt.Scale(scheme="set3"), title="Author"),
            tooltip=["id", "author", "likes", "lastModified"],
        )
        .properties(
            width=800,
            height=400,
            title="Filtered Top LLM Models by Likes"
        )
    )
    st.altair_chart(filtered_chart, use_container_width=True)

    # Filtered Data Table
    st.write("Filtered Data Table")
    st.dataframe(filtered_df)

    # Additional Visualization: Filtered Likes Over Time
    st.subheader("Filtered Likes Over Time")
    filtered_time_chart = (
        alt.Chart(filtered_df)
        .mark_line(opacity=0.8, color="purple")
        .encode(
            x=alt.X("lastModified:T", title="Date"),
            y=alt.Y("likes:Q", title="Likes"),
            tooltip=["id", "author", "likes", "lastModified"],
        )
        .properties(
            width=800,
            height=400,
            title="Filtered Likes Over Time"
        )
    )
    st.altair_chart(filtered_time_chart, use_container_width=True)

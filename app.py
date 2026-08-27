import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# PAGE CONFIGURATION


st.set_page_config(
    page_title="Online Retail Customer Segmentation",
    page_icon="🛍️",
    layout="wide"
)

# LOAD DASHBOARD DATA


@st.cache_data
def load_dashboard_data():

    monthly_revenue = pd.read_csv(
        "data/dashboard/monthly_revenue.csv"
    )

    top_products = pd.read_csv(
        "data/dashboard/top_products.csv"
    )

    country_revenue = pd.read_csv(
        "data/dashboard/country_revenue.csv"
    )

    day_sales = pd.read_csv(
        "data/dashboard/day_sales.csv"
    )

    kpis = pd.read_csv(
        "data/dashboard/kpis.csv"
    )

    rfm = pd.read_csv(
        "data/rfm_customer_segments.csv"
    )

    return (
        monthly_revenue,
        top_products,
        country_revenue,
        day_sales,
        kpis,
        rfm
    )


# LOAD ML MODELS


@st.cache_resource
def load_models():

    kmeans = joblib.load(
        "models/kmeans_model.pkl"
    )

    scaler = joblib.load(
        "models/scaler.pkl"
    )

    return kmeans, scaler


# LOAD EVERYTHING


try:

    (
        monthly_revenue,
        top_products,
        country_revenue,
        day_sales,
        kpis,
        rfm
    ) = load_dashboard_data()

    kmeans, scaler = load_models()

except Exception as e:

    st.error(
        f"Unable to load project files: {e}"
    )

    st.stop()

# HEADER


st.title(
    "🛍️ Online Retail Customer Segmentation"
)

st.markdown(
    """
    ### RFM Analysis + K-Means Clustering

    Analyze sales performance and understand customer
    purchasing behavior through data-driven segmentation.
    """
)

# SIDEBAR

st.sidebar.title("📊 Dashboard")

page = st.sidebar.radio(
    "Select Analysis",
    [
        "Overview",
        "Sales Analysis",
        "Customer Segmentation",
        "Customer Details"
    ]
)

# OVERVIEW

if page == "Overview":

    st.header("📊 Business Overview")

    revenue = float(
        kpis.loc[
            kpis["Metric"] == "Total Revenue",
            "Value"
        ].iloc[0]
    )

    orders = int(
        kpis.loc[
            kpis["Metric"] == "Total Orders",
            "Value"
        ].iloc[0]
    )

    customers = int(
        kpis.loc[
            kpis["Metric"] == "Total Customers",
            "Value"
        ].iloc[0]
    )

    products = int(
        kpis.loc[
            kpis["Metric"] == "Total Products",
            "Value"
        ].iloc[0]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Revenue",
        f"£{revenue:,.2f}"
    )

    col2.metric(
        "Total Orders",
        f"{orders:,}"
    )

    col3.metric(
        "Total Customers",
        f"{customers:,}"
    )

    col4.metric(
        "Total Products",
        f"{products:,}"
    )

    st.divider()

    st.subheader("📈 Monthly Revenue Trend")

    fig, ax = plt.subplots(
        figsize=(12, 5)
    )

    ax.plot(
        monthly_revenue["YearMonth"],
        monthly_revenue["Revenue"],
        marker="o"
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    ax.set_title("Monthly Revenue Trend")

    plt.xticks(rotation=45)

    st.pyplot(fig)

# SALES ANALYSIS

elif page == "Sales Analysis":

    st.header("📈 Sales Analysis")

    st.subheader(
        "🛍️ Top 10 Products by Revenue"
    )

    product_chart = top_products.set_index(
        "Description"
    )["Revenue"]

    st.bar_chart(product_chart)

    st.subheader(
        "🌍 Top 10 Countries by Revenue"
    )

    country_chart = country_revenue.set_index(
        "Country"
    )["Revenue"]

    st.bar_chart(country_chart)

    st.subheader(
        "📅 Revenue by Day of Week"
    )

    day_chart = day_sales.set_index(
        "DayOfWeek"
    )["Revenue"]

    st.bar_chart(day_chart)

# CUSTOMER SEGMENTATION


elif page == "Customer Segmentation":

    st.header("👥 Customer Segmentation")

    total_segments = rfm[
        "Cluster"
    ].nunique()

    total_customers = rfm[
        "CustomerID"
    ].nunique()

    col1, col2 = st.columns(2)

    col1.metric(
        "Customer Segments",
        total_segments
    )

    col2.metric(
        "Customers Analyzed",
        f"{total_customers:,}"
    )

    st.divider()

    st.subheader(
        "Customer Distribution by Segment"
    )

    segment_counts = (
        rfm["Customer_Segment"]
        .value_counts()
    )

    st.bar_chart(
        segment_counts
    )

    st.subheader(
        "💰 Revenue Contribution by Segment"
    )

    segment_revenue = (
        rfm.groupby(
            "Customer_Segment"
        )["Monetary"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    st.bar_chart(
        segment_revenue
    )

    st.subheader(
        "📊 Segment Performance"
    )

    segment_summary = (
        rfm.groupby(
            "Customer_Segment"
        )
        .agg(
            Customers=("CustomerID", "count"),
            Avg_Recency=("Recency", "mean"),
            Avg_Frequency=("Frequency", "mean"),
            Avg_Monetary=("Monetary", "mean")
        )
        .round(2)
    )

    st.dataframe(
        segment_summary,
        use_container_width=True
    )

# CUSTOMER DETAILS

elif page == "Customer Details":

    st.header("🔎 Customer Details")

    segments = sorted(
        rfm[
            "Customer_Segment"
        ]
        .dropna()
        .unique()
        .tolist()
    )

    selected_segment = st.selectbox(
        "Select Customer Segment",
        ["All"] + segments
    )

    if selected_segment == "All":

        filtered_data = rfm

    else:

        filtered_data = rfm[
            rfm["Customer_Segment"]
            == selected_segment
        ]

    st.write(
        f"Customers Found: "
        f"{len(filtered_data):,}"
    )

    st.dataframe(
        filtered_data[
            [
                "CustomerID",
                "Recency",
                "Frequency",
                "Monetary",
                "Cluster",
                "Customer_Segment"
            ]
        ],
        use_container_width=True
    )
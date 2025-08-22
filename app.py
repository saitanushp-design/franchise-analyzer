import streamlit as st

# -----------------------
# Simple Business Analyzer
# -----------------------

st.set_page_config(page_title="Franchise Location Analyzer", layout="wide")

st.title("🏬 Franchise Location Analyzer")
st.write("Enter a city/location to analyze its potential for setting up a new franchise.")

# User input
location = st.text_input("📍 Enter Location (e.g., Bangalore, Hyderabad, Chennai):")

# Example database (this can later be replaced with an API call)
location_data = {
    "bangalore": {
        "avg_budget": "₹15–25 lakhs (depending on area)",
        "pros": [
            "High IT hub population with good spending power",
            "Strong demand for food, retail, and fitness businesses",
            "Young working-class demographic"
        ],
        "challenges": [
            "High rental costs in prime areas",
            "Heavy traffic can affect accessibility",
            "High competition in urban centers"
        ],
        "marketing": [
            "Leverage social media & tech events",
            "Offer student and corporate discounts",
            "Partner with food delivery and e-commerce platforms"
        ],
        "legal": [
            "Shop & Establishment Act registration",
            "GST registration",
            "Trade license from BBMP"
        ]
    },
    "hyderabad": {
        "avg_budget": "₹10–20 lakhs (depending on area)",
        "pros": [
            "Growing IT & pharma hub",
            "Lower rentals than Bangalore",
            "Good demand for food and educational franchises"
        ],
        "challenges": [
            "Emerging competition in urban pockets",
            "Seasonal business fluctuations"
        ],
        "marketing": [
            "Focus on student & family audiences",
            "Digital ads targeting tech employees",
            "Local event sponsorships"
        ],
        "legal": [
            "Trade license from GHMC",
            "GST registration",
            "Labour law compliance"
        ]
    }
}

# Display info if location found
if location:
    loc_key = location.lower()
    if loc_key in location_data:
        data = location_data[loc_key]
        st.subheader(f"📊 Analysis for {location.title()}")

        st.metric("💰 Estimated Setup Budget", data["avg_budget"])

        st.write("### ✅ Advantages")
        for p in data["pros"]:
            st.write(f"- {p}")

        st.write("### ⚠️ Challenges")
        for c in data["challenges"]:
            st.write(f"- {c}")

        st.write("### 📢 Marketing Suggestions")
        for m in data["marketing"]:
            st.write(f"- {m}")

        st.write("### 📜 Legal & Regulatory Notes")
        for l in data["legal"]:
            st.write(f"- {l}")

    else:
        st.warning("❌ Sorry, location not found in database. Please try Bangalore or Hyderabad for now.")

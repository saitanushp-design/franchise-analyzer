import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
import io

def generate_pdf(location):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph(f"{location} Business Location Analysis Report", styles['Title']))
    story.append(Spacer(1, 20))

    # Sections
    story.append(Paragraph("📍 Best Location", styles['Heading2']))
    story.append(Paragraph(f"{location} – recommended commercial hub with good foot traffic.", styles['Normal']))
    story.append(Spacer(1, 12))

    story.append(Paragraph("💰 Setup Budget", styles['Heading2']))
    story.append(Paragraph("Estimated ₹35–45 lakhs for mid-sized setup.", styles['Normal']))
    story.append(Spacer(1, 12))

    story.append(Paragraph("⚖️ Legal & Regulatory Guidance", styles['Heading2']))
    story.append(Paragraph("Shops & Establishments Act registration, GST, and local trade license needed.", styles['Normal']))
    story.append(Spacer(1, 12))

    story.append(Paragraph("⚠️ Challenges & Solutions", styles['Heading2']))
    challenges = [
        ("High rental costs", "Negotiate lease, explore off-main-road locations"),
        ("Competition", "Offer unique services and strong customer experience"),
        ("Traffic/accessibility", "Prefer areas near metro stations or with parking")
    ]
    challenge_list = []
    for ch, sol in challenges:
        text = f"<b>Challenge:</b> {ch} <br/><b>Solution:</b> {sol}"
        challenge_list.append(ListItem(Paragraph(text, styles['Normal'])))
    story.append(ListFlowable(challenge_list, bulletType='bullet'))
    story.append(Spacer(1, 12))

    story.append(Paragraph("📢 Marketing Ideas", styles['Heading2']))
    marketing_points = [
        "Instagram influencer tie-ups",
        "Targeted Google/Facebook ads",
        "Campus activations at nearby colleges",
        "Loyalty programs & referral offers"
    ]
    marketing_list = [ListItem(Paragraph(point, styles['Normal'])) for point in marketing_points]
    story.append(ListFlowable(marketing_list, bulletType='bullet'))

    doc.build(story)
    buffer.seek(0)
    return buffer

# --- Streamlit UI ---
st.title("📊 Business Location Analyzer")
st.write("Enter a city and generate a business analysis PDF report.")

location = st.text_input("Enter Location:", "Bangalore")

if st.button("Generate PDF"):
    pdf_data = generate_pdf(location)
    st.download_button(
        label="📥 Download Report",
        data=pdf_data,
        file_name=f"{location}_Business_Analysis.pdf",
        mime="application/pdf"
    )

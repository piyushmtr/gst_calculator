import streamlit as st

st.set_page_config(page_title="GST Calculator", page_icon="💰")

st.title("💰 GST Calculator App")
st.write("Easily calculate GST amount and total price")

# User input
amount = st.number_input("Enter Amount (₹)", min_value=0.0, format="%.2f")
gst_rate = st.slider("Select GST Rate (%)", 0, 50, step=1)

# GST Calculation
gst_amount = (amount * gst_rate) / 100
final_price = amount + gst_amount

# Output
st.subheader("🔍 Calculation Result:")
st.write(f"**Entered Amount:** ₹ {amount:.2f}")
st.write(f"**GST ({gst_rate}%):** ₹ {gst_amount:.2f}")
st.write(f"**Final Price (with GST):** ₹ {final_price:.2f}")

# Reverse GST calculator (optional)
st.markdown("---")
st.subheader("🔄 Reverse GST Calculator (from Final Price)")

final_amount = st.number_input("Enter Final Price (with GST)", min_value=0.0, format="%.2f", key="reverse")
gst_percent = st.slider("GST Rate for Reverse Calculation (%)", 0, 50, step=1, key="reverse_slider")

if final_amount > 0 and gst_percent > 0:
    original_price = final_amount / (1 + gst_percent / 100)
    reverse_gst = final_amount - original_price

    st.write(f"**Original Price (before GST):** ₹ {original_price:.2f}")
    st.write(f"**GST Amount:** ₹ {reverse_gst:.2f}")

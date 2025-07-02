import streamlit as st
from utils.prediction import get_predictions
from utils.style import apply_styles

st.set_page_config(page_title="پیش‌بینی فوتبال", layout="wide")

st.title("📊 پیش‌بینی نتایج فوتبال بر اساس چند منبع معتبر")

selected_league = st.selectbox("انتخاب لیگ:", [
    "لیگ قهرمانان اروپا", "لیگ اروپا", "لیگ برتر انگلیس", "لالیگا اسپانیا",
    "بوندسلیگا آلمان", "سری آ ایتالیا", "لیگ ۱ فرانسه", "لیگ هلند", "لیگ ایران"
])

predictions_df = get_predictions(selected_league)

if predictions_df.empty:
    st.warning("❗ هیچ بازی‌ای در این تاریخ برای این لیگ وجود ندارد.")
else:
    styled_df = apply_styles(predictions_df)
    st.dataframe(styled_df, use_container_width=True)
def apply_styles(df):
    def highlight(row):
        style = [""] * len(row)
        if "ارزش شرط" in df.columns:
            val_str = str(row["ارزش شرط"]).replace("%", "").replace("٪", "")
            try:
                val = float(val_str)
                if val >= 85:
                    style[-2] = "background-color: lightblue"
                elif val >= 75:
                    style[-2] = "background-color: lightgreen"
                else:
                    style[-2] = "background-color: orange"
            except:
                pass
        return style

    return df.style.apply(highlight, axis=1)
from shiny import App, render, ui, reactive
import pandas as pd
from pathlib import Path

# 1. Point to your Excel Data (with file extension)
EXCEL_PATH = Path(__file__).parent / "2027 Bean Counts.xlsx"

# 2. Define User Interface (UI) Layout
app_ui = ui.page_fluid(
    ui.panel_title("Boeing Project Dashboard"),
    
    ui.layout_sidebar(
        ui.sidebar(
            ui.h3("Filters"),
            # We will populate choices dynamically inside the server instead 
            # to prevent global crash loops if the Excel file is missing
            ui.input_select(
                "category_filter", 
                "Select Category:", 
                choices=[]
            ),
        ),
        # Main Layout Window
        ui.layout_column_wrap(
            ui.value_box(
                "Total Records",
                ui.output_text("total_count")
            ),
            ui.card(
                ui.card_header("Filtered Data View"),
                ui.output_data_frame("data_table")
            )
        )
    )
)

# 3. Define Server Logic (Reactivity)
def server(input, output, session):
    
    # Safely load the data reactively
    @reactive.calc
    def full_df():
        try:
            return pd.read_excel(EXCEL_PATH, sheet_name=0)
        except Exception as e:
            # Fallback mock data so your deployment doesn't crash if the file moves
            return pd.DataFrame({"Category": ["Error Loading Excel"], "Data": [str(e)]})

    # Dynamically update the filter dropdown options once the data loads
    @reactive.effect
    def _():
        df = full_df()
        if "Category" in df.columns:
            choices = list(df["Category"].dropna().unique())
            ui.update_select("category_filter", choices=choices)

    # Filtered dataset based on selection
    @reactive.calc
    def filtered_df():
        df = full_df()
        selected_cat = input.category_filter()
        if "Category" in df.columns and selected_cat:
            return df[df["Category"] == selected_cat]
        return df

    # Output: Total Count metric box
    @render.text
    def total_count():
        return str(len(filtered_df()))

    # Output: Interactive Data Table
    @render.data_frame
    def data_table():
        return render.DataTable(filtered_df(), page_size=10)

# 4. Initialize the App
app = App(app_ui, server)

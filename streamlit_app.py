{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from IPython.display import display, HTML\n",
    "\n",
    "# 1. Load your Excel Data\n",
    "df = pd.read_excel('2027 Bean Counts.xlsx', sheet_name=0)\n",
    "\n",
    "# 2. Calculate Dashboard Metrics\n",
    "total_records = len(df)\n",
    "unique_categories = df['Category'].nunique() if 'Category' in df.columns else 0\n",
    "\n",
    "# 3. Display Clean Dashboard Header with Summary Metrics\n",
    "display(HTML(f'''\n",
    "    <div style=\"font-family: Arial, sans-serif; padding: 20px; background-color: #f8f9fa; border-radius: 8px; margin-bottom: 20px;\">\n",
    "        <h1 style=\"color: #0056b3; margin-top: 0;\">Boeing Project Dashboard</h1>\n",
    "        <div style=\"display: flex; gap: 30px; margin-top: 15px;\">\n",
    "            <div style=\"background: white; padding: 15px 25px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);\">\n",
    "                <span style=\"color: #6c757d; font-size: 14px; font-weight: bold;\">TOTAL RECORDS</span>\n",
    "                <h2 style=\"margin: 5px 0 0 0; color: #212529;\">{total_records}</h2>\n",
    "            </div>\n",
    "            <div style=\"background: white; padding: 15px 25px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);\">\n",
    "                <span style=\"color: #6c757d; font-size: 14px; font-weight: bold;\">UNIQUE CATEGORIES</span>\n",
    "                <h2 style=\"margin: 5px 0 0 0; color: #212529;\">{unique_categories}</h2>\n",
    "            </div>\n",
    "        </div>\n",
    "    </div>\n",
    "'''))\n",
    "\n",
    "# 4. Display the Data Frame with interactive browser search and filter capabilities\n",
    "print('Interactive Dataset Table (Use filters below to sort/search):')\n",
    "df"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

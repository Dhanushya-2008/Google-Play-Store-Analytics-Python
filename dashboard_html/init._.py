import os
os.makedirs"dashboard_html", exist_ok=True)  # makes folder if it doesn't exist

fig1.write_html(fig,"dashboard_html/Category_Graph_1.html")  # Task 1
fig2.write_html(fig,"dashboard_html/Type_Graph_2.html")      # Task 2
fig3.write_html(fig,"dashboard_html/Rating_Graph_3.html")    # Task 3
fig4.write_html(fig,"dashboard_html/Sentiment_Graph_4.html") # Task 4
fig5.write_html(fig,"dashboard_html/Installs_Graph_5.html")  # Task 5
fig6.write_html(fig,"dashboard_html/Updates_Graph_6.html")   # Task 6

import streamlit as st
import mysql.connector
import pandas as pd
from streamlit_option_menu import option_menu

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abinesh",
    database='zomato'
)

if mydb.is_connected():
    st.markdown(f"## <span style='color:white'></span>", unsafe_allow_html=True)

mycursor = mydb.cursor(buffered=True)

# Styling the App
st.markdown(
    """
    <style>
    .stApp {
        background-color:#333333; /* Dark Charcoal */
    }
    label[data-testid="stSelectLabel"] {
        color: white !important;
    }
    label[data-testid="stTextInputLabel"] {
        color: white !important;
    }
    .css-1d391kg p {
        color: white !important; /* Text inside markdown elements */
    }
    .css-16huue1.e16nr0p34 {
        color: white !important; /* Slider label text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    selected_page = option_menu(
        "Main Menu",
        ["Home", "Customers", "Orders", "Restaurants", "Deliveries","Queries"],
        icons=['house', 'filter', 'person', 'cart', 'truck', 'search'],
        # menu_icon="cast",
        default_index=0,
    )

if selected_page == "Home":  
    st.markdown("<h1 style='color:white;'>Welcome to Zomato </h1>", unsafe_allow_html=True)
   

if selected_page == "Customers":
    st.markdown(f"## <span style='color:white'>Customers</span>", unsafe_allow_html=True)
    mycursor.execute("SELECT * FROM customers")
    customers = mycursor.fetchall()
    df_customers = pd.DataFrame(customers, columns=['customer_id', 'name', 'email', 'phone','location',
                                                    'signup_date','is_premium','preferred_cuisine','total_orders','average_rating'])
    st.write(df_customers)
    
    
if selected_page == "Orders":
    st.markdown(f"## <span style='color:white'>Orders</span>", unsafe_allow_html=True)
    mycursor.execute("SELECT * FROM orders")
    orders = mycursor.fetchall()
    df_orders = pd.DataFrame(orders, columns=['order_id','customer_id', 'restaurant_id','order_date', 
                                              'delivery_time', 'status','total_amount','discount_applied','payment_mode','feedback_rating'])
    st.write(df_orders)

 
if selected_page == "Restaurants":
    st.markdown(f"## <span style='color:white'>Restaurants</span>", unsafe_allow_html=True)
    mycursor.execute("SELECT * FROM restaurants")
    restaurants =mycursor.fetchall()
    df_restaurants = pd.DataFrame(restaurants, columns=['restaurant_id', 'name', 'cusine_type','location', 'owner_name',
    
                                                        'average_delivery_time','contact_number','rating','total_orders','is_active'])
    st.write(df_restaurants)


if selected_page == "Deliveries":
    st.markdown(f"## <span style='color:white'>Deliveries</span>", unsafe_allow_html=True)
    mycursor.execute("SELECT * FROM deliveries")
    deliveries = mycursor.fetchall()
    df_deliveries = pd.DataFrame(deliveries, columns=['delivery_id','order_id', 'delivery_person_id', 'delivery_status', 
                                                      'distance', 'delivery_time', 'estimated_time', 'delivery_fee','vehicle_type'])
    st.write(df_deliveries)

if selected_page == "Queries":
    st.markdown(f"## <span style='color:white'>SQL Queries</span>", unsafe_allow_html=True)
    option = st.selectbox("Queries:",
        ("None",
        "1. What are the names of all the restaurants and their corresponding cuisines?",
        "2. Which restaurants have the most number of orders?", 
        "3. What are the top 10 most rated restaurants?",
        "4. List the customers id,name and phone number who gave average rating more than 4.",
        "5. List the customers name and email who are premium",
        "6. On which date,orders id feedback rating was too low?",
        "7. List the customers who  have placed the highest number of orders?",
        "8. List the delivery persons id and their types of vechicles used for delivery.",
        "9. What is the most common cuisine ordered?",
        "10. Who are the delivery persons delivered their orders at long distance and what is the distance?",
        "11. Which restaurants have delivered orders in the shortest average time?",
        "12. What are the busiest days for orders?",
        "13. Which payment mode is most commonly used?",
        "14. List all the canceled orders and their total amount",
        "15. Which delivery vehicle type is most commonly used?",
        "16. Which customers have given the highest average feedback ratings?",
        "17. How many orders are delivered late?",
        "18. What is the average discount applied per order?",
        "19. Which restaurant has received the highest average feedback rating?",
        "20. Which restaurant are presently in active?"),


        index=None,
        placeholder="Select a query...")

    st.write('You selected:', option)
    
    if option == "1. What are the names of all the restaurants and their corresponding cuisines?":
        mycursor.execute("SELECT name, cusine_type FROM restaurants")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Restaurant Name', 'Cuisine Type']))
    
    elif option == "2. Which restaurants have the most number of orders?":
        mycursor.execute("SELECT name, total_orders FROM restaurants ORDER BY total_orders DESC")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Restaurant Name', 'Total Orders']))
        
    elif option == "3. What are the top 10 most rated restaurants?":
        mycursor.execute("SELECT name, rating FROM restaurants ORDER BY rating DESC LIMIT 10")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Restaurant Name', 'Rating']))
    
    elif option == "4. List the customers id,name and phone number who gave average rating more than 4.":
        mycursor.execute("SELECT customer_id, name, phone FROM customers WHERE average_rating > 4")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Customer ID', 'Customer Name', 'Phone Number']))
        
    elif option == "5. List the customers name and email who are premium":
        mycursor.execute("SELECT name,email FROM customers WHERE is_premium = 1")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Customer Name','Email']))
    elif option == "6. On which date,orders id feedback rating was too low?":
        mycursor.execute("SELECT order_id,order_date, feedback_rating FROM orders WHERE feedback_rating < 3")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Order ID','Order Date', 'Feedback Rating']))

    elif option == "7. List the customers who  have placed the highest number of orders?":
        mycursor.execute("SELECT name, total_orders FROM customers ORDER BY total_orders DESC")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Customer Name', 'Total Orders']))

    elif option == "8. List the delivery persons id and their types of vechicles used for delivery.":
        mycursor.execute("SELECT delivery_person_id, vehicle_type FROM deliveries")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Delivery Person ID','Vehicle Type']))

    elif option == "9. What is the most common cuisine ordered?":
        mycursor.execute("SELECT cusine_type, COUNT(*) AS count FROM restaurants GROUP BY cusine_type ORDER BY count DESC LIMIT 1")  
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Cuisine Type', 'Count']))

    elif option =="10. Who are the delivery persons delivered their orders at long distance and what is the distance?":
        mycursor.execute("SELECT delivery_person_id, distance FROM deliveries WHERE distance > 10")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Delivery Person ID', 'Distance']))

    elif option == "11. Which restaurants have delivered orders in the shortest average time?":
        mycursor.execute("SELECT name, average_delivery_time FROM restaurants ORDER BY average_delivery_time ASC LIMIT 5")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Restaurant Name', 'Average Delivery Time']))

    elif option == "12. What are the busiest days for orders?":
        mycursor.execute("SELECT order_date, COUNT(order_id) FROM orders GROUP BY order_date ORDER BY COUNT(order_id) DESC LIMIT 5")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Order Date,Order Time', 'Number of Orders']))

    elif option == "13. Which payment mode is most commonly used?":
        mycursor.execute("SELECT payment_mode, COUNT(order_id) FROM orders GROUP BY payment_mode ORDER BY COUNT(order_id) DESC LIMIT 1")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Payment Mode', 'Number of Orders']))

    elif option =="14. List all the canceled orders and their total amount":
        mycursor.execute("SELECT order_id, total_amount FROM orders WHERE status = 'Cancelled'")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Order ID', 'Total Amount']))


    elif option == "15. Which delivery vehicle type is most commonly used?":
        mycursor.execute("SELECT vehicle_type, COUNT(*) FROM deliveries GROUP BY vehicle_type ORDER BY COUNT(*) DESC LIMIT 1")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Delivery Vehicle Type', 'Number of Deliveries']))

    elif option == "16. Which customers have given the highest average feedback ratings?":
        mycursor.execute("SELECT customer_id,name,average_rating from customers where average_rating=(select max(average_rating) from customers)")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Customer ID', 'Customer Name','Average Feedback Rating']))

    elif option == "17. How many orders are delivered late?":
        mycursor.execute("SELECT COUNT(*) FROM deliveries WHERE delivery_time > estimated_time")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Number of Late Deliveries']))


    elif option == "18. What is the average discount applied per order?":
        mycursor.execute("SELECT AVG(discount_applied) FROM orders")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Average Discount']))

    elif option == "19. Which restaurant has received the highest average feedback rating?":
        mycursor.execute('''SELECT r.name, AVG(rating) AS avg_rating 
        FROM restaurants r
        JOIN orders o ON r.name = r.name
        GROUP BY r.name
        ORDER BY avg_rating DESC
        LIMIT 1;'''
)
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Restaurant Name', 'Average Feedback Rating']))

    elif option =="20. Which restaurant are presently in active?":
        mycursor.execute("SELECT name FROM restaurants WHERE is_active = 1")
        results = mycursor.fetchall()
        st.write(pd.DataFrame(results, columns=['Restaurant Name']))



    


  

        
      
      



    
    # elif option == "6. What is the total number of ratings for each restaurant, and what are their corresponding restaurant names?":
    #     mycursor.execute("SELECT name, COUNT(rating) FROM restaurants GROUP BY name")
    #     results = mycursor.fetchall()
    #     st.write(pd.DataFrame(results, columns=['Restaurant Name', 'Number of Ratings']))
    
    # elif option == "7. What is the total number of orders for each customer, and what are their corresponding customer names?":
    #     mycursor.execute('''SELECT name, COUNT(order_id) AS num_orders 
    #                             FROM customers 
    #                             JOIN orders ON customers.customer_id = orders.customer_id 
    #                             GROUP BY name''')
    #     results = mycursor.fetchall()
    #     st.write(pd.DataFrame(results, columns=['Customer ID', 'Number of Orders']))
    
    # elif option == "8. What are the names of all the restaurants that have been ordered from in the past week?":
    #     mycursor.execute("SELECT name FROM orders WHERE order_date >= CURDATE() - INTERVAL 7 DAY")
    #     results = mycursor.fetchall()
    #     st.write(pd.DataFrame(results, columns=['Restaurant Name']))
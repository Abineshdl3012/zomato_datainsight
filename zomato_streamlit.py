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
        ["Home", "Crud Operations","Queries"],
        icons=['house', 'filter', 'search'],
        # menu_icon="cast",
        default_index=0,
    )


if selected_page == "Home":  
    st.markdown("<h1 style='color:white;'>Welcome to Zomato </h1>", unsafe_allow_html=True)


    
    # display tables in tabs

    tabs=st.tabs(["Customers","Orders","Restaurants","Deliveries"])

    with tabs[0]:
        st.header("Customers Table")
        mycursor.execute("SELECT * FROM customers")
        records = mycursor.fetchall()
        df = pd.DataFrame(records, columns=[i[0] for i in mycursor.description])
        st.dataframe(df)

    with tabs[1]:
        st.header("Orders Table")
        mycursor.execute("SELECT * FROM orders")
        records = mycursor.fetchall()
        df = pd.DataFrame(records, columns=[i[0] for i in mycursor.description])
        st.dataframe(df)

    with tabs[2]:
        st.header("Restaurants Table")
        mycursor.execute("SELECT * FROM restaurants")
        records = mycursor.fetchall()
        df = pd.DataFrame(records, columns=[i[0] for i in mycursor.description])
        st.dataframe(df)

    with tabs[3]:
        st.header("Deliveries Table")
        mycursor.execute("SELECT * FROM deliveries")
        records = mycursor.fetchall()
        df = pd.DataFrame(records, columns=[i[0] for i in mycursor.description])
        st.dataframe(df)

    #crud operations page

if selected_page == "Crud Operations":
    table=st.selectbox("Select Table",["Customers","Orders","Restaurants","Deliveries"])
    operations=st.selectbox("Select Operation",["Create","Read","Update","Delete"])
    
    

    if table=="Customers":
        if operations=="Create":
            customer_id=st.text_input("Enter Customer ID")
            name=st.text_input("Enter Name")
            email=st.text_input("Enter Email")
            phone=st.text_input("Enter Phone")
            location=st.text_input("Enter Location")
            signup_date=st.text_input("Enter Signup Date")
            is_premium=st.text_input("Enter Is Premium")
            # preferred_cuisine=st.text_input("Enter Preferred Cuisine")
            total_orders=st.text_input("Enter Total Orders")
            average_rating=st.text_input("Enter Average Rating")

            if st.button("Create"):
                sql="INSERT INTO customers (customer_id,name,email,phone,location,signup_date,is_premium,total_orders,average_rating) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values=(customer_id,name,email,phone,location,signup_date,is_premium,total_orders,average_rating)
                mycursor.execute(sql,values)
                mydb.commit()
                st.success("Customer Created Successfully")

        elif operations=="Read":
            mycursor.execute("SELECT * FROM customers")
            records=mycursor.fetchall()
            df=pd.DataFrame(records,columns=[i[0] for i in mycursor.description])
            st.dataframe(df)

        elif operations=="Update":
            customer_id=st.text_input("Enter Customer ID")
            name=st.text_input("Enter Name")
            email=st.text_input("Enter Email")
            phone=st.text_input("Enter Phone")
            location=st.text_input("Enter Location")
            signup_date=st.text_input("Enter Signup Date")
            is_premium=st.text_input("Enter Is Premium")
            # preferred_cuisine=st.text_input("Enter Preferred Cuisine")
            total_orders=st.text_input("Enter Total Orders")
            average_rating=st.text_input("Enter Average Rating")

            if st.button("Update"):
                sql="UPDATE customers SET name=%s,email=%s,phone=%s,location=%s,signup_date=%s,is_premium=%s,total_orders=%s,average_rating=%s WHERE customer_id=%s"
                values=(name,email,phone,location,signup_date,is_premium,total_orders,average_rating,customer_id)
                mycursor.execute(sql,values)
                mydb.commit()
                st.success("Customer Updated Successfully")

        elif operations=="Delete":
            customer_id=st.text_input("Enter Customer ID")    
            if st.button("Delete"):
                sql="DELETE FROM customers WHERE customer_id=%s"
                values=(customer_id,)
                mycursor.execute(sql,values)
                mydb.commit()
                st.success("Customer Deleted Successfully")

    if table == "Orders":
        if operations == "Create":
            order_id = st.text_input("Enter Order ID")
            customer_id = st.text_input("Enter Customer ID")
            restaurant_id = st.text_input("Enter Restaurant ID")
            order_date = st.text_input("Enter Order Date")
            delivery_time=st.text_input("Enter the Delivery time")
            status=st.text_input("Enter the Status")
            total_amount=st.text_input("Enter the Total Amount")
            discount_applied=st.text_input("Enter the Discount Applied")
            payment_mode=st.text_input("Enter the Payment Mode")
            feedback_rating=st.text_input("Enter the Feedback Rating")

            if st.button("Create"):
                sql="INSERT INTO orders (order_id,customer_id,restaurant_id,order_date,delivery_time,status,total_amount,discount_applied,payment_mode,feedback_rating) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values=(order_id,customer_id,restaurant_id,order_date,delivery_time,status,total_amount,discount_applied,payment_mode,feedback_rating)
                mycursor.execute(sql,values)
                mydb.commit()
                st.success("Order Created Successfully")

        elif operations == "Read":
            mycursor.execute("SELECT * FROM orders")
            records = mycursor.fetchall()
            df = pd.DataFrame(records, columns=[i[0] for i in mycursor.description])
            st.dataframe(df)

        elif operations == "Update":
            order_id = st.text_input("Enter Order ID")
            customer_id = st.text_input("Enter Customer ID")
            restaurant_id = st.text_input("Enter Restaurant ID")
            order_date = st.text_input("Enter Order Date")
            delivery_time=st.text_input("Enter the Delivery time")
            status=st.text_input("Enter the Status")
            total_amount=st.text_input("Enter the Total Amount")
            discount_applied=st.text_input("Enter the Discount Applied")
            payment_mode=st.text_input("Enter the Payment Mode")
            feedback_rating=st.text_input("Enter the Feedback Rating")

            if st.button("Update"):
                sql="UPDATE orders SET customer_id=%s,restaurant_id=%s,order_date=%s,delivery_time=%s,status=%s,total_amount=%s,discount_applied=%s,payment_mode=%s,feedback_rating=%s WHERE order_id=%s"
                values=(customer_id,restaurant_id,order_date,delivery_time,status,total_amount,discount_applied,payment_mode,feedback_rating,order_id)
                mycursor.execute(sql,values)
                mydb.commit()
                st.success("Order Updated Successfully")

        elif operations == "Delete":
            order_id = st.text_input("Enter Order ID")

            if st.button("Delete"):
                sql="DELETE FROM orders WHERE order_id=%s"
                values=(order_id,)
                mycursor.execute(sql,values)
                mydb.commit()
                st.success("Order Deleted Successfully")

    if table == "Restaurants":
        if operations == "Create":
            restaurant_id = st.text_input("Enter Restaurant ID")
            name = st.text_input("Enter Name")
            cuisine = st.text_input("Enter Cuisine")
            location = st.text_input("Enter Location")
            owner_name = st.text_input("Enter Owner Name")
            contact_number = st.text_input("Enter Contact Number")
            rating = st.text_input("Enter Rating")
            total_orders = st.text_input("Enter Total Orders")
            is_active = st.text_input("Enter Is Active")

            if st.button("Create"):
                sql="INSERT INTO restaurants (restaurant_id,name,cuisine,location,owner_name,contact_number,rating,total_orders,is_active) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values=(restaurant_id,name,cuisine,location,owner_name,contact_number,rating,total_orders,is_active)
                mycursor.execute(sql,values)
                mydb.commit()
                st.success("Restaurant Created Successfully")

        elif operations == "Read":
            mycursor.execute("SELECT * FROM restaurants")
            records = mycursor.fetchall()
            df = pd.DataFrame(records, columns=[i[0] for i in mycursor.description])
            st.dataframe(df)

        elif operations == "Update":
            restaurant_id = st.text_input("Enter Restaurant ID")
            name = st.text_input("Enter Name")
            cuisine = st.text_input("Enter Cuisine")
            location = st.text_input("Enter Location")            
            owner_name = st.text_input("Enter Owner Name")
            contact_number = st.text_input("Enter Contact Number")            
            rating = st.text_input("Enter Rating")
            total_orders = st.text_input("Enter Total Orders")
            is_active = st.text_input("Enter Is Active")

            if st.button("Update"):
                sql="UPDATE restaurants SET name=%s,cuisine=%s,location=%s,owner_name=%s,contact_number=%s,rating=%s,total_orders=%s,is_active=%s WHERE restaurant_id=%s"
                values=(name,cuisine,location,owner_name,contact_number,rating,total_orders,is_active,restaurant_id)
                mycursor.execute(sql,values)
                mydb.commit()
                st.success("Restaurant Updated Successfully")

        elif operations == "Delete":
            restaurant_id = st.text_input("Enter Restaurant ID")

            if st.button("Delete"):
                sql="DELETE FROM restaurants WHERE restaurant_id=%s"
                values=(restaurant_id,) 
                mycursor.execute(sql,values)
                mydb.commit()
                st.success("Restaurant Deleted Successfully")   

    if table == "Deliveries":
        if operations == "Create":
            delivery_id = st.text_input("Enter Delivery ID")
            order_id = st.text_input("Enter Order ID")
            delivery_person_id = st.text_input("Enter Delivery Person ID")
            delivery_status = st.text_input("Enter Delivery Status")    
            distance=st.text_input("Enter the Distance")
            delivery_time = st.text_input("Enter Delivery Time")
            estimated_time=st.text_input("Enter the Estimated Time")
            delivery_fee=st.text_input("Enter the Delivery Fee")
            vehicle_type=st.text_input("Enter the Vehicle Type")

            if st.button("Create"):
                sql="INSERT INTO deliveries (delivery_id,order_id,delivery_person_id,delivery_status,distance,delivery_time,estimated_time,delivery_fee,vehicle_type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values=(delivery_id,order_id,delivery_person_id,delivery_status,distance,delivery_time,estimated_time,delivery_fee,vehicle_type)
                mycursor.execute(sql,values)
                mydb.commit()
                st.success("Delivery Created Successfully")

        elif operations == "Read":
            mycursor.execute("SELECT * FROM deliveries")
            records = mycursor.fetchall()
            df = pd.DataFrame(records, columns=[i[0] for i in mycursor.description])
            st.dataframe(df)

        elif operations == "Update":
            delivery_id = st.text_input("Enter Delivery ID")
            order_id = st.text_input("Enter Order ID")
            delivery_person_id = st.text_input("Enter Delivery Person ID")
            delivery_status = st.text_input("Enter Delivery Status")
            distance=st.text_input("Enter the Distance")
            delivery_time = st.text_input("Enter Delivery Time")
            estimated_time=st.text_input("Enter the Estimated Time")
            delivery_fee=st.text_input("Enter the Delivery Fee")
            vehicle_type=st.text_input("Enter the Vehicle Type")

            if st.button("Update"):
                sql="UPDATE deliveries SET order_id=%s,delivery_person_id=%s,delivery_status=%s,distance=%s,delivery_time=%s,estimated_time=%s,delivery_fee=%s,vehicle_type=%s WHERE delivery_id=%s"
                values=(order_id,delivery_person_id,delivery_status,distance,delivery_time,estimated_time,delivery_fee,vehicle_type,delivery_id)
                mycursor.execute(sql,values)
                mydb.commit()
                st.success("Delivery Updated Successfully")

        elif operations == "Delete":
            delivery_id = st.text_input("Enter Delivery ID")

            if st.button("Delete"):
                sql="DELETE FROM deliveries WHERE delivery_id=%s"
                values=(delivery_id,) 
                mycursor.execute(sql,values)
                mydb.commit()
                st.success("Delivery Deleted Successfully")


# Queries page    
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



    


  

        
      
      



    
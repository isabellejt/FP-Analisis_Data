import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.header("E-commerce Public Dataset")
tab1, tab2 = st.tabs(["Order Data", "Customer Data"])

with tab1:
    order_df = pd.read_csv("order_data.csv")
    order_summary = order_df.groupby(by="product_category_name_english").agg({"review_score": "mean"}).sort_values(by='review_score',ascending=True)

    st.write("Order data")
    st.dataframe(order_df)

    st.write("Order data by Review")
    st.dataframe(order_summary)
    
    bottom_five=order_summary[0:5]
    top_five=order_summary[-5:]

    fig1, ax = plt.subplots(nrows=1, ncols=2, figsize=(100, 50))
    plt.suptitle('Products with Ratings',fontsize=150)
        
    ax[0].barh(y=top_five['review_score'].keys(),width=top_five['review_score'],color="blue")
    ax[0].tick_params(labelsize=60)
    ax[0].set_title("Products with highest ratings",size=80)
    ax[1].barh(y=bottom_five['review_score'].keys(),width=bottom_five['review_score'],color='red')
    ax[1].tick_params(labelsize=60)
    ax[1].set_title("Products with lowest ratings",size=80)

    st.pyplot(fig1)

    with st.expander(label='See Explanation'):
        st.write('lima kategori produk dengan rating tertinggi yaitu cds_dvds_musicals, fashion_childrens_clothes, books_general_interest, costruction_tools_tools, flowers. sementara lima produk dengan rating terendah yaitu security_and_services, diapers_and_hygiene, office_furniture, home_comfort_2, fashion_male_clothing')



with tab2:
    customer_df= pd.read_csv("customer_data.csv")
    customer_summary=customer_df.groupby(by='payment_type').customer_id.nunique().sort_values(ascending=True)

    st.write("Customer data")
    st.dataframe(customer_df)

    st.write("Customer data by Payment Method")
    st.dataframe(customer_summary)

    colors = ('#8B4513', '#FFF8DC', '#93C572', '#E67F0D','#FCDC2A')
    fig2=plt.figure()
    plt.title("Payment Method Chosen")
    plt.pie(x=customer_summary[customer_summary.keys()],labels=customer_summary.keys(),colors=colors,autopct='%1.1f%%')
    st.pyplot(fig2)

    with st.expander(label='See Explanation'):
        st.write('paling banyak sebesar 75.2% menggunakan credit card, 19.5% menggunakan boleto, 3.8% memakai voucher, 1.5% menggunakan debit card, dan sisanya not defined.')
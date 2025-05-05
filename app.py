import streamlit as st
import preprocess
import helper
import matplotlib.pyplot as plt
import seaborn as sns
# Upload the file through the Streamlit sidebar
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # Read file as bytes
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")

    # Show the uploaded data as text


    # Process the data using the prepros function
    df = preprocess.prepros(data)
    user=df["sender"].unique().tolist()
    # user.remove("Meta AI")
    user.sort()
    user.insert(0,"Overall")
    selected=st.sidebar.selectbox("show analysis wrt",user)
    if st.sidebar.button("SHOW ANALYSIS"):

        number_msg,num_words,num_media,num_link=helper.help_to_fetch(selected,df)
        total_words=len(num_words)
        st.markdown("""
                            <h1 style='font-size: 36px; text-align: center; color:"yellow; font-weight: bold;'>
                                WhatsApp Chat Analyzer
                            </h1>
                            <hr style='border: 1px solid #4CAF50;' />
                        """, unsafe_allow_html=True)
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.markdown(f"<h3 style='font-size: 18px; text-align: center;'>TOTAL MESSAGES</h3>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='font-size: 22px; text-align: center;'>{number_msg}</h2>", unsafe_allow_html=True)

        with col2:
            st.markdown(f"<h3 style='font-size: 18px; text-align: center;'>TOTAL WORDS</h3>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='font-size: 22px; text-align: center;'>{total_words}</h2>", unsafe_allow_html=True)

        with col3:
            st.markdown(f"<h3 style='font-size: 18px; text-align: center;'>TOTAL MEDIA</h3>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='font-size: 22px; text-align: center;'>{num_media}</h2>", unsafe_allow_html=True)

        with col4:
            st.markdown(f"<h3 style='font-size: 18px; text-align: center;'>TOTAL LINK</h3>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='font-size: 22px; text-align: center;'>{num_link}</h2>", unsafe_allow_html=True)

        # if selected=="Overall":
        st.title("MOST BUSY USERS")
        graph, newtabel = helper.most_busy_users(df)

        col1, col2 = st.columns(2)
        with col1:
            fig = plt.figure()
            plott = fig.add_axes([0, 0, 1, 1])
            plott.bar(graph.index, graph.values, color="red")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        with col2:
            st.dataframe(newtabel)

        # if selected=="Overall":
        st.title("WORDCLOUD")
        col1, = st.columns(1)
        with col1:
            pic = helper.create_word_cloud(selected, df)
            fig = plt.figure()
            plott = fig.add_axes([0, 0, 1, 1])
            plott.imshow(pic)
            st.pyplot(fig)
        st.title("MOST USED WORDS")
        col1,col2 = st.columns(2)
        with col1:
            most_common_wordss=helper.most_used_words(selected,df)
            fig = plt.figure()
            plott = fig.add_axes([0, 0, 1, 1])
            plott.barh(most_common_wordss["MOST USED WORDS"], most_common_wordss["FREQUENCY OF MOST USED WORDS"])
            plt.xticks(rotation="vertical")
            st.pyplot(fig)
        with col2:
            st.dataframe(most_common_wordss)
        col1, = st.columns(1)
        with col1:
            st.title("MOST USED EMOJIS")
            most_common_emoji=helper.most_cmn_emoji(selected,df)
            st.dataframe(most_common_emoji)
        st.title("WEEKLY AND MONTHLY TIMELINE")
        col1,col2 = st.columns(2)
        with col1:
            timeline = helper.montly_timeline(selected, df)
            fig = plt.figure()
            plott = fig.add_axes([0, 0, 1, 1])
            plott.plot(timeline["time"], timeline["message"])
            plt.xticks(rotation="vertical")
            st.pyplot(fig)
            st.dataframe(timeline)
        with col2:
            daily_timeline = helper.daily_timeline(selected, df)
            fig = plt.figure()
            plott = fig.add_axes([0, 0, 1, 1])
            plt.plot(daily_timeline["new_date"],daily_timeline["message"] ,color="black")
            st.pyplot(fig)
            st.dataframe(daily_timeline)
        st.title("WEEKLY AND MONTHLY ACTIVITY")
        col1, col2 = st.columns(2)
        with col1:
            active = helper.weekly_active(selected, df)
            fig = plt.figure()
            plott = fig.add_axes([0, 0, 1, 1])
            plt.bar(active["active"],active["count"])
            st.pyplot(fig)
        with col2:
            active_monthly = helper.monthly_active(selected, df)
            fig = plt.figure()
            plott = fig.add_axes([0, 0, 1, 1])
            plt.bar(active_monthly["month"],active_monthly["count"],color="orange")
            st.pyplot(fig)
        st.title("HEAT MAP ")
        col1, = st.columns(1)
        import seaborn as sns
        import matplotlib.pyplot as plt
        import streamlit as st

        with col1:
            # Assuming 'helper.heatwave(selected, df)' generates the heatwave data correctly
            heatwave = helper.heatwave(selected, df)

            # Create the figure with a specified size
            fig, ax = plt.subplots(figsize=(14, 8))  # Specify figure size here

            # Create the heatmap on the ax object (it will be part of the 'fig')
            sns.heatmap(heatwave, annot=True, cmap="YlGnBu", fmt="d", annot_kws={"size": 10},
                        cbar_kws={'label': 'Count'}, ax=ax)

            # Adjust the x-axis labels for better readability
            plt.xticks(rotation=45, ha="right")

            # Add a title
            plt.title("Heatmap of Periods by Year", fontsize=16)

            # Display the plot in Streamlit
            st.pyplot(fig)
        st.title("UPLODED CHAT WHICH CAN BE USED SEARCH ...")
        st.dataframe(df)

    # plt.figure(figsize=(12, 6))
    # sns.heatmap(pivot_data, annot=True, cmap="YlGnBu")
    #
    # plt.title("Heatmap of Periods by Year")
    # plt.show()









    # Display the processed DataFrame in Streamlit

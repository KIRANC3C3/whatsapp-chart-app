import numpy as np
import re
import streamlit as st
import main
import help
import matplotlib.pyplot as plt
# import emoji
st.sidebar.title("whatsapp chat analysis")
st.sidebar.write('*****************************')
st.sidebar.write('Ajmeera kiranchandra')
st.sidebar.write('9705902611')
st.sidebar.write('*****************************')


uploaded_file=st.sidebar.file_uploader("choose a file.")
if uploaded_file != None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")# utf-8 string
    # Remove the time portion "10:16 pm -" from each line, keeping the date
    data = re.sub(r'\d{1,2}:\d{1,2}\s[APap][Mm]\s-\s', '', data)
    # Remove the time portion "23:16 -" from each line, keeping the date
    data = re.sub(r'\s\d{1,2}:\d{1,2}\s-\s', '', data)

    df=main.total(data)# passing data

    st.dataframe(df)  # to display dataframe
    # unique users
    user_list=df['user'].unique().tolist()
    #user_list.remove("group notification")

    user_list.sort()
    user_list.insert(0,"overall")

    selected_user=st.sidebar.selectbox("show analysis:",user_list)

    if st.sidebar.button("show analysis:"):

        num_message,media,group_messages=help.count(selected_user,df)
        #media=help.count(selected_user,df)

        col1,col2,col3=st.columns(3)

        with col1:
            st.header("Total messages:")
            st.title(num_message)
        with col2:
            st.header("media messages:")
            st.title(media)

        with col3:
            st.header("group notifications:")
            st.title(group_messages)

            # timeline
        st.header("Timeline")

        timeline = help.timeline(selected_user,df)

        fig,ax=plt.subplots()
        plt.xticks(rotation='vertical')
        ax.plot(timeline['time'],timeline['message'])

        st.pyplot(fig)




        if selected_user=='overall':
            st.title('Top 5 messages')
            a=df['user'].value_counts().head()
            #st.dataframe(a)
            fig,ax=plt.subplots()
            plt.xticks(rotation='vertical')

            col1,col2,col3=st.columns(3)

            with col1:
                st.header('bar blot')
                f = plt.figure()
                f.set_figwidth(6)
                f.set_figheight(5)
                ax.bar(a.index,a.values)

                st.pyplot(fig)

            with col2:
                st.header('users with their messages')
                a = df['user'].value_counts().head()
                st.dataframe(a)

            with col3:
                st.header('messages contribution')
                a1=df['user'].value_counts().head()/df.shape[0]
                st.dataframe(a1)

        st.title('Frequently used words')
        cloud=help.word_cloud(selected_user,df)
        fig,ax=plt.subplots()
        ax.imshow(cloud)
        st.pyplot(fig)

st.sidebar.write('(Exported chat from whatsapp without media data)')













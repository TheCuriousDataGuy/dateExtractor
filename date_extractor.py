import streamlit as st
from datetime import datetime
import re


def getPostID(text):
    a= re.findall(r"\D(\d{19})\D", text)
    a = int(''.join(a))
    a = format(a, 'b')
    return a


def getTimestamp(postID):
    first41chars = postID[:41]
    timestamp = int(first41chars,2)
    return timestamp


def timestampToDate(ts):
    actual_time = datetime.utcfromtimestamp(ts/1000)
    return actual_time



def main():

    # st.title('Date extractor for Linkedin Post')
    # user_input = st.text_area("Paste the link to the linkedin post to get the post date", '"https://www.linkedin.com/posts/andrew-akbashev_career-phd-research-activity-6994809664748027904-sPab?utm_source=share&utm_medium=member_desktop"')
    # if user_input is not None:
    #     postID = getPostID(user_input)
    #     timestamp = getTimestamp(postID)
    #     actualdate = timestampToDate(timestamp)
    # st.title(actualdate)

    user_input = st.sidebar.text_input("Enter the link to the post")
    state = st.sidebar.button("Get Date!")
    if state:
        postID = getPostID(user_input)
        timestamp = getTimestamp(postID)
        actualdate = timestampToDate(timestamp)

        if actualdate:
              
            
            st.write(f"Published Date - {actualdate}")
           
            st.markdown("---")
                
        else:
            st.write("No news for this term")

if __name__ == "__main__":
    main()
import streamlit as st
from datetime import datetime
import pytz
import re


def getPostID(text):
    a= re.findall(r"\D(\d{19})\D", text)
    a= re.findall(r"\d{19}", text)
    a = int(''.join(a))
    a = format(a, 'b')
    return a


def getTimestamp(postID):
    first41chars = postID[:41]
    timestamp = int(first41chars,2)
    return timestamp


def timestampToDate(ts):
    actual_time = datetime.utcfromtimestamp(ts/1000).strftime("%Y-%m-%d %H:%M:%S %Z")
    tz = pytz.timezone('Europe/Paris')
    localtime = datetime.fromtimestamp(ts/1000, tz).strftime("%Y-%m-%d %H:%M:%S %Z")
    return actual_time, localtime



def main():


    user_input = st.sidebar.text_input("Enter the link to the post")
    state = st.sidebar.button("Get Date!")
    if state:
        postID = getPostID(user_input)
        timestamp = getTimestamp(postID)
        dates = timestampToDate(timestamp)
        
        if dates:
              
            
            st.write(f"Published Date - {dates[0]}")
            st.write(f"Published Date (local time) - {dates[1]}")

            st.markdown("---")
                
        else:
            st.write("No news for this term")

if __name__ == "__main__":
    main()
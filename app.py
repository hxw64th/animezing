import streamlit as st

# Setare configurare pagină
st.set_page_config(page_title="animezing zone", layout="wide")


# ----- INTRODUCERE ----
with st.container():
    st.title("There's Animezing!")
    st.write("As you can see, we're at the beginning but ready to advance more in the world of social media!")

# ---- DESPRE CANAL ----
with st.container():
    st.write("___")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("The beginning of the channel")
        st.write("##")
        st.write(
            """
            - The first clip that we posted was 
              "Loser Guy Gets To Date The Most Beautiful And Popular Girl In School", and it was pretty good, but we've grown and continue to evolve after each and every video!

            - After the first video, I felt quite confident, seeing that people liked my content. I had around 120 views after a month, and I felt like I was so good:)

            - The first month was quite challenging because it was difficult to find time to write the script and edit the video, but I eventually figured out a way to accomplish everything I needed to do after a while. 

            - At some point, I reached a moment where I had no time for the channel at all. I barely had time to eat, so I took a break from all activities and focused on school. After some time, I began to get back into the channel, although I didn't have much confidence. Then, the third video, "Son and His Super Hot Mom Are Teleported In A Video Game" started to explode in some way. I had gained 10k views in a month, which was and still is quite significant for me.

            - After posting the fourth video, "Human Is Reincarnated As A Demon By A Super Hot Demon Girl [1]" it began to skyrocket almost instantly! I hit 2k views in a single day, which means a lot for me!
            """
        )



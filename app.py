import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


st.sidebar.title("Deep Dive IPL")
# Load an image from file in the same directory
image_filename = 'OIP.jpeg'
custom_width = 150

st.sidebar.image(image_filename, caption=' ', width=custom_width)


option = st.sidebar.radio("SELECT" ,
                 ("Home" , "Season Wise Analysis","Player Wise", "Team Wise Analysis" , "King" ))


# READING THE DATAFRAMES
df = pd.read_csv("IPL_Matches_2008_2022.csv")
players_df = pd.read_csv('IPL Player Stat.csv')


# pd.set_option('display.max_columns' , 85)
# pd.set_option('display.max_rows' , 85)


if option == 'Home':
    st.title("Overall Analysis")


     # 1  Most number of winns All Over
    st.header("1. Most Number Of Wins By teams In History Of IPL")
    temp = helper.most_wins(df)
    st.table(temp)

    bar , axe = plt.subplots(figsize = (20,14))
    plt.pie(x =temp['count'].head(10) , labels=temp['WinningTeam'].head(10)  , autopct="%.1f%%" )
    plt.title("Most Wins By teams By Start Of IPL" , fontsize = 17)
    st.pyplot(bar )

    # Draw a thicker horizontal line in black color
    st.markdown(""" 
        <style> 
            .horizontal-rule {
                border: 2px solid blue; 
                margin: 20px 0; 
            }
        </style> 
    """, unsafe_allow_html=True)
    st.markdown("<hr class='horizontal-rule'>", unsafe_allow_html=True)



    # 2 Most PLayer of the match all over
    st.header("2. Most PLayer Of The Match In History Of IPL")
    top_ten = helper.player_of_match(df)

    st.table(top_ten)

    fig = plt.figure(figsize=(10, 10))
    sns.barplot(x=top_ten['Player_of_Match'], y=top_ten['count'] , color = 'red')
    plt.xlabel('Player of the Match')
    plt.ylabel('Count')
    plt.title('Player of the Match Counts')
    plt.xticks(rotation=90)
    # Show plot in Streamlit
    st.pyplot(fig)

    # Draw a thicker horizontal line in black color
    st.markdown(""" 
        <style> 
            .horizontal-rule {
                border: 2px solid blue; 
                margin: 20px 0; 
            }
        </style> 
    """, unsafe_allow_html=True)
    st.markdown("<hr class='horizontal-rule'>", unsafe_allow_html=True)

    # 3 Toss Decsion
    st.header("3. Toss Decision By The Teams")
    decision_making = helper.toss_dicion(df)

    st.table(decision_making)
    # Set the palette
    custom_palette = ["red", "blue"]  # Example: red and blue
    sns.set_palette(custom_palette)

    # Create the plot
    fig = sns.catplot(x='Toss Winner', y='Count', hue='Decision', data=decision_making, kind='bar', height=5, aspect=2)
    plt.xticks(rotation=90)
    plt.title("IPL TEAMS TOSS DECISION PLOT")
    plt.xlabel("IPL Teams")
    plt.ylabel("Toss Decision")

    # Show the plot in Streamlit
    st.pyplot(fig)

if option == 'Season Wise Analysis':

    st.header("Total Number of Winnig Matches By the Team Per Season")
    year = st.selectbox("Selct Season" , df['Season'].unique())

    if st.button("Check Now"):
        wins = helper.season_wise_winnig(df , year)
        st.table(wins)

        # Create the stem plot
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.stem(wins['WinningTeam'], wins['count'], basefmt=" ")

        # Set plot labels and title
        plt.title("Top Teams Won per Season")
        plt.xlabel("Winning Team")
        plt.ylabel("Number of Wins")

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=90)

        # Show the plot in Streamlit
        st.pyplot(fig)


if option == 'Player Wise':

    st.header("Player Wise Analysis")

    player = st.sidebar.selectbox("Select Player Role" , ['Batter' , 'Bowler'])

    if player == 'Batter':
        whatUWant = st.selectbox("Select Player Role" , ['runs' , 'batting_avg' , 'boundaries' , 'batting_strike_rate'])

        top_ten = helper.battiing(players_df , whatUWant)
        st.table(top_ten)
        # Create the figure and plot

        # plt.bar(x=top_ten['player'], height=top_ten[whatUWant], color='red')
        if st.button("Check Now"):
            fig = plt.figure(figsize=(10, 10))
            # Set plot labels and title based on 'whatUWant'
            if whatUWant == 'batting_strike_rate':
                plt.bar(x=top_ten['player'], height=top_ten[whatUWant], color='orange')
                plt.xlabel('Player', fontsize=20)
                plt.ylabel('Batting Strike Rate', fontsize=20)
                plt.title('Top Players Based On Their Strike Rate', fontsize=20)
            elif whatUWant == 'runs':
                plt.bar(x=top_ten['player'], height=top_ten[whatUWant], color='red')
                plt.xlabel('Player Name', fontsize=20)
                plt.ylabel('Runs Scored', fontsize=20)
                plt.title('Top Players Based On Top Run Scored', fontsize=20)
            elif whatUWant == 'boundaries':
                plt.bar(x=top_ten['player'], height=top_ten[whatUWant], color='blue')
                plt.xlabel('Player Name', fontsize=20)
                plt.ylabel('Number Of Boundaries Hitted', fontsize=20)
                plt.title('Top Players Based Hitting Boundaries', fontsize=20)
            elif (whatUWant == 'batting_avg'):
                plt.bar(x=top_ten['player'], height=top_ten[whatUWant], color='brown')
                plt.xlabel('Player Name' , fontsize = 20)
                plt.ylabel('Batting Average', fontsize = 20)
                plt.title('Top Players Based Batting Average', fontsize = 20)

            # Rotate x-axis labels for better readability
            plt.xticks(rotation=90)

            # Show the plot in Streamlit
            st.pyplot(fig)

    if player == 'Bowler':

        whatUWant = st.selectbox("Select Player Role" , ['wickets' , 'bowling_economy'])
        top_ten = helper.bowling(players_df , whatUWant)


        if st.button("Analyse Now"):
            st.table(top_ten)
            # Create the figure and plot
            fig = plt.figure(figsize=(8, 8))


            # Set plot labels and title based on 'whatUWant'
            if whatUWant == 'bowling_economy':
                bars = plt.bar(x=top_ten['player'], height=top_ten[whatUWant], color='coral')
                plt.xlabel('Player', fontsize=20)
                plt.ylabel('Best Economy', fontsize=20)
                plt.title('Top Players Based on Economy', fontsize=20)
            elif whatUWant == 'wickets':
                bars = plt.bar(x=top_ten['player'], height=top_ten[whatUWant], color='pink')
                plt.xlabel('Player Name', fontsize=20)
                plt.ylabel('Wickets Taken', fontsize=20)
                plt.title('Top Players Based on Highest Wicket Taking', fontsize=20)
            elif whatUWant == 'bowling_avg':
                bars = plt.bar(x=top_ten['player'], height=top_ten[whatUWant], color='blue')
                plt.xlabel('Player Name', fontsize=20)
                plt.ylabel('Bowling Average', fontsize=20)
                plt.title('Top Players Based on Their Bowling Average', fontsize=20)

            # Rotate x-axis labels for better readability
            plt.xticks(rotation=90)

            # Show the plot in Streamlit
            st.pyplot(fig)

if option == 'Team Wise Analysis':

    st.header("Distribution According to the Number Of Qualifiers Matches Played By The Team")
    last_df = helper.qualifiers(df)
    # st.table(last_df)

    # Create the pie chart
    fig, ax = plt.subplots(figsize=(10, 7))
    cols = ['red', 'green', 'blue', 'cyan', 'yellow']  # Adjust colors as needed
    ax.pie(x=last_df['count'], labels=last_df['Team Name'], autopct="%.1f%%", colors=cols)
    plt.title("Distribution Of Teams Based On Their Number Of Qualifier Matches", fontsize=15, color='blue')

    # Show the plot in Streamlit
    st.pyplot(fig)


    # Draw a thicker horizontal line in black color
    st.markdown(""" 
        <style> 
            .horizontal-rule {
                border: 2px solid blue; 
                margin: 20px 0; 
            }
        </style> 
    """, unsafe_allow_html=True)

    st.markdown("<hr class='horizontal-rule'>", unsafe_allow_html=True)

    #Final
    st.header("Distribution According to the Number Of Final Matches Played By The Team")
    last_df_final = helper.final_match(df)
    st.table(last_df_final)

    fig , axe = plt.subplots(figsize = (10,7))
    cols=['cyan','red','b','green','y']
    axe.pie(x =last_df_final['count'], labels=last_df_final['Team Name']  , autopct="%.1f%%" , colors=cols)
    plt.title("Distribution Of Teams Based On Their Number Of Qualifier Matches" , fontsize = 15 , color='blue')
    st.pyplot(fig)

if option == 'King':
    st.header("Welcome To The King's Landing")

    # Load an image from file
    image_filename = 'virat.jpg'  # Replace with the filename of your image
    image = open(image_filename, 'rb').read()
    # Set custom width for the image
    custom_width = 350

    # Display the image
    st.image(image, caption='King Kohli',width=custom_width)

    st.header("King's Scoreboard.")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Total Runs Scored")
        st.write('7579')
    with col2:
        st.header("Centuries")
        st.write('8')
    with col3:
        st.header("Fifties")
        st.write('52')

    col4 , col5 , col6 = st.columns(3)
    with col4:
        st.header("Strike Rate")
        st.write('130.63')
    with col5:
        st.header("Higest Score")
        st.write('113')
    with col6:
        st.header("Number Of Boundaries")
        st.write('918')



# Define the content of your footer
footer_content = """
<footer style="text-align: center">
    <hr>
    <p>                 Developed By 
    <p> Yagnik Kacha || Karansinh Thakur || Vijaykumar Sankhala </p>
    <p>                    Contact </p>
    <p> kachayagnik136@gmail.com  &nbsp&nbsp karansinhthakur8@gmail.com &nbsp&nbsp vijaykumarsankhala3496@gmail.com</p>
    <p>            Deep Dive IPL @ copywrite  all rights reserved</p>
</footer>
"""

# Display the footer using markdown
st.markdown(footer_content, unsafe_allow_html=True)


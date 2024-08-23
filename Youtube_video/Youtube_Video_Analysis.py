from googleapiclient.discovery import build
import pandas as pd
import matplotlib.pyplot as plt


def fetch_video_data(api_key, video_id):

    """Fetches the data from the api"""
    youtube = build('youtube', 'v3', developerKey=api_key)
    response = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()

    video = response['items'][0]
    title = video['snippet']['title']
    like_count = int(video['statistics']['likeCount'])
    comment_count = int(video['statistics']['commentCount'])
    view_count = int(video['statistics']['viewCount'])
    published_at = pd.to_datetime(video['snippet']['publishedAt'])

    return title, like_count, comment_count, view_count, published_at


def calculate_statistics(view_count, like_count, comment_count, days_since):
    # To calculate the views per day
    rate_of_view = view_count // days_since

    stats = {
        'Mean Value for Views,Like,Comments': pd.Series([view_count, like_count, comment_count]).mean(),
        'Median Value for Views,Like,Comments': pd.Series([view_count, like_count, comment_count]).median(),
        'Standard Deviation Value Views,Like,Comments': pd.Series([view_count, like_count, comment_count]).std(),
        'Views Per Day': rate_of_view
    }

    return rate_of_view, stats


def plot_data(title, yt_df, stats):
    # To plot the data
    plt.figure(figsize=(14, 8))

    # Bar chart plotting
    plt.subplot(2, 2, 1)
    plt.bar(yt_df['Labels'], yt_df['Count'], color='skyblue')
    plt.title(f'Bar Chart for {title}')
    plt.xlabel('Labels')
    plt.ylabel('Count')

    # Pie Chart plotting
    plt.subplot(2, 2, 2)
    plt.pie(yt_df['Count'], labels=yt_df['Labels'], autopct='%1.1f%%', colors=['lightcoral', 'lightblue', 'lightgreen'])
    plt.title(f'Pie Plot for {title}')

    # Scatter plot
    plt.subplot(2, 2, 3)
    plt.scatter(yt_df['Labels'], yt_df['Count'], color='purple')
    plt.title(f'Scatter Plot for {title}')
    plt.xlabel('Labels')
    plt.ylabel('Count')

    # Display statistics
    plt.subplot(2, 2, 4)
    stats_df = pd.DataFrame(list(stats.items()), columns=['Statistic', 'Value'])
    plt.table(cellText=stats_df.values, colLabels=stats_df.columns, loc='center')
    plt.axis('off')
    plt.title(f'Video Analysis for {title}')

    plt.tight_layout()
    plt.show()


def main():
    # API key and video ID
    """Initialization of API"""
    api_key = 'AIzaSyAxUF3Vxy08sZgFx_7qoybg7sb2XEAXxmw'
    video_id = 'jNQXAC9IVRw'

    # Fetch video data
    title, like_count, comment_count, view_count, published_at = fetch_video_data(api_key, video_id)

    # Calculate days since published
    days_since = (pd.Timestamp.now(tz='UTC') - published_at.tz_convert('UTC')).days

    # Calculate rate of view and statistics
    rate_of_view, stats = calculate_statistics(view_count, like_count, comment_count, days_since)

    # Print the data gathered
    print(f"Title : {title}")
    print(f"Count of Likes : {like_count}")
    print(f"Count of Comments : {comment_count}")
    print(f"Views Per Day : {rate_of_view:.2f} views/day")
    print("\nStatistical Analysis:")
    for stat, value in stats.items():
        print(f"{stat}: {value:.2f}")

    # Data for plotting
    data = {
        'Labels': ['Views', 'Likes', 'Comments'],
        'Count': [view_count, like_count, comment_count]
    }

    yt_df = pd.DataFrame(data)

    # Plot the data
    plot_data(title, yt_df, stats)


if __name__ == '__main__':
    main()

# print(video)
# print(response)
# print(youtube)
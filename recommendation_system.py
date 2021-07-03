
import pandas as pd
pd.set_option('display.max_columns', 20)

#############################################
#  Verinin Hazırlanması
#############################################

movie = pd.read_csv('dataset/movie.csv')
rating = pd.read_csv('dataset/rating.csv')

user_Id=108170
movie_id = rating[(rating["userId"] ==108170) & (rating["rating"] == 5.0)].sort_values(by="timestamp", ascending=False)["movieId"][0:1].values[0]
movie_title = movie[movie["movieId"] == movie_id]["title"].str.replace('(\(\d\d\d\d\))', '').str.strip().values[0]

# 2 dataframei merge ediyoruz
df = movie.merge(rating, how="left", on="movieId")

df["timestamp"] = pd.to_datetime(df["timestamp"], format='%Y-%m-%d')
df['title'] = df.title.str.replace('(\(\d\d\d\d\))', '')
df['title'] = df['title'].apply(lambda x: x.strip())
a = pd.DataFrame(df["title"].value_counts())
rare_movies = a[a["title"] <= 1000].index
common_movies = df[~df["title"].isin(rare_movies)]
user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")

"""def item_based_recommender(movie_name, user_movie_df):
    movie = user_movie_df[movie_name]
    return user_movie_df.corrwith(movie).sort_values(ascending=False)[1:6]"""


def item_based_recommender(movie_name):
    # film umd'de yoksa önce ismi barındıran ilk filmi getir.
    # eger o da yoksa filmin isminin ilk iki harfini barındıran ilk filmi getir.
    if movie_name not in user_movie_df:
        # ismi barındıran ilk filmi getir.
        if [col for col in user_movie_df.columns if movie_name.capitalize() in col]:
            new_movie_name = [col for col in user_movie_df.columns if movie_name.capitalize() in col][0]
            movie = user_movie_df[new_movie_name]
            print(F"{movie_name}'i barındıran ilk  film: {new_movie_name}\n")
            print(F"{new_movie_name} için öneriler geliyor...\n")
            return user_movie_df.corrwith(movie).sort_values(ascending=False).head(10)
        # filmin ilk 2 harfini barındıran ilk filmi getir.
        else:
            new_movie_name = [col for col in user_movie_df.columns if col.startswith(movie_name.capitalize()[0:2])][0]
            movie = user_movie_df[new_movie_name]
            print(F"{movie_name}'nin ilk 2 harfini barındıran ilk film: {new_movie_name}\n")
            print(F"{new_movie_name} için öneriler geliyor...\n")
            return user_movie_df.corrwith(movie).sort_values(ascending=False).head(10)
    else:
        print(F"{movie_name} için öneriler geliyor...\n")
        movie = user_movie_df[movie_name]
        return user_movie_df.corrwith(movie).sort_values(ascending=False).head(10)

item_based_recommender( "North by Nort")

item_based_recommender(movie_title, user_movie_df)


#############################################
# Öneri yapılacak kullanıcının izlediği filmlerin belirlenmesi
#############################################

user_df = user_movie_df[user_movie_df.index == 108170]
movies_watched = user_df.columns[user_df.notna().any()].tolist()
movies_watched

len(movies_watched) # 186
# Doğrulamak için:
user_movie_df.loc[user_movie_df.index == 108170, user_movie_df.columns == "Tin Cup"]


#############################################
# Aynı filmleri izleyen diğer kullanıcıların verisine ve id'lerine erişmek
#############################################

movies_watched_df = user_movie_df[movies_watched]
movies_watched_df.shape

user_movie_count = movies_watched_df.T.notnull().sum()
user_movie_count.head()

# user ıd yi değişken kısmına almak için reset index kullanarak yukarı taşıyoruz
user_movie_count = user_movie_count.reset_index()


# değişken isimlerini veriyoruz
user_movie_count.columns = ["userId", "movie_count"]

perc = len(movies_watched) * 60 / 100      # 111.6
users_same_movies = user_movie_count[user_movie_count["movie_count"] > perc]["userId"]
users_same_movies # Userımızla aynı filmlerin  %60'ını izlemiş diğer kullanıcılamızın olduğu User_ıd seriesi

# userla aynı filmleri izleyen kaç kişi var:
# user_movie_count[user_movie_count["movie_count"] == len(movies_watched)].count()

#############################################
# Öneri yapılacak kullanıcı ile en benzer kullanıcıların belirlenmesi
#############################################

# Bunun için 3 adım gerçekleştireceğiz:

# 1. Userımızın ve diğer kullanıcıların verilerini bir araya getireceğiz.
movies_watched_df # userımızın izlediği filmlerin olduğu dataframe

final_df = pd.concat([movies_watched_df[movies_watched_df.index.isin(users_same_movies.index)],user_df[movies_watched]])
final_df.head()

# 2. Korelasyon df'ini oluşturacağız.

# Duplice kayıtları uçuruyoruz
corr_df = final_df.T.corr().unstack().sort_values().drop_duplicates()

# index'i düzeltiyoruz
corr_df = pd.DataFrame(corr_df, columns=["corr"])
corr_df.index.names = ['user_id_1', 'user_id_2']
corr_df = corr_df.reset_index()
corr_df.head()
top_users = corr_df[(corr_df["user_id_1"] == 108170) & (corr_df["corr"] >= 0.65)][["user_id_2", "corr"]].reset_index(drop=True)

# 3. En benzer kullanıcıları (Top Users) buluyoruz

# Sıralıyoruz
top_users = top_users.sort_values(by='corr', ascending=False)
top_users.head()

# isimlendirmesini yapıyoruz
top_users.rename(columns={"user_id_2": "userId"}, inplace=True)
top_users.head()

#
rating = pd.read_csv('DataSet/rating.csv')

#rating tablosunu top_usersla birleştiriyoruz.
top_users_ratings = top_users.merge(rating[["userId", "movieId", "rating"]], how='inner')

# Bu birleştirme ile çoklama kayıtlar oluşuyor
top_users_ratings.head()
#

#############################################
#  Weighted rating'lerin  hesaplanması
#############################################
#
top_users_ratings['weighted_rating'] = top_users_ratings['corr'] * top_users_ratings['rating']
#
top_users_ratings.head()
# Ratinglerde düzeltme yaptık

#############################################
# Weighted average recommendation score'un hesaplanması ve ilk beş filmin tutulması
#############################################
#
temp = top_users_ratings.groupby('movieId').sum()[['corr', 'weighted_rating']]
# movieId ye göre groupby yapıp corr 'un ve weighted ratingin sumını alıyorum

# isimlediriyoruz
temp.columns = ['sum_corr', 'sum_weighted_rating']

temp.head()
#

recommendation_df = pd.DataFrame()

# rating toplamlarını corr toplamlarına bölerek ortalama bir skor buluyoruz
recommendation_df['weighted_average_recommendation_score'] = temp['sum_weighted_rating'] / temp['sum_corr']

recommendation_df['movieId'] = temp.index
recommendation_df = recommendation_df.sort_values(by='weighted_average_recommendation_score', ascending=False)
recommendation_df.head(5)

# Peki bu filmler hangi filmler?
movie = pd.read_csv('DataSet/movie.csv')
movie.loc[movie['movieId'].isin(recommendation_df.head(5)['movieId'])]


#############################################
# İzlediği filmlerden en son en yüksek puan verdiği filmin adına göre item-based öneri yapmak
#############################################
item_based_recommender(movie_title, user_movie_df)


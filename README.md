# Movie Recommendation System

##Introduction

In today's digital era, recommendation systems play a crucial role in enhancing user experience by providing personalized content. These systems are widely used in e-commerce, streaming platforms, and online marketplaces to suggest relevant products, movies, or services based on user behavior. By utilizing collaborative filtering techniques, this project aims to develop an effective movie recommendation system.

##Project Overview

This project focuses on building a recommendation system using collaborative filtering techniques to suggest movies based on user preferences. It consists of two major approaches:

Item-Based Collaborative Filtering: Recommends movies similar to a specific movie based on user ratings.

User-Based Collaborative Filtering: Identifies users with similar taste and suggests movies accordingly.

##Technologies Used

-Pandas: Used for data manipulation and preprocessing.

-NumPy: Supports numerical operations for efficiency.

-Scikit-learn: Used for similarity calculations.

-Matplotlib & Seaborn: Employed for data visualization.

##Implementation Steps

1. Data Preparation and Cleaning

The datasets (movies and ratings) are loaded and merged.

Missing and duplicate values are handled appropriately.

The timestamp column is converted into a readable format.

2. Data Transformation

The dataset is transformed into a user-item matrix.

Rare movies with low interaction are filtered out to improve recommendations.

3. Item-Based Collaborative Filtering

Computes the correlation between movies based on user ratings.

Provides movie recommendations similar to a given movie.

4. User-Based Collaborative Filtering

Identifies users with similar viewing patterns.

Suggests movies that similar users have rated highly.

5. Generating Movie Recommendations

Identifies movies watched and rated highly by the target user.

Finds users with similar preferences and recommends movies they enjoyed.

##Conclusion

This project demonstrates the effectiveness of recommendation systems in improving user engagement. By leveraging collaborative filtering techniques, the model personalizes movie recommendations, enhancing the overall viewing experience.

#Film Öneri Sistemi

##Giriş

Günümüz dijital çağında, öneri sistemleri kişiselleştirilmiş içerik sunarak kullanıcı deneyimini geliştirmede kritik bir rol oynar. E-ticaret, akış platformları ve çevrimiçi pazar yerlerinde yaygın olarak kullanılan bu sistemler, kullanıcı davranışlarına dayalı olarak alakalı ürünler, filmler veya hizmetler önerir. Bu proje, iş birliğine dayalı filtreleme tekniklerini kullanarak etkili bir film öneri sistemi geliştirmeyi amaçlamaktadır.

##Proje Özeti

Bu proje, kullanıcı tercihlerini analiz ederek film önerileri sunan bir sistem geliştirmeye odaklanmaktadır. İki ana yaklaşıma sahiptir:

Öğe Tabanlı İş Birliğine Dayalı Filtreleme: Kullanıcı derecelendirmelerine dayanarak belirli bir filme benzeyen filmleri önerir.

Kullanıcı Tabanlı İş Birliğine Dayalı Filtreleme: Benzer zevklere sahip kullanıcıları belirleyerek öneriler sunar.

##Kullanılan Teknolojiler

-Pandas: Veri manipülasyonu ve ön işleme için kullanılmıştır.

-NumPy: Sayısal işlemler için destek sağlar.

-Scikit-learn: Benzerlik hesaplamaları için kullanılmıştır.

-Matplotlib & Seaborn: Veri görselleştirme için kullanılmıştır.

##Uygulama Adımları

1. Veri Hazırlığı ve Temizleme

Filmler ve derecelendirmeler veri kümeleri yüklenerek birleştirilmiştir.

Eksik ve tekrar eden veriler uygun şekilde işlenmiştir.

Zaman damgası sütunu okunabilir bir biçime dönüştürülmüştür.

2. Veri Dönüşümü

Veri kümesi, kullanıcı-film matrisine dönüştürülmüştür.

Düşük etkileşime sahip nadir filmler filtrelenerek öneri kalitesi artırılmıştır.

3. Öğe Tabanlı İş Birliğine Dayalı Filtreleme

Kullanıcı puanlarına dayanarak filmler arasındaki korelasyon hesaplanmıştır.

Belirli bir filme benzer filmler önerilmiştir.

4. Kullanıcı Tabanlı İş Birliğine Dayalı Filtreleme

Benzer izleme alışkanlıklarına sahip kullanıcılar belirlenmiştir.

Benzer kullanıcıların yüksek puan verdiği filmler önerilmiştir.

5. Film Önerileri Üretme

Kullanıcının izlediği ve yüksek puan verdiği filmler belirlenmiştir.

Benzer tercihlere sahip kullanıcıların izlediği filmler önerilmiştir.

Sonuç

Bu proje, öneri sistemlerinin kullanıcı etkileşimini nasıl artırabileceğini göstermektedir. İş birliğine dayalı filtreleme teknikleri kullanılarak geliştirilen model, film önerilerini kişiselleştirerek genel izleme deneyimini iyileştirmektedir.

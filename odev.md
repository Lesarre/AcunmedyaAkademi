Karar Ağaçları -> Denetimli öğrenme algoritmalarından biridir.Sınıflandırma ve regresyon problemleri için kullanılır.Kök-düğüm-yaprak yapısından oluşur.Eğitim kümesini alır ve özelliklerine göre daha küçük alt kümelere bölerek çalışır.
Avantajları:
-Anlaması ve yorumlaması kolaydır
-Verinin ön hazırlığı konusunda uğraştırıcı değildir.
-Sayısal ve kategorik verileri işleyebilir.
Dezavantajları:
-Verilerdeki değişiklikler karar ağacının yapısının değişmesine neden olabilir.
-Veriyi iyi bir şekilde açıklamayan karmaşık ağaçlar üretilebilir.
-Karar ağacı eğitimi zaman açısından maliyetlidir
-Overfitting riski yüksektir.
-Regresyon için tam anlamıyla yeterli değildir.

Rastgele Orman -> Denetimli öğrenme algoritmalarından biridir.Regresyon ve sınıflandırma problemlerinde kullanılır.Birden fazla karar ağacının üretilip kullanılmasına dayanır.Birbirinden bağımsız olarak çalışan birden fazla karar ağacının bir araya gelerek aralarından en yüksek puan alan değerin seçilmesi işlemidir.Ağaç sayısı arttıkça başarı oranı artar.Kökü bulma ve düğümleri bölme işlemi rastgeledir.
Avantajları:
-Hata oranı daha düşüktür.
-Yeterli miktarda veri varsa Overfitting riski azdır.
-Yüksek boyutlu veri kümelerini işler.
-Hem sınıflandırma hem de regresyon için performanslıdır.
-Eksik verileri işleyebilir.
Dezavantajları:
-Eğitilmesi uzun sürebilir.
-Yorumlanabilirliği azdır.
-Optimum performans için hiperparametre ayarı gerekir.
-Yüksek gürültülü verilerde iyi performans gösteremeyebilir.

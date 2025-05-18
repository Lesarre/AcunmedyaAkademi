# Davies-Bouldin Metodu ve Özellik Ölçekleme (Feature Scaling)

## 📌 Davies-Bouldin Metodu Nedir?

Davies-Bouldin skoru, bir **kümeleme (clustering)** algoritmasının başarımını değerlendirmek için kullanılan içsel bir değerlendirme metriğidir. Yani, kümeleme sonuçlarının **kalitesini**, dış bir etiket olmadan ölçer.

### 🧠 Temel Fikir:
- Bir kümeleme sonucu hem kümeler **birbirine uzak** hem de **kendi içinde kompakt (sıkı)** olmalıdır.
- Davies-Bouldin skoru **düşükse**, kümeler birbirinden daha ayrık ve içsel olarak daha tutarlıdır. **Skor ne kadar düşükse, o kadar iyi.**

### 🔢 Hesaplama Formülü:
DB(i) = max<sub>j≠i</sub> [(s<sub>i</sub> + s<sub>j</sub>) / d<sub>ij</sub>]

Burada:
- **s<sub>i</sub>**: Küme i'nin içsel yayılımı (kendi merkezine olan ortalama uzaklık)
- **d<sub>ij</sub>**: Küme i ile j'nin merkezleri arasındaki mesafe
- **DB**: Tüm kümeler için bu değerlerin ortalamasıdır.

### 📈 Kullanım:
Scikit-learn ile kolayca kullanılabilir:
```python
from sklearn.metrics import davies_bouldin_score
score = davies_bouldin_score(X, labels)
print("Davies-Bouldin Skoru:", score)
```

---

## ⚖️ Özellik Ölçekleme (Feature Scaling) Nedir?

Özellik ölçekleme, farklı ölçeklerdeki değişkenleri **aynı ölçeğe getirerek** makine öğrenmesi algoritmalarının daha **etkili ve doğru** çalışmasını sağlar.

### 🎯 Neden Önemlidir?
- Bir veri kümesinde `yaş` gibi bir özellik 0-100 arasında iken, `gelir` gibi bir özellik 10.000-1.000.000 arasında olabilir.
- Mesafeye dayalı algoritmalar (KNN, KMeans, SVM vs.) büyük ölçekli değişkenlere daha fazla ağırlık verir ve bu adaletsizliğe neden olur.

### 🚀 Yaygın Ölçekleme Teknikleri:

#### 1. **Min-Max Normalizasyonu**
Verileri 0-1 aralığına çeker:
```
X_scaled = (X - X.min()) / (X.max() - X.min())
```

Scikit-learn:
```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

#### 2. **Z-Score Standardizasyonu (Standartlaştırma)**
Verinin ortalamasını 0, standart sapmasını 1 yapar:
```
X_scaled = (X - mean) / std
```

Scikit-learn:
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 🧪 Özet

| Konu | Açıklama |
|------|----------|
| **Davies-Bouldin Skoru** | Kümeleme kalitesini ölçer. Düşük değer daha iyi. |
| **Özellik Ölçekleme** | Değişkenleri aynı ölçeğe getirerek algoritmaların daha adil çalışmasını sağlar. |

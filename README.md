# Data Science SQL Project 11

### Proje Kurulumu
Projeyi öncelikle forklayın ve clone edin.
Proje sayımız ilerledikçe proje yönetimimizi kolaylaştırmak adına projelerimizi belli klasör kalıplarında saklamak işimizi kolaylaştırmak adına iyi bir alışkanlıktır.
Örnek bir Lokasyon: Code2Work/DataScience/data-project-2.

### Proje Kurulumu Komutlar
Aşağıdaki komutları sıtrayla çalıştırınız.
* python -m venv venv
* venv\Scripts\activate
* pip install -r requirements.txt => Install all dependencies
* python watch.py => Python run all tests

## Bonus
* Eğer daha detaylı bir şekilde testlerin içerisine bakmak isterseniz
* pytest .\tests\test_question.py -s -v 

### Projeye Başlamadan Önce
* Belirtilen sql querylerini yazabilmek için scripts klasörü altındaki bulunan init_db.py dosyası içerisindeki tüm queryleri 
sırasıyla kendi local veritabanınızda çalıştırınız. 
* Veritabanınızın hazır olduğundan emin olmak için tüm tablolara birer SELECT sorgusu atıp sonuçların doğru olduğundan emin olunuz.
* Çalışırken sadece data klasörü altında bulunan questions.py dosyasında çalışacağız. Bunun klasör dışındaki kodları değiştirmeyiniz !
* connect_db fonksiyonu içerisinde veritabanına bağlanma bilgileri var. Projenizi kendi localinizde test ederken burada bilgileri kendi local veritabanı bilgilerinizle değiştirerek test ediniz. Ancak kodunuzu <b>pushlarken bu veritabanı bilgilerini ilk bulduğunuz şekilde bırakınız.</b> Çünkü kodlarınız Cloud bir ortamda bu bilgilerle bir veritabanına bağlancaklardır.

# Questions
* Senaryo:
    Cyberpunk 2077 evreninde karakterlerin dijital bir veri kümesinden temizlenip analiz edilmesini sağlayacaksın. Elimizde bazı karakter bilgileri olan bir .csv dosyası var (senaryoya göre bozulmuş, eksik, karışık vs.). Ayrıca bir API’den karakter güncellemeleri çekeceğiz ve string bazlı bazı istatistikler yapacağız. Senin görevin, bu sistemdeki fonksiyonları tanımlamak ve testleri geçmek olacak.
* task_manager.py dosyasının içerisindeki fonksiyonların içerisini doldurmaya çalışın
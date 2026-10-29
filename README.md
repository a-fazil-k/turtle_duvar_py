# Duvardan Kaçan Kaplumbağa (ROS 2)

Bu proje, ROS 2 kullanılarak hazırlanmış bir "Robotiğe Giriş" dersi ödevidir. Projede `turtlesim` simülasyonundaki kaplumbağanın otonom olarak hareket etmesi ve ekran sınırlarına yaklaştığında çarpmadan yön değiştirmesi sağlanmıştır.

## Özellikler (Yapılan İsterler)
- **Paket:** `turtle_duvar_py` adında ament_python paketi oluşturuldu.
- **Abone (Subscriber):** `/turtle1/pose` konusu dinlenerek kaplumbağanın anlık x ve y koordinatları alındı.
- **Yayıncı (Publisher):** `/turtle1/cmd_vel` konusuna hız verileri basıldı. Kaplumbağa 1.0 veya 10.0 sınırlarına yaklaştığında açısal hız verilerek yönü değiştirildi.
- **Loglama:** Saniyede bir (Timer ile) kaplumbağanın anlık konumu terminale `get_logger().info()` ile yazdırıldı.
- **Bonus:** İleri gidiş hızı ve duvar sınır değerleri parametrik hale getirildi.

## Çalıştırma Adımları
1. Çalışma alanını derleyin: `colcon build --packages-select turtle_duvar_py`
2. Simülasyonu başlatın: `ros2 run turtlesim turtlesim_node`
3. Yeni terminalde düğümü çalıştırın: `ros2 run turtle_duvar_py kacan_kaplumbaga`

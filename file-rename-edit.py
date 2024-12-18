import os

# Kullanıcıdan klasör yolunu al
folder_path = 'klasor/yolu'

# Klasördeki tüm dosyaları al
files = os.listdir(folder_path)

# Dosyaları sıralama
files.sort()

# Dosyaların adlarını değiştirme
for index, file in enumerate(files):
    # Dosya yolunu oluştur
    old_file_path = os.path.join(folder_path, file)
    
    # Yeni dosya adını oluştur (000001, 000002, vb.)
    new_file_name = f"{str(index + 1).zfill(6)}{os.path.splitext(file)[1]}"
    new_file_path = os.path.join(folder_path, new_file_name)
    
    # Dosyayı yeniden adlandır
    os.rename(old_file_path, new_file_path)

print("Dosya isimleri başarıyla değiştirildi.")

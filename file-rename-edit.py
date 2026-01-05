import os

# Kullanıcıdan klasör yolunu al
folder_path = input("Lütfen klasör yolunu girin: ").strip().strip('\'"')

# Sadece dosya olanları ve gizli olmayanları al
files = [
    f for f in os.listdir(folder_path)
    if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith('.')
]

# Dosyaları sıralama
files.sort()

# Dosyaların adlarını değiştirme
for index, file in enumerate(files):
    old_file_path = os.path.join(folder_path, file)
    new_file_name = f"{str(index + 1).zfill(6)}{os.path.splitext(file)[1]}"
    new_file_path = os.path.join(folder_path, new_file_name)
    os.rename(old_file_path, new_file_path)

print("Dosya isimleri başarıyla değiştirildi.")
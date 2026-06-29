import os
from PIL import Image

def convert_images_to_webp(directory, delete_original=False):
    # Поддерживаемые форматы для конвертации
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    
    # Обход всех файлов в указанной папке
    for filename in os.listdir(directory):
        if filename.lower().endswith(valid_extensions):
            # Формируем полные пути к файлам
            file_path = os.path.join(directory, filename)
            name_without_ext = os.path.splitext(filename)[0]
            webp_path = os.path.join(directory, f"{name_without_ext}.webp")
            
            try:
                # Открываем и сохраняем в формате WebP
                with Image.open(file_path) as img:
                    img.save(webp_path, 'WEBP', quality=85) # quality от 1 до 100
                print(f"Успешно конвертирован: {filename} -> {name_without_ext}.webp")
                
                # Удаляем оригинал, если включена опция
                if delete_original:
                    os.remove(file_path)
                    print(f"Исходный файл удален: {filename}")
                    
            except Exception as e:
                print(f"Ошибка при обработке файла {filename}: {e}")

# Запуск скрипта для текущей папки
if __name__ == "__main__":
    # '.' означает текущую папку, где лежит скрипт
    # Поменяйте False на True, если хотите сразу удалять старые JPG/PNG файлы
    convert_images_to_webp('.', delete_original=False)

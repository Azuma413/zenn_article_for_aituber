# Article.mdの文字数をカウントします
# python counter.py

def count_characters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return len(content)
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

if __name__ == "__main__":
    file_path = "Article.md"
    char_count = count_characters(file_path)
    
    if char_count is not None:
        print(f"Number of characters in {file_path}: {char_count}/6000")

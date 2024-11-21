# Об'єкт для роботи з базою даних
class DatabaseHandler:
    def __init__(self, db_path="data.db"):
        import sqlite3
        self.connection = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT NOT NULL,
                url TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def save_result(self, query, url):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO results (query, url) VALUES (?, ?)', (query, url))
        self.connection.commit()

    def clear_results(self):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM results')
        self.connection.commit()

    def get_results(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM results')
        return cursor.fetchall()


# Об'єкт для парсингу сайтів
class WebScraper:
    def __init__(self):
        import requests
        self.session = requests.Session()

    def search(self, query):
        # Простий приклад пошуку на Google (можна адаптувати)
        from bs4 import BeautifulSoup
        response = self.session.get(f"https://www.google.com/search?q={query}")
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and "http" in href:
                results.append(href)
        return results


# Об'єкт для інтерфейсу користувача
class UserInterface:
    def __init__(self, db_handler, scraper):
        self.db_handler = db_handler
        self.scraper = scraper

    def run(self):
        while True:
            print("\n1. Пошук інформації")
            print("2. Переглянути результати")
            print("3. Очистити базу даних")
            print("4. Вихід")
            choice = input("Оберіть дію: ")

            if choice == "1":
                query = input("Введіть пошуковий запит: ")
                results = self.scraper.search(query)
                for url in results:
                    print(f"Знайдено: {url}")
                    self.db_handler.save_result(query, url)
            elif choice == "2":
                results = self.db_handler.get_results()
                if not results:
                    print("Результати відсутні.")
                else:
                    for result in results:
                        print(f"[{result[0]}] Запит: {result[1]}, URL: {result[2]}")
            elif choice == "3":
                self.db_handler.clear_results()
                print("Базу даних очищено.")
            elif choice == "4":
                print("До побачення!")
                break
            else:
                print("Неправильний вибір. Спробуйте ще раз.")


# Основна функція запуску програми
def run():
    db_handler = DatabaseHandler()
    scraper = WebScraper()
    ui = UserInterface(db_handler, scraper)
    ui.run()


if __name__ == "__main__":
    run()

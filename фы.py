from datetime import datetime, timedelta  # Добавляем импорт необходимых классов

class Pokemon:
    def __init__(self, name, hp, power, *args, **kwargs):
        self.name = name
        self.hp = hp
        self.power = power
        self.last_feed_time = None  # Добавляем атрибут для хранения времени последнего кормления
    
    def feed(self, feed_interval=20, hp_increase=10):
        current_time = datetime.now()  # Исправлено: datetime.now() вместо datetime.current()
        
        # Если покемон еще никогда не кормился, разрешаем кормление
        if self.last_feed_time is None:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        
        delta_time = timedelta(seconds=feed_interval)  # Исправлено: timedelta вместо timedelete и передаем seconds
        
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            next_feed_time = self.last_feed_time + delta_time  # Исправлено: правильный расчет времени следующего кормления
            return f"Следующее время кормления покемона: {next_feed_time.strftime('%H:%M:%S')}"


class Wizard(Pokemon):
    def feed(self, feed_interval=20, hp_increase=20):  # Для Волшебника увеличиваем здоровье больше
        return super().feed(feed_interval, hp_increase)


class Fighter(Pokemon):
    def feed(self, feed_interval=10, hp_increase=10):  # Для Бойца уменьшаем интервал кормления
        return super().feed(feed_interval, hp_increase)


# Пример использования
if __name__ == "__main__":
    # Создаем покемонов разных типов
    pikachu = Pokemon("Пикачу", 100, 50)
    gandalf = Wizard("Гендальф", 80, 70)
    warrior = Fighter("Воин", 120, 80)
    
    # Тестируем кормление
    print("Тестирование покемона:")
    print(pikachu.feed())  # Первое кормление
    print(pikachu.feed())  # Попытка покормить сразу после первого
    
    print("\nТестирование волшебника:")
    print(gandalf.feed())  # Первое кормление - увеличение на 20 HP
    
    print("\nТестирование бойца:")
    print(warrior.feed())  # Первое кормление

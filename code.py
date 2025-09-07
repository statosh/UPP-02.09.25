def calculate_average(numbers):
    """
    Вычисляет среднее арифметическое значение списка чисел.
    
    Args:
        numbers (list): Список чисел
        
    Returns:
        float: Среднее значение, или None если список пуст
    """
    return sum(numbers) / len(numbers) if numbers else None

# Пример использования
numbers_list = [10, 20, 30, 40]
result = calculate_average(numbers_list)
print(f"Среднее значение: {result}" if result is not None else "Список пуст")

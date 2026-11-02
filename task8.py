def reverse_string(text):
  try:
    return text[::-1]
  except ValueError as e:
    print(f"Ошибка: {e}\n")

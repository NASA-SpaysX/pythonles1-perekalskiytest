import io
import runpy
import sys


def run_student_code():
    buf = io.StringIO()
    old_stdout = sys.stdout
    try:
        sys.stdout = buf
        runpy.run_path("main.py", run_name="__main__")
    finally:
        sys.stdout = old_stdout
    return buf.getvalue().strip().splitlines()


def test_output_lines():
    output = run_student_code()

    # Явно покажем размер и весь вывод
    assert len(output) >= 2, (
        f"Ожидалось минимум 2 строки вывода, получили {len(output)}. "
        f"Полный вывод: {output!r}"
    )

    # Первая строка — строка
    expected0 = "Hello, world!"
    actual0 = output[0] if len(output) > 0 else None
    assert actual0 == expected0, (
        f"Первая строка не совпала: ожидалось {expected0!r}, "
        f"получено {actual0!r}. Полный вывод: {output!r}"
    )

    # Вторая строка — число 42, но сравниваем как строку
    expected1 = "42"
    actual1 = output[1] if len(output) > 1 else None
    assert actual1 == expected1, (
        f"Вторая строка не совпала: ожидалось {expected1!r}, "
        f"получено {actual1!r}. Полный вывод: {output!r}"
    )

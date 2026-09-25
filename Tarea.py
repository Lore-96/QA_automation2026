def fizz_buzz_val(n):
    """Devuelve la respuesta FizzBuzz para un número individual."""
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def fizz_buzz_sequence(limit=100):
    """Genera la lista con el rango completo."""
    return [fizz_buzz_val(i) for i in range(1, limit + 1)]


def list2num(digits):
    """Convierte una lista de digitos en el numero que representa."""
    return int("".join(str(digit) for digit in digits))


def expand(sequence):
    """Describe cada grupo consecutivo como cantidad y valor."""
    if not sequence:
        return []

    expanded = []
    current_value = sequence[0]
    count = 1
    for value in sequence[1:]:
        if value == current_value:
            count += 1
        else:
            expanded.extend([count, current_value])
            current_value = value
            count = 1
    expanded.extend([count, current_value])
    return expanded


def test_ejercicios():
    # Tests para FizzBuzz
    assert fizz_buzz_val(3) == "Fizz"
    assert fizz_buzz_val(5) == "Buzz"
    assert fizz_buzz_val(15) == "FizzBuzz"
    assert fizz_buzz_val(2) == "2"
    
    # Tests para list2num
    assert list2num([1, 2, 1, 1]) == 1211
    assert list2num([1]) == 1
    
    # Tests para expand
    assert expand([1]) == [1, 1]              # "un uno"
    assert expand([1, 1]) == [2, 1]           # "dos unos"
    assert expand([2, 1]) == [1, 2, 1, 1]     # "un dos, un uno"
    assert expand([1, 2, 1, 1]) == [1, 1, 1, 2, 2, 1] # "un uno, un dos, dos unos"

    print("¡Todos los tests pasaron exitosamente!")

# Ejecutar los tests
if __name__ == "__main__":
    test_ejercicios()
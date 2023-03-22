def sort_by_bubble(unordered_list: list):
    """
    Description: Devuelve una lista ordenada usando el método de la burbuja.
    """

    swapped = True
    while swapped:
        for i in range(len(unordered_list) - 1):
            swapped = False
            if unordered_list[i] > unordered_list[i + 1]:
                swapped = True
                unordered_list[i], unordered_list[i +
                                                  1] = unordered_list[i + 1], unordered_list[i]

    return unordered_list  # Ahora ordenada.


def get_greater_item(search_list: list):
    """
    Description: Devuelve e elemento mayor de la lista.
    """

    greater = search_list[0]
    for item in search_list[1:]:
        if item > greater:
            greater = item

    return greater


def search_item(search_item, search_list:list):
    """
    Description: Devuelve la posición del item buscado. Si no se encontró,
                 devuelve -1.
    """

    position_found = -1
    for i in range(len(search_list) - 1):
        if search_item == search_list[i]:
            position_found = i
            break

    return position_found


number_list = [5, 3, 1, 2, 4]
print("Lista desordenada:", number_list)

print("El elemento mayor es:", get_greater_item(number_list))

print(f"El número 1 está en la posición {search_item(1, number_list)}")

number_list = sort_by_bubble(number_list)

print("Lista ordenada:   ", number_list)

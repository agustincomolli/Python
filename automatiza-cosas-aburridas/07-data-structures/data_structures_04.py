"""
Establecer valores predeterminados
"""

MESSAGE = "Era un día soleado y frío de abril, y los relojes daban las trece."
count: dict[str, int] = {}

for character in MESSAGE:
    count.setdefault(character, 0)
    count[character] += 1

print(count)

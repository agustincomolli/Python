"""
Ejemplo de pilas de llamadas de funciones (call stack).
"""


def talking_to_alice():
    """Hablando de Alice."""
    print("Empiezas hablando de Alice")
    talking_to_bob()
    talking_to_david()
    print("Terminas hablando de Alice")


def talking_to_bob():
    """Hablando de Bob."""
    print("Empiezas hablando de Bob")
    talking_to_carol()
    print("Terminas hablando de Bob")


def talking_to_carol():
    """Hablando de Carol."""
    print("Empiezas hablando de Carol")
    print("Terminas hablando de Carol")


def talking_to_david():
    """Hablando de David."""
    print("Empiezas hablando de David")
    print("Terminas hablando de David")


talking_to_alice()

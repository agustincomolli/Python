default_color = "\033[0m"
red_color = "\033[31m"
green_color = "\033[32m"
yellow_color = "\033[33m"
blue_color = "\033[34m"
magenta_color = "\033[35m"
cyan_color = "\033[36m"

print(f"{'30 Días Abajo - ¿Qué te pareció?':^80}")

for i in range(1, 31):
    answer = input(f"Día {i: >2}\n" + green_color)
    message = f"Pensaste que el día {i:>2} era"
    print(default_color, end="")

    print(f"{message:^80}")
    print(f"{answer:^80}")

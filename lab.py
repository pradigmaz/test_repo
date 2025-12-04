import math

def calculate_pelmeni_machines():
    print("--- Расчет пельменного цеха (Часть 1) ---")
    
    # Ввод исходных данных
    try:
        Q_sut = float(input("Введите суточную выработку (т): "))
        t_smena = float(input("Введите длительность смены (ч): "))
        p_pa = float(input("Производительность пельменного автомата (т/ч): "))
    except ValueError:
        print("Ошибка ввода! Введите числа.")
        return

    # 1. Производительность технологической линии (P_tlp)
    # Формула: Q_sut / (2 * t) (т.к. две смены)
    P_tlp = Q_sut / (2 * t_smena)
    
    # 2. Количество пельменных автоматов (n_pa)
    # Округляем в большую сторону (math.ceil)
    n_pa = math.ceil(P_tlp / p_pa)

    print(f"\n[Результат Этапа 1]")
    print(f"Производительность линии: {P_tlp:.3f} т/ч")
    print(f"Необходимо пельменных автоматов: {n_pa} шт.")

if __name__ == "__main__":
    calculate_pelmeni_machines()

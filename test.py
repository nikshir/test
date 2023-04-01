TEST_DATA: list[tuple[int, str, bool]] = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS: float = 1.1
ANTIBONUS: float = 0.8


def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
    """
    Функция, которая добавляет очки репутации к текущей с учетом бонуса.

    :param current_rep: текущее значение репутации
    :param rep_points: очки репутации, которые нужно добавить
    :param buf_effect: флаг, указывающий на наличие бонуса
    :return: новое значение с учетом эффекта бонуса
    """
    current_rep += rep_points
    if buf_effect:
        return current_rep * BONUS
    return current_rep


def remove_rep(
        current_rep: float, rep_points: int, debuf_effect: bool
) -> float:
    """
    Функция, вычитает очки репутации из текущей с учетом эффекта антибонуса.

    :param current_rep: текущее значение репутации
    :param rep_points: очки репутации, которые нужно вычесть
    :param debuf_effect: флаг, указывающий на наличие эффекта антибонуса
    :return: новое значение репутации с учетом эффекта антибонуса
    """
    current_rep -= rep_points
    if debuf_effect:
        return current_rep * ANTIBONUS
    return current_rep


def main(duel_res: list[tuple[int, str, bool]]) -> str:
    """
    Основная функция, которая вычисляет итоговую репутацию персонажа
    на основе данных о поединках.

    :param duel_res: список кортежей с данными о поединках
    :return: строка с информацией о количестве поединков и итоговой репутации
    """
    current_rep: float = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        if result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return (
        f'После {len(duel_res)} поединков, репутация персонажа — '
        f'{current_rep:.3f} очков.'
    )


# Тестовый вызов функции main.
print(main(TEST_DATA))

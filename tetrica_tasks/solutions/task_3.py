"""
Когда пользователь заходит на страницу урока, мы сохраняем время его захода. Когда пользователь выходит с урока
(или закрывает вкладку, браузер – в общем как-то разрывает соединение с сервером), мы фиксируем время выхода с урока.
Время присутствия каждого пользователя на уроке хранится у нас в виде интервалов. В функцию передается словарь,
содержащий три списка с таймстемпами (время в секундах):

lesson – начало и конец урока
pupil – интервалы присутствия ученика
tutor – интервалы присутствия учителя

Интервалы устроены следующим образом – это всегда список из четного количества элементов. Под четными индексами
(начиная с 0) время входа на урок, под нечетными - время выхода с урока.
Нужно написать функцию appearance, которая получает на вход словарь с интервалами и возвращает время общего присутствия
ученика и учителя на уроке (в секундах).
"""
def merge_intervals(intervals: list[int]) -> list[tuple[int, int]]:
    # Преобразуем список [start1, end1, start2, end2, ...] в непересекающиеся интервалы
    paired = sorted((intervals[i], intervals[i + 1]) for i in range(0, len(intervals), 2))
    merged = []
    for start, end in paired:
        if not merged or merged[-1][1] < start:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    return merged

def intersect_intervals(a: list[tuple[int, int]], b: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # Находим пересечения двух списков интервалов
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        start = max(a[i][0], b[j][0])
        end = min(a[i][1], b[j][1])
        if start < end:
            result.append((start, end))
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return result

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    lesson = [(lesson_start, lesson_end)]
    pupil = merge_intervals(intervals['pupil'])
    tutor = merge_intervals(intervals['tutor'])

    pupil_in_lesson = intersect_intervals(pupil, lesson)
    tutor_in_lesson = intersect_intervals(tutor, lesson)
    common_time = intersect_intervals(pupil_in_lesson, tutor_in_lesson)

    return sum(end - start for start, end in common_time)

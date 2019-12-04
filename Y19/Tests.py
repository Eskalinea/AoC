from Y19 import *
__author__ = "Faremir"
__copyright__ = "GNU3"
__credits__ = "Eskalinea"

__license__ = "GNU"
__version__  = "1.0.1"
__email__ = "jirka.f.blahut@gmail.com"

"""
# GUIDE:

Zkratky:
CTRL + 1 (ta vedle esc) mám nastavené jako line comment
CTRL + 2 jako block comment
F11 mám run (F5 zůstává), F12 je reformat code

Funkcionalita:
1) funkce/classy pro danný den si vždy nadefinuj v daném souboru. Každý den má dvě části. Je lepší dané fce oddělit.
      Zpracování výsledků můžeš zavolat i tady pokud se ti to bude zdát logické (třeba že by fce neměla vracet výpočet neco*100 :D)
2) volání probíhá dle názvů v __init__.py př:
      D01.<jmeno_fce> nebo D<cislo_dne>.<jmeno_objektu>  ==>  D01.hello()
3) na stránce advent of code např. "https://adventofcode.com/2019/day/1/input" si lze stáhnout input k danému zadání
      vždy to rozparsuj a nevkládej to jako string. :D normálně with open(file, "r") as input_f: a pak třeba input_f.readlines()
      když budeš dané zadání stahovat ulož ho do složky Programming/Python/AoC/Y19/Assignments pod daný den. Např 01.txt
           - když potom spustíš main tak se ti automaticky přiloží k dané funkci. stačí ho vždy poslat jen dovntiř tu v testingu
4) vždy vracej výsledky jako part_one, part_two: Když potom spustíš fci main tak se ti výsledky ukážou zarovnané v té tabulce co jsem ti posílal
5) pokud nevis co delas tak nemen zadnou fci pod day_24 (ale to se u tohohle rychle naučíš. :D)


Example:
    func:
            def day_01(file = ""):
                part_one = D01.hello()
                return part_one, part_two
                return part_one, part_two
      
    Output:
      
        ║════════ Advent of Code ════════║
        ║ Use default filesystem [y/n]?  ╠═ y -- uživatelskej input. Kdybys chtěla můžu ho později smazat !!!!
        ╠═════════════ 2019 ═════════════║
        ║ • Day: 01                      ║
        ║  	◦ Part one: hello world      ║
        ║  	◦ Part two: None             ║
"""
def day_01(file = ""):
    """
    Test: Day 1
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_02(file = ""):
    """
    Test: Day 2
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_03(file = ""):
    """
    Test: Day 3
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_04(file = ""):
    """
    Test: Day 4
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_05(file = ""):
    """
    Test: Day 5
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_06(file = ""):
    """
    Test: Day 6
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_07(file = ""):
    """
    Test: Day 7
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_08(file = ""):
    """
    Test: Day 8
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_09(file = ""):
    """
    Test: Day 9
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_10(file = ""):
    """
    Test: Day 10
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_11(file = ""):
    """
    Test: Day 11
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_12(file = ""):
    """
    Test: Day 12
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_13(file = ""):
    """
    Test: Day 13
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_14(file = ""):
    """
    Test: Day 14
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_15(file = ""):
    """
    Test: Day 15
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_16(file = ""):
    """
    Test: Day 16
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_17(file = ""):
    """
    Test: Day 17
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_18(file = ""):
    """
    Test: Day 18
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_19(file = ""):
    """
    Test: Day 19
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_20(file = ""):
    """
    Test: Day 20
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_21(file = ""):
    """
    Test: Day 21
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_22(file = ""):
    """
    Test: Day 22
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_23(file = ""):
    """
    Test: Day 23
    """
    part_one, part_two = None, None
    return part_one, part_two


def day_24(file = ""):
    """
    Test: Day 24
    """
    part_one, part_two = None, None
    return part_one, part_two


def testing(default):
    print("\u2560" + "\u2550" * 13 + " 2019 " + "\u2550" * 13 + "\u2551")
    days = {"01": day_01, "02": day_02, "03": day_03, "04": day_04, "05": day_05, "06": day_06, "07": day_07, "08": day_08, "09": day_09, "10": day_10, "11": day_11, "12": day_12, "13": day_13, "14": day_14, "15": day_15, "16": day_16, "17": day_17, "18": day_18, "19": day_19, "20": day_20, "21": day_21, "22": day_22, "23": day_23, "24": day_24}
    for day, func in days.items():
        print_day(day, default, func)


def print_day(day, default, func):
    """
    Prints out formatted result of both parts of each day

    :param day: Day number
    :param default: Use default filesystem
    :param func:
    :return:
    """
    print("\u2551 \u2022 Day: " + day + " " * 22 + "\u2551")
    try:
        if default:
            file = "Y19/assignments/" + day + ".txt."
        else:
            file = input("Enter full path to file:")
        list(map(print_part, func(file), ("one", "two")))
    except FileNotFoundError:
        print("\u2560   \u25E6 " + "Input file not specified" + "   \u2551")
    print("\u2560" + ("\u2550" * 32) + "\u2551")


def print_part(result, num):
    """
    Prints out result of day part

    :param result: Result value
    :param num: part number: One | Two
    """
    part_string = " \t\u25E6 Part " + num + ": " + str(result)
    print("\u2551 " + part_string + " " * (31 - len(part_string)) + "\u2551")

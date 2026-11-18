#!/usr/bin/env python3
"""Deterministic Meihua Yishu casting helper.

This script intentionally stays small: it calculates the hexagram structure
only. Interpretation remains in references/meihua.md.

Default solar time mode matches the working convention used by this skill:
solar year + month + day for the upper trigram, plus earthly-branch hour for
the lower trigram and moving line. Use --minute only when separating multiple
fresh questions inside the same two-hour branch.

The classic mode accepts an already-known lunar year-branch number, lunar month,
and lunar day. It avoids bundling a bulky calendar conversion table.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


TRIGRAMS = {
    1: ("乾", "☰", "111", "金"),
    2: ("兑", "☱", "011", "金"),
    3: ("离", "☲", "101", "火"),
    4: ("震", "☳", "001", "木"),
    5: ("巽", "☴", "110", "木"),
    6: ("坎", "☵", "010", "水"),
    7: ("艮", "☶", "100", "土"),
    8: ("坤", "☷", "000", "土"),
}

HEXAGRAMS = {
    (1, 1): (1, "乾为天"), (1, 2): (10, "天泽履"), (1, 3): (13, "天火同人"), (1, 4): (25, "天雷无妄"),
    (1, 5): (44, "天风姤"), (1, 6): (6, "天水讼"), (1, 7): (33, "天山遁"), (1, 8): (12, "天地否"),
    (2, 1): (43, "泽天夬"), (2, 2): (58, "兑为泽"), (2, 3): (49, "泽火革"), (2, 4): (17, "泽雷随"),
    (2, 5): (28, "泽风大过"), (2, 6): (47, "泽水困"), (2, 7): (31, "泽山咸"), (2, 8): (45, "泽地萃"),
    (3, 1): (14, "火天大有"), (3, 2): (38, "火泽睽"), (3, 3): (30, "离为火"), (3, 4): (21, "火雷噬嗑"),
    (3, 5): (50, "火风鼎"), (3, 6): (64, "火水未济"), (3, 7): (56, "火山旅"), (3, 8): (35, "火地晋"),
    (4, 1): (34, "雷天大壮"), (4, 2): (54, "雷泽归妹"), (4, 3): (55, "雷火丰"), (4, 4): (51, "震为雷"),
    (4, 5): (32, "雷风恒"), (4, 6): (40, "雷水解"), (4, 7): (62, "雷山小过"), (4, 8): (16, "雷地豫"),
    (5, 1): (9, "风天小畜"), (5, 2): (61, "风泽中孚"), (5, 3): (37, "风火家人"), (5, 4): (42, "风雷益"),
    (5, 5): (57, "巽为风"), (5, 6): (59, "风水涣"), (5, 7): (53, "风山渐"), (5, 8): (20, "风地观"),
    (6, 1): (5, "水天需"), (6, 2): (60, "水泽节"), (6, 3): (63, "水火既济"), (6, 4): (3, "水雷屯"),
    (6, 5): (48, "水风井"), (6, 6): (29, "坎为水"), (6, 7): (39, "水山蹇"), (6, 8): (8, "水地比"),
    (7, 1): (26, "山天大畜"), (7, 2): (41, "山泽损"), (7, 3): (22, "山火贲"), (7, 4): (27, "山雷颐"),
    (7, 5): (18, "山风蛊"), (7, 6): (4, "山水蒙"), (7, 7): (52, "艮为山"), (7, 8): (23, "山地剥"),
    (8, 1): (11, "地天泰"), (8, 2): (19, "地泽临"), (8, 3): (36, "地火明夷"), (8, 4): (24, "地雷复"),
    (8, 5): (46, "地风升"), (8, 6): (7, "地水师"), (8, 7): (15, "地山谦"), (8, 8): (2, "坤为地"),
}

BIN_TO_TRIGRAM = {value[2]: key for key, value in TRIGRAMS.items()}
BRANCH_BY_HOUR = {
    23: (1, "子"), 0: (1, "子"), 1: (2, "丑"), 2: (2, "丑"),
    3: (3, "寅"), 4: (3, "寅"), 5: (4, "卯"), 6: (4, "卯"),
    7: (5, "辰"), 8: (5, "辰"), 9: (6, "巳"), 10: (6, "巳"),
    11: (7, "午"), 12: (7, "午"), 13: (8, "未"), 14: (8, "未"),
    15: (9, "申"), 16: (9, "申"), 17: (10, "酉"), 18: (10, "酉"),
    19: (11, "戌"), 20: (11, "戌"), 21: (12, "亥"), 22: (12, "亥"),
}


@dataclass
class Cast:
    upper: int
    lower: int
    moving: int
    upper_sum: int
    lower_sum: int
    rule: str


def mod8(value: int) -> int:
    return value % 8 or 8


def mod6(value: int) -> int:
    return value % 6 or 6


def hex_name(upper: int, lower: int) -> str:
    number, name = HEXAGRAMS[(upper, lower)]
    return f"{number}. {name}"


def binary(upper: int, lower: int) -> str:
    return TRIGRAMS[upper][2] + TRIGRAMS[lower][2]


def from_binary(bits: str) -> tuple[int, int]:
    return BIN_TO_TRIGRAM[bits[:3]], BIN_TO_TRIGRAM[bits[3:]]


def change(bits: str, moving: int) -> str:
    # bits are stored upper-to-lower; moving lines count from bottom.
    index = 6 - moving
    parts = list(bits)
    parts[index] = "0" if parts[index] == "1" else "1"
    return "".join(parts)


def mutual(bits: str) -> tuple[int, int]:
    # Lower mutual uses lines 2-4; upper mutual uses lines 3-5.
    # With upper-to-lower storage, those slices are [2:5] and [1:4].
    return BIN_TO_TRIGRAM[bits[1:4]], BIN_TO_TRIGRAM[bits[2:5]]


def relation(ti: str, yong: str) -> str:
    generates = {"木": "火", "火": "土", "土": "金", "金": "水", "水": "木"}
    controls = {"木": "土", "土": "水", "水": "火", "火": "金", "金": "木"}
    if ti == yong:
        return "比和"
    if generates[yong] == ti:
        return "用生体"
    if generates[ti] == yong:
        return "体生用"
    if controls[ti] == yong:
        return "体克用"
    if controls[yong] == ti:
        return "用克体"
    return "未知"


def time_cast(year: int, month: int, day: int, hour: int, minute: int | None) -> Cast:
    branch_num, branch_name = BRANCH_BY_HOUR[hour]
    upper_sum = year + month + day
    lower_sum = upper_sum + branch_num + (minute or 0)
    rule = f"solar y+m+d; hour branch {branch_name}={branch_num}"
    if minute is not None:
        rule += f"; minute refinement +{minute}"
    return Cast(mod8(upper_sum), mod8(lower_sum), mod6(lower_sum), upper_sum, lower_sum, rule)


def classic_cast(year_branch: int, lunar_month: int, lunar_day: int, hour: int, minute: int | None) -> Cast:
    if not 1 <= year_branch <= 12:
        raise ValueError("year_branch must be 1..12: 子=1, 丑=2, ... 亥=12")
    branch_num, branch_name = BRANCH_BY_HOUR[hour]
    upper_sum = year_branch + lunar_month + lunar_day
    lower_sum = upper_sum + branch_num + (minute or 0)
    rule = f"classic lunar branch={year_branch}; lunar month/day; hour branch {branch_name}={branch_num}"
    if minute is not None:
        rule += f"; minute refinement +{minute}"
    return Cast(mod8(upper_sum), mod8(lower_sum), mod6(lower_sum), upper_sum, lower_sum, rule)


def number_cast(first: int, second: int, third: int | None) -> Cast:
    moving_source = third if third is not None else first + second
    rule = "two-number cast" if third is None else "three-number cast"
    return Cast(mod8(first), mod8(second), mod6(moving_source), first, second, rule)


def print_cast(cast: Cast) -> None:
    bits = binary(cast.upper, cast.lower)
    changed_bits = change(bits, cast.moving)
    changed_upper, changed_lower = from_binary(changed_bits)
    mutual_upper, mutual_lower = mutual(bits)

    moving_in_upper = cast.moving >= 4
    ti = cast.lower if moving_in_upper else cast.upper
    yong = cast.upper if moving_in_upper else cast.lower
    ti_pos = "下卦" if moving_in_upper else "上卦"
    yong_pos = "上卦" if moving_in_upper else "下卦"
    ti_element = TRIGRAMS[ti][3]
    yong_element = TRIGRAMS[yong][3]

    print(f"rule: {cast.rule}")
    print(f"upper_sum: {cast.upper_sum} -> {cast.upper} {TRIGRAMS[cast.upper][0]}")
    print(f"lower_sum: {cast.lower_sum} -> {cast.lower} {TRIGRAMS[cast.lower][0]}")
    print(f"moving_line: {cast.moving}")
    print(f"main: {hex_name(cast.upper, cast.lower)} ({TRIGRAMS[cast.upper][0]} over {TRIGRAMS[cast.lower][0]})")
    print(f"binary: {bits}")
    print(f"ti_yong: 体={TRIGRAMS[ti][0]}({ti_pos},{ti_element}) 用={TRIGRAMS[yong][0]}({yong_pos},{yong_element}) -> {relation(ti_element, yong_element)}")
    print(f"mutual: {hex_name(mutual_upper, mutual_lower)} ({TRIGRAMS[mutual_upper][0]} over {TRIGRAMS[mutual_lower][0]})")
    print(f"changed: {hex_name(changed_upper, changed_lower)} ({TRIGRAMS[changed_upper][0]} over {TRIGRAMS[changed_lower][0]})")


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate Meihua Yishu hexagram structure.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_time = sub.add_parser("time", help="Cast by solar year/month/day/hour.")
    p_time.add_argument("year", type=int)
    p_time.add_argument("month", type=int)
    p_time.add_argument("day", type=int)
    p_time.add_argument("hour", type=int, choices=range(24))
    p_time.add_argument("--minute", type=int, choices=range(60), help="Only for separating multiple fresh questions in the same two-hour branch.")

    p_classic = sub.add_parser("classic", help="Cast by lunar year branch number/month/day/hour.")
    p_classic.add_argument("year_branch", type=int, help="子=1, 丑=2, ... 亥=12")
    p_classic.add_argument("lunar_month", type=int)
    p_classic.add_argument("lunar_day", type=int)
    p_classic.add_argument("hour", type=int, choices=range(24))
    p_classic.add_argument("--minute", type=int, choices=range(60), help="Only for separating multiple fresh questions in the same two-hour branch.")

    p_num = sub.add_parser("num", help="Cast by two or three numbers.")
    p_num.add_argument("first", type=int)
    p_num.add_argument("second", type=int)
    p_num.add_argument("third", type=int, nargs="?")

    args = parser.parse_args()
    if args.command == "time":
        cast = time_cast(args.year, args.month, args.day, args.hour, args.minute)
    elif args.command == "classic":
        cast = classic_cast(args.year_branch, args.lunar_month, args.lunar_day, args.hour, args.minute)
    else:
        cast = number_cast(args.first, args.second, args.third)
    print_cast(cast)


if __name__ == "__main__":
    main()

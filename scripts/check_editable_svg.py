#!/usr/bin/env python3
"""Lightweight audit for human-editable scientific SVG files."""

from __future__ import annotations
import sys
import xml.etree.ElementTree as ET
from collections import Counter

NS = {"svg": "http://www.w3.org/2000/svg"}

def lname(tag: str) -> str:
    return tag.split("}", 1)[-1]

def main(path: str) -> int:
    root = ET.parse(path).getroot()
    issues = []
    warnings = []

    if "viewBox" not in root.attrib:
        issues.append("Missing viewBox.")

    ids = []
    counts = Counter()
    for el in root.iter():
        counts[lname(el.tag)] += 1
        if el.get("id"):
            ids.append(el.get("id"))

    dup = [k for k, v in Counter(ids).items() if v > 1]
    if dup:
        issues.append(f"Duplicate ids: {dup}")

    if counts["text"] == 0:
        warnings.append("No <text> elements found; text may have been outlined.")

    if counts["g"] < 2:
        warnings.append("Very few <g> groups; semantic grouping may be insufficient.")

    if counts["foreignObject"] > 0:
        warnings.append("Contains <foreignObject>; cross-editor compatibility may be weaker.")

    if counts["image"] > 0:
        warnings.append(f"Contains {counts['image']} raster/image element(s); verify they are intentional assets.")

    paths = [el for el in root.iter() if lname(el.tag) == "path"]
    giant = [el.get("id", "<unnamed>") for el in paths if len(el.get("d", "")) > 10000]
    if giant:
        warnings.append(f"Very large path data found: {giant}; possible flattening.")

    anonymous_groups = [el for el in root.iter() if lname(el.tag) == "g" and not el.get("id")]
    if anonymous_groups:
        warnings.append(f"{len(anonymous_groups)} group(s) have no id.")

    print("Editable SVG audit")
    print("------------------")
    print("Counts:", dict(counts))
    if issues:
        print("\nERRORS:")
        for x in issues:
            print(" -", x)
    if warnings:
        print("\nWARNINGS:")
        for x in warnings:
            print(" -", x)
    if not issues:
        print("\nPASS: no blocking structural issues detected.")

    return 1 if issues else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_editable_svg.py figure.svg")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))

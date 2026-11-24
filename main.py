#!/usr/bin/env python3
"""VP of Great Questions — make.fun entry (u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)"""
import os

ENTRY_LINE = "Vice President of Great Questions and Zero Answers"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(ENTRY_LINE + "\n")

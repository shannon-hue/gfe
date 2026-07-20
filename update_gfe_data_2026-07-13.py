#!/usr/bin/env python3
"""
GFE Weekly Refresh — week of 2026-07-13 (Mon Jul 13 – Sun Jul 19)
Generated: 2026-07-20
Includes: aaralsip@gmail.com (internal, active from Jul 1), 2h grace period on KPI
16 reviewer emails total.
Run: python3 update_gfe_data_2026-07-13.py  (from ~/Documents/GitHub/gfe)

KPI notes:
- 3 true KPI misses (all breck reviewer, Alaina Gray & ReNu Infusions)
- 5 initial "miss" submissions were covered by a second reviewer on our team
- Counts use 0.949 dedup ratio (consistent with June baseline)
"""
import json, os

GFE_FILE = os.path.join(os.path.dirname(__file__), "gfe_data.json")
WEEK_KEY = "2026-07-13"

NEW_WEEK = {
    "completed_total": 1094, "completed_advance": 581, "completed_lm": 513,
    "reviewer_counts": {
        "aaralsip@gmail.com": 30,
        "allison.h@spakinect.com": 73,
        "breck+gfesupport@joinmoxie.com": 22,
        "courtneydanielle22@yahoo.com": 303,
        "crystal.a@spakinect.com": 49,
        "erica.n@spakinect.com": 46,
        "erin.shannon+gfe@joinmoxie.com": 203,
        "gennydamato@gmail.com": 85,
        "helen.b@spakinect.com": 117,
        "ivy.c@spakinect.com": 8,
        "jade.s@spakinect.com": 1,
        "joseph.s@spakinect.com": 14,
        "lindsay.c@spakinect.com": 6,
        "mchenfnp@gmail.com": 51,
        "samantha.r@spakinect.com": 33,
        "stephanie.h@spakinect.com": 53,
    },
    "completed_by_group": {
        "all": 1094, "spk_int": 860, "spakinect": 522,
        "spk_brk": 756, "internal": 338, "breck": 234,
    },
    "kpi_eligible": 564, "kpi_met": 561, "kpi_missed": 3, "kpi_pct": 99.5,
    "wknd_excl": 20, "lm_total": 513, "lm_completed_before": 417, "lm_pct": 81.3,
    "avg_ta_hrs": 30.0, "max_ta_hrs": 720.0,
    "qualiphy_count": 0, "qualiphy_before": 0, "kpi_qualiphy_save": 0,
}

NEW_MISS_RECORDS = [
    # True KPI misses: advance-submitted, never reviewed by our team
    # (Alaina Gray reviewed by mpjones@lakeregional.com, not in our reviewer list)
    {
        "id": 257242, "client": "A. Titus", "medspa": "ReNu Infusions",
        "cat": "spk_brk", "segment": "Silver",
        "submitted": "2026-07-13 00:22", "appt": "2026-07-14 15:00",
        "appt_day": "Tue", "sub_day": "Mon",
        "is_weekend_appt": False, "is_weekend_sub": False,
        "hrs_advance": 38.6, "advance_fmt": "38h 38m",
        "finished": None, "completed_before": False,
    },
    {
        "id": 255962, "client": "K. Pierce", "medspa": "Alaina Gray Aesthetics",
        "cat": "breck", "segment": "Momentum",
        "submitted": "2026-07-09 10:00", "appt": "2026-07-15 16:45",
        "appt_day": "Wed", "sub_day": "Thu",
        "is_weekend_appt": False, "is_weekend_sub": False,
        "hrs_advance": 150.8, "advance_fmt": "150h 45m",
        "finished": None, "completed_before": False,
    },
    {
        "id": 257569, "client": "L. Smiith", "medspa": "Alaina Gray Aesthetics",
        "cat": "breck", "segment": "Momentum",
        "submitted": "2026-07-13 00:24", "appt": "2026-07-16 14:30",
        "appt_day": "Thu", "sub_day": "Mon",
        "is_weekend_appt": False, "is_weekend_sub": False,
        "hrs_advance": 86.1, "advance_fmt": "86h 6m",
        "finished": None, "completed_before": False,
    },
]

NEW_META = {
    "refreshed": "2026-07-20", "today": "2026-07-19",
    "last_week": "2026-07-13", "this_week": "2026-07-20",
    "this_month": "2026-07", "last_month": "2026-06",
    "this_month_start": "2026-07-06",
    "last_month_start": "2026-06-01", "last_month_end": "2026-06-30",
}

with open(GFE_FILE, "r") as f:
    data = json.loads(f.read())

data[WEEK_KEY] = json.loads(json.dumps(NEW_WEEK))

existing_miss_ids = {r["id"] for r in data.get("_miss_records", [])}
added = 0
for rec in NEW_MISS_RECORDS:
    if rec["id"] not in existing_miss_ids:
        data["_miss_records"].append(json.loads(json.dumps(rec)))
        added += 1

data["_meta"] = json.loads(json.dumps(NEW_META))

with open(GFE_FILE, "w") as f:
    f.write(json.dumps(data, indent=2))

all_weeks = sorted(k for k in data if k.startswith("20"))
print(f"✓ gfe_data.json updated")
print(f"  Week keys ({len(all_weeks)}): {all_weeks[-5:]}")
print(f"  {WEEK_KEY}: KPI {NEW_WEEK['kpi_pct']}% ({NEW_WEEK['kpi_met']}/{NEW_WEEK['kpi_eligible']}) · avg TA {NEW_WEEK['avg_ta_hrs']}h · {NEW_WEEK['completed_total']} completions")
print(f"  Miss records added: {added}")
print(f"  _meta.refreshed → {NEW_META['refreshed']}, last_week → {NEW_META['last_week']}")

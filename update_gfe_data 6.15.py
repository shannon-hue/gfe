#!/usr/bin/env python3
"""
GFE Weekly Refresh — week of 2026-06-08 (Mon Jun 8 – Sun Jun 14)
Generated: 2026-06-15
Run: python3 update_gfe_data.py  (from ~/Documents/GitHub/gfe)
"""

import json, os

GFE_FILE = os.path.join(os.path.dirname(__file__), "gfe_data.json")

# ── New week entry ───────────────────────────────────────────────────────────

WEEK_KEY = "2026-06-08"

NEW_WEEK = {
    "completed_total": 1293,
    "completed_advance": 864,
    "completed_lm": 429,
    "reviewer_counts": {
        "allison.h@spakinect.com": 88,
        "breck+gfesupport@joinmoxie.com": 11,
        "courtneydanielle22@yahoo.com": 411,
        "crystal.a@spakinect.com": 62,
        "erica.n@spakinect.com": 20,
        "erin.shannon+gfe@joinmoxie.com": 235,
        "gennydamato@gmail.com": 31,
        "helen.b@spakinect.com": 111,
        "ivy.c@spakinect.com": 43,
        "joseph.s@spakinect.com": 66,
        "lindsay.c@spakinect.com": 125,
        "mchenfnp@gmail.com": 42,
        "samantha.r@spakinect.com": 18,
        "stephanie.h@spakinect.com": 30,
    },
    "completed_by_group": {
        "all": 189,
        "spk_int": 517,
        "spakinect": 148,
        "spk_brk": 118,
        "internal": 47,
        "breck": 2,
    },
    "kpi_eligible": 715,
    "kpi_met": 710,
    "kpi_missed": 5,
    "kpi_pct": 99.3,
    "wknd_excl": 18,
    "lm_total": 384,
    "lm_completed_before": 339,
    "lm_pct": 88.3,
    "avg_ta_hrs": 5.3,
    "max_ta_hrs": 720.0,
    "qualiphy_count": 0,
    "qualiphy_before": 0,
    "kpi_qualiphy_save": 0,
}

# ── New miss records ─────────────────────────────────────────────────────────

NEW_MISS_RECORDS = [
    {
        "id": 240241,
        "client": "T. Fast",
        "medspa": "Kopper Aesthetics",
        "cat": "spakinect",
        "submitted": "2026-06-05 18:38",
        "appt": "2026-06-08 09:00",
        "appt_day": "Mon",
        "sub_day": "Fri",
        "is_weekend_appt": False,
        "is_weekend_sub": False,
        "hrs_advance": 62.4,
        "advance_fmt": "2d 14h",
        "finished": None,
        "completed_before": False,
    },
    {
        "id": 239024,
        "client": "B. Ramsey",
        "medspa": "Nurse Injector Brooke",
        "cat": "spakinect",
        "submitted": "2026-06-03 17:07",
        "appt": "2026-06-08 22:30",
        "appt_day": "Mon",
        "sub_day": "Wed",
        "is_weekend_appt": False,
        "is_weekend_sub": False,
        "hrs_advance": 125.4,
        "advance_fmt": "5d 5h",
        "finished": "2026-06-10 17:53",
        "completed_before": False,
    },
    {
        "id": 240517,
        "client": "B. Ogden",
        "medspa": "Careen Aesthetics",
        "cat": "spk_int",
        "submitted": "2026-06-06 14:24",
        "appt": "2026-06-09 13:30",
        "appt_day": "Tue",
        "sub_day": "Sat",
        "is_weekend_appt": False,
        "is_weekend_sub": True,
        "hrs_advance": 71.1,
        "advance_fmt": "2d 23h",
        "finished": None,
        "completed_before": False,
    },
    {
        "id": 231719,
        "client": "E. Lara",
        "medspa": "Wild Moon Collective",
        "cat": "spakinect",
        "submitted": "2026-05-19 22:00",
        "appt": "2026-06-12 13:30",
        "appt_day": "Fri",
        "sub_day": "Tue",
        "is_weekend_appt": False,
        "is_weekend_sub": False,
        "hrs_advance": 567.5,
        "advance_fmt": "23d 15h",
        "finished": None,
        "completed_before": False,
    },
    {
        "id": 216507,
        "client": "C. Brignole",
        "medspa": "Rejuvenate Austin",
        "cat": "spakinect",
        "submitted": "2026-04-22 15:01",
        "appt": "2026-06-13 12:45",
        "appt_day": "Sat",
        "sub_day": "Wed",
        "is_weekend_appt": True,
        "is_weekend_sub": False,
        "hrs_advance": 1245.7,
        "advance_fmt": "51d 21h",
        "finished": None,
        "completed_before": False,
    },
]

# ── Updated _meta ────────────────────────────────────────────────────────────

NEW_META = {
    "refreshed": "2026-06-15",
    "today": "2026-06-14",
    "last_week": "2026-06-08",
    "this_week": "2026-06-15",
    "this_month": "2026-06",
    "last_month": "2026-05",
    "this_month_start": "2026-06-01",
    "last_month_start": "2026-05-05",
    "last_month_end": "2026-05-25",
}

# ── Load, update, save ───────────────────────────────────────────────────────

with open(GFE_FILE, "r") as f:
    data = json.loads(f.read())

# Insert new week
data[WEEK_KEY] = json.loads(json.dumps(NEW_WEEK))

# Append new miss records (avoid duplicates by ID)
existing_miss_ids = {r["id"] for r in data.get("_miss_records", [])}
for rec in NEW_MISS_RECORDS:
    if rec["id"] not in existing_miss_ids:
        data["_miss_records"].append(json.loads(json.dumps(rec)))

# Update _meta
data["_meta"] = json.loads(json.dumps(NEW_META))

with open(GFE_FILE, "w") as f:
    f.write(json.dumps(data, indent=2))

# ── Confirmation ─────────────────────────────────────────────────────────────

all_weeks = sorted(k for k in data if k.startswith("20"))
print(f"✓ gfe_data.json updated")
print(f"  Week keys ({len(all_weeks)}): {all_weeks[-5:]}")
print(f"  {WEEK_KEY}: KPI {NEW_WEEK['kpi_pct']}% ({NEW_WEEK['kpi_met']}/{NEW_WEEK['kpi_eligible']}) · avg TA {NEW_WEEK['avg_ta_hrs']}h · {NEW_WEEK['completed_total']} completions")
print(f"  Miss records added: {len([r for r in NEW_MISS_RECORDS if r['id'] not in existing_miss_ids])}")
print(f"  _meta.refreshed → {NEW_META['refreshed']}, last_week → {NEW_META['last_week']}")
print()
print("Next steps:")
print("  git add gfe_data.json")
print('  git commit -m "Weekly refresh 2026-06-08"')
print("  git push")

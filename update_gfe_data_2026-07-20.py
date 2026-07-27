#!/usr/bin/env python3
"""
GFE Weekly Refresh — week of 2026-07-20 (Mon Jul 20 – Sun Jul 26)
Generated: 2026-07-27
Includes: aaralsip@gmail.com (internal, active from Jul 1), 2h grace period on KPI
16 reviewer emails total.
Run: python3 update_gfe_data_2026-07-20.py  (from ~/Documents/GitHub/gfe)

KPI notes:
- 3 confirmed KPI misses (kpi_eligible=720, kpi_met=717, kpi_pct=99.6%)
- Paige Whitten (Alaina Gray, ID 257668): FLAG — mpjones@lakeregional.com
  covered this before the appointment (same pattern as Jul 13 Alaina Gray cases).
  Check with Shannon whether to remove.
- Fi Fabiani (Radiant Renewal, ID 255408): courtney completed 5 days late
- Angelica Serna (Inspire Body Spa, ID 250332): erin completed ~10h after appt+2h deadline

Sanity checks enforced at runtime:
- kpi_missed == len(NEW_MISS_RECORDS)  [count must match table]
- all miss records have non-'unknown' segment  [segment must be populated]
- kpi_met + kpi_missed == kpi_eligible
"""
import json, os, sys

GFE_FILE = os.path.join(os.path.dirname(__file__), "gfe_data.json")
WEEK_KEY = "2026-07-20"

NEW_WEEK = {
    "completed_total": 1120, "completed_advance": 739, "completed_lm": 381,
    "reviewer_counts": {
        "aaralsip@gmail.com": 0,
        "allison.h@spakinect.com": 42,
        "breck+gfesupport@joinmoxie.com": 15,
        "courtneydanielle22@yahoo.com": 449,
        "crystal.a@spakinect.com": 49,
        "erica.n@spakinect.com": 29,
        "erin.shannon+gfe@joinmoxie.com": 179,
        "gennydamato@gmail.com": 109,
        "helen.b@spakinect.com": 77,
        "ivy.c@spakinect.com": 39,
        "jade.s@spakinect.com": 23,
        "joseph.s@spakinect.com": 9,
        "lindsay.c@spakinect.com": 0,
        "mchenfnp@gmail.com": 3,
        "samantha.r@spakinect.com": 56,
        "stephanie.h@spakinect.com": 41,
    },
    "completed_by_group": {
        "all": 1120, "internal": 561, "spakinect": 365,
        "breck": 194, "spk_int": 926, "spk_brk": 559,
    },
    "kpi_eligible": 720, "kpi_met": 717, "kpi_missed": 3, "kpi_pct": 99.6,
    "wknd_excl": 19, "lm_total": 381, "lm_completed_before": 324, "lm_pct": 85.0,
    "avg_ta_hrs": 83.0, "max_ta_hrs": 720.0,
    "qualiphy_count": 0, "qualiphy_before": 0, "kpi_qualiphy_save": 0,
}

NEW_MISS_RECORDS = [
    # FLAG: Paige Whitten — breck started review on Jul 13 but never finished.
    # mpjones@lakeregional.com completed on Jul 13 08:09 (before Jul 23 appt).
    # Same pattern as last week's Alaina Gray cases. Check with Shannon.
    {
        "id": 257668, "client": "P. Whitten", "medspa": "Alaina Gray Aesthetics",
        "cat": "breck", "segment": "Green",
        "submitted": "2026-07-13 00:54", "appt": "2026-07-23 12:15",
        "appt_day": "Thu", "sub_day": "Mon",
        "is_weekend_appt": False, "is_weekend_sub": False,
        "hrs_advance": 252.4, "advance_fmt": "252h 21m",
        "finished": None, "completed_before": False,
    },
    # Fi Fabiani — advance 323h, courtney completed Jul 26 (5 days after Jul 21 appt)
    {
        "id": 255408, "client": "F. Fabiani", "medspa": "Radiant Renewal",
        "cat": "spk_int", "segment": "Silver",
        "submitted": "2026-07-08 02:36", "appt": "2026-07-21 13:45",
        "appt_day": "Mon", "sub_day": "Wed",
        "is_weekend_appt": False, "is_weekend_sub": False,
        "hrs_advance": 323.2, "advance_fmt": "323h 9m",
        "finished": "2026-07-26 10:27", "completed_before": False,
    },
    # Angelica Serna — advance 607h, erin completed Jul 22 06:24 (~10h after appt+2h deadline)
    {
        "id": 250332, "client": "A. Serna", "medspa": "Inspire Body Spa",
        "cat": "all", "segment": "Silver",
        "submitted": "2026-06-26 11:44", "appt": "2026-07-21 18:30",
        "appt_day": "Mon", "sub_day": "Fri",
        "is_weekend_appt": False, "is_weekend_sub": False,
        "hrs_advance": 606.8, "advance_fmt": "606h 46m",
        "finished": "2026-07-22 06:24", "completed_before": False,
    },
]

NEW_META = {
    "refreshed": "2026-07-27", "today": "2026-07-26",
    "last_week": "2026-07-20", "this_week": "2026-07-27",
    "this_month": "2026-07", "last_month": "2026-06",
    "this_month_start": "2026-07-06",
    "last_month_start": "2026-06-01", "last_month_end": "2026-06-30",
}

with open(GFE_FILE, "r") as f:
    data = json.loads(f.read())

# ── Auto-fill segments from _segments lookup ──────────────────────────────────
segs = data.get("_segments", {})
for rec in NEW_MISS_RECORDS:
    if rec.get("segment", "unknown") == "unknown":
        looked_up = segs.get(rec["medspa"], "unknown")
        rec["segment"] = looked_up

# ── Sanity checks — fail loudly before writing anything ──────────────────────
errors = []

if NEW_WEEK["kpi_missed"] != len(NEW_MISS_RECORDS):
    errors.append(
        f"kpi_missed={NEW_WEEK['kpi_missed']} but {len(NEW_MISS_RECORDS)} miss records — "
        f"these must match so the top KPI number and the table agree"
    )

if NEW_WEEK["kpi_met"] + NEW_WEEK["kpi_missed"] != NEW_WEEK["kpi_eligible"]:
    errors.append(
        f"kpi_met({NEW_WEEK['kpi_met']}) + kpi_missed({NEW_WEEK['kpi_missed']}) "
        f"!= kpi_eligible({NEW_WEEK['kpi_eligible']})"
    )

unknown_segs = [r["medspa"] for r in NEW_MISS_RECORDS if r.get("segment", "unknown") == "unknown"]
if unknown_segs:
    errors.append(f"Segment still 'unknown' for: {unknown_segs} — look up in HubSpot before running")

if errors:
    print("✗ Sanity check failed — nothing written:")
    for e in errors:
        print(f"  • {e}")
    sys.exit(1)

# ── Write ─────────────────────────────────────────────────────────────────────
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
print(f"  Segments auto-filled from _segments: {[r['medspa'] + '=' + r['segment'] for r in NEW_MISS_RECORDS]}")

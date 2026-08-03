#!/usr/bin/env python3
"""
GFE Weekly Refresh — week of 2026-07-27 (Mon Jul 27 – Sun Aug 2)
Generated: 2026-08-03
Includes all 20 reviewers: 4 internal, 14 spakinect, 2 breck
Run: python3 update_gfe_data_2026-07-27.py  (from ~/Documents/GitHub/gfe)

KPI notes:
- 2 confirmed KPI misses (kpi_eligible=711, kpi_met=709, kpi_pct=99.7%)
- Omni's KPI field showed 3 missed; only 2 confirmed miss records found.
  Flag for Shannon to verify if a 3rd record exists.
- M. Terranova (Your Glow Cove Med Spa, ID 266070): submitted Tue Jul 29,
  appt Sat Aug 1 — no review completed by any team reviewer
- S. Kerem (Purskin Medical Aesthetics, ID 267173): submitted Thu Jul 31,
  appt Sat Aug 22 — no review completed (530h advance, very far out)
- wknd_excl=61: Omni count of advance submissions where both submission
  AND appointment fall on Sat/Sun; Jul 27 (Sun), Aug 1 (Sat), Aug 2 (Sun)
  are all weekend days in this window — higher than typical weeks
- avg_ta_hrs=199.5, max_ta_hrs=9237: max is an outlier (~385 days advance),
  likely a single edge-case record; all prior-week maxes were ~720h
- completed_advance + completed_lm = 1252 ≠ completed_total 1261:
  9-record gap due to null hours_from_request_created_to_next_appointment

Sanity checks enforced at runtime:
- kpi_missed == len(NEW_MISS_RECORDS)
- kpi_met + kpi_missed == kpi_eligible
- all miss records have non-'unknown' segment
"""
import json, os, sys

GFE_FILE = os.path.join(os.path.dirname(__file__), "gfe_data.json")
WEEK_KEY = "2026-07-27"

NEW_WEEK = {
    "completed_total": 1261, "completed_advance": 825, "completed_lm": 427,
    "reviewer_counts": {
        "aaralsip@gmail.com": 32,
        "allison.h@spakinect.com": 39,
        "amber.b@spakinect.com": 0,
        "breck+gfesupport@joinmoxie.com": 5,
        "courtneydanielle22@yahoo.com": 558,
        "crystal.a@spakinect.com": 21,
        "erica.n@spakinect.com": 50,
        "erin.shannon+gfe@joinmoxie.com": 178,
        "gennydamato@gmail.com": 135,
        "helen.b@spakinect.com": 39,
        "ivy.c@spakinect.com": 62,
        "jade.s@spakinect.com": 0,
        "johan.k@spakinect.com": 0,
        "joseph.s@spakinect.com": 0,
        "lindsay.c@spakinect.com": 0,
        "maria.g@spakinect.com": 0,
        "mchenfnp@gmail.com": 0,
        "nichole.v@spakinect.com": 0,
        "samantha.r@spakinect.com": 62,
        "stephanie.h@spakinect.com": 80,
    },
    "completed_by_group": {
        "all": 1261, "internal": 725, "spakinect": 353,
        "breck": 183, "spk_int": 1078, "spk_brk": 536,
    },
    "kpi_eligible": 711, "kpi_met": 709, "kpi_missed": 2, "kpi_pct": 99.7,
    "wknd_excl": 61, "lm_total": 393, "lm_completed_before": 370, "lm_pct": 94.1,
    "avg_ta_hrs": 199.5, "max_ta_hrs": 9237.0,
    "qualiphy_count": 0, "qualiphy_before": 0, "kpi_qualiphy_save": 0,
}

NEW_MISS_RECORDS = [
    # M. Terranova — advance 66h, no review. Appt Sat Aug 1 (within this week).
    {
        "id": 266070, "client": "M. Terranova", "medspa": "Your Glow Cove Med Spa",
        "cat": "spakinect", "segment": "Momentum",
        "submitted": "2026-07-29 16:00", "appt": "2026-08-01 10:00",
        "appt_day": "Sat", "sub_day": "Tue",
        "is_weekend_appt": True, "is_weekend_sub": False,
        "hrs_advance": 66.0, "advance_fmt": "66h 0m",
        "finished": None, "completed_before": False,
    },
    # S. Kerem — advance 530h (~22 days), no review. Appt Sat Aug 22.
    {
        "id": 267173, "client": "S. Kerem", "medspa": "Purskin Medical Aesthetics",
        "cat": "spakinect", "segment": "Growth",
        "submitted": "2026-07-31 14:40", "appt": "2026-08-22 16:15",
        "appt_day": "Sat", "sub_day": "Thu",
        "is_weekend_appt": True, "is_weekend_sub": False,
        "hrs_advance": 529.6, "advance_fmt": "529h 35m",
        "finished": None, "completed_before": False,
    },
]

NEW_META = {
    "refreshed": "2026-08-03", "today": "2026-08-02",
    "last_week": "2026-07-27", "this_week": "2026-08-03",
    "this_month": "2026-08", "last_month": "2026-07",
    "this_month_start": "2026-08-03",
    "last_month_start": "2026-07-01", "last_month_end": "2026-07-31",
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
    errors.append(f"Segment still 'unknown' for: {unknown_segs} — look up in Omni before running")

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

all_weeks = sorted(k for k in data if k.startswith("20") and len(k) == 10)
print(f"✓ gfe_data.json updated")
print(f"  Week keys ({len(all_weeks)}): {all_weeks[-5:]}")
print(f"  {WEEK_KEY}: KPI {NEW_WEEK['kpi_pct']}% ({NEW_WEEK['kpi_met']}/{NEW_WEEK['kpi_eligible']}) · avg TA {NEW_WEEK['avg_ta_hrs']}h · {NEW_WEEK['completed_total']} completions")
print(f"  Miss records added: {added}")
print(f"  _meta.refreshed → {NEW_META['refreshed']}, last_week → {NEW_META['last_week']}")
print(f"  Segments auto-filled from _segments: {[r['medspa'] + '=' + r['segment'] for r in NEW_MISS_RECORDS]}")

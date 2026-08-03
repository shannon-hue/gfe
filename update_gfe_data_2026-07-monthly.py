#!/usr/bin/env python3
"""
GFE Monthly Rollup — July 2026 (Jul 1 – Jul 31)
Generated: 2026-08-03
All 20 reviewers: 4 internal, 14 spakinect, 2 breck. Excludes medspa 134/158/728/2018.
Run: python3 update_gfe_data_2026-07-monthly.py  (from ~/Documents/GitHub/gfe)

Data sources:
- completed_total / reviewer_counts: review_finished_at in July 2026 (Omni)
- KPI eligible/met: created_at in July 2026, advance >24h, excl both-weekend (Omni askOmni)
- LM stats: created_at in July 2026, ≤24h advance (Omni askOmni)
- avg/max_ta_hrs: hours_from_request_created_to_next_appointment for July completions (Omni)

Notes:
- completed_total=5173 is deduplicated (distinct gfe_review_request_id with review_finished_at in July)
- completed_advance + completed_lm = 3378+1791 = 5169 ≠ 5173: 4-record gap from
  null hours_from_request_created_to_next_appointment
- reviewer_counts are non-deduplicated (per-reviewer row counts)
- completed_by_group is non-deduplicated per-group sum
- wknd_excl=89: advance submissions where BOTH created_at AND next_appointment_start_time
  fall on Saturday or Sunday, excluded from KPI eligible
- max_ta_hrs=11016 (~459 days): extreme outlier; same data quality caveat as weekly max

Sanity checks enforced at runtime:
- kpi_met + kpi_missed == kpi_eligible
"""
import json, os, sys

GFE_FILE = os.path.join(os.path.dirname(__file__), "gfe_data.json")
MONTH_KEY = "2026-07"

NEW_MONTH = {
    "completed_total": 5173,  # deduped distinct requests reviewed in July
    "completed_advance": 3378,
    "completed_lm": 1791,
    "reviewer_counts": {
        "aaralsip@gmail.com": 119,
        "allison.h@spakinect.com": 229,
        "amber.b@spakinect.com": 0,
        "breck+gfesupport@joinmoxie.com": 83,
        "courtneydanielle22@yahoo.com": 1714,
        "crystal.a@spakinect.com": 158,
        "erica.n@spakinect.com": 218,
        "erin.shannon+gfe@joinmoxie.com": 783,
        "gennydamato@gmail.com": 591,
        "helen.b@spakinect.com": 324,
        "ivy.c@spakinect.com": 174,
        "jade.s@spakinect.com": 61,
        "johan.k@spakinect.com": 0,
        "joseph.s@spakinect.com": 41,
        "lindsay.c@spakinect.com": 11,
        "maria.g@spakinect.com": 0,
        "mchenfnp@gmail.com": 154,
        "nichole.v@spakinect.com": 0,
        "samantha.r@spakinect.com": 260,
        "stephanie.h@spakinect.com": 321,
    },
    "completed_by_group": {
        # Non-deduped group sums:
        # internal (courtney, mchenfnp, genny, aaralsip): 1714+154+591+119 = 2578
        # breck (breck+, erin.shannon): 83+783 = 866
        # spakinect (14): 229+0+158+218+324+174+61+0+41+11+0+0+260+321 = 1797
        "all": 5241, "internal": 2578, "spakinect": 1797,
        "breck": 866, "spk_int": 4375, "spk_brk": 2663,
    },
    "kpi_eligible": 3080, "kpi_met": 3060, "kpi_missed": 20, "kpi_pct": 99.4,
    "wknd_excl": 89, "lm_total": 1704, "lm_completed_before": 1556, "lm_pct": 91.3,
    "avg_ta_hrs": 211.5, "max_ta_hrs": 11016.0,
    "qualiphy_count": 0, "qualiphy_before": 0, "kpi_qualiphy_save": 0,
    "month": "2026-07", "month_start": "2026-07-01", "month_end": "2026-07-31",
}

with open(GFE_FILE, "r") as f:
    data = json.loads(f.read())

# ── Sanity checks ─────────────────────────────────────────────────────────────
errors = []

if NEW_MONTH["kpi_met"] + NEW_MONTH["kpi_missed"] != NEW_MONTH["kpi_eligible"]:
    errors.append(
        f"kpi_met({NEW_MONTH['kpi_met']}) + kpi_missed({NEW_MONTH['kpi_missed']}) "
        f"!= kpi_eligible({NEW_MONTH['kpi_eligible']})"
    )

reviewer_total = sum(NEW_MONTH["reviewer_counts"].values())
if reviewer_total != NEW_MONTH["completed_by_group"]["all"]:
    errors.append(
        f"reviewer_counts sum ({reviewer_total}) != completed_by_group['all'] "
        f"({NEW_MONTH['completed_by_group']['all']})"
    )

if errors:
    print("✗ Sanity check failed — nothing written:")
    for e in errors:
        print(f"  • {e}")
    sys.exit(1)

# ── Write ─────────────────────────────────────────────────────────────────────
data[MONTH_KEY] = json.loads(json.dumps(NEW_MONTH))

with open(GFE_FILE, "w") as f:
    f.write(json.dumps(data, indent=2))

all_keys = sorted(k for k in data if k.startswith("20"))
print(f"✓ gfe_data.json updated")
print(f"  All keys ({len(all_keys)}): {all_keys[-6:]}")
print(f"  {MONTH_KEY}: KPI {NEW_MONTH['kpi_pct']}% ({NEW_MONTH['kpi_met']}/{NEW_MONTH['kpi_eligible']}) · {NEW_MONTH['completed_total']} completions (deduped) · avg TA {NEW_MONTH['avg_ta_hrs']}h")
print(f"  LM: {NEW_MONTH['lm_completed_before']}/{NEW_MONTH['lm_total']} ({NEW_MONTH['lm_pct']}%)")
print(f"  Reviewer non-dedup total: {reviewer_total}")

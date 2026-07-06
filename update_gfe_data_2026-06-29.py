#!/usr/bin/env python3
"""
GFE Weekly Refresh — week of 2026-06-29 (Mon Jun 29 – Sun Jul 5)
Generated: 2026-07-06
Run: python3 update_gfe_data_2026-06-29.py  (from ~/Documents/GitHub/gfe)
"""
import json, os

GFE_FILE = os.path.join(os.path.dirname(__file__), "gfe_data.json")
WEEK_KEY = "2026-06-29"

NEW_WEEK = {
    "completed_total": 894, "completed_advance": 584, "completed_lm": 310,
    "reviewer_counts": {
        "breck+gfesupport@joinmoxie.com": 31,
        "courtneydanielle22@yahoo.com": 300,
        "crystal.a@spakinect.com": 31,
        "erica.n@spakinect.com": 33,
        "erin.shannon+gfe@joinmoxie.com": 139,
        "gennydamato@gmail.com": 89,
        "helen.b@spakinect.com": 61,
        "jade.s@spakinect.com": 17,
        "joseph.s@spakinect.com": 11,
        "lindsay.c@spakinect.com": 11,
        "mchenfnp@gmail.com": 28,
        "samantha.r@spakinect.com": 33,
        "stephanie.h@spakinect.com": 110,
    },
    "completed_by_group": {"all": 894, "spk_int": 724, "spakinect": 307, "spk_brk": 477, "internal": 417, "breck": 170},
    "kpi_eligible": 712, "kpi_met": 701, "kpi_missed": 11, "kpi_pct": 98.5,
    "wknd_excl": 12, "lm_total": 362, "lm_completed_before": 287, "lm_pct": 79.3,
    "avg_ta_hrs": 27.0, "max_ta_hrs": 720.0,
    "qualiphy_count": 0, "qualiphy_before": 0, "kpi_qualiphy_save": 0,
}

NEW_MISS_RECORDS = [
    {"id":None,"client":"V. Martinez","medspa":"ETHEREAL x MASHA","cat":"internal","submitted":None,"appt":"2026-07-01 15:15","appt_day":"Wed","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":None,"client":"B. Wolfe","medspa":"Level Up Wellness + IV Therapy","cat":"spk_brk","submitted":None,"appt":"2026-06-30 12:00","appt_day":"Mon","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":None,"client":"C. Wainschel","medspa":"Define Aesthetics","cat":"spk_int","submitted":None,"appt":"2026-07-01 18:00","appt_day":"Wed","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":None,"client":"A. Dehne","medspa":"ETHEREAL x MASHA","cat":"internal","submitted":None,"appt":"2026-06-30 18:00","appt_day":"Mon","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":None,"client":"A. Finley","medspa":"ETHEREAL x MASHA","cat":"internal","submitted":None,"appt":"2026-07-01 13:00","appt_day":"Wed","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":None,"client":"J. Fregoso","medspa":"Nour Beauty Aesthetics","cat":"internal","submitted":None,"appt":"2026-07-03 13:00","appt_day":"Fri","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":None,"client":"A. Martinson","medspa":"Elixir Beauty and Wellness","cat":"spakinect","submitted":None,"appt":"2026-06-30 14:30","appt_day":"Mon","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":None,"client":"Y. Escobar","medspa":"ETHEREAL x MASHA","cat":"internal","submitted":None,"appt":"2026-06-30 19:45","appt_day":"Mon","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":None,"client":"A. Reyes","medspa":"True Essence Aesthetics","cat":"spakinect","submitted":None,"appt":"2026-07-02 15:45","appt_day":"Thu","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":None,"client":"T. Miller","medspa":"Pure Bliss Aesthetics","cat":"spk_int","submitted":None,"appt":"2026-07-01 14:30","appt_day":"Wed","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":None,"client":"L. Rodriguez","medspa":"Nurse Injector Brooke","cat":"spakinect","submitted":None,"appt":"2026-07-02 12:00","appt_day":"Thu","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
]

NEW_META = {
    "refreshed": "2026-07-06", "today": "2026-07-05",
    "last_week": "2026-06-29", "this_week": "2026-07-06",
    "this_month": "2026-07", "last_month": "2026-06",
    "this_month_start": "2026-07-06",
    "last_month_start": "2026-06-01", "last_month_end": "2026-06-22",
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

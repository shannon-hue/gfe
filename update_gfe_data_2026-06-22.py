#!/usr/bin/env python3
"""
GFE Weekly Refresh — week of 2026-06-22 (Mon Jun 22 – Sun Jun 28)
Generated: 2026-06-29
Run: python3 update_gfe_data_2026-06-22.py  (from ~/Documents/GitHub/gfe)
"""
import json, os

GFE_FILE = os.path.join(os.path.dirname(__file__), "gfe_data.json")
WEEK_KEY = "2026-06-22"

NEW_WEEK = {
    "completed_total": 1207, "completed_advance": 777, "completed_lm": 430,
    "reviewer_counts": {
        "allison.h@spakinect.com": 187,
        "breck+gfesupport@joinmoxie.com": 42,
        "courtneydanielle22@yahoo.com": 452,
        "crystal.a@spakinect.com": 26,
        "erica.n@spakinect.com": 58,
        "erin.shannon+gfe@joinmoxie.com": 141,
        "gennydamato@gmail.com": 46,
        "helen.b@spakinect.com": 25,
        "jade.s@spakinect.com": 56,
        "joseph.s@spakinect.com": 18,
        "lindsay.c@spakinect.com": 20,
        "mchenfnp@gmail.com": 50,
        "samantha.r@spakinect.com": 31,
        "stephanie.h@spakinect.com": 55,
    },
    "completed_by_group": {"all": 1207, "spk_int": 1024, "spakinect": 476, "spk_brk": 659, "internal": 548, "breck": 183},
    "kpi_eligible": 810, "kpi_met": 798, "kpi_missed": 12, "kpi_pct": 98.5,
    "wknd_excl": 41, "lm_total": 398, "lm_completed_before": 350, "lm_pct": 87.9,
    "avg_ta_hrs": 18.9, "max_ta_hrs": 720.0,
    "qualiphy_count": 0, "qualiphy_before": 0, "kpi_qualiphy_save": 0,
}

NEW_MISS_RECORDS = [
    {"id":245957,"client":"C. Orozco","medspa":"Rajeunir Wellness","cat":"spakinect","submitted":"2026-06-17 14:31","appt":"2026-06-22 15:30","appt_day":"Mon","sub_day":"Wed","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":121.0,"advance_fmt":"5d 1h","finished":"2026-06-23 09:39","completed_before":False},
    {"id":246674,"client":"B. Lopez","medspa":"Rajeunir Wellness","cat":"spakinect","submitted":"2026-06-18 15:57","appt":"2026-06-23 09:00","appt_day":"Tue","sub_day":"Thu","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":113.0,"advance_fmt":"4d 17h","finished":"2026-06-23 09:20","completed_before":False},
    {"id":236892,"client":"L. Longoria","medspa":"Aida Aesthetics","cat":"spk_int","submitted":"2026-05-30 13:44","appt":"2026-06-25 18:30","appt_day":"Wed","sub_day":"Fri","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":628.8,"advance_fmt":"26d 4h","finished":None,"completed_before":False},
    {"id":246699,"client":"M. Vann","medspa":"Boon Therapeutics","cat":"spk_int","submitted":"2026-06-18 16:21","appt":"2026-06-25 16:00","appt_day":"Wed","sub_day":"Thu","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":167.6,"advance_fmt":"6d 23h","finished":None,"completed_before":False},
    {"id":248956,"client":"G. Perez","medspa":"Nature Health Medical","cat":"spk_int","submitted":"2026-06-23 19:17","appt":"2026-06-25 13:30","appt_day":"Wed","sub_day":"Mon","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":42.2,"advance_fmt":"1d 18h","finished":"2026-06-29 07:20","completed_before":False},
    {"id":220319,"client":"B. Williams","medspa":"Rejuvenate Austin","cat":"spakinect","submitted":"2026-04-29 15:38","appt":"2026-06-25 14:00","appt_day":"Wed","sub_day":"Tue","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":1366.4,"advance_fmt":"56d 22h","finished":None,"completed_before":False},
    {"id":197050,"client":"L. Mager","medspa":"Restore & Balance Medical Services","cat":"internal","submitted":"2026-03-17 19:05","appt":"2026-06-23 10:00","appt_day":"Tue","sub_day":"Mon","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":2342.9,"advance_fmt":"97d 22h","finished":None,"completed_before":False},
    {"id":248460,"client":"N. Stephanie","medspa":"Alaina Gray Aesthetics","cat":"breck","submitted":"2026-06-22 21:10","appt":"2026-06-24 15:00","appt_day":"Tue","sub_day":"Mon","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":41.8,"advance_fmt":"1d 17h","finished":None,"completed_before":False},
    {"id":249499,"client":"T. Thompson","medspa":"Old Town MedSpa","cat":"spk_int","submitted":"2026-06-24 19:30","appt":"2026-06-26 15:30","appt_day":"Thu","sub_day":"Tue","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":44.0,"advance_fmt":"1d 20h","finished":None,"completed_before":False},
    {"id":249866,"client":"G. Hakobyan","medspa":"Graise Aesthetics","cat":"spk_int","submitted":"2026-06-25 13:37","appt":"2026-06-26 14:00","appt_day":"Thu","sub_day":"Wed","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":24.4,"advance_fmt":"1d 0h","finished":None,"completed_before":False},
    {"id":248259,"client":"S. Rothkirch","medspa":"Elora Aesthetics","cat":"spakinect","submitted":"2026-06-22 15:56","appt":"2026-06-25 15:00","appt_day":"Wed","sub_day":"Mon","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":71.1,"advance_fmt":"2d 23h","finished":None,"completed_before":False},
    {"id":226677,"client":"M. Fabbio","medspa":"Rejuvenate Austin","cat":"spakinect","submitted":"2026-05-11 10:29","appt":"2026-06-23 09:45","appt_day":"Tue","sub_day":"Sun","is_weekend_appt":False,"is_weekend_sub":True,"hrs_advance":1031.3,"advance_fmt":"42d 23h","finished":None,"completed_before":False},
]

NEW_META = {
    "refreshed": "2026-06-29", "today": "2026-06-28",
    "last_week": "2026-06-22", "this_week": "2026-06-29",
    "this_month": "2026-06", "last_month": "2026-05",
    "this_month_start": "2026-06-01",
    "last_month_start": "2026-05-05", "last_month_end": "2026-05-25",
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

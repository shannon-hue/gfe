#!/usr/bin/env python3
"""
GFE Weekly Refresh — week of 2026-06-15 (Mon Jun 15 – Sun Jun 21)
Generated: 2026-06-22
Run: python3 update_gfe_data_2026-06-15.py  (from ~/Documents/GitHub/gfe)
"""
import json, os

GFE_FILE = os.path.join(os.path.dirname(__file__), "gfe_data.json")
WEEK_KEY = "2026-06-15"

NEW_WEEK = {
    "completed_total": 1028, "completed_advance": 694, "completed_lm": 330,
    "reviewer_counts": {
        "allison.h@spakinect.com": 129, "breck+gfesupport@joinmoxie.com": 12,
        "courtneydanielle22@yahoo.com": 421, "crystal.a@spakinect.com": 22,
        "erica.n@spakinect.com": 11, "erin.shannon+gfe@joinmoxie.com": 127,
        "gennydamato@gmail.com": 48, "helen.b@spakinect.com": 55,
        "ivy.c@spakinect.com": 12, "jade.s@spakinect.com": 33,
        "joseph.s@spakinect.com": 58, "lindsay.c@spakinect.com": 26,
        "mchenfnp@gmail.com": 39, "samantha.r@spakinect.com": 35,
    },
    "completed_by_group": {"all": 1028, "spk_int": 889, "spakinect": 381, "spk_brk": 520, "internal": 508, "breck": 139},
    "kpi_eligible": 875, "kpi_met": 862, "kpi_missed": 13, "kpi_pct": 98.5,
    "wknd_excl": 47, "lm_total": 498, "lm_completed_before": 430, "lm_pct": 86.3,
    "avg_ta_hrs": 26.0, "max_ta_hrs": 720.0,
    "qualiphy_count": 0, "qualiphy_before": 0, "kpi_qualiphy_save": 0,
}

NEW_MISS_RECORDS = [
    {"id":244238,"client":"H. Teaford","medspa":"Define Aesthetics","cat":"spk_int","submitted":"2026-06-14 01:34","appt":"2026-06-15 12:00","appt_day":"Mon","sub_day":"Sun","is_weekend_appt":False,"is_weekend_sub":True,"hrs_advance":34.4,"advance_fmt":"1d 10h","finished":None,"completed_before":False},
    {"id":235609,"client":"D. Davis","medspa":"Drip & Glow Aesthetics","cat":"spk_brk","submitted":"2026-05-28 06:58","appt":"2026-06-15 18:00","appt_day":"Mon","sub_day":"Thu","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":443.0,"advance_fmt":"18d 11h","finished":None,"completed_before":False},
    {"id":228594,"client":"C. Proulxfini","medspa":"3Eleven Aesthetics","cat":"spk_int","submitted":"2026-05-14 00:30","appt":"2026-06-15 20:30","appt_day":"Mon","sub_day":"Thu","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":788.0,"advance_fmt":"32d 19h","finished":None,"completed_before":False},
    {"id":237281,"client":"E. Gielda","medspa":"Youngblood Aesthetics","cat":"spakinect","submitted":"2026-05-31 18:23","appt":"2026-06-16 10:00","appt_day":"Tue","sub_day":"Sun","is_weekend_appt":False,"is_weekend_sub":True,"hrs_advance":375.6,"advance_fmt":"15d 15h","finished":None,"completed_before":False},
    {"id":239498,"client":"M. Robinson","medspa":"Elisa Grace Medspa & Boutique","cat":"spk_brk","submitted":"2026-06-04 13:51","appt":"2026-06-16 13:15","appt_day":"Tue","sub_day":"Thu","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":287.4,"advance_fmt":"11d 23h","finished":None,"completed_before":False},
    {"id":241732,"client":"S. Blue","medspa":"Alaina Gray Aesthetics","cat":"breck","submitted":"2026-06-09 12:39","appt":"2026-06-16 16:00","appt_day":"Tue","sub_day":"Tue","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":171.3,"advance_fmt":"7d 3h","finished":None,"completed_before":False},
    {"id":242214,"client":"C. Saylor","medspa":"Salena Dodman Aesthetics","cat":"spk_int","submitted":"2026-06-10 08:41","appt":"2026-06-17 16:15","appt_day":"Wed","sub_day":"Wed","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":175.6,"advance_fmt":"7d 7h","finished":None,"completed_before":False},
    {"id":244785,"client":"B. Karm","medspa":"Tox & Tonic - Queen Creek","cat":"spk_int","submitted":"2026-06-15 14:49","appt":"2026-06-18 15:00","appt_day":"Thu","sub_day":"Mon","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":72.2,"advance_fmt":"3d 0h","finished":None,"completed_before":False},
    {"id":246175,"client":"M. Brazell","medspa":"Milay Aesthetics","cat":"spk_int","submitted":"2026-06-17 18:43","appt":"2026-06-18 18:30","appt_day":"Thu","sub_day":"Wed","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":23.8,"advance_fmt":"0d 23h","finished":None,"completed_before":False},
    {"id":246179,"client":"M. Olivares","medspa":"Nature Health Medical","cat":"spk_int","submitted":"2026-06-17 18:46","appt":"2026-06-19 12:00","appt_day":"Fri","sub_day":"Wed","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":41.2,"advance_fmt":"1d 17h","finished":None,"completed_before":False},
    {"id":246564,"client":"L. Evans","medspa":"Rejuvenate Austin","cat":"spakinect","submitted":"2026-06-18 13:38","appt":"2026-06-19 15:00","appt_day":"Fri","sub_day":"Thu","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":25.4,"advance_fmt":"1d 1h","finished":None,"completed_before":False},
    {"id":246512,"client":"T. Alegria","medspa":"Beauty Rx Aesthetics","cat":"spakinect","submitted":"2026-06-18 12:48","appt":"2026-06-19 18:00","appt_day":"Fri","sub_day":"Thu","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":29.2,"advance_fmt":"1d 5h","finished":None,"completed_before":False},
    {"id":246590,"client":"J. Williams","medspa":"Thrive Concierge","cat":"spk_int","submitted":"2026-06-18 14:04","appt":"2026-06-19 21:00","appt_day":"Fri","sub_day":"Thu","is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":30.9,"advance_fmt":"1d 6h","finished":None,"completed_before":False},
]

NEW_META = {
    "refreshed": "2026-06-22", "today": "2026-06-21",
    "last_week": "2026-06-15", "this_week": "2026-06-22",
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

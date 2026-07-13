#!/usr/bin/env python3
"""
GFE Weekly Refresh — week of 2026-07-06 (Mon Jul 6 – Sun Jul 12)
Generated: 2026-07-13
Includes: aaralsip@gmail.com (internal, active from Jul 1), 2h grace period on KPI
Run: python3 update_gfe_data_2026-07-06.py  (from ~/Documents/GitHub/gfe)
"""
import json, os

GFE_FILE = os.path.join(os.path.dirname(__file__), "gfe_data.json")
WEEK_KEY = "2026-07-06"

NEW_WEEK = {
    "completed_total": 993, "completed_advance": 637, "completed_lm": 356,
    "reviewer_counts": {
        "aaralsip@gmail.com": 47,
        "allison.h@spakinect.com": 67,
        "breck+gfesupport@joinmoxie.com": 23,
        "erica.n@spakinect.com": 59,
        "erin.shannon+gfe@joinmoxie.com": 189,
        "gennydamato@gmail.com": 180,
        "helen.b@spakinect.com": 114,
        "ivy.c@spakinect.com": 61,
        "jade.s@spakinect.com": 22,
        "joseph.s@spakinect.com": 20,
        "mchenfnp@gmail.com": 80,
        "samantha.r@spakinect.com": 36,
        "stephanie.h@spakinect.com": 95,
    },
    "completed_by_group": {"all": 993, "spk_int": 781, "spakinect": 474, "spk_brk": 686, "internal": 307, "breck": 212},
    "kpi_eligible": 760, "kpi_met": 735, "kpi_missed": 25, "kpi_pct": 96.7,
    "wknd_excl": 23, "lm_total": 372, "lm_completed_before": 309, "lm_pct": 83.1,
    "avg_ta_hrs": 30.7, "max_ta_hrs": 720.0,
    "qualiphy_count": 0, "qualiphy_before": 0, "kpi_qualiphy_save": 0,
}

NEW_MISS_RECORDS = [
    {"id":251608,"client":"A. Zivkovic","medspa":"Renova Med Spa","cat":"spakinect","submitted":None,"appt":"2026-07-11 11:30","appt_day":"Sat","sub_day":None,"is_weekend_appt":True,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":251107,"client":"C. Mcdonald","medspa":"Milay Aesthetics","cat":"spk_int","submitted":None,"appt":"2026-07-09 12:00","appt_day":"Thu","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":250736,"client":"M. Bonnette","medspa":"FAB Medical Aesthetics","cat":"internal","submitted":None,"appt":"2026-07-09 13:00","appt_day":"Thu","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":250488,"client":"F. Martinez","medspa":"Re-Glo Aesthetics","cat":"spk_int","submitted":None,"appt":"2026-07-08 13:00","appt_day":"Wed","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":251382,"client":"J. Pascarella","medspa":"Self Aesthetics & Wellness","cat":"spk_int","submitted":None,"appt":"2026-07-10 08:30","appt_day":"Thu","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":249936,"client":"M. Knizacky","medspa":"Salena Dodman Aesthetics","cat":"spk_int","submitted":None,"appt":"2026-07-06 14:00","appt_day":"Mon","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":249888,"client":"A. Khanuja","medspa":"WOW Health & Beauty","cat":"spk_int","submitted":None,"appt":"2026-07-06 11:00","appt_day":"Mon","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":251396,"client":"T. Cotton","medspa":"Restore & Balance Medical Services","cat":"internal","submitted":None,"appt":"2026-07-10 11:30","appt_day":"Thu","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":252228,"client":"E. Cuevas","medspa":"Angel Face Aesthetics","cat":"internal","submitted":None,"appt":"2026-07-12 15:30","appt_day":"Sat","sub_day":None,"is_weekend_appt":True,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":249888,"client":"V. Ordonez","medspa":"Palace Med Spa","cat":"internal","submitted":None,"appt":"2026-07-06 14:00","appt_day":"Mon","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":252170,"client":"S. Baur","medspa":"Rych Aesthetics","cat":"internal","submitted":None,"appt":"2026-07-12 15:00","appt_day":"Sat","sub_day":None,"is_weekend_appt":True,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":251138,"client":"K. Holmes","medspa":"Kajal Luxe Med Spa","cat":"internal","submitted":None,"appt":"2026-07-09 20:45","appt_day":"Thu","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":250557,"client":"R. Shah","medspa":"Lifted Aesthetics","cat":"spk_int","submitted":None,"appt":"2026-07-08 12:00","appt_day":"Wed","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":251450,"client":"C. Cornell","medspa":"Paradise Medspa & Wellness","cat":"spk_int","submitted":None,"appt":"2026-07-10 13:15","appt_day":"Thu","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":250498,"client":"R. Smith","medspa":"LOLA's Med Spa","cat":"spk_brk","submitted":None,"appt":"2026-07-08 10:00","appt_day":"Wed","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":249862,"client":"M. Harrell","medspa":"Level Up Wellness + IV Therapy","cat":"spk_brk","submitted":None,"appt":"2026-07-06 13:45","appt_day":"Mon","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":249896,"client":"A. Chapman","medspa":"Salena Dodman Aesthetics","cat":"spk_int","submitted":None,"appt":"2026-07-06 09:00","appt_day":"Mon","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":251088,"client":"M. Greene","medspa":"Palace Med Spa","cat":"internal","submitted":None,"appt":"2026-07-09 15:45","appt_day":"Thu","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":251647,"client":"L. Akhverdyan","medspa":"KatherineO-RN","cat":"internal","submitted":None,"appt":"2026-07-11 16:00","appt_day":"Sat","sub_day":None,"is_weekend_appt":True,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":251372,"client":"M. Young","medspa":"Restore & Balance Medical Services","cat":"internal","submitted":None,"appt":"2026-07-09 14:45","appt_day":"Thu","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":251703,"client":"J. Pastor","medspa":"IKontura Aesthetics & Wellness","cat":"internal","submitted":None,"appt":"2026-07-11 18:00","appt_day":"Sat","sub_day":None,"is_weekend_appt":True,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":250700,"client":"L. Hickey-Woodcook","medspa":"You Beauty & Aesthetics","cat":"internal","submitted":None,"appt":"2026-07-08 19:00","appt_day":"Wed","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":250088,"client":"V. Chavez","medspa":"Serene Skin Studio","cat":"spk_int","submitted":None,"appt":"2026-07-07 21:00","appt_day":"Tue","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":251122,"client":"M. Maghathe","medspa":"Raw Aesthetic","cat":"spk_int","submitted":None,"appt":"2026-07-09 21:15","appt_day":"Thu","sub_day":None,"is_weekend_appt":False,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":None,"completed_before":False},
    {"id":251819,"client":"C. Magevski","medspa":"Rajeunir Wellness","cat":"spakinect","submitted":None,"appt":"2026-07-11 17:30","appt_day":"Sat","sub_day":None,"is_weekend_appt":True,"is_weekend_sub":False,"hrs_advance":None,"advance_fmt":None,"finished":"2026-07-12 16:05","completed_before":False},
]

NEW_META = {
    "refreshed": "2026-07-13", "today": "2026-07-12",
    "last_week": "2026-07-06", "this_week": "2026-07-13",
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

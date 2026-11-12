#!/usr/bin/env python3
"""Generates one guide page per bank Pista ships a reading pack for.

Usage: tools/gen_guides.py ../pista
Reads feature/sms-ingestion/src/main/assets/rule_packs/*.json (the app's bundled packs) and writes
pista/banks/<slug>/index.md plus pista/banks/index.md. Re-run after adding or changing a pack.
Only says what the pack really reads: payment kinds come from the pack's rule ids.
"""
import json, pathlib, sys

NAMES = {
    "aubank": "AU Small Finance Bank", "axis": "Axis Bank", "bob": "Bank of Baroda", "federal": "Federal Bank",
    "hdfc": "HDFC Bank", "icici": "ICICI Bank", "idfcfb": "IDFC FIRST Bank", "indusind": "IndusInd Bank",
    "kotak": "Kotak Mahindra Bank", "pnb": "Punjab National Bank", "rblbank": "RBL Bank",
    "rmgb": "Rajasthan Marudhara Gramin Bank", "sbi": "State Bank of India", "sbmbank": "SBM Bank India",
    "unionbank": "Union Bank of India", "yesbank": "Yes Bank",
}
# rule-id fragment -> what the user would call it (order = order shown)
KINDS = [
    (("upi", "vpa"), "UPI payments"),
    (("cc", "card"), "Credit and debit card spends"),
    (("neft", "imps", "ft"), "NEFT and IMPS transfers"),
    (("atm",), "ATM withdrawals"),
    (("pos",), "Card swipes at shops (POS)"),
    (("fastag",), "FASTag tolls and recharges"),
    (("emi",), "EMI debits"),
    (("refund",), "Card refunds"),
    (("salary", "credit", "cr"), "Money received, including salary credits"),
]

def kinds(pack):
    # Whole hyphen-separated words of the rule ids ("deposit" must not read as "pos").
    words = {w for r in pack.get("rules", []) for w in r.get("id", "").split("-")}
    return [label for frags, label in KINDS if words & set(frags)]

def page(slug, name, pack):
    found = kinds(pack)
    senders = sorted({s.split("-")[-1] for s in pack.get("senders", [])})
    lines = "\n".join(f"- {k}" for k in found) if found else "- Payments Pista's smart reader recognises (amount, merchant and date)"
    return f"""---
app: pista
title: "Track {name} spending automatically"
eyebrow: "Pista: Expense Tracker"
lede: "Pista reads your {name} SMS alerts on your phone and turns them into a list of expenses. No bank login, no ads, no loan offers."
root: "../../../"
toc: false
---
## How it works with {name}

When {name} sends you an SMS alert for a payment, Pista reads it on your phone and shows the payment in its Inbox with the amount, the merchant and the date. You swipe right to add it or left to ignore it. Confirm a merchant twice and Pista files it for you from then on.

## What Pista reads from {name} alerts

{lines}

Pista recognises {name} alerts sent from these SMS sender names: {", ".join(senders)}. One-time passwords, promotional messages and personal SMS are never stored.

## Got a {name} message Pista could not read?

Banks change their message formats. If an alert is missed, open **Help Pista read** in the Inbox, tap the amount in the message once, and Pista learns that format on your phone. New formats also reach the app without an update.

## Private by design

- Your SMS are read on your phone and are never uploaded.
- Pista never asks for your {name} net-banking login, card number or UPI PIN.
- No ads and no loan offers.

<p><a class="button" href="https://play.google.com/store/apps/details?id=io.pennytrail.app">Get Pista on Google Play</a></p>

Pista is not affiliated with {name}. Make sure SMS alerts are turned on for your account in the bank's own app.
"""

def main():
    app = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "../pista")
    packs = sorted((app / "feature/sms-ingestion/src/main/assets/rule_packs").glob("in.*.json"))
    out = pathlib.Path(__file__).resolve().parent.parent / "pista" / "banks"
    rows = []
    for f in packs:
        slug = f.name.split(".")[1]
        name = NAMES.get(slug)
        if not name:
            print(f"skip {f.name}: add its display name to NAMES"); continue
        pack = json.loads(f.read_text())
        d = out / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.md").write_text(page(slug, name, pack))
        rows.append((slug, name))
    items = "\n".join(f'<li><a class="card-link" href="{s}/"><strong>{n}</strong><span>What Pista reads from {n} SMS alerts.</span><em>Read more →</em></a></li>' for s, n in rows)
    (out / "index.md").write_text(f"""---
app: pista
title: "Banks Pista reads"
eyebrow: "Pista: Expense Tracker"
lede: "Pista tracks your spending from bank SMS alerts. These banks are supported out of the box, and Pista can learn others."
root: "../../"
toc: false
---
<ul class="cards">
{items}
</ul>

Your bank is not listed? Pista's smart reader handles many other banks, and you can teach it any message it misses by tapping the amount once.

<p><a class="button" href="https://play.google.com/store/apps/details?id=io.pennytrail.app">Get Pista on Google Play</a></p>
""")
    print(f"wrote {len(rows)} bank pages to {out}")

if __name__ == "__main__":
    main()

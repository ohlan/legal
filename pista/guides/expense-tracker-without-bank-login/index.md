---
app: pista
title: "An expense tracker without bank login"
eyebrow: "Pista: Expense Tracker"
lede: "You can track every UPI and card payment automatically without linking a bank account or sharing a password."
root: "../../../"
toc: false
---
## Three ways apps track your spending

1. **Bank linking.** You approve access to your accounts and the app pulls your statements to its servers. It is automatic, but your full transaction history leaves your phone.
2. **Typing it in.** Private, but most people stop after two weeks.
3. **Reading bank SMS on the phone.** Your bank already texts you for each payment. An app can read those alerts on the device and build your expense list without any login.

Pista uses the third way.

## What Pista needs, and what it never asks for

- **Needs:** permission to read SMS, so it can find bank alerts. It only keeps messages from bank sender names; personal SMS and one-time passwords are not stored.
- **Never asks for:** net-banking user ID or password, card number, CVV, UPI PIN, or account linking.

## Where your data lives

Your transactions are stored on your phone. SMS are read on the device and never uploaded. Backup is optional and goes to your own Google Drive, encrypted with a passphrase only you know. The details are in the [privacy policy](../../privacy/).

## Does it catch everything?

It catches every payment your bank sends an SMS for. Some banks skip SMS for very small UPI payments; you can add those by hand in two taps. If a message format is new, tap the amount once and Pista learns it.

See the [banks Pista reads](../../banks/).

<p><a class="button" href="https://play.google.com/store/apps/details?id=io.pennytrail.app">Get Pista on Google Play</a></p>

---
app: pista
title: "Pista help and FAQ"
eyebrow: "Pista: Expense Tracker"
lede: "Short answers to the questions people ask most. If yours isn't here, send it from Settings → Send feedback."
root: "../../"
---

## Getting started

### How does Pista know what I spent?

Your bank sends an SMS when money moves. Pista reads that message on your phone, picks out the amount, the merchant, the date and the account, and puts it in the **Inbox** with a suggested category. Swipe right to add it, left to ignore it, or tap to change anything first.

### Do I have to give my bank login or link an account?

No. Pista never asks for a bank login, card number, PIN or OTP, and it never connects to your bank. It only reads the alert messages your bank already sends you.

### Can I use Pista without SMS access?

Yes. Add expenses by hand with the **+** button, or import a statement from Settings → Data. You can turn SMS tracking on later from Settings.

### Which banks work?

See the [banks Pista reads](../banks/). A bank that isn't listed often still works through Pista's general reader, and you can teach Pista a message it didn't understand (see below).

## Privacy

### Does my data leave my phone?

Your transactions, budgets, goals and messages stay on your phone. Nothing is uploaded to a Pista server. The few things that do leave the phone, such as an optional backup to your own Google Drive, are listed in the [privacy policy](../privacy/).

### Does Pista read my personal messages or OTPs?

Messages from phone numbers (friends, family) are never read as transactions and are not stored. One-time passwords, payment requests and failed payments are recognised and left out.

### Is Pista AI private?

Yes. Pista AI runs on your phone. Your questions and your money data are not sent anywhere to answer them. That is also why it needs a phone with enough memory and a one-time model download.

## The Inbox and automatic tracking

### A payment is missing. Why?

The usual reasons, most likely first:

1. **Your bank didn't send an SMS.** Many UPI payments only show a notification in the payment app. Turn on Settings → SMS tracking → **Catch UPI app payments** to pick those up from Google Pay, PhonePe, Paytm and BHIM. They always wait for your review.
2. **Your phone stopped Pista in the background.** Some phones (Xiaomi, Vivo, Oppo, Realme, OnePlus, Samsung) do this to save battery. Open Settings → SMS tracking → **Keep Pista running** and follow the steps for your phone. Pista also catches up each time you open it.
3. **The message is in a format Pista doesn't know yet.** Open the Inbox and tap **Help Pista read**. Pick the message, tap the amount in it, and Pista learns that format on your phone and reads the sender's other messages too.

### How does Pista start adding things by itself?

Confirm the same merchant with the same category **twice in a row** and Pista adds that merchant's future payments for you. You can see and change every such merchant in Settings → **Merchants Pista knows**. Payments in a foreign currency are never added automatically.

### Pista added something to the wrong category. How do I fix it?

Open the transaction and change the category. Pista offers to update that merchant's other transactions too. If one merchant really belongs in two categories, Pista stops adding it automatically and asks you each time.

### Why is a transfer or an investment "not counted"?

Moving money between your own accounts isn't spending, and neither is money you invest. Pista keeps both out of your spending totals so the numbers show what you actually spent. You can choose which categories are left out in Settings → Categories.

### I paid my credit card bill. Why isn't that an expense?

The purchases on the card were already counted when you made them. Counting the bill payment as well would count them twice, so Pista records it as a transfer and marks the card bill as paid.

## Budgets, goals and insights

### What is "safe to spend"?

What is left of your budget for the month, divided by the days left including today. It tells you how much you can spend each day and still finish the month inside your budget.

### Why does "this month" compare with only part of last month?

Twelve days of this month against all of last month would always look like a big drop. Pista compares the same days of both months, so the comparison is fair.

### What is the lighter part of the bar for this month?

An estimate of where the month will end if you spend as you usually do, including bills that are still due. It is a forecast, not a fact, and it never changes the totals of what you have actually spent.

## Pista AI

### Why can't I use Pista AI on my phone?

The model runs on the phone and needs about 6 GB of memory or more. On phones with less, Pista still shows exact insights and check-ins; only the chat needs the model.

### Can the AI be wrong?

It can word things badly, so Pista checks every figure in an answer against your own data and removes any sentence whose number doesn't match. Pista AI does not give investment, loan, insurance or tax advice.

## Backup and moving phones

### How do I back up or move to a new phone?

Sign in with Google in Settings and turn on backup. The backup goes to a private app folder in **your own** Google Drive, and you can protect it with a passphrase. On the new phone, sign in with the same account and choose Restore.

### I forgot my backup passphrase. Can you recover it?

No. The passphrase never leaves your phone and Pista has no copy, so an encrypted backup can't be opened without it. You can make a new backup with a new passphrase from the phone that still has your data.

### How do I delete everything?

Settings → Danger zone → **Wipe local data** removes your transactions, accounts, budgets, goals and settings from the phone. Backups in your Google Drive are yours: delete them from Drive's settings under "Manage apps".

## Plans and billing

### What is free and what is Pro?

The Basic plan covers tracking: bank SMS reading, the Inbox, insights, recurring bills, the Spend widget, a few budgets, a savings goal and weekly backup. Pro adds Pista AI, period comparisons, PDF and CSV reports, the Goals widget, unlimited budgets and goals, daily backup and extra themes. The current list and prices are on the upgrade screen in the app.

### How does the trial work?

Signing in with Google starts 30 days of full access, once per Google account. Nothing is charged, and no card is needed. When it ends you stay on Basic unless you choose a plan.

### How do I cancel or get a refund?

Subscriptions are managed by Google Play: open Play Store → your profile → Payments and subscriptions. Refunds follow Google Play's policy; see the [terms of service](../terms/).

## Splitting with friends

### Does Pista message my friends?

No. Pista never contacts anyone. "Ask" opens your phone's share sheet with a message you can edit and send yourself from any app.

### What is the pay link in the "Ask" message?

A link that opens a page showing your UPI ID and the amount, with a button for the friend's UPI app. The details live only in the link itself and are never sent to Pista. Always check the name and UPI ID before paying.

<p><a class="button" href="https://play.google.com/store/apps/details?id=io.pennytrail.app">Get Pista on Google Play</a></p>

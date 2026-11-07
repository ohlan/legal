---
title: "Pista Privacy Policy"
eyebrow: "Pista · Legal"
lede: "How Pista handles your data. Most of it never leaves your phone."
effective: "November 7, 2026"
nav: privacy
root: "../"
---
Pista ("Pista: Expense Tracker", formerly PennyTrail) is a personal expense tracking app for Android. This policy explains what data the app accesses, how it is used, when it may leave your device, and how you can control it. It should be read together with the [Pista Terms of Service](terms/).

## Summary

- Pista stores your expense data locally on your device.
- SMS-based transaction tracking is optional and requires your explicit permission. SMS messages are read and parsed on your device.
- The AI assistant ("Ask Pista") and AI insights run entirely on your device. Your questions and financial data are not sent to any AI server.
- Google sign-in and Google Drive backup are optional and use your own Google account.
- Pista uses Google Firebase for crash reports, app usage analytics and remote settings. These never include your SMS messages, transactions, amounts or merchant names.
- If you turn on "Help improve SMS reading" (off by default), or report a missed SMS, only an anonymised message layout is shared — never amounts, names, account numbers or the original message.
- Pista does not sell your personal data and does not use your SMS or financial data for advertising.
- Pista is not a bank, broker, tax advisor, or financial advisor. Insights, AI answers and classifications are informational only.

## Data We Access Or Store

Depending on which features you use, Pista may access or store the following data.

### Expense And Financial Data

Transactions, amounts, dates, currencies and exchange rates, merchant or vendor names, categories, accounts or wallet labels, budgets, savings goals, recurring expense rules, notes, and related preferences.

This data is stored on your device and is used to show your expense history, budgets, goals, reminders, widgets, reports and spending insights.

### SMS Data

If you enable SMS auto-tracking, Pista requests access to bank and transaction SMS messages through Android SMS permissions. The app may process and store the SMS sender, message body, received time, parsing status, matched rule information, and transaction drafts.

This data is used only to detect financial transactions, queue drafts in Inbox, learn your merchant categories on your device, avoid duplicate imports, and let you review the original message behind a transaction. SMS processing happens on your device.

SMS access is optional. If you do not enable it, you can still use Pista by adding transactions manually.

### Receipt Photos And Attachments

If you attach receipt photos, Pista stores those images in app-private storage on your device. Receipt images may be included in Drive backups if Drive backup is enabled.

### On-Device AI

Pista Pro includes an AI assistant and AI-written insights powered by a language model that runs on your device. The model file is downloaded from Google Play the first time you use these features. Your questions, the answers, and the spending data used to produce them are processed on your device and are not sent to Pista or to any AI provider. Recent conversation turns are kept in app memory only to answer follow-up questions.

### Google Account Data

If you sign in with Google, Pista receives your Google account email address and display name through Google sign-in (Credential Manager). They are stored locally on your device and used to show your profile, to start your Pro trial, to restore purchases, and to connect Google Drive backup if you enable it.

Pista checks on your device whether your email is on a complimentary-access list (for example, Founders Circle members). Your email is not sent to Pista for this check.

Each Google account can use the free trial once. When your trial starts, Pista stores a one-way hash of your Google account email (a fixed-length code from which the email cannot be read back) in our Google Cloud Firestore database, together with the app version. No email address, name, date, device identifier or financial data is stored with it. The app can only add such a code, never read, change or delete one; it only learns whether the code already exists. We keep these codes for as long as we offer the free trial.

Pista also stores a small record in your own Google Drive AppData folder with your trial start date and any launch-offer perks, so a reinstall can resume your trial and perks. This record contains no financial data.

### Google Drive Backup Data

If you enable Drive backup, Pista uploads backup snapshots to your Google Drive AppData folder. Snapshots may include your local database (including SMS-derived data), receipt attachments, and app settings. This folder is managed by Google and is not visible as a normal Drive file.

### Purchases

Pro subscriptions are sold through Google Play Billing. Google processes your payment. Pista receives only the purchase status, product, and purchase token needed to unlock Pro features; it never receives your card or payment details.

### Diagnostics And Usage Analytics

Pista uses Firebase Crashlytics to collect crash reports: stack traces, app version, device model, operating system version, and a Firebase installation identifier. Crash reports are used to fix bugs and do not include SMS bodies or transaction details.

Pista uses Google Analytics for Firebase to understand how features are used, for example when a trial starts, the paywall is viewed, a purchase completes, an export is made, or a goal is created. Events may include simple values such as the plan, the export format, or a goal milestone percentage. They never include SMS content, transaction amounts, merchant names, or your notes. Firebase Analytics collects an app instance identifier, device and app information, approximate location derived from your IP address, and, where available and allowed by your device settings, your device's advertising ID. Pista shows no ads and does not use this data for advertising. You can reset or delete your advertising ID in Android settings.

### Feedback And Missed-SMS Reports

If you send feedback from Settings, Pista sends your message, the topic you chose, and — only if you leave it attached — a diagnostics line (app version, Android version, device manufacturer and model, and language) to our Google Cloud Firestore database. If you enter a reply email, that is sent too so we can answer you. If in-app sending is unavailable, the app opens your email app instead, and your email provider processes that message.

If you report a missed SMS, the message is masked on your device before sending: every digit is replaced with "#", and links, email addresses and UPI IDs are removed. Only the masked text (up to 600 characters), the bank's sender header (for example "HDFCBK", never a phone number), and the app version are sent. No account, email, or device identifier is attached.

Please do not include sensitive financial information in feedback messages.

## Permissions We Request

Pista may request these Android permissions:

- SMS (read and receive): to detect bank transaction SMS when you enable SMS auto-tracking.
- Notifications: to show reminders, inbox and budget alerts, and summaries you enable.
- Camera: to capture receipt photos when you choose to attach one.
- Internet and network state: for Google sign-in, Drive backup, purchases, AI model download, Firebase services, and the optional sharing features described above.
- Exact alarms: to deliver reminders at the time you choose.
- Run at startup and foreground service: to reschedule reminders after a restart and finish backups and SMS imports reliably.
- Google Play Billing: to sell Pro subscriptions.
- Advertising ID (added by Google Analytics for Firebase): see Diagnostics And Usage Analytics.

Permission use is limited to the app features described in this policy.

## How We Use Data

Pista uses data to:

- create, edit, restore, and delete expense records;
- parse SMS messages into transaction drafts and learn merchant categories on your device;
- detect transfers, investments, recurring payments, subscriptions, and spending patterns;
- show budgets, goals, widgets, insights, AI answers, and reports;
- send reminders and alerts you enable;
- create optional backups in your Google Drive AppData folder;
- manage your Pro trial and subscription;
- diagnose crashes, understand feature usage, and improve the app;
- respond to feedback and improve support for more banks' SMS formats.

Pista does not use your SMS or financial data for advertising, profiling for ads, or sale to third parties.

## When Data Leaves Your Device

Most features work entirely on your device. Data leaves your device only in these cases:

- **Google sign-in:** Google authenticates you and shares your email and name with the app.
- **Google Drive backup (optional):** backup snapshots and the small trial record are uploaded to your own Google Drive AppData folder.
- **Free trial:** a one-way hash of your Google account email is sent to Google Cloud Firestore to record that the account has used its trial, as described above.
- **Purchases:** handled by Google Play.
- **Firebase Crashlytics and Analytics:** crash reports and usage events as described above are sent to Google.
- **Firebase Remote Config:** the app downloads feature settings and parsing-rule updates. It does not upload your SMS or transactions to do this.
- **AI model download:** the on-device model is downloaded from Google Play. Your data is not uploaded.
- **Feedback and missed-SMS reports:** sent to Google Cloud Firestore only when you choose to send them.
- **"Help improve SMS reading" (off by default):** each message format you teach Pista in the Inbox is anonymised on your device and sent to Google Cloud Firestore. Only the bank's public sender header (for example "HDFCBK"), the fixed banking wording of the message with every amount, merchant, name, account digit, date, time and reference number replaced by a placeholder (for example "{amount}"), whether it was money spent or received, and the app version are sent. Messages you have not taught are never shared. No account, email, device identifier or transaction data is attached. We use these formats only to add support for more banks to Pista's built-in parsing rules. You can turn this off at any time in Settings or on the teach screen; formats already shared cannot be linked back to you and so cannot be deleted individually.
- **Exports and sharing:** CSV or PDF exports leave the app only when you share or save them.

Free-trial records, anonymised SMS formats, missed-SMS reports, and feedback are stored in Google Cloud Firestore in a write-only database: the app can create entries but cannot read them back. Feedback is kept only as long as needed to answer and act on it.

## Backup And Sync

Drive backup is optional. If enabled, Pista can protect snapshots with a passphrase before upload. Passphrase protection is recommended because the backup can include financial records, receipt attachments, and SMS-derived app data. The passphrase is stored on your device only for automatic backups, protected by Android Keystore and Google Tink, and must be entered again to restore after reinstalling or on a new device.

You may also back up without a passphrase. This is easier to restore, but the backup is then protected only by your Google account.

Pista keeps a limited number of recent backup snapshots and deletes older ones when backup cleanup runs.

Disconnecting your Google account or wiping local data does not delete snapshots already uploaded to Google Drive AppData. To remove them, open your Google Drive settings on the web, go to "Manage apps", find Pista, and choose "Delete hidden app data".

## Data Retention And Deletion

Local transactions, SMS-derived drafts, settings, accounts, budgets, goals, categories, recurring rules, and attachments remain on your device until you delete them, wipe local data, uninstall the app, or a cleanup feature removes them.

Deleted transactions stay in Trash for 30 days, after which they are permanently deleted automatically, unless you restore or delete them sooner.

Settings includes a "Wipe local data" option that deletes local app data on the device. It does not delete Google Drive backups that were already uploaded.

If you disable SMS auto-tracking, Pista stops future SMS ingestion. Existing SMS-derived records remain until you delete them or wipe local data.

Crash and analytics data are retained by Google according to Firebase's data retention settings for the app.

## Security

Pista relies on Android app-private storage and the Android security model to protect local data from other apps. Network connections use HTTPS. Optional Drive backups are passphrase-encrypted before upload when you choose passphrase mode.

Home-screen widgets show spending and goal amounts on your home screen, where anyone with access to your unlocked phone can see them. Remove the widgets if you prefer.

No app or system can guarantee absolute security. Keep your device protected with a screen lock and install apps only from trusted sources.

## Children

Pista is intended for adults managing personal finances. It is not directed to children under 18. If you believe a child has provided personal data through the app, contact us so we can help remove it where possible.

## Your Rights And Choices

Depending on where you live (for example under the GDPR, UK GDPR, CCPA, or India's Digital Personal Data Protection Act), you may have rights to access, correct, delete, or port your personal data, to withdraw consent, and to complain to a data protection authority. Because Pista is local-first, most of your data is under your direct control. You can:

- view and edit your data at any time in the app;
- export your transactions to CSV or PDF;
- delete individual records, or wipe all local data with "Wipe local data" in Settings;
- use Pista without SMS auto-tracking, Google sign-in, or Drive backup;
- deny or revoke SMS, notification, or camera permissions in Android settings;
- disconnect Google Drive backup and delete its hidden app data from Google Drive;
- turn "Help improve SMS reading" on or off at any time;
- reset or delete your advertising ID in Android settings;
- contact us to ask about, or request deletion of, feedback you sent us.

Anonymised SMS formats and missed-SMS reports contain no identifier, so we cannot find or delete a specific person's entries. If you ask us to delete your free-trial record, we can compute its code from your email and remove it; your account then counts as never having used the trial.

## Third-Party Services

Pista uses:

- Google Play Services and Credential Manager for Google sign-in;
- Google Drive API for optional backup and the trial record;
- Google Play Billing for subscriptions;
- Google Play for app updates, in-app reviews, and AI model delivery;
- Firebase Crashlytics for crash diagnostics;
- Google Analytics for Firebase for usage analytics;
- Firebase Remote Config for feature settings and parsing-rule updates;
- Google Cloud Firestore for free-trial records, feedback, missed-SMS reports, and opt-in SMS format sharing;
- Android platform services for SMS, notifications, camera, widgets, and alarms.

These services are provided by Google and governed by Google's Privacy Policy (https://policies.google.com/privacy).

## Changes To This Policy

We may update this policy as Pista changes. If changes are material, we will update the effective date and, where appropriate, notify you in the app or in release notes.

## Contact

Developer: TranscenD

Email: manifest.singularity@gmail.com

For privacy questions, data requests, or grievances (including under India's DPDP Act), email us with the subject "Privacy". We aim to respond within 30 days.

# Flight-Price-Notifier
DAY - 40 -- Project - python X Flight Price Notifier

# ✈️ Flight Price Notifier

An automated flight deal tracking and multi-channel notification system built with Python.

This project searches for the cheapest flights using the Amadeus API, compares them with stored prices in Google Sheets (via Sheety), and sends alerts through:

- 📧 Gmail (SMTP)
- 📱 SMS (Twilio)
- 💬 WhatsApp (Twilio)

---

# 🚀 Features

- 🔎 Search flights using Amadeus API
- ✈️ Direct flight search with automatic fallback to indirect flights
- 🛑 Stop detection (0 stop / multiple stops)
- 📊 Price comparison with stored lowest prices
- 📧 Email notifications to all users
- 📱 SMS notifications
- 💬 WhatsApp notifications
- 🔐 Environment variable configuration (.env)
- 🧠 Input validation system (ALL / SMS / WHATSAPP / GMAIL)

---

# 🏗 Project Structure

```
40_FLIGHT_PRICE_NOTIFIER.py
FLIGHT_SEARCH.py
FLIGHT_DATA_MANAGER.py
FLIGHT_NOTIFICATION_MANAGER.py
FLIGHT_DATA.py
```

---

# ⚙️ Setup Guide

## 1️⃣ Install Dependencies

```bash
pip install requests python-dotenv twilio
```

---

# 📊 Google Sheets Setup

## Step 1 — Create Your Own Google Sheet

Go to:

https://docs.google.com/spreadsheets/

Click **Blank** and create a new sheet.

⚠️ You DO NOT need to "Make a Copy" if you created the sheet yourself.

You only need **Make a Copy** if:
- The sheet is someone else's template
- You have View-only access

If you can edit cells → no copy needed.

---

## Step 2 — Create `prices` Sheet

Rename the first sheet to:

```
prices
```

Add columns (Row 1):

| city | iataCode | lowestPrice |

Example:

| city   | iataCode | lowestPrice |
|--------|----------|------------|
| Paris  | PAR      | 50000      |
| London | LON      | 45000      |

---

## Step 3 — Create `users` Sheet

Click ➕ at the bottom and create new sheet.

Rename it:

```
users
```

Add columns (Row 1):

| timestamp | firstName | lastName | email |

If you use a Google Form, this will auto-generate.

---

# 🔗 Connect Google Sheet to Sheety

1. Go to https://sheety.co/
2. Login with Google
3. Create New Project
4. Select your Google Sheet
5. Enable **Basic Authentication**

Sheety will generate endpoints like:

```
https://api.sheety.co/xxxxx/project/prices
https://api.sheety.co/xxxxx/project/users
```

Copy these into `.env`.

---

# 🔑 API Setup

## ✈️ Amadeus API

1. Go to https://developers.amadeus.com/
2. Create account
3. Create new app
4. Get:
   - API Key
   - API Secret

---

## 📱 Twilio (SMS & WhatsApp)

1. Go to https://www.twilio.com/
2. Create account
3. Get:
   - Account SID
   - Auth Token
4. Get Twilio number
5. Enable WhatsApp sandbox

---

## 📧 Gmail SMTP

1. Enable 2-Step Verification
2. Go to Google → Security → App Passwords
3. Generate App Password
4. Use the 16-character password

⚠️ Do NOT use your real Gmail password.

---

# 🔐 Create `.env` File

Create a file named:

```
.env
```

Place it in the root directory.

Add:

```
# Amadeus
AMADEUS_API_KEY=your_key
AMADEUS_SECRET=your_secret

# Sheety
SheetyPricesEndpointURL=your_prices_endpoint
Sheety_USERS_Endpoint_URL=your_users_endpoint
SheetyUserName=your_sheety_username
ShetyPassword=your_sheety_password

# Twilio
SID=your_twilio_sid
Auth_tokens=your_auth_token
Twilio_SMS_No=your_twilio_sms_number
My_SMS=your_number
Twilio_WhatsApp_No=your_twilio_whatsapp_number
My_Whatsapp=your_whatsapp_number

# Gmail
User_Gmail=your_email@gmail.com
User_Password=your_app_password
```

---

# 🚨 Important

Add this to `.gitignore`:

```
.env
```

Never upload `.env` to GitHub.

---

# 🧠 How the System Works

1. Fetch destinations from `prices` sheet.
2. Fetch customer emails from `users` sheet.
3. Search for cheapest flight.
4. If no direct flight → retry indirect.
5. Detect number of stops.
6. Compare price with stored lowest price.
7. If cheaper → send notification.

---

# ▶️ Run Project

```bash
python 40_FLIGHT_PRICE_NOTIFIER.py
```

You will be prompted:

```
Notify via (ALL / SMS / WHATSAPP / GMAIL):
```

Choose your preferred method.

---

# ❌ Common Errors

## FileNotFoundError

Cause:
- `.env` missing
- Wrong location
- Wrong filename

Fix:
- Create `.env` in root folder
- Ensure name is exactly `.env`

---

## 401 Unauthorized (Sheety)

Cause:
- Wrong username/password

Fix:
- Check Basic Authentication in Sheety

---

## No Alerts Sent

Cause:
- Current flight price is not lower than stored lowestPrice

---

# 🎯 Future Improvements

- Store user notification preference in sheet
- Auto-update lowest price after alert
- Add logging system
- Add scheduler (cron / task scheduler)
- Convert to Flask web app
- Docker support

---

# 🏁 Status

✅ Fully Functional  
✅ Direct + Indirect Flight Logic  
✅ Multi-Channel Notification  
🔒 Day 40 Milestone Completed  

---

Built as part of 100 Days of Code journey.

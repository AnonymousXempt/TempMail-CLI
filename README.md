# TempMail-CLI

A command-line tool to generate temporary email addresses and monitor inbox messages in real time.

---

## Description

**TempMail-CLI** is a fast and minimal command-line tool that allows users to generate disposable email addresses and instantly receive messages for anonymous or testing purposes.

It’s built for anyone who values privacy or needs to quickly generate temp emails without relying on a browser. Whether you're testing signups or want to avoid spam, **TempMail-CLI** gives you seamless inbox access right from your terminal.

---

## Features

- **Generate disposable email addresses** instantly for anonymous use  
- **Auto-refresh inbox** to fetch new emails in real time  
- **Read full email contents** including sender/recipient metadata  
- **Enhance privacy** by avoiding use of your personal or work email  
- **Protect against spam** by using temporary emails for risky signups  
- **Perfect for testing or free trials** where permanent email isn’t needed  
- **Cross-platform CLI interface** with clean, colored output  
- **Minimal dependencies**  and lightweight footprint

---

## Installation

1. **Clone the repository**
   ```
   git clone https://github.com/AnonymousXempt/TempMail-CLI.git
   ```

2. **Navigate into the project directory**
   ```
   cd tempmail-cli
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

---

## Usage

Run the tool with:

```
python main.py
```

### Menu Options:
- `[1] Generate new email`: Creates a temporary inbox and displays the address  
- `[2] Go to inbox`: Opens real-time inbox viewer for the current address  
- `[0] Exit`: Closes the program

### Inbox Controls:
- `v`: View email contents  
- `m`: Return to the main menu  
- *(Inbox auto-refreshes every 5 seconds)*

---

## Screenshot

![Screenshot 2025-06-19 135107](https://github.com/user-attachments/assets/a16d0a44-87c9-4a8c-a830-3819dfe4d865)

---

## Roadmap

- [x] **CLI App** – Fully functional terminal interface to generate and monitor temp emails in real-time
- [ ] Bot Integrations
   - [ ] **Discord Bot** – Interact with temp mail features using bot commands or DMs [(Goto)](https://github.com/AnonymousXempt/TempMail-Discord)
   - [ ] **Telegram Bot** – Lightweight access via chat interface, ideal for mobile usage
- [ ] **PyPI Package** - Publish as a pip-installable package (tempmail-cli) for simpler installation and updates

---

## License

This project is licensed under the **MIT License**.  
See the [`LICENSE`](./LICENSE) file for details.

## Acknowledgments
This project leverages the Temp-Mail API: https://api.internal.temp-mail.io/api/v3 for generating and retrieving temporary emails.

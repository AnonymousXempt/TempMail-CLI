from colorama import Fore, Style

def print_header(title):
    print("\n" + Fore.CYAN + Style.BRIGHT + f"{title.center(55)}")
    print(Fore.CYAN + "_" * 55)

def print_menu(current_email):
    print_header("Temp Mail CLI")
    print(Fore.YELLOW + f" Current Email: {current_email or '[Not Generated]'}")
    print("_" * 55)
    print(" [1] Generate new email")
    print(" [2] Go to inbox")
    print(" [0] Exit")
    print("_" * 55)

def print_email_previews(emails):
    print(f"\n{'No.':<4}{'From':<25}{'Subject':<30}{'Date'}")
    print("-" * 80)
    for i, email in enumerate(emails, 1):
        print(f"{i:<4}{email.get('from', ''):<25}{email.get('subject', ''):<30}{email.get('date', '')}")

def print_email_detail(email):
    print("\n" + "=" * 40)
    print(f"From   : {email.get('from', 'N/A')}")
    print(f"To     : {email.get('to', 'N/A')}")
    print(f"Subject: {email.get('subject', 'N/A')}")
    print(f"Date   : {email.get('date', 'N/A')}")
    print("-" * 40)
    print("Body:\n")
    print(email.get('body_text', '(No body content)').strip())
    print("=" * 40 + "\n")
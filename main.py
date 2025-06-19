import time
from colorama import init, Fore
from src.utils import clear_screen
from src.email_client import generate_new_email, retrieve_emails
from src.ui import print_menu, print_email_previews, print_email_detail

init(autoreset=True)

def inbox_loop(current_email):
    refresh_interval = 5
    emails = []

    while True:
        clear_screen()
        print(Fore.GREEN + f"\n📥 Inbox for: {current_email}")
        print("-" * 60)

        try:
            emails = retrieve_emails(current_email)
        except Exception as e:
            print(Fore.RED + f"Error retrieving emails: {e}")
            time.sleep(refresh_interval)
            continue

        if not emails:
            print("No emails yet...")
        else:
            print_email_previews(emails)

        print("\n[v] View email  [m] Return to menu  [Refreshes in 5s]")
        start = time.time()

        while time.time() - start < refresh_interval:
            try:
                import msvcrt
                if msvcrt.kbhit():
                    key = msvcrt.getwch().lower()
                    if key == "m":
                        return
                    elif key == "v":
                        if not emails:
                            continue
                        clear_screen()
                        print_email_previews(emails)
                        selection = input("\nEnter email number to view (or 'q'): ").strip()
                        if selection.lower() == "q":
                            continue
                        if selection.isdigit() and 1 <= int(selection) <= len(emails):
                            selected = emails[int(selection) - 1]
                            clear_screen()
                            print_email_detail(selected)
                            input("\nPress Enter to return...")
            except ImportError:
                import select, sys
                i, _, _ = select.select([sys.stdin], [], [], 1)
                if i:
                    action = sys.stdin.readline().strip().lower()
                    if action == 'm':
                        return
                    elif action == 'v' and emails:
                        clear_screen()
                        print_email_previews(emails)
                        selection = input("\nEnter email number to view (or 'q'): ").strip()
                        if selection.lower() == 'q':
                            continue
                        if selection.isdigit() and 1 <= int(selection) <= len(emails):
                            selected = emails[int(selection) - 1]
                            clear_screen()
                            print_email_detail(selected)
                            input("\nPress Enter to return...")

def main():
    current_email = None
    while True:
        clear_screen()
        print_menu(current_email)
        choice = input("Enter option [0-2]: ").strip()

        if choice == "1":
            try:
                current_email = generate_new_email()
                print(f"\nNew temp email generated: {Fore.CYAN}{current_email}")
                time.sleep(2)
                inbox_loop(current_email)
            except Exception as e:
                print(Fore.RED + str(e))
                time.sleep(2)

        elif choice == "2":
            if not current_email:
                print(Fore.RED + "\nPlease generate an email first.")
                time.sleep(2)
            else:
                inbox_loop(current_email)

        elif choice == "0":
            print("\nExiting... Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option.")
            time.sleep(2)

if __name__ == "__main__":
    main()
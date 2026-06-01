import os

sys32hosts = r"C:\Windows\System32\drivers\etc\hosts"


def presetEighteenPlus():
    entries = [
        "127.0.0.1 pornhub.com",
        "127.0.0.1 www.pornhub.com",

        "127.0.0.1 xvideos.com",
        "127.0.0.1 www.xvideos.com",

        "127.0.0.1 xnxx.com",
        "127.0.0.1 www.xnxx.com",

        "127.0.0.1 redtube.com",
        "127.0.0.1 www.redtube.com",

        "127.0.0.1 youporn.com",
        "127.0.0.1 www.youporn.com",

        "127.0.0.1 xhamster.com",
        "127.0.0.1 www.xhamster.com",

        "127.0.0.1 spankbang.com",
        "127.0.0.1 www.spankbang.com",

        "127.0.0.1 brazzers.com",
        "127.0.0.1 www.brazzers.com",

        "127.0.0.1 tube8.com",
        "127.0.0.1 www.tube8.com",

        "127.0.0.1 rule34.com",
        "127.0.0.1 www.rule34.com",

        "127.0.0.1 erome.com",
        "127.0.0.1 www.erome.com",

        "127.0.0.1 onlyfans.com",
        "127.0.0.1 www.onlyfans.com\n"
    ]

    with open(sys32hosts, "r+") as f:
        content = f.read()
        for entry in entries:
            if entry not in content:
                f.write("\n# ADDED BY JOLIFY - 18+ filter\n" + entry)
    print("18+ blocked succesfully!\n")

def presetSocialMedia():
    entries = [
        "127.0.0.1 instagram.com",
        "127.0.0.1 www.instagram.com",

        "127.0.0.1 tiktok.com",
        "127.0.0.1 www.tiktok.com",

        "127.0.0.1 facebook.com",
        "127.0.0.1 www.facebook.com",

        "127.0.0.1 x.com",
        "127.0.0.1 twitter.com",
        "127.0.0.1 www.x.com",
        "127.0.0.1 www.twitter.com",

        "127.0.0.1 reddit.com",
        "127.0.0.1 www.reddit.com",

        "127.0.0.1 9gag.com",
        "127.0.0.1 www.9gag.com",

        "127.0.0.1 snapchat.com",
        "127.0.0.1 www.snapchat.com\n"
    ]

    with open(sys32hosts, "r+") as f:
        content = f.read()
        for entry in entries:
            if entry not in content:
                f.write("\n# ADDED BY JOLIFY - Social Media filter\n" + entry)
    print("Social Media blocked succesfully!\n")


def main():
    
    print("Welcome to Jolify!")
    while True:

        content = "Empty"
        with open(sys32hosts, "r+") as f:
                    content = f.read()

        print("1. Block custom website")
        print("2. Block major 18+ sites")
        print("3. Block Social Media")
        print("4. Show current content")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "2":
            presetEighteenPlus()

        elif choice == "3":
            presetSocialMedia()

        elif choice == "1":
            while True:
                site = input("Enter website (example.com): ").strip()

                entries = [
                    f"127.0.0.1 {site}.com",
                    f"127.0.0.1 www.{site}"
                ]

                with open(sys32hosts, "r+") as f:
                    content = f.read()
                    for entry in entries:
                        if entry not in content:
                            f.write("\n# ADDED BY JOLIFY\n" + entry)
                print(f"{site} has been blocked succesfully!")
                blockMore = input("Block another site?: ").lower().strip()
                if blockMore == "n" or blockMore == "n":
                    break

        elif choice == "4":
            print(f"{content}" + "\n")

        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
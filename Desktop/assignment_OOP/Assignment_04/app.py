class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

if __name__ == "__main__":
    user1 = Bank()
    user2 = Bank()

    print("Before changing the bank name:")
    print(f"User 1 Bank name: {user1.bank_name}")
    print(f"User 2 Bank name: {user2.bank_name}")

    # Let's change the bank name to show the classmethod in action
    Bank.change_bank_name("XYZ Bank")

    print("\nAfter changing the bank name:")
    print(f"User 1 Bank name: {user1.bank_name}")
    print(f"User 2 Bank name: {user2.bank_name}")


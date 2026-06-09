class DonationSystem:

    def register_donation(self, donor_name, amount):

        if donor_name.strip() == "":
            return "Invalid donor name"

        if amount <= 0:
            return "Invalid donation amount"

        return f"Donation of £{amount} received from {donor_name}"
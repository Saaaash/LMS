class Duecalculation:

    def calculateDue(self, days):
        max_days = 10
        due_amount = 5
        if days > max_days:
            due_days = days - max_days
            due = due_days * due_amount
            print("You have to pay due amount of Rs. {} only, for {} days".format(due, due_days))
        else:
            print("Thank you.")

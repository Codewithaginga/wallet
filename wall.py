from itertools import permutations
import random


class Bank:
    pin = 7446
    balance = 568_345
    loan_limit = 723_567
    deposit_limit_per_day = 1_000_000

    @staticmethod
    def service():
        card_pin = int(input('Enter pin: ' '\n'))

        num = ['1', '2', '3', '5', '6', '7', '8', '9', '0']
        second_authentication = ''
        for i in range(4):
            second_authentication = second_authentication + random.choices(num)[0]
        print(second_authentication)

        pin1 = input('Enter pin from your phone to access your account: ' '\n')
        if pin1 != second_authentication:
            b = Bank()
            b.service()

        elif Bank.pin != card_pin:

            b = Bank()
            b.service()
        else:
            print('WELCOME')

        print('1. Check balance')
        print('2. Withdraw cash')
        print('3. Apply for Loan')
        print('4. Deposit cash')
        print('5. quit')
        choice = int(input('Enter option: '))

        if choice == 1:

            bal_check = Bank.balance
            print(f'Your balance is {bal_check:,}. Thank you for Banking with us.')

        elif choice == 2:
            print(f'Withdraw')

            withdraw = int(input('Enter amount: '))
            if withdraw > Bank.balance:
                print('You have insufficient funds in your account.')

                withdraw1 = int(input('Enter amount: '))
                if withdraw1 > Bank.balance:
                    print('You have insufficient funds in your account.')

                else:
                    print(f'Confirmed you have you withdraw {withdraw:,} from your account.'
                          f'Thank you banking with us.')
                b = Bank()
                b.service()

            else:

                print(f'Confirmed you have you withdraw {withdraw:,} from your account.'
                      f'Thank you banking with us.')

        elif choice == 3:

            print('Apply for Loan with us')

            print(f'Your loan limit is {Bank.loan_limit:,}')

            request_loan = int(input('Enter loan amount: ' '\n'))

            if request_loan > Bank.loan_limit:

                print(f'Failed your loan limit is {Bank.loan_limit:,}. Try again')
                request_loan1 = int(input('Enter loan amount: ' '\n'))
                if request_loan1 > Bank.loan_limit:
                    print(f'Failed your loan limit is {Bank.loan_limit:,}. Try again')

                else:
                    print(f'your loan of {request_loan1:,} have being approved.'
                          f'payable in 3 months window.')

                    request_loan2 = int(input('Enter loan amount: ' '\n'))
                    if request_loan2 > Bank.loan_limit:
                        print(f'Failed your loan limit is {Bank.loan_limit:,}. Try again')

                        print(f'Please Try Again Later')
                    else:
                        print(f'your loan of {request_loan2:,} have being approved.'
                              f'payable in 3 months window.')

            else:
                print(f'your loan of {request_loan:,} have being approved.'
                      f'payable in 3 months window.')

        elif choice == 4:
            print('Deposit here')

            deposit = int(input('Enter amount: ' '\n'))

            if deposit > Bank.deposit_limit_per_day:
                print(f'Failed your daily deposit limit is {Bank.deposit_limit_per_day} ')
                b = Bank()
                b.service()

            else:

                print(f'Confirmed you have deposit {deposit:,} ,Thank you for banking with us')

        elif choice == 5:
            print('Thank you for staying with us')

        else:

            print('THANK YOU FOR BANKING WITH US')


b = Bank()
b.service()

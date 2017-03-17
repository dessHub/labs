def calculate_tax(payroll):
        while True:
           try:
             for key in payroll.keys():
                 income = payroll[key]
                 if income <= 1000 or income < 0:
                    payroll[key] = 0
                 elif income in range(1001, 10001):
                     payroll[key] = 0.1 * (payroll[key]-1000)
                 elif income in range(10001, 20201):
                     payroll[key] = ((0.1*(10000-1000)) + (0.15*(payroll[key]-10000)))
                 elif income in range(20201, 30751):
                     payroll[key] = ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(payroll[key]-20200)))
                 elif income in range(30751 , 50001):
                     payroll[key] = ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(30750-20200)) + (0.25*(payroll[key]-30750)))
                 elif income > 50000:
                     payroll[key] = ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(30750-20200)) + (0.25*(50000-30750)) + (0.3*(payroll[key]-50000)))
                 else:
                      pass
             return payroll
             break

           except (AttributeError,TypeError):
               raise ValueError('The provided input is not a dictionary')

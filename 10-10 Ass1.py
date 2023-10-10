def calculate_emi(principal_amount, rate_of_interest, time_in_months):

    si = (principal_amount * rate_of_interest * time_in_months) / (12 * 100)
    

    emi = (si + principal_amount) / time_in_months
    
    return emi
principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (annual): "))
time_in_years = float(input("Enter the time period (in years): "))
time_in_months = time_in_years * 12
emi = calculate_emi(principal_amount, rate_of_interest, time_in_months)
print(f"The EMI is: {emi:.2f}")

# encoding=gbk

def calculate_annual_interest_rate(total_payment, total_loan_amount, loan_period_months):
    total_interest = total_payment - total_loan_amount
    monthly_interest_rate = total_interest / (total_loan_amount * loan_period_months)
    annual_interest_rate = monthly_interest_rate * 12 * 100  # Convert to percentage
    return annual_interest_rate

# 输入每月还款额、总借款额和借款周期
# 请输入总借款额：
total_loan_amount = float( 100000 )
# 请输入每月还款额：
monthly_payment = float( 1833.7 )
# "请输入借款周期（月数）："
loan_period_months = int( 60 )

# 调用函数计算实际年化利率
annual_interest_rate = calculate_annual_interest_rate(monthly_payment * loan_period_months, total_loan_amount, loan_period_months)

print("实际年化利率：{:.2f}%".format(annual_interest_rate))
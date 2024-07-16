# encoding=gbk

def calculate_annual_interest_rate(monthly_payment, total_loan_amount, loan_period_months):
    total_payment = monthly_payment * loan_period_months
    total_interest = total_payment - total_loan_amount
    annual_interest_rate = (total_interest / total_loan_amount) / (loan_period_months / 12) * 100
    return annual_interest_rate

# ����ÿ�»����ܽ���ͽ������
 

# �������ܽ��
total_loan_amount = float( 100000 )
# ������ÿ�»���
monthly_payment = float( 1833.7 )
# "�����������ڣ���������"
loan_period_months = int( 60 )

annual_interest_rate = calculate_annual_interest_rate(monthly_payment, total_loan_amount, loan_period_months)
print("ʵ���껯���ʣ�{:.2f}%".format(annual_interest_rate))

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# import libraries and modules

# %%
import pandas as pd
import numpy as np
from datetime import datetime

# %% [markdown]
# define variables needed

# %%
Interest_Rate = float(input("Enter your interest rate: "))
Monthly_interest = Interest_Rate / 12 / 100


# %%
Years = int(input("Enter the legnth of loan in years: "))
Payments_Year = 12


# %%
Principal = int(input("Enter your loan amount in $: "))


# %%
Addl_Payment = int(input("Enter additional monthly payments (if any): "))


# %%
start_date_input = str(input("Enter the start date as yyyy-mm-dd: "))
start_date = datetime.strptime(start_date_input, "%Y-%m-%d")

# %% [markdown]
# build a datetimeindex for the next x amount of years based on MS (month, start)

# %%
date_range = pd.date_range(start_date, periods=(Years * Payments_Year), freq='MS')
date_range.name = 'Payment_Date'

# periods: number of periods to generate, freq: "MS" stands for "month start"

print(date_range)

# %% [markdown]
# This helpful function creates a range for the next 30 years starting on Jan 1, 2016. The range will be used to build up the basic DataFrame we will use for the amortization schedule. Note that we need to make sure the first period is 1 not 0, hence the need to use the df.index += 1 :

# %%
df = pd.DataFrame(index=date_range,columns=['Payment', 'Principal', 'Interest', 'Addl_Payment', 'Balance'], dtype='float')
df.reset_index(inplace=True)
df.index += 1
df.index.name = "Period"

print(df)

# %% [markdown]
# calculate the payment, Principal, Interest, Addl_Principal columns

# %%
df['Payment'] = Principal * (Monthly_interest / (1 - (1 + Monthly_interest)**(-(Years*Payments_Year))))

df["Principal"] = -1 * np.ppmt(Monthly_interest, df.index, Years*Payments_Year, Principal)

df["Interest"] = -1 * np.ipmt(Monthly_interest, df.index, Years*Payments_Year, Principal)

df["Addl_Payment"] = Addl_Payment

df['Cumulative_Principal'] = (df['Principal'] + df['Addl_Payment']).cumsum()

df['Cumulative_Interest'] = (df['Interest']).cumsum()

df['Balance'] = Principal - df['Cumulative_Principal']
df['Balance'] = df['Balance'].clip(0)

df = df.round(2)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)


# %%




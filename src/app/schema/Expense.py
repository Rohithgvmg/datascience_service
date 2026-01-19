from pydantic import BaseModel, Field
from typing import Optional

class Expense(BaseModel):
    amount: Optional[str] = Field(title="amount", description="The numeric value of the transaction")
    merchant: Optional[str] = Field(title="merchant", description="The shop, person, or entity where the money was spent")
    currency: Optional[str] = Field(title="currency", description="The currency of the transaction (e.g., INR, USD)")
    transaction_type: Optional[str] = Field(
        title="type", 
        description="Whether the money was 'debited' (spent/sent) or 'credited' (received/added)"
    )
    bank_name: Optional[str] = Field(
        title="bank", 
        description="The name of the bank that sent the SMS (e.g., KVB, SBI, HDFC)"
    )

# this class defines how the LLM must return the data 
# description helps LLM to understand the field 
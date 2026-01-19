import re
import unicodedata
class MessageUtil:
    def normalize_text(self, text: str) -> str:
        # This converts styled characters (like 𝖸𝗈𝗎𝗋) back to standard (Your)
        return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')

    def isBankSms(self,message):
        # checks message came from bank itself pr not
        
        clean_message = self.normalize_text(message)
        mandatory_words = ['a/c', 'INR', 'KVB']
        action_words = ['debited', 'credited'] 
        # either must be present
       
        pattern = "^" + "".join([f"(?=.*{re.escape(w)})" for w in mandatory_words]) 
        pattern += f"(?=.*({'|'.join(action_words)}))"

        isValid= bool(re.search(pattern,clean_message,flags=re.IGNORECASE))

        if not isValid:
           print('Message is not valid bank message')
        
        return isValid

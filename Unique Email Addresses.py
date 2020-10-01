class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for raw_email in emails:
            username,domain_name = raw_email.split("@")
            if "+" in username:
                username = username.split("+")[0]
            username = username.replace(".","")
            res.add(username+"@"+domain_name)
        return len(res)

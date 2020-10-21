#My Version of simplified & using python premade methods based on the idea of leetcode answer
def numUniqueEmails3(emails):
    lst = []
    final_lst = []
    for addr in emails:
        lst.append(addr.split('@'))
    for split_lst in lst:
        string = ""
        local = (split_lst[0].split('+')[0].replace('.', ''))
        domain = split_lst[1]
        string = local + domain
        final_lst.append(string)

    return len(set(final_lst))

#leetcode answer
def numUniqueEmails2(emails):
    seen = set()
    for email in emails:
        local,domain = email.split('@')
        if '+' in local:
            local = local[:local.index('+')]
        seen.add(local.replace('.','')+'@'+domain)
        
    return len(seen)

#My Version of using understanding of indexing algorithm
def numUniqueEmails(emails):
    temp_lst = []
    final_lst = []
    for address in emails:
        string = ""
        for i in range(0,len(address)):
            if address[i] != ".":
                if address[i] == "+" or address[i] == "@":
                    break
                string += address[i]
        for j in range(i,len(address)):
            if address[j] == "@":
                break
        for k in range(j, len(address)):
            string += address[k]

        temp_lst.append(string)

        final_lst = set(temp_lst)
        final_num = len(final_lst)
    return final_num

#emails = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails3(emails))
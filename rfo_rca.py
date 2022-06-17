from datetime import date as dt

def main(product,priority,date,issue_desc,ticket_number):

    #Leaving strings as "final_var" in case a change like .lower() (i.e) is needed in the future. 
    
    final_product = product
    final_date = date.replace("-","").replace("/","")
    final_issue_desc = issue_desc.replace(" ","_").replace("issue","").replace("Issue","").replace("ISSUE","")

    final_string_rfo = "RFO-" + str(final_date) + "-" + priority + "-" + final_product + "-" + final_issue_desc[:-1] + "-" + str(ticket_number)

    final_string_rca = "RCA-" + str(final_date) + "-" + priority + "-" + final_product + "-" + final_issue_desc[:-1] + "-" + str(ticket_number)

    print("\nRFO: " + final_string_rfo)
    print("\nRCA: " + final_string_rca + "\n")

    
if __name__ == "__main__":

    today = dt.today()

    today.strftime("%YYYY%MM%DD")
    final_today = str(today).replace("-","")

    # This was to test the date - print("Date: " + final_today)
    
    product = input("Product's name?\n")
    priority = input("Priority? (P1 i.e)\n")
    date = input("Date? (Remember, use yyyymmdd / If left BLANK, today's date will be added.)\n")

    if date == "":
        date = final_today

    issue_desc = input("What's the issue? (Remember to NOT use issue on the name) \n")
    ticket_number = input("What's the TSD Number?\n")
    
    main(product,priority,date,issue_desc,ticket_number)


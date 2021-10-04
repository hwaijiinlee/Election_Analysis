import csv
import os

load_file = os.path.join("Multiple_Prop.csv")

total_votes = 0

propa_options = []
propb_options = []
propc_options = []
propa_votes = {}
propb_votes = {}
propc_votes = {}
winning_propa = ""
winning_propb = ""
winning_propc = ""
winning_propa_count = 0
winning_propb_count = 0
winning_propc_count = 0
winning_propa_percentage = 0
winning_propb_percentage = 0
winning_propc_percentage = 0

with open(load_file) as prop_data:
    reader = csv.reader(prop_data)
    header = next(reader)

    for row in reader:
        total_votes = total_votes + 1
        propa_ans = row[1]
        propb_ans = row[2]
        propc_ans = row[3]

        if propa_ans not in propa_options:
            propa_options.append(propa_ans)
            propa_votes[propa_ans] = 0
        propa_votes[propa_ans] += 1

        if propb_ans not in propb_options:
            propb_options.append(propb_ans)
            propb_votes[propb_ans] = 0
        propb_votes[propb_ans] += 1
    
    for propa_ans in propa_votes:
        propa_tvotes = propa_votes.get(propa_ans)
        propa_tpercent = float(propa_tvotes) / total_votes * 100
        propa_results = (f"Prop A Results: {propa_ans}: {propa_tpercent:.1f}% ({propa_tvotes:,})")
        # print(propa_results)

        if (propa_tvotes > winning_propa_count) and (propa_tpercent > winning_propa_percentage):
            winning_propa_count = propa_tvotes
            winning_propa_percentage = propa_tpercent
            winning_propa = propa_ans
    
    winning_propa_summary = (
        f"Prop A Result: {winning_propa}\n"
        f"Prop A Vote Count: {winning_propa_count}\n"
        f"Prop A Percentage: {winning_propa_percentage}%\n")
    print(winning_propa_summary)

    for propb_ans in propb_votes:
        propb_tvotes = propb_votes.get(propb_ans)
        propb_tpercent = float(propb_tvotes) / total_votes * 100
        propb_results = (f"Prop B Responses: {propb_ans}: {propb_tpercent:.1f}% ({propb_tvotes:,})")
        # print(propb_results)

        if (propb_tvotes > winning_propb_count) and (propb_tpercent > winning_propb_percentage):
            winning_propb_count = propb_tvotes
            winning_propb_percentage = propb_tpercent
            winning_propb = propb_ans
    
    winning_propb_summary = (
        f"Prop B Result: {winning_propb}\n"
        f"Prop B Vote Count: {winning_propb_count}\n"
        f"Prop B Percentage: {winning_propb_percentage}%")
    print(winning_propb_summary)
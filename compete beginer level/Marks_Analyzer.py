def calculator(details):
    int_details = list(map(int, details))
    cal = {"count":0,"Total":0,"Average":0.0,"Highest":0,"Lowest":100}
    for each in int_details:
        cal["count"]+=1
        cal["Total"]+=each
        if each > cal["Highest"]:
            cal["Highest"]=each
        if each < cal["Lowest"]:
            cal["Lowest"]=each
    cal["Average"]=cal["Total"]/cal["count"]
    return cal
marks = input("Enter the marks you got(Separated by commas) : ").strip().replace(" ","").split(",")

results = calculator(marks)

print(f"""
Number of Subjects  : {results['count']}
Total Marks         : {results['Total']}
Average Marks       : {results['Average']}
Highest Marks       : {results['Highest']}
Lowest Marks        : {results['Lowest']}
""")
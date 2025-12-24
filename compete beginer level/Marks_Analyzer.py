def calculator(details):
    int_details = list(map(int, details))
    cal = {"count":0,"Total":0,"Average":0,"Highest":0,"Lowest":0}
    for each in int_details:
        cal["count"]+=1
        cal["Total"]+=each
        if each > cal["Highest"]:
            cal["Highest"]=each
        if each < cal["Lowest"]:
            cal["Lowest"]=each
    cal["Average"]=cal["total"]//cal["count"]
    return cal

while True:
    marks = input("Enter the marks you got(separated by commas, 'END' to quit) : ").strip().replace(" ","").split(",")
    if marks[0].upper() == "END":
        break
results = calculator(marks)

print(f"""
Number of Students : {results['count']}
""")
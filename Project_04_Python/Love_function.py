def love():
    singleness = 1
    maturity_score = input("Please enter your maturity score (1-10): ")
    if not maturity_score.isdigit() or int(maturity_score) < 1 or int(maturity_score) > 10:
        return "Kindly input a number between 1 and 10"
    maturity_score = int(maturity_score) #Converting the maturity number entered by user to integer
    
    intelligence_score = input("Please enter your intelligence score (1-10): ")
    if not intelligence_score.isdigit() or int(intelligence_score) < 1 or int(intelligence_score) > 10:
        return "Kindly input a number between 1 and 10"
    intelligence_score = int(intelligence_score) #Converting the Intelligence number entered by user to integer
    
    trust_score = input("Please enter your trust score (1-10): ")
    if not trust_score.isdigit() or int(trust_score) < 1 or int(trust_score) > 10:
        return "Kindly input a number between 1 and 10"
    trust_score = int(trust_score) #Converting the trust number entered by user to integer
    
    love_score = input("Please enter your love score (1-10): ")
    if not love_score.isdigit() or int(love_score) < 1 or int(love_score) > 10:
        return "Kindly input a number between 1 and 10"
    love_score = int(love_score) #Converting the love number entered by user to integer
    
    total_score = singleness + maturity_score + intelligence_score + trust_score + love_score #Caculating all the inputs to get a total score
    
    if singleness != 1:
        return "Kindly input the number 1 here"
    elif total_score >= 21:
        return "Congrats! You are closer to your desired romantic relationship"
    else:
        return "Sorry, you are not eligible for a romantic relationship yet"

    #Sir pls I've been able to organise my repo so you can award my bonus mark, Thanks. 
    #The reason i left the task 15 like that for now is because it has not been graded. I've already created a folder for it and will delete it after grading. 

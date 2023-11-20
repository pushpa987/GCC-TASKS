from flask import Flask, render_template, request
app = Flask(__name__,static_url_path='/static')
@app.route('/intro')
def intro():
    return render_template('intro.html')
grade_points = {
    'A+': 10,
    'A': 9,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 5,
    'F': 0
}
@app.route('/s11', methods=['GET', 'POST'])
def s11():
    if request.method == 'POST':
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        lab1 = request.form['Lab1']
        lab2 = request.form['Lab2']
        lab3 = request.form['Lab3']
        lab4 = request.form['Lab4']
        grades = [sub1, sub2, sub3, sub4, lab1, lab2, lab3,lab4]
        
        
        
        credits=[3,3,3,3,1.5,1.5,1.5,1.5]# ming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_grade_points = sum(grade_points.get(grade, 0) * credit for grade, credit in zip(grades, credits))
        total_credits = sum(credits)
 
        # Calculate the CGPA
        cgpa = total_grade_points / total_credits


        # Calculate the percentage
        percentage = cgpa * 9.5 -3
        if percentage>75:
            return render_template('result.html',percentage=percentage, actualpercentage=percentage,sem="1-1") 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage,actualpercentage=percentage,sem="1-1")  
        else:
            return render_template('result2.html',percentage=percentage,actualpercentage=percentage,sem="1=1")
    return render_template('s11.html')
    
@app.route('/s12', methods=['GET', 'POST'])
def s12():
    if request.method == 'POST':
        prev = request.form['Previouspercentage']
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        sub5 = request.form['Subject5']
        lab1 = request.form['Lab1']
        lab2 = request.form['Lab2']
        lab3 = request.form['Lab3']
     
        grades = [sub1, sub2, sub3, sub4,sub5, lab1, lab2, lab3]
        credits=[3,3,3,3,3,1.5,1.5,1.5] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_grade_points = sum(grade_points.get(grade, 0) * credit for grade, credit in zip(grades, credits))
        total_credits = sum(credits)
 
        # Calculate the CGPA
        cgpa = total_grade_points / total_credits


        # Calculate the percentage
        percentage = cgpa * 9.5 -3
        actualpercentage=(percentage+float(prev))/2
        if actualpercentage>75:
            return render_template('result.html',percentage=percentage ,actualpercentage=actualpercentage ,sem="1-2") 
        elif actualpercentage>65:
            return render_template('result1.html',percentage=percentage,actualpercentage=actualpercentage,sem="1-2")  
        else:
            return render_template('result2.html',percentage=percentage,actualpercentage=actualpercentage,sem="1-2")
    return render_template('s12.html')
@app.route('/s21', methods=['GET', 'POST'])
def s21():
    if request.method == 'POST':
        prev = request.form['Previouspercentage']
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        sub5 = request.form['Subject5']
        lab1 = request.form['Lab1']
        lab2 = request.form['Lab2']
        lab3 = request.form['Lab3']
        lab4 = request.form['Lab4']
        grades = [sub1, sub2, sub3, sub4,sub5, lab1, lab2, lab3,lab4]
        credits=[3,3,3,3,3,1.5,1.5,1.5,2.0] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_grade_points = sum(grade_points.get(grade, 0) * credit for grade, credit in zip(grades, credits))
        total_credits = sum(credits)
 
        # Calculate the CGPA
        cgpa = total_grade_points / total_credits


        # Calculate the percentage
        percentage = cgpa * 9.5 -3
        actualpercentage=(percentage+float(prev))/2
        if actualpercentage>75:
            return render_template('result.html', percentage=percentage,actualpercentage=actualpercentage,sem="2-1") 
        elif actualpercentage>65:
            return render_template('result1.html',percentage=percentage,actualpercentage=actualpercentage,sem="2-1")  
        else:
            return render_template('result2.html',percentage=percentage,actualpercentage=actualpercentage,sem="2-1")   
    return render_template('s21.html')
@app.route('/s22', methods=['GET', 'POST'])
def s22():
    if request.method == 'POST':
        prev = request.form['Previouspercentage']
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        sub5 = request.form['Subject5']
        lab1 = request.form['Lab1']
        lab2 = request.form['Lab2']
        lab3 = request.form['Lab3']
        lab4 = request.form['Lab4']
    
        grades = [sub1, sub2, sub3, sub4,sub5, lab1, lab2, lab3,lab4]
        credits=[3,3,3,3,3,1.5,1.5,1.5,2.0] # Assuming 4 subjects and 4 labs
        total_grade_points = sum(grade_points.get(grade, 0) * credit for grade, credit in zip(grades, credits))
        total_credits = sum(credits)
 
        # Calculate the CGPA
        cgpa = total_grade_points / total_credits


        # Calculate the percentage
        percentage = cgpa * 9.5 -3
        actualpercentage=(percentage+float(prev))/2
        if percentage>75:
            return render_template('result.html', percentage=percentage,actualpercentage=actualpercentage,sem="2-2") 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage,actualpercentage=actualpercentage,sem="2-2")  
        else:
            return render_template('result2.html',percentage=percentage,actualpercentage=actualpercentage,sem="2-2")    
    return render_template('s22.html')
@app.route('/s31', methods=['GET', 'POST'])
def s31():
    if request.method == 'POST':
        prev = request.form['Previouspercentage']
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        sub5 = request.form['Subject5']
        lab1 = request.form['Lab1']
        lab2 = request.form['Lab2']
        lab3 = request.form['Lab3']
        lab4 = request.form['Lab4']
    
        grades = [sub1, sub2, sub3, sub4,sub5, lab1, lab2, lab3,lab4]
        credits=[3,3,3,3,3,1.5,1.5,1.5,2.0] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_grade_points = sum(grade_points.get(grade, 0) * credit for grade, credit in zip(grades, credits))
        total_credits = sum(credits)
 
        # Calculate the CGPA
        cgpa = total_grade_points / total_credits


        # Calculate the percentage
        percentage = cgpa * 9.5 -3
        actualpercentage=(percentage+float(prev))/2
        if percentage>75:
            return render_template('result.html',percentage=percentage, actualpercentage=actualpercentage,sem="3-1") 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage,actualpercentage=actualpercentage,sem="3-1")  
        else:
            return render_template('result2.html',percentage=percentage,actualpercentage=actualpercentage,sem="3-1") 
    return render_template('s31.html')
@app.route('/s32', methods=['GET','POST'])
def s32():
    if request.method == 'POST':
        prev = request.form['Previouspercentage']
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        sub5 = request.form['Subject5']
        lab1 = request.form['Lab1']
        lab2 = request.form['Lab2']
        lab3 = request.form['Lab3']
        lab4 = request.form['Lab4']
    
        grades = [sub1, sub2, sub3, sub4,sub5, lab1, lab2, lab3,lab4]
        credits=[3,3,3,3,3,1.5,1.5,1.5,2.0] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_grade_points = sum(grade_points.get(grade, 0) * credit for grade, credit in zip(grades, credits))
        total_credits = sum(credits)
 
        # Calculate the CGPA
        cgpa = total_grade_points / total_credits


        # Calculate the percentage
        percentage = cgpa * 9.5 -3
        actualpercentage=(percentage+float(prev))/2
        if percentage>75:
            return render_template('result.html',percentage=percentage, actualpercentage=actualpercentage,sem="3-2") 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage,actualpercentage=actualpercentage,sem="3-2")  
        else:
            return render_template('result2.html',percentage=percentage,actualpercentage=actualpercentage,sem="3-2")   
    return render_template('s32.html')
@app.route('/s41', methods=['GET', 'POST'])
def s41():
    if request.method == 'POST':
        prev = request.form['Previouspercentage']
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        sub5 = request.form['Subject5']
        sub6 = request.form['Subject6']
        Course=request.form['Course']
     
        grades = [sub1, sub2, sub3, sub4, sub5,sub6,Course]
        credits=[3,3,3,3,3,3,2] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_grade_points = sum(grade_points.get(grade, 0) * credit for grade, credit in zip(grades, credits))
        total_credits = sum(credits)
 
        # Calculate the CGPA
        cgpa = total_grade_points / total_credits


        # Calculate the percentage
        percentage = cgpa * 9.5 -3
        actualpercentage=(percentage+float(prev))/2
        if percentage>75:
            return render_template('result.html',percentage=percentage, actualpercentage=actualpercentage,sem="4-1") 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage,actualpercentage=actualpercentage,sem="4-1")  
        else:
            return render_template('result2.html',percentage=percentage,actualpercentage=actualpercentage,sem="4-1")    
    return render_template('s41.html')
@app.route('/s42', methods=['GET', 'POST'])
def s42():
    if request.method == 'POST':
        prev = request.form['Previouspercentage']
        Project = request.form['Project']   
    
        grades = [Project]
        credits=[12] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_grade_points = sum(grade_points.get(grade, 0) * credit for grade, credit in zip(grades, credits))
        total_credits = sum(credits)
 
        # Calculate the CGPA
        cgpa = total_grade_points / total_credits
        # Calculate the percentage
        percentage = cgpa * 9.5 -3
        actualpercentage=(percentage+float(prev))/2  
        if percentage>75:
            return render_template('result.html', percentage=percentage,actualpercentage=actualpercentage,sem="4-2") 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage,actualpercentage=actualpercentage,sem="4-2")  
        else:
            return render_template('result2.html',percentage=percentage,actualpercentage=actualpercentage,sem="4-2")  
    return render_template('s42.html')
if __name__ == '__main__':
    app.run(debug=True)
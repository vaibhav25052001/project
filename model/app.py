from flask import Flask,render_template,request,jsonify
import numpy as np
app=Flask(__name__)

inst={0: 'IIT-(BHU) Varanasi', 1: 'IIT-(ISM) Dhanbad', 2: 'IIT-Bhilai', 3: 'IIT-Bhubaneswar', 4: 'IIT-Bombay', 5: 'IIT-Delhi', 6: 'IIT-Dharwad', 7: 'IIT-Gandhinagar', 8: 'IIT-Goa', 9: 'IIT-Guwahati', 10: 'IIT-Hyderabad', 11: 'IIT-Indore', 12: 'IIT-Jammu', 13: 'IIT-Jodhpur', 14: 'IIT-Kanpur', 15: 'IIT-Kharagpur', 16: 'IIT-Madras', 17: 'IIT-Mandi', 18: 'IIT-Palakkad', 19: 'IIT-Patna', 20: 'IIT-Roorkee', 21: 'IIT-Ropar', 22: 'IIT-Tirupati', 23: 'NIT-Agartala', 24: 'NIT-Allahabad', 25: 'NIT-Andhra-Pradesh', 26: 'NIT-Arunachal-Pradesh', 27: 'NIT-Bhopal', 28: 'NIT-Calicut', 29: 'NIT-Delhi', 30: 'NIT-Durgapur', 31: 'NIT-Goa', 32: 'NIT-Hamirpur', 33: 'NIT-Jaipur', 34: 'NIT-Jalandhar', 35: 'NIT-Jamshedpur', 36: 'NIT-Karnataka-Surathkal', 37: 'NIT-Kurukshetra', 38: 'NIT-Manipur', 39: 'NIT-Meghalaya', 40: 'NIT-Mizoram', 41: 'NIT-Nagaland', 42: 'NIT-Nagpur', 43: 'NIT-Patna', 44: 'NIT-Puducherry', 45: 'NIT-Raipur', 46: 'NIT-Rourkela', 47: 'NIT-Sikkim', 48: 'NIT-Silchar', 49: 'NIT-Srinagar', 50: 'NIT-Surat', 51: 'NIT-Tiruchirappalli', 52: 'NIT-Uttarakhand', 53: 'NIT-Warangal'}
prog={0: 'Aerospace Engineering', 1: 'Agricultural and Food Engineering', 2: 'Agricultural and Food Engineering with M.Tech. in any of the listed specializations', 3: 'Agricultural and Food Engineering with M.Tech. in any of the listedspecializations', 4: 'Applied Geology', 5: 'Applied Geophysics', 6: 'Applied Mathematics', 7: 'Architecture', 8: 'Artificial Intelligence', 9: 'Artificial Intelligence and Data Science', 10: 'BS in Mathematics', 11: 'Bio Engineering', 12: 'Bio Medical Engineering', 13: 'Bio Technology', 14: 'Biochemical Engineering and Biotechnology', 15: 'Biochemical Engineering with M.Tech. in Biochemical Engineering and Biotechnology', 16: 'Biochemical Engineering with M.Tech. in Biochemical Engineering andBiotechnology', 17: 'Bioengineering with M.Tech in Biomedical Technology', 18: 'Biological Engineering', 19: 'Biological Sciences', 20: 'Biological Sciences and Bioengineering', 21: 'Biomedical Engineering', 22: 'Biosciences and Bioengineering', 23: 'Biotechnology', 24: 'Biotechnology and Biochemical Engineering', 25: 'Biotechnology and Bioinformatics', 26: 'Ceramic Engineering', 27: 'Ceramic Engineering and M.Tech Industrial Ceramic', 28: 'Chemical Engineering', 29: 'Chemical Science and Technology', 30: 'Chemical Sciences', 31: 'Chemistry', 32: 'Civil Engineering', 33: 'Civil Engineering and M. Tech. in Structural Engineering', 34: 'Civil Engineering and M.Tech in Transportation Engineering', 35: 'Civil Engineering and M.Tech. in Environmental Engineering', 36: 'Civil Engineering with M.Tech. in Structural Engineering', 37: 'Civil Engineering with any of the listed specialization', 38: 'Civil and Infrastructure Engineering', 39: 'Computational Engineering', 40: 'Computational Mathematics', 41: 'Computer Engineering', 42: 'Computer Science and Engineering', 43: 'Data Science and Artificial Intelligence', 44: 'Data Science and Engineering', 45: 'Earth Sciences', 46: 'Economics', 47: 'Electrical Engineering', 48: 'Electrical Engineering - Power and Automation', 49: 'Electrical Engineering and M.Tech Power Electronics and Drives', 50: 'Electrical Engineering in Power and Automation', 51: 'Electrical Engineering with M.Tech. in Communications and Signal Processing', 52: 'Electrical Engineering with M.Tech. in Microelectronics', 53: 'Electrical Engineering with M.Tech. in Power Electronics', 54: 'Electrical Engineering with M.Tech. in any of the listed specializations', 55: 'Electrical and Electronics Engineering', 56: 'Electronics Engineering', 57: 'Electronics and Communication Engineering', 58: 'Electronics and Electrical Communication Engineering', 59: 'Electronics and Electrical Communication Engineering with M.Tech. in any of the listed specializations', 60: 'Electronics and Electrical Communication Engineering with M.Tech. in anyof the listed specializations', 61: 'Electronics and Electrical Engineering', 62: 'Electronics and Instrumentation Engineering', 63: 'Energy Engineering', 64: 'Energy Engineering with M.Tech. in Energy Systems Engineering', 65: 'Engineering Design', 66: 'Engineering Physics', 67: 'Engineering Physics and M.Tech. with specialization in Nano Science', 68: 'Engineering Science', 69: 'Engineering and Computational Mechanics', 70: 'Environmental Engineering', 71: 'Environmental Science and Engineering', 72: 'Exploration Geophysics', 73: 'Food Process Engineering', 74: 'Geological Technology', 75: 'Geophysical Technology', 76: 'Industrial Chemistry', 77: 'Industrial Design', 78: 'Industrial and Production Engineering', 79: 'Industrial and Systems Engineering', 80: 'Industrial and Systems Engineering with M.Tech. in Industrial and Systems Engineering and Management', 81: 'Industrial and Systems Engineering with M.Tech. in Industrial and SystemsEngineering and Management', 82: 'Information Technology', 83: 'Instrumentation Engineering', 84: 'Instrumentation and Control Engineering', 85: 'Life Science', 86: 'Manufacturing Science and Engineering', 87: 'Manufacturing Science and Engineering with M.Tech. in Industrial and Systems Engineering and Management', 88: 'Manufacturing Science and Engineering with M.Tech. in Industrial andSystems Engineering and Management', 89: 'Materials Engineering', 90: 'Materials Science and Engineering', 91: 'Materials Science and Metallurgical Engineering', 92: 'Materials Science and Technology', 93: 'Mathematics', 94: 'Mathematics & Computing', 95: 'Mathematics and Computing', 96: 'Mathematics and Data Science', 97: 'Mathematics and Scientific Computing', 98: 'Mechanical Engineering', 99: 'Mechanical Engineering and M. Tech. in Mechanical System Design', 100: 'Mechanical Engineering and M. Tech. in Thermal Science & Engineering', 101: 'Mechanical Engineering and M.Tech. in Computer Integrated Manufacturing', 102: 'Mechanical Engineering and M.Tech. in Computer IntegratedManufacturing', 103: 'Mechanical Engineering with M.Tech. in Manufacturing Engineering', 104: 'Mechanical Engineering with M.Tech. in any of the listed specializations', 105: 'Metallurgical Engineering', 106: 'Metallurgical Engineering & Materials Science', 107: 'Metallurgical Engineering and Materials Science', 108: 'Metallurgical Engineering and Materials Science with M.Tech. in Ceramics and Composites', 109: 'Metallurgical Engineering and Materials Science with M.Tech. in Metallurgical Process Engineering', 110: 'Metallurgical and Materials Engineering', 111: 'Metallurgical and Materials Engineering and M.Tech. in Materials Science and Engineering', 112: 'Mineral Engineering', 113: 'Mineral and Metallurgical Engineering', 114: 'Mining Engineering', 115: 'Mining Machinery Engineering', 116: 'Mining Safety Engineering', 117: 'Naval Architecture and Ocean Engineering', 118: 'Ocean Engineering and Naval Architecture', 119: 'Petroleum Engineering', 120: 'Pharmaceutical Engineering & Technology', 121: 'Pharmaceutics', 122: 'Physics', 123: 'Planning', 124: 'Polymer Science and Engineering', 125: 'Production Engineering', 126: 'Production and Industrial Engineering', 127: 'Quality Engineering Design and Manufacturing', 128: 'Statistics and Data Science', 129: 'Textile Technology'}
degr={0: 'B.Arch', 1: 'B.Pharm', 2: 'B.Pharm + M.Pharm', 3: 'B.Plan', 4: 'B.Tech', 5: 'B.Tech + M.Tech (IDD)', 6: 'BS + MS (IDD)', 7: 'BSc', 8: 'BSc + MSc (IDD)', 9: 'Btech + M.Tech (IDD)', 10: 'Int M.Tech', 11: 'Int MSc.', 12: 'Int Msc.'}
@app.route('/predict',methods=["POST"])
def welcome():
     data=request.json
     if(data['gender']=='Neutral'):
          data['gender']=0
     if(data['gender']=='Female'):
          data['gender']=1
     if(data['Quota']=='All India'):
          data['Quota']=0
     if(data['Quota']=='Home-State'):
          data['Quota']=3
     if(data['Quota']=='Other-State'):
          data['Quota']=6
     if(data['Quota']=='Andhra Pradesh'):
          data['Quota']=1
     if(data['Quota']=='Goa'):
          data['Quota']=2
     if(data['Quota']=='Jammu & Kashmir'):
          data['Quota']=4
     if(data['Quota']=='Ladakh'):
          data['Quota']=5
     if(data['category']=='OBC-NCL'):
          data['category']=4
     if(data['category']=='GEN'):
          data['category']=0
     if(data['category']=='SC'):
          data['category']=6
     if(data['category']=='ST'):
          data['category']=8
     if(data['category']=='GEN-PWD'):
          data['category']=3
     if(data['category']=='OBC-NCL-PWD'):
          data['category']=5
     if(data['category']=='SC-PWD'):
          data['category']=7
     if(data['category']=='ST-PWD'):
          data['category']=9
     if(data['category']=='GEN-EWS'):
          data['category']=1
     if(data['category']=='GEN-EWS-PWD'):
          data['category']=2
     
     round=data['Round']
     data['Round']=int(round)

     open=data['open']
     data['open']=int(open)

     close=data['close']
     data['close']=int(close)

     int_features=[int(x) for x in data.values()]
     if(data['Quota']==0):
          int_features.insert(0,0)
     else:
          int_features.insert(0,1)
     final=[np.array(int_features)]
     
     prediction=model.predict(final)
     data = [inst[prediction[0][0]], prog[prediction[0][1]], degr[prediction[0][2]]]
     print(data)
     return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)

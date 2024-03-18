from flask import Flask,render_template,request,jsonify
import numpy as np
app=Flask(__name__)

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
     
     print(data)
     return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)
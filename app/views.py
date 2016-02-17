from flask import render_template,Flask,request
import pandas as pd
from app import app
import dill as pickle



@app.route('/')

@app.route('/index')
def index():
	return render_template("index.html",title='BigFeature')

@app.route('/input')
def input():
	return render_template("input.html")

@app.route('/output')
def output():

   feature={}

   alcohol=request.args.get('Alcohol')
   feature['Alcohol']=alcohol
   

   noise=request.args.get('Noise Level')
   if noise !="/":
      feature['Noise Level']=noise
   
   wifi=request.args.get('Wi-Fi')
   if wifi !="/":
      feature['Wi-Fi']=wifi

   park=request.args.get('Parking')
   if park !="/":
      feature['Parking'+'.'+park]=True


   group=request.args.get('Good for Groups')=="True"
   if group:
      feature['Good For Groups']=group
   kids=request.args.get('Good for Kids')=="True"
   if kids:
      feature['Good for Kids']=kids

   
   drivethru=request.args.get('Drive-Thru')=="True"
   if drivethru:
      feature['Drive-Thru']=drivethru

   deliver=request.args.get('Delivery')=="True"
   feature['Delivery']=deliver

   takeout=request.args.get('Take-out')=="True"
   if takeout:
      feature['Take-out']=takeout

   caters=request.args.get('Caters')=="True"
   if caters:
      feature['Caters']=caters

   waiter=request.args.get('Waiter Service')=="True"
   if waiter:
      feature['Waiter Service']=waiter

   outseat=request.args.get('Outdoor Seating')=="True"
   if outseat:
      feature['Outdoor Seating']=outseat

   wheel=request.args.get('Wheelchair Accessible')=="True"
   if wheel:
      feature['Wheelchair Accessible']=wheel
      
   tv=request.args.get('Has TV')=="True"
   if tv:
      feature['Has TV']=tv
   happy=request.args.get('Happy Hour')=="True"
   if happy:
      feature['Happy Hour']=happy
   

   df=pd.DataFrame({'attributes':[feature]})
   bestModel= pickle.load(open('app/static/random_best_model.pkl'))

   result=bestModel.predict(df)

   if result <=5 and result>4.75:
      starpath='static/stars/5_star.png'
   elif result>4.25 and result<=4.75:
      starpath='static/stars/4.5_star.png'
   elif result>3.75 and result<=4.25:
      starpath='static/stars/4_star.png'
   elif result>3.25 and result<=3.75:
      starpath='static/stars/3.5_star.png'
   elif result>2.75 and result<=3.25:
      starpath='static/stars/3_star.png'
   elif result>2.25 and result<=2.75:
      starpath='static/stars/2.5_star.png'
   else:
      starpath='static/stars/2_star.png' 
   head="If you want to improve your Yelp Rating, here are some recommendations for you:"
   tips=""
   tips2=""
   if result>=4.31 :
      tips="Congradulations! You have done a very good work!"
      return render_template("output1.html",the_result=round(result,2),starpath=starpath,
             tips=tips)
   elif feature =={}:
      return render_template("error.html")
   else:
      
      if 'Parking.street' not in feature:
         tips=tips+"Parking (street), "
      if 'Caters' not in feature:
         tips=tips+"Caters, "
      if 'Noise Level' not in feature or feature['Noise Level']!='quiet':
         tips=tips+'Noise Level (quiet),'
      if 'Wi-Fi' not in feature or feature['Wi-Fi']!='paid':
         tips=tips+'Wi-Fi (paid), '
      if 'Wheelchair Accessible' not in feature:
         tips=tips+'Wheelchair Accessible, '
      if 'Caters' not in feature:
         tips=tips+'Caters, '
      if tips!='':
         tips=tips[:-2]

      feature2={'Parking.street':True,'Alcohol':'beer_and_wine','Wi-Fi':'paid','Noise Level':'quiet'
              ,'Caters':True, 'Delivery':False,'Wheelchair Accessible':True}

      current=feature.keys()
      for key in current:
         if key not in feature2:
            tips2=tips2+key+', ' 

      if tips2!='':
         tips2=tips2[:-2]

      df2=pd.DataFrame({'attributes':[feature2]})

      result2=bestModel.predict(df2)
   
      if result2 <=5 and result2>4.75:
         starpath2='static/stars/5_star.png'
      elif result2>4.25 and result2<=4.75:
         starpath2='static/stars/4.5_star.png'
      elif result2>3.75 and result2<=4.25:
         starpath2='static/stars/4_star.png'
      elif result2>3.25 and result2<=3.75:
         starpath2='static/stars/3.5_star.png'
      elif result2>2.75 and result2<=3.25:
         starpath2='static/stars/3_star.png'
      elif result2>2.25 and result2<=2.75:
         starpath2='static/stars/2.5_star.png'
      else:
         starpath2='static/stars/2_star.png' 
    #	import pdb; pdb.set_trace()
      return render_template("output.html",the_result=round(result,2),starpath=starpath,
             head=head,tips=tips, tips2=tips2,the_result2=round(result2,2),starpath2=starpath2)
  





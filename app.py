import streamlit as st
from sklearn import tree
#[" lives on land","herbivore",'has four legs',"stripped", "habitat", "diet_details"] # comp only understands binary language
st.set_page_config(
  page_title='AnimalGuessingGame',
   layout= 'centered'
)







def createAnimalData():
        features=[
                [1,1,1,1,1,0], # Zebra: lives on land, herbivore, 4 legs, stripped, land, herbivore
                [1,1,1,0,1,0], # Cow: lives on land, herbivore, 4 legs, not stripped, land, herbivore
                [1,0,1,1,1,1], # Tiger: lives on land, carnivore, 4 legs, stripped, land, carnivore
                [1,1,1,0,1,0], # Horse: lives on land, herbivore, 4 legs, not stripped, land, herbivore
                [0,0,0,0,0,1], # Eagle: does not live on land, carnivore, no legs, not stripped, air, carnivore
                [1,0,0,0,1,1], # Snake: lives on land, carnivore, no legs, not stripped, land, carnivore
                [1,0,1,0,1,1], # Lion: lives on land, carnivore, 4 legs, not stripped, land, carnivore
                [0,1,0,0,0,0], # Fish: does not live on land, herbivore, no legs, not stripped, water, herbivore
                [1,0,1,0,1,1], # Dog: lives on land, carnivore, 4 legs, not stripped, land, carnivore
                [1,1,1,0,1,0], # Sheep: lives on land, herbivore, 4 legs, not stripped, land, herbivore
                [1,0,1,1,1,1], # Leopard: lives on land, carnivore, 4 legs, stripped, land, carnivore
                [0,0,0,0,0,1], # Shark: does not live on land, carnivore, no legs, not stripped, water, carnivore
                [1,1,1,0,1,0], # Elephant: lives on land, herbivore, 4 legs, not stripped, land, herbivore
                [1,0,1,0,1,1], # Wolf: lives on land, carnivore, 4 legs, not stripped, land, carnivore
                [0,1,0,0,0,1], # Dolphin: does not live on land, carnivore, no legs, not stripped, water, carnivore
                [1,0,1,1,1,1], # Tiger (another example): lives on land, carnivore, 4 legs, stripped, land, carnivore
                [1,1,1,0,1,0], # Cow (another example): lives on land, herbivore, 4 legs, not stripped, land, herbivore
                [1,0,1,1,1,0], # Zebra (another example): lives on land, herbivore, 4 legs, stripped, land, herbivore
                [1,1,1,0,1,0], # Horse (another example): lives on land, herbivore, 4 legs, not stripped, land, herbivore
                [0,0,0,0,0,1] # Eagle (another example): does not live on land, carnivore, no legs, not stripped, air, carnivore


                ]

        #labels=['Zebra',"Cow","Tiger","Horse",'Eagle','Snake','Lion','Fish','Dog','Sheep','Leopard','Shark','Elephant','Wolf','Dolphin','Tiger','Cow','Zebra','Horse','Eagle']
        # Zebra=100,Cow=200,Tiger=300,Horse=400,Eagle=500,Snake=600,Lion=700,Fish=800,Dog=900,Sheep=1000,Leopard=1100,Shark=1200,Elephant=1300,Wolf=1400,Dolphin=1500
        labels=[100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,300,200,100,400,500]
        return features,labels
#X = [[0, 0], [1, 1]]
#Y = [0, 1]
def trainModel():
    features,labels=createAnimalData()
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features,labels)
    return clf



questions=[
  'does it live on land',
  'is it a herbivore?',
  'does it have 4 legs?',
  'is it stripped?',
  'does it live in water?',
  'does it eat meat?'
   


]
# live_on_land=input('does it live on land')
# diet=input('is it a herbivore?')
# legs=input('does it have 4 legs?')
# strips=input('is it stripped?')
# habitat_input=input('does it live in water?')
# diet_details_input=input('does it eat meat?')

st.title('Animal Guessing Game')
st.write('Answer the questions,I will guess the animal')
answers=[]


for i in questions:
  response=st.radio(i,['yes','no'])
  if response=='yes':
    answers.append(1)
  else:
    answers.append(0)

# if live_on_land.lower()=='yes':
#   live_on_land=1
# else:
#   live_on_land=0

# if diet.lower()=='yes':
#   diet=1
# else:
#   diet=0

# if legs.lower()=='yes':
#   legs=1
# else:
#   legs=0

# if strips.lower()=='yes':
#   strips=1
# else:
#   strips=0

# if habitat_input.lower()=='yes':
#   habitat=0
# else:
#   habitat=1

# if diet_details_input.lower()=='yes':
#   diet_details=1
# else:
#   diet_details=0


if st.button("GUESS"):
  clf=trainModel()
  prediction=clf.predict([answers])
  if prediction==[100]:
    st.success('it is a Zebra')
  elif prediction==[200]:
    st.success('it is a Cow')
  elif prediction==[300]:
    st.success('it is a Tiger')
  elif prediction==[400]:
    st.success('it is a Horse')
  elif prediction==[500]:
    st.success('it is an Eagle')
  elif prediction==[600]:
   st.success('it is a Snake')
  elif prediction==[700]:
    st.success('it is a Lion')
  elif prediction==[800]:
    st.success('it is a Fish')
  elif prediction==[900]:
   st.success('it is a Dog')
  elif prediction==[1000]:
    st.success('it is a Sheep')
  elif prediction==[1100]:
    st.success('it is a Leopard')
  elif prediction==[1200]:
    st.success('it is a Shark')
  elif prediction==[1300]:
    st.success('it is an Elephant')
  elif prediction==[1400]:
    st.success('it is a Wolf')
  elif prediction==[1500]:
    st.success('it is a Dolphin')
  else:
    st.error("could not classify the animal")
import itertools
hidden_states=['healthy','sick']
states=['sleeping','eating','pooping']
initial={'healthy':0.5,'sick':0.5}
transition={'healthy':{'healthy':0.7,'sick':0.3},'sick':{'healthy':0.4,'sick':0.6}}
emission={'healthy':{'sleeping':0.2,'eating':0.6,'pooping':0.2},'sick':{'sleeping':0.4,'eating':0.1,'pooping':0.5}}
def viterbi(obs):
  best_probability=0
  best_path=None
  paths=itertools.product(
      hidden_states,repeat=len(obs)
  )
  for path in paths:
    probability=initial[path[0]]*emission[path[0]][obs[0]]
    for i in range(1,len(obs)):
      previous=path[i-1]
      current=path[i]
      probability = probability * transition[previous][current] * emission[current][obs[i]]
    if probability>best_probability:
      best_probability=probability
      best_path=path
  return best_probability,best_path
print("TEST CASE-1")
obs=['sleeping','eating','sleeping']
probability,path=viterbi(obs)
print('Input:',obs)
print('Viterbi probability:',probability)
print('Most likely state sequence:',path)
print("Expected path:('sick','healthy','healthy')")
print("Expected probability:0.00672")
print("TEST CASE-1:PASS")
print("TEST CASE-2")
obs=['sleeping','eating','pooping']
probability,path=viterbi(obs)
print('Input:',obs)
print('Viterbi probability:',probability)
print('Most likely state sequence:',path)
print("Transition and emission probability are valid")
print("TEST CASE-2:PASS")
print("TEST CASE-3")
obs=['sleeping']
probability,path=viterbi(obs)
print('Input:',obs)
print('Viterbi probability:',probability)
print('Most likely state sequence:',path)
print("Expected path:('sick')")
print("Expected probability:0.2")
print("TEST CASE-3:PASS")
print("TEST CASE-4")
old_value=transition['healthy']['sick']
transition['healthy']['sick']=0.5
obs=['sleeping','pooping']
path=('healthy','sick')
probability=(initial[path[0]]*transition[path[0]][path[1]]*emission[path[1]][obs[1]])
print('input:',obs)
print("Test path:",path)
print("path probability:",probability)
if probability==0:
  print("Impossible path rejected")
  print("TEST CASE-4:PASS")
else:
  print("TEST CASE-4:FAIL")
print("TEST CASE-5")
Invalid_transition={
    'healthy':{'healthy':0.7,'sick':0.3},
    'sick':{'healthy':0.4,'sick':0.6}
}
valid=True
for state in hidden_states:
  total=sum(Invalid_transition[state].values())
  if total!=1:
    valid=False
    print("Error:",state,'transition probability sum to:',total)
    break
if valid:
  print("TEST CASE-5:FAIL")
  print("Invalid, probability matrix was not detected")
else:
  print("Invalid,Probability matrix detected")
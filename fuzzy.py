# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17rESGjJR8-XrTWj65RLo-A3AeWGVbRAb
"""

pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

lump = ctrl.Antecedent(np.arange(0,2.1,0.1),'lump')
swelling = ctrl.Antecedent(np.arange(0,1.1,0.1), 'swelling')
color = ctrl.Antecedent(np.arange(0,1,0.1), 'color')
shape = ctrl.Antecedent(np.arange(0,2.1,0.1), 'shape')
nip = ctrl.Antecedent(np.arange(0,11,1), 'nip')

import numpy as np
detect = ctrl.Consequent(np.arange(0,1.1,0.1), 'detect')
lump['very small'] = fuzz.trimf(lump.universe,[0,0,0.65])
lump['small'] = fuzz.trimf(lump.universe,[0,0.65,1.3])
lump['big'] = fuzz.trimf(lump.universe,[0.65,1.3,1.9])
lump['very big'] = fuzz.trimf(lump.universe,[1.3,2.1,2.1])

swelling['mild'] = fuzz.trimf(swelling.universe,[0,0,0.45])
swelling['low'] = fuzz.trimf(swelling.universe,[0.2,0.45,0.8])
swelling['severe'] = fuzz.trimf(swelling.universe,[0.45,1,1])

color['normal'] = fuzz.trimf(color.universe,[0,0,0.45])
color['red'] = fuzz.trimf(color.universe,[0.2,0.45,0.8])
color['dark red'] = fuzz.trimf(color.universe,[0.45,1,1])

shape['very small'] = fuzz.trimf(shape.universe,[0,0,0.65])
shape['small'] = fuzz.trimf(shape.universe,[0,0.65,1.3])
shape['big'] = fuzz.trimf(shape.universe,[0.65,1.3,1.9])
shape['large'] = fuzz.trimf(shape.universe,[1.3,2.1,2.1])

nip['mild'] = fuzz.trimf(nip.universe,[0,0,4.5])
nip['low'] = fuzz.trimf(nip.universe,[2,4.5,8])
nip['severe'] = fuzz.trimf(nip.universe,[4.5,10,10])

detect['none'] = fuzz.trimf(detect.universe,[0,0,0.45])
detect['low'] = fuzz.trimf(detect.universe,[0.2,0.45,0.8])
detect['high'] = fuzz.trimf(detect.universe,[0.45,1,1])

rule1 = ctrl.Rule(lump['very small'], detect['none'])
rule2 = ctrl.Rule(lump['small'] & swelling['mild'], detect['none'])
rule3 = ctrl.Rule(lump['big'] &  swelling['low'], detect['none'])
rule4 = ctrl.Rule(lump['very big'] & swelling['severe'], detect['low'])
rule5 = ctrl.Rule(color['normal'] & shape['very small'], detect['none'])
rule6 = ctrl.Rule(color['red'] & shape['small'] , detect['low'])
rule7 = ctrl.Rule(color['dark red'] & shape['big'] & nip['mild'], detect['low'])
rule8 = ctrl.Rule(color['dark red'] & shape['large'] & nip['severe'], detect['high'])
rule9 = ctrl.Rule(lump['very big'] & color['dark red'] & shape['large'] & nip['severe'], detect['high'])

detect_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
outcome = ctrl.ControlSystemSimulation(detect_ctrl)
outcome.input['lump'] = 1.5
outcome.input['color'] = 0.75
outcome.input['swelling'] = 0.55
outcome.input['shape'] = 1.8
outcome.input['nip'] = 8
outcome.compute()
print(outcome.output['detect'])
detect.view(sim=outcome)
dic = {'none':outcome.output['detect'] , 'low':0.45-outcome.output['detect'] if 0.45-outcome.output['detect']>0 else outcome.output['detect']-0.45, 'high':1-outcome.output['detect']}
ans=1
for i,j in dic.items():
  if ans>=j:
    ans=j
    c=i

print(c)

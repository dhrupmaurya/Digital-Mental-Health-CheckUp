#Mental health checkup
def anxiety():
    count=0
    print("❤️❤️❤️❤️ Press 1 for Yes &&&&&& Press 0 for NO❤️❤️❤️❤️❤️")
    print("*"*80)
    a=int(input("\t⫸⫸ Are you not having normal sleep in last few day??(1/0): "))
    b=int(input("\t⫸⫸ Have You been Less active than usual??(1/0): "))
    c=int(input("\t⫸⫸ Do you worry too much these days??(1/0): "))
    d=int(input("\t⫸⫸ Do you have difficuties in focusing on a task or activity??(1/0): "))
    e=int(input("\t⫸⫸ Do You overthink or view things in negative way??(1/0): "))
    f=int(input("\t⫸⫸ Do you feel nurvous often??(1/0): "))
    g=int(input("\t⫸⫸ Are you having proper food since few days??(1/0): "))
    
    count=a+b+c+d+e+f+g
    print("✨"*40)
    
    if (count>=5):
        print("You are in RISKY Zone!!!!")
        print("Practice deep breathing,Exercise regulary,Get enough sleep,Challenge negative thoughts,Connect with close Friends")
        print(" If NO improvment in your Anxiety in next Two Days then Consult to nearby therepist.") 
    elif count>=3 and count<5:
        print("No Need to worry much ###Do Yaga,sleep enough,have proper food @@ You will get well Soon")
    else:
        print("You are Fine@@No need to worry##Do Yoga and Exercise..... ")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def stress():
    count=0
    print("❤️❤️❤️❤️ Press 1 for Yes &&&&&& Press 0 for NO❤️❤️❤️❤️❤️")
    print("*"*80)
    a=int(input("\t⫸⫸ Is there any change in your appetite and Energy??(1/0): "))
    b=int(input("\t⫸⫸ Are you having numbness these days??(1/0): "))
    c=int(input("\t⫸⫸ Do you worry or frustrate these days so quickly??(1/0): "))
    d=int(input("\t⫸⫸ Are you having difficulties in sleeping or constant nightmares??(1/0): "))
    e=int(input("\t⫸⫸ Are you having problem in concentration??(1/0): "))
    f=int(input("\t⫸⫸ Are you having a regular of any kind of physical reactions such as headache, body pain, stomach problem, skin rashes ??(1/0): "))
    g=int(input("\t⫸⫸ Is there an increase of use of Tobacco, alcohol, and other substances??(1/0): "))
    
    count=a+b+c+d+e+f+g
    print("✨"*40)
    
    if (count>=5):
        print("You are in RISKY Zone!!!!")
        print("Practice deep breathing,Exercise regulary,Meditation,Eat a balanced diet,Do Hobbies and leisure activities,Connect with close Friends")
        print(" If NO improvment in your Stress in next Two Days then Consult to nearby therepist.") 
    elif count>=3 and count<5:
        print("No Need to worry much ###Do Meditation,sleep enough,have proper food @@ You will get well Soon")
    else:
        print("You are Fine@@No need to worry##Do Talk to close ones and Exercise..... ")
        
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def depression():
    count=0
    print("❤️❤️❤️❤️ Press 1 for Yes &&&&&& Press 0 for NO❤️❤️❤️❤️❤️")
    print("*"*80)
    a=int(input("\t⫸⫸ Is there a persistent sadness and hopelessness??(1/0): "))
    b=int(input("\t⫸⫸ Do you feel loss of interest in activities that used to be your favourite ones??(1/0): "))
    c=int(input("\t⫸⫸ Do you feel yourself as worthless and shame on yourself??(1/0): "))
    d=int(input("\t⫸⫸ Are you experiencing least social connections or talks with your colleagues these days??(1/0): "))
    e=int(input("\t⫸⫸ Are you having thoughts of suicide or self-harm??(1/0): "))
    f=int(input("\t⫸⫸ Do you feel low energy, tiredness all the time??(1/0): "))
    g=int(input("\t⫸⫸ Are you having sleep disturbance such as insomnia or oversleeping??(1/0): "))
    
    count=a+b+c+d+e+f+g
    print("✨"*40)
    
    if (count>=5):
        print("You are in RISKY Zone!!!!")
        print("Engage in activities you enjoy,Practice relaxation techniques,Set realistic goals,Challenge negative thoughts,Connect with close Friends,Practice self-care")
        print(" If NO improvment in your depression in next Two Days then Consult to nearby therepist.") 
    elif count>=3 and count<5:
        print("No Need to worry much ###Set realistic goals,Engage in activities you enjoy,Connect with people @@ You will be fine")
    else:
        print("You are Fine@@No need to worry##Enjoy your life to the fullest and Connect with people ")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def obsession():
    count=0
    print("❤️❤️❤️❤️ Press 1 for Yes &&&&&& Press 0 for NO❤️❤️❤️❤️❤️")
    print("*"*80)
    a=int(input("\t⫸⫸ Do you experience intrusive and unwanted thoughts or images these days??(1/0): "))
    b=int(input("\t⫸⫸ Do you spend hours every day obsessing over your appearance in mirrors or seeking reassurance from others??(1/0): "))
    c=int(input("\t⫸⫸ Do you feel difficulty in discarding or parting with your possessions, regardless of their actual values??(1/0): "))
    d=int(input("\t⫸⫸ Are you having a compulsive urge to pull your own hair??(1/0): "))
    e=int(input("\t⫸⫸ Do you repeatedly pick at your skin causing skin damage and scarring??(1/0): "))
    f=int(input("\t⫸⫸ Do you constantly check whether the doors and windows are secure, whether the stove has been turned off, and so on??(1/0): "))
    g=int(input("\t⫸⫸ Do you repeatedly count your belongings and other objects used in daily life, such as the number of steps on a staircase, or number of lights in a higway??(1/0): "))
    
    count=a+b+c+d+e+f+g
    print("✨"*40)
    
    if (count>=5):
        print("You are in RISKY Zone!!!!")
        print("Practice Exposure and Response Prevention (ERP) Therapy,Practice Mindfulness,Identify and Challenge Negative Thoughts,Connect with close Friends")
        print(" If NO improvment in your Obsession and Compulsion Disorder in next Two Days then Consult to nearby therepist.") 
    elif count>=3 and count<5:
        print("No Need to worry much ###Reduce stress,Connect with Supportive People@@ You will get well Soon")
    else:
        print("You are Fine@@No need to worry##Just Establish a Routine ")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def nostalgia():
    count=0
    print("❤️❤️❤️❤️ Press 1 for Yes &&&&&& Press 0 for NO❤️❤️❤️❤️❤️")
    print("*"*80)
    a=int(input("\t⫸⫸ Do you long for past or for past experience??(1/0): "))
    b=int(input("\t⫸⫸ Do you feel nostalgic in response to a trigger such as a small sound or image??(1/0): "))
    c=int(input("\t⫸⫸ Are you having a sense of loss or sadness associated with the past??(1/0): "))
    d=int(input("\t⫸⫸ Do you feel disconnected from the present moment??(1/0): "))
    e=int(input("\t⫸⫸ Do you usually Romanticize or idealise your past??(1/0): "))
    f=int(input("\t⫸⫸ At times do you smile or laugh because of remembering some past activities while you are working on your present stuff??(1/0): "))
    g=int(input("\t⫸⫸ Have you ever been lost so much in your past that you cant listen or pay attention to the surroundings??(1/0): "))
    
    count=a+b+c+d+e+f+g
    print("✨"*40)
    
    if (count>=5):
        print("You are in RISKY Zone!!!!")
        print("Practice Mindfulness,Identify Triggers,Set Boundaries,Connect with the Present,Maintain Social Connections")
        print(" If NO improvment in your Nostalgia Disorder in next Two Days then Consult to nearby therepist.") 
    elif count>=3 and count<5:
        print("No Need to worry much ###Identify Triggers,Seek Support,Be in Present @@ You will get well Soon")
    else:
        print("You are Fine@@No need to worry##Just Try to be in Present...... ")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def fear():
    count=0
    print("❤️❤️❤️❤️ Press 1 for Yes &&&&&& Press 0 for NO❤️❤️❤️❤️❤️")
    print("*"*80)
    a=int(input("\t⫸⫸ Do you have an Intense and persistent fear or anxiety in response to a specific object or situation, such as flying, heights, or spiders??(1/0): "))
    b=int(input("\t⫸⫸ Do you have physical symptoms such as rapid heartbeat, sweating etc. in response to the feared objects or situations??(1/0): "))
    c=int(input("\t⫸⫸ At times do you have difficulties in thinking about anything other than the feared objects??(1/0): "))
    d=int(input("\t⫸⫸ At times do you feel difficulties in proceeding with your daily routine due to fear??(1/0): "))
    e=int(input("\t⫸⫸ Sometimes Do you have panic attacks in response to the feared objects or situations??(1/0): "))
    f=int(input("\t⫸⫸ Are you aware that the fear is excessive or irrational, feel unable to control it??(1/0): "))
    g=int(input("\t⫸⫸ At times Do you cancel your plans because of the feared objects or situations??(1/0): "))
    
    count=a+b+c+d+e+f+g
    print("✨"*40)
    
    if (count>=5):
        print("You are in RISKY Zone!!!!")
        print("Exposure Therapy,Cognitive Restructuring,Relaxation Techniques,Medication,Mindfulness Practice")
        print(" If NO improvment in your Fear Disorder in next Two Days then Consult to nearby therepist.") 
    elif count>=3 and count<5:
        print("No Need to worry much ###Do Meditation,Be Selfconfident,Relaxation Techniques @@ You will get well Soon")
    else:
        print("You are Fine@@No need to worry##Do Mindfulness Practice.....  ")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def hapiness():
    count=0
    print("❤️❤️❤️❤️ Press 1 for Yes &&&&&& Press 0 for NO❤️❤️❤️❤️❤️")
    print("*"*80)
    a=int(input("\t⫸⫸ Do you have persistent feelings of dissatisfaction or emptiness, despite having achieved goals or experienced positive events??(1/0): "))
    b=int(input("\t⫸⫸ Do you feel constant pursuit of pleasure or excitement, even if it leads to negative consequences??(1/0): "))
    c=int(input("\t⫸⫸ Are you having difficulty in experiencing positive emotions, even in response to positive events??(1/0): "))
    d=int(input("\t⫸⫸ Do you feel Irritability, mood swings, or impatience when experiencing negative emotions??(1/0): "))
    e=int(input("\t⫸⫸ Do you expect to be happy all the time or believing that happiness should come easily and without effort??(1/0): "))
    f=int(input("\t⫸⫸ Do you face difficulty in accepting negative emotions as a natural part of the human experience??(1/0): "))
    g=int(input("\t⫸⫸ Do you feel guilt or shame for not feeling happy all the time??(1/0): "))
    
    count=a+b+c+d+e+f+g
    print("✨"*40)
    
    if (count>=5):
        print("You are in RISKY Zone!!!!")
        print("Identify and Challenge Negative Thought Patterns,Cultivate Gratitude,Set Realistic Goals,Build Strong Relationships,Seek Professional Help")
        print(" If NO improvment in your Unrealistic Expectation of Happiness in next Two Days then Consult to nearby therepist.") 
    elif count>=3 and count<5:
        print("No Need to worry much ##Set the realistic goal,seek help from others @@ You will get well Soon")
    else:
        print("You are Fine@@No need to worry##Just accept each and everything ")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
while True:
    print("*"*80)
    print(" \t\t  ⚡⚡⚡ MENTAL HEALTH CHECKUP SERVICES ⚡⚡⚡ ")
    print("\t")
    
    print("\t\t 1.☞ Anxiety ")
    print("\t\t 2.☞ Stress ")
    print("\t\t 3.☞ Depression ")
    print("\t\t 4.☞ Obsession and Compulsion Disorder ")
    print("\t\t 5.☞ Nostalgia Disorder ")
    print("\t\t 6.☞ Fear Disorder ")
    print("\t\t 7.☞ Unrealistic Expectation of Happiness ")
    print("\t\t 8.☞ Exit ")

    print("*"*80)
    ch=int(input("Input Your Choice:"))
    print("*"*80)
    if ch == 1:
        anxiety()
    elif ch==2:
        stress()
    elif ch==3:
        depression()
    elif ch==4:
        obsession()
    elif ch==5:
        nostalgia()
    elif ch==6:
        fear()
    elif ch==7:
        hapiness()
    elif ch==8:
        break
    else :
        print("Please Provide Valid Input.....")







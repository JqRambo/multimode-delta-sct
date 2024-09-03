import fourth_mode_filter as f4f


def fivethmodedis(period1,period2,period3,period4,period5,f1_final,f2_final,f3_final,f4_final,f5_final):
    fre1= int(f1_final)
    fre2= int(f2_final)
    fre3= int(f3_final)
    fre4= int(f4_final)
    fre5= int(f5_final)

    period1_mode,period2_mode,period3_mode,period4_mode=f4f.fourthmodedis(period1,period2,period3,period4,f1_final,f2_final,f3_final,f4_final)

    if period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==1:
        if abs(fre5-fre1)<=1 and abs(fre5-fre2)>1 and abs(fre5-fre3)>1 and abs(fre5-fre4)>1:
            if period1>period5:
                if period5/period1>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period1/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1


        elif abs(fre5-fre1)>1 and abs(fre5-fre2)<=1 and abs(fre5-fre3)>1 and abs(fre5-fre4)>1:
            if period2>period5:
                if period5/period2>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
                   

        elif abs(fre5-fre1)>1 and abs(fre5-fre2)>1 and abs(fre5-fre3)<=1 and abs(fre5-fre4)>1:
            if period3>period5:
                if period5/period3>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
      

        elif abs(fre5-fre1)>1 and abs(fre5-fre2)>1 and abs(fre5-fre3)>1 and abs(fre5-fre4)<=1:
            if period4>period5:
                if period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
      

        elif abs(fre5-fre1)<=1 and abs(fre5-fre2)<=1 and abs(fre5-fre3)>1 and abs(fre5-fre4)>1:
            if period1>period2>period5 or period2>period1>period5:
                if period5/period1>0.9 or period5/period2>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period1>period5>period2:
                if period5/period1>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period2>period5>period1:
                if period5/period2>0.9 or period1/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period1/period5>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1


        elif abs(fre5-fre1)<=1 and abs(fre5-fre2)>1 and abs(fre5-fre3)<=1 and abs(fre5-fre4)>1:
            if period1>period3>period5 or period3>period1>period5:
                if period5/period1>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period1>period5>period2:
                if period5/period1>0.9 or period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period3>period5>period1:
                if period5/period3>0.9 or period1/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period1/period5>0.9 or period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1


        elif abs(fre5-fre1)<=1 and abs(fre5-fre2)>1 and abs(fre5-fre3)>1 and abs(fre5-fre4)<=1:
            if period1>period4>period5 or period4>period1>period5:
                if period5/period1>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period1>period5>period4:
                if period5/period1>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period4>period5>period1:
                if period5/period4>0.9 or period1/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period1/period5>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1


        elif abs(fre5-fre1)>1 and abs(fre5-fre2)<=1 and abs(fre5-fre3)<=1 and abs(fre5-fre4)>1:
            if period2>period3>period5 or period3>period2>period5:
                if period5/period2>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:                    
                    period5_mode=1
            elif period2>period5>period3:
                if period5/period2>0.9 or period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period3>period5>period2:
                if period5/period3>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period2/period5>0.9 or period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1


        elif abs(fre5-fre1)>1 and abs(fre5-fre2)<=1 and abs(fre5-fre3)>1 and abs(fre5-fre4)<=1:
            if period2>period4>period5 or period4>period2>period5:
                if period5/period2>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period2>period5>period4:
                if period5/period2>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period4>period5>period2:
                if period5/period4>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period2/period5>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1


        elif abs(fre5-fre1)>1 and abs(fre5-fre2)>1 and abs(fre5-fre3)<=1 and abs(fre5-fre4)<=1:
            if period3>period4>period5 or period4>period3>period5:
                if period5/period3>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period3>period5>period4:
                if period5/period2>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period4>period5>period3:
                if period5/period4>0.9 or period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period3/period5>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1


        elif abs(fre5-fre1)<=1 and abs(fre5-fre2)<=1 and abs(fre5-fre3)<=1 and abs(fre5-fre4)>1:
            period5_mode=0
        

        elif abs(fre5-fre1)<=1 and abs(fre5-fre2)<=1 and abs(fre5-fre3)>1 and abs(fre5-fre4)<=1:
            period5_mode=0


        elif abs(fre5-fre1)>1 and abs(fre5-fre2)<=1 and abs(fre5-fre3)<=1 and abs(fre5-fre4)<=1:
            period5_mode=0


        elif abs(fre5-fre1)<=1 and abs(fre5-fre2)<=1 and abs(fre5-fre3)<=1 and abs(fre5-fre4)<=1:
            
            period5_mode=0
            
        
        elif abs(fre5-abs(fre1+fre2))<=2 or abs(fre5-abs(fre1-fre2))<=2 or abs(fre5-abs(2*fre1+fre2))<=2 or abs(fre5-abs(2*fre1+fre2))<=2 or abs(fre5-abs(fre1+2*fre2))<=2 or abs(fre5-abs(fre1+2*fre2))<=2 or abs(fre5-abs(3*fre1+fre2))<=2 or abs(fre5-abs(3*fre1-fre2))<=2 or  abs(fre5-abs(fre1+fre3))<=2 or abs(fre5-abs(fre1-fre3))<=2 or abs(fre5-abs(2*fre1+fre3))<=2 or abs(fre5-abs(2*fre1+fre3))<=2 or abs(fre5-abs(fre1+2*fre3))<=2 or abs(fre5-abs(fre1+2*fre3))<=2 or abs(fre5-abs(3*fre1+fre3))<=2 or abs(fre5-abs(3*fre1-fre3))<=2 or abs(fre5-abs(fre1+fre4))<=2 or abs(fre5-abs(fre1-fre4))<=2 or abs(fre5-abs(2*fre1+fre4))<=2 or abs(fre5-abs(2*fre1+fre4))<=2 or abs(fre5-abs(fre1+2*fre4))<=2 or abs(fre5-abs(fre1+2*fre4))<=2 or abs(fre5-abs(3*fre1+fre4))<=2 or abs(fre5-abs(3*fre1-fre4))<=2 or abs(fre5-abs(fre2+fre3))<=2 or abs(fre5-abs(fre2-fre3))<=2 or abs(fre5-abs(2*fre2+fre3))<=2 or abs(fre5-abs(2*fre2+fre3))<=2 or abs(fre5-abs(fre2+2*fre3))<=2 or abs(fre5-abs(fre2+2*fre3))<=2 or abs(fre5-abs(3*fre2+fre3))<=2 or abs(fre5-abs(3*fre2-fre3))<=2 or abs(fre5-abs(fre2+fre4))<=2 or abs(fre5-abs(fre2-fre4))<=2 or abs(fre5-abs(2*fre2+fre4))<=2 or abs(fre5-abs(2*fre2+fre4))<=2 or abs(fre5-abs(fre2+2*fre4))<=2 or abs(fre5-abs(fre2+2*fre4))<=2 or abs(fre5-abs(3*fre2+fre4))<=2 or abs(fre5-abs(3*fre2-fre4))<=2 or abs(fre5-abs(fre3+fre4))<=2 or abs(fre5-abs(fre3-fre4))<=2 or abs(fre5-abs(2*fre3+fre4))<=2 or abs(fre5-abs(2*fre3+fre4))<=2 or abs(fre5-abs(fre3+2*fre4))<=2 or abs(fre5-abs(fre3+2*fre4))<=2 or abs(fre5-abs(3*fre3+fre4))<=2 or abs(fre5-abs(3*fre3-fre4))<=2:
            period5_mode=0

        elif abs(fre5-abs(fre1+fre2+fre3))<=2 or abs(fre5-abs(fre1+fre2+fre4))<=2 or abs(fre5-abs(fre2+fre3+fre4))<=2:
            period5_mode=0

        elif abs(fre5-abs(fre1+fre2-fre3))<=2 or abs(fre5-abs(fre1+fre2-fre4))<=2 or abs(fre5-abs(fre2+fre3-fre4))<=2:
            period5_mode=0

        else:
            period5_mode=1
    
    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==0:
        if abs(fre5-fre1)<=1 and abs(fre5-fre2)>1 and abs(fre5-fre3)>1:
            if period1>period5:
                if period5/period1>0.9:
                    period5_mode=0
                else:                                      
                    period5_mode=1
            else:
                if period1/period5>0.9:                        
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre1)>1 and abs(fre5-fre2)<=1 and abs(fre5-fre3)>1:
            if period2>period5:
                if period5/period2>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period2/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre1)>1 and abs(fre5-fre2)>1 and abs(fre5-fre3)<=1:
            if period3>period5:
                if period5/period3>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period3/period5>0.9:
                    period5_mode=0
                else:              
                    period3_mode=0
                    period5_mode=1
        elif abs(fre5-fre1)<=1 and abs(fre5-fre2)<=1 and abs(fre5-fre3)>1:
            if period1>period2>period5 or period2>period1>period5:
                if period5/period1>0.9 or period5/period2>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period1>period5>period2:
                if period5/period1>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period2>period5>period1:
                if period1/period5>0.9 or period5/period2>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period2/period5>0.9 or period1/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1


        elif abs(fre5-fre1)<=1 and abs(fre5-fre2)>1 and abs(fre5-fre3)<=1:
            if period1>period3>period5 or period3>period1>period5:
                if period5/period1>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period1>period5>period3:
                if period5/period1>0.9 or period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period3>period5>period1:
                if period1/period5>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period3/period5>0.9 or period1/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-fre1)>1 and abs(fre5-fre2)<=1 and abs(fre5-fre3)<=1:
            if period2>period3>period5 or period3>period2>period5:
                if period5/period2>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period2>period5>period3:
                if period5/period2>0.9 or period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period3>period5>period2:
                if period2/period5>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:                        
                    period5_mode=1
            else:
                if period3/period5>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-abs(fre1+fre2))<=2 or abs(fre5-abs(fre1-fre2))<=2 or abs(fre5-abs(2*fre1+fre2))<=2 or abs(fre5-abs(fre1+2*fre2))<=2 or abs(fre5-abs(3*fre1+fre2))<=2 or abs(fre5-abs(fre1+3*fre2))<=2 or abs(fre5-abs(fre1+fre3))<=2 or abs(fre5-abs(fre1-fre3))<=2 or abs(fre5-abs(fre1+2*fre3))<=2 or abs(fre5-abs(fre1-2*fre3))<=2 or abs(fre5-abs(fre2+fre3))<=2 or abs(fre5-abs(fre2-fre3))<=2 or abs(fre5-abs(fre2+2*fre3))<=2 or abs(fre5-abs(fre2-2*fre3))<=2 or abs(fre5-abs(2*fre2+fre3))<=2 or abs(fre5-abs(2*fre2-fre3))<=2:
            period5_mode=0
        elif abs(fre5-abs(fre1+fre2+fre3))<=2:
            period5_mode=0
        else:
            period5_mode=1

    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==1:
        if abs(fre5-fre1)<=1 and abs(fre5-fre2)>1 and abs(fre5-fre4)>1:
            if period1>period5:
                if period5/period1>0.9:
                    period5_mode=0
                else:                                      
                    period5_mode=1
            else:
                if period1/period5>0.9:                        
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre1)>1 and abs(fre5-fre2)<=1 and abs(fre5-fre4)>1:
            if period2>period5:
                if period5/period2>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period2/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre1)>1 and abs(fre5-fre2)>1 and abs(fre5-fre4)<=1:
            if period4>period5:
                if period5/period4>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period4/period5>0.9:
                    period5_mode=0
                else:              
                    period4_mode=0
                    period5_mode=1
        elif abs(fre5-fre1)<=1 and abs(fre5-fre2)<=1 and abs(fre5-fre4)>1:
            #124 or 214
            if period1>period2>period5 or period2>period1>period5:
                if period5/period1>0.9 or period5/period2>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period1>period5>period2:
                if period5/period1>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period2>period5>period1:
                if period1/period5>0.9 or period5/period2>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period2/period5>0.9 or period1/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-fre1)<=1 and abs(fre5-fre2)>1 and abs(fre5-fre4)<=1:
            if period1>period4>period5 or period4>period1>period5:
                if period5/period1>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period1>period5>period4:
                if period5/period1>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period4>period5>period1:
                if period1/period5>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period4/period5>0.9 or period1/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-fre1)>1 and abs(fre5-fre2)<=1 and abs(fre5-fre4)<=1:
            #234 or 324
            if period2>period4>period5 or period4>period2>period5:
                if period5/period2>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period2>period5>period4:
                if period5/period2>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period4>period5>period2:
                if period2/period5>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:                        
                    period5_mode=1
            else:
                if period4/period5>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-abs(fre1+fre2))<=2 or abs(fre5-abs(fre1-fre2))<=2 or abs(fre5-abs(2*fre1+fre2))<=2 or abs(fre5-abs(fre1+2*fre2))<=2 or abs(fre5-abs(3*fre1+fre2))<=2 or abs(fre5-abs(fre1+3*fre2))<=2 or abs(fre5-abs(fre1+fre4))<=2 or abs(fre5-abs(fre1-fre4))<=2 or abs(fre5-abs(fre1+2*fre4))<=2 or abs(fre5-abs(fre1-2*fre4))<=2 or abs(fre5-abs(fre2+fre4))<=2 or abs(fre5-abs(fre2-fre4))<=2 or abs(fre5-abs(fre2+2*fre4))<=2 or abs(fre5-abs(fre2-2*fre4))<=2 or abs(fre5-abs(2*fre2+fre4))<=2 or abs(fre5-abs(2*fre2-fre4))<=2:
            period5_mode=0
        elif abs(fre5-abs(fre1+fre2+fre4))<=2:
            period5_mode=0
        else:
            period5_mode=1

    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==1:
        if abs(fre5-fre1)<=1 and abs(fre5-fre3)>1 and abs(fre5-fre4)>1:
            if period1>period5:
                if period5/period1>0.9:
                    period5_mode=0
                else:                                      
                    period5_mode=1
            else:
                if period1/period5>0.9:                        
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre1)>1 and abs(fre5-fre3)<=1 and abs(fre5-fre4)>1:
            if period3>period5:
                if period5/period3>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period3/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre1)>1 and abs(fre5-fre3)>1 and abs(fre5-fre4)<=1:
            if period4>period5:
                if period5/period4>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period4/period5>0.9:
                    period5_mode=0
                else:              
                    period4_mode=0
                    period5_mode=1
        elif abs(fre5-fre1)<=1 and abs(fre5-fre3)<=1 and abs(fre5-fre4)>1:
            #124 or 214
            if period1>period3>period5 or period3>period1>period5:
                if period5/period1>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period1>period5>period3:
                if period5/period1>0.9 or period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period3>period5>period1:
                if period1/period5>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period3/period5>0.9 or period1/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-fre1)<=1 and abs(fre5-fre3)>1 and abs(fre5-fre4)<=1:
            if period1>period4>period5 or period4>period1>period5:
                if period5/period1>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period1>period5>period4:
                if period5/period1>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period4>period5>period1:
                if period1/period5>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period4/period5>0.9 or period1/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-fre1)>1 and abs(fre5-fre3)<=1 and abs(fre5-fre4)<=1:
            #234 or 324
            if period3>period4>period5 or period4>period3>period5:
                if period5/period3>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period3>period5>period4:
                if period5/period3>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period4>period5>period3:
                if period3/period5>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:                        
                    period5_mode=1
            else:
                if period4/period5>0.9 or period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-abs(fre1+fre3))<=2 or abs(fre5-abs(fre1-fre3))<=2 or abs(fre5-abs(2*fre1+fre3))<=2 or abs(fre5-abs(fre1+2*fre3))<=2 or abs(fre5-abs(3*fre1+fre3))<=2 or abs(fre5-abs(fre1+3*fre3))<=2 or abs(fre5-abs(fre1+fre4))<=2 or abs(fre5-abs(fre1-fre4))<=2 or abs(fre5-abs(fre1+2*fre4))<=2 or abs(fre5-abs(fre1-2*fre4))<=2 or abs(fre5-abs(fre3+fre4))<=2 or abs(fre5-abs(fre3-fre4))<=2 or abs(fre5-abs(fre3+2*fre4))<=2 or abs(fre5-abs(fre3-2*fre4))<=2 or abs(fre5-abs(2*fre3+fre4))<=2 or abs(fre5-abs(2*fre3-fre4))<=2:
            period5_mode=0
        elif abs(fre5-abs(fre1+fre3+fre4))<=2:
            period5_mode=0
        else:
            period5_mode=1

    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==1:
        if abs(fre5-fre2)<=1 and abs(fre5-fre3)>1 and abs(fre5-fre4)>1:
            if period2>period5:
                if period5/period2>0.9:
                    period5_mode=0
                else:                                      
                    period5_mode=1
            else:
                if period2/period5>0.9:                        
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre2)>1 and abs(fre5-fre3)<=1 and abs(fre5-fre4)>1:
            if period3>period5:
                if period5/period3>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period3/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre2)>1 and abs(fre5-fre3)>1 and abs(fre5-fre4)<=1:
            if period4>period5:
                if period5/period4>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period4/period5>0.9:
                    period5_mode=0
                else:              
                    period4_mode=0
                    period5_mode=1
        elif abs(fre5-fre2)<=1 and abs(fre5-fre3)<=1 and abs(fre5-fre4)>1:
            #124 or 214
            if period2>period3>period5 or period3>period2>period5:
                if period5/period2>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period2>period5>period3:
                if period5/period2>0.9 or period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period3>period5>period2:
                if period2/period5>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period3/period5>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-fre2)<=1 and abs(fre5-fre3)>1 and abs(fre5-fre4)<=1:
            if period2>period4>period5 or period4>period2>period5:
                if period5/period2>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period2>period5>period4:
                if period5/period2>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period4>period5>period2:
                if period2/period5>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period4/period5>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-fre2)>1 and abs(fre5-fre3)<=1 and abs(fre5-fre4)<=1:
            #234 or 324
            if period3>period4>period5 or period4>period3>period5:
                if period5/period3>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period3>period5>period4:
                if period5/period3>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period4>period5>period3:
                if period3/period5>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:                        
                    period5_mode=1
            else:
                if period4/period5>0.9 or period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-abs(fre2+fre3))<=2 or abs(fre5-abs(fre2-fre3))<=2 or abs(fre5-abs(2*fre2+fre3))<=2 or abs(fre5-abs(fre2+2*fre3))<=2 or abs(fre5-abs(3*fre2+fre3))<=2 or abs(fre5-abs(fre2+3*fre3))<=2 or abs(fre5-abs(fre2+fre4))<=2 or abs(fre5-abs(fre2-fre4))<=2 or abs(fre5-abs(fre2+2*fre4))<=2 or abs(fre5-abs(fre2-2*fre4))<=2 or abs(fre5-abs(fre3+fre4))<=2 or abs(fre5-abs(fre3-fre4))<=2 or abs(fre5-abs(fre3+2*fre4))<=2 or abs(fre5-abs(fre3-2*fre4))<=2 or abs(fre5-abs(2*fre3+fre4))<=2 or abs(fre5-abs(2*fre3-fre4))<=2:
            period5_mode=0
        elif abs(fre5-abs(fre2+fre3+fre4))<=2:
            period5_mode=0
        else:
            period5_mode=1

    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==0:
        if abs(fre5-fre1)<=1 and abs(fre5-fre2)>1:
            if period1>period5:
                if period5/period1>0.9:                                
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period1/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre1)>1 and abs(fre5-fre2)<=1:
            if period2>period5:
                if period5/period2>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period2/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre1)<=1 and abs(fre5-fre2)<=1:
            if period1>period2>period5 or period2>period1>period5:
                if period5/period1>0.9 or period5/period2>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period1>period5>period2:
                if period5/period1>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period2>period5>period1:
                if period1/period5>0.9 or period5/period2>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period2/period5>0.9 or period1/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-abs(fre1+fre2))<=2 or abs(fre5-abs(fre1-fre2))<=2 or abs(fre5-abs(2*fre1+fre2))<=2 or abs(fre5-abs(fre1+2*fre2))<=2 or abs(fre5-abs(3*fre1+fre2))<=2 or abs(fre5-abs(fre1+3*fre2))<=2:
            period5_mode=0
        else:
            period5_mode=1   


    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==0:
        if abs(fre5-fre1)<=1 and abs(fre5-fre3)>1:
            if period1>period5:
                if period5/period1>0.9:                                
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period1/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre1)>1 and abs(fre5-fre3)<=1:
            if period3>period5:
                if period5/period3>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period3/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre1)<=1 and abs(fre5-fre3)<=1:
            if period1>period3>period5 or period3>period1>period5:
                if period5/period1>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period1>period5>period3:
                if period5/period1>0.9 or period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period3>period5>period1:
                if period1/period5>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period3/period5>0.9 or period1/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-abs(fre1+fre3))<=2 or abs(fre5-abs(fre1-fre3))<=2 or abs(fre5-abs(2*fre1+fre3))<=2 or abs(fre5-abs(fre1+2*fre3))<=2 or abs(fre5-abs(3*fre1+fre3))<=2 or abs(fre5-abs(fre1+3*fre3))<=2:
            period5_mode=0
        else:
            period5_mode=1   


    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==1:
        if abs(fre5-fre1)<=1 and abs(fre5-fre4)>1:
            if period1>period5:
                if period5/period1>0.9:                                
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period1/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre1)>1 and abs(fre5-fre4)<=1:
            if period4>period5:
                if period5/period4>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period4/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre1)<=1 and abs(fre5-fre4)<=1:
            if period1>period4>period5 or period4>period1>period5:
                if period5/period1>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period1>period5>period4:
                if period5/period1>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period4>period5>period1:
                if period1/period5>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period4/period5>0.9 or period1/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-abs(fre1+fre4))<=2 or abs(fre5-abs(fre1-fre4))<=2 or abs(fre5-abs(2*fre1+fre4))<=2 or abs(fre5-abs(fre1+2*fre4))<=2 or abs(fre5-abs(3*fre1+fre4))<=2 or abs(fre5-abs(fre1+3*fre4))<=2:
            period5_mode=0
        else:
            period5_mode=1   


    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==0:
        if abs(fre5-fre2)<=1 and abs(fre5-fre3)>1:
            if period2>period5:
                if period5/period2>0.9:                                
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period2/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre2)>1 and abs(fre5-fre3)<=1:
            if period3>period5:
                if period5/period3>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period3/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre2)<=1 and abs(fre5-fre3)<=1:
            if period2>period3>period5 or period3>period2>period5:
                if period5/period2>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period2>period5>period3:
                if period5/period2>0.9 or period3/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period3>period5>period2:
                if period2/period5>0.9 or period5/period3>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            else:
                if period3/period5>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-abs(fre2+fre3))<=2 or abs(fre5-abs(fre2-fre3))<=2 or abs(fre5-abs(2*fre2+fre3))<=2 or abs(fre5-abs(fre2+2*fre3))<=2 or abs(fre5-abs(3*fre2+fre3))<=2 or abs(fre5-abs(fre2+3*fre3))<=2:
            period5_mode=0
        else:
            period5_mode=1   


    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==1:
        if abs(fre5-fre2)<=1 and abs(fre5-fre4)>1:
            if period2>period5:
                if period5/period2>0.9:                                
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period2/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre2)>1 and abs(fre5-fre4)<=1:
            if period4>period5:
                if period5/period4>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period4/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre2)<=1 and abs(fre5-fre4)<=1:
            if period2>period4>period5 or period4>period2>period5:
                if period5/period2>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period2>period5>period4:
                if period5/period2>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period4>period5>period2:
                if period2/period5>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            #412 or 421
            else:
                if period4/period5>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-abs(fre2+fre4))<=2 or abs(fre5-abs(fre2-fre4))<=2 or abs(fre5-abs(2*fre2+fre4))<=2 or abs(fre5-abs(fre2+2*fre4))<=2 or abs(fre5-abs(3*fre2+fre4))<=2 or abs(fre5-abs(fre2+3*fre4))<=2:
            period5_mode=0
        else:
            period5_mode=1   

    
    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==1:
        if abs(fre5-fre3)<=1 and abs(fre5-fre4)>1:
            if period2>period5:
                if period5/period2>0.9:                                
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period2/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre3)>1 and abs(fre5-fre4)<=1:
            if period4>period5:
                if period5/period4>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
            else:
                if period4/period5>0.9:
                    period5_mode=0
                else:              
                    period5_mode=1
        elif abs(fre5-fre3)<=1 and abs(fre5-fre4)<=1:
            if period2>period4>period5 or period4>period2>period5:
                if period5/period2>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period2>period5>period4:
                if period5/period2>0.9 or period4/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            elif period4>period5>period2:
                if period2/period5>0.9 or period5/period4>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
            #412 or 421
            else:
                if period4/period5>0.9 or period2/period5>0.9:
                    period5_mode=0
                else:
                    period5_mode=1
        elif abs(fre5-abs(fre3+fre4))<=2 or abs(fre5-abs(fre3-fre4))<=2 or abs(fre5-abs(2*fre3+fre4))<=2 or abs(fre5-abs(fre3+2*fre4))<=2 or abs(fre5-abs(3*fre3+fre4))<=2 or abs(fre5-abs(fre3+3*fre4))<=2:
            period5_mode=0
        else:
            period5_mode=1   


    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==0:
        if period1>period5:
            if period5/period1>0.9 or period5/period1<0.4:
                period5_mode=0
            else:
                period5_mode=1
        else:
            if period1/period5>0.9 or period1/period5<0.4:
                period5_mode=0
            else:
                period5_mode=1 

    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==0:
        if period2>period5:
            if period5/period2>0.9 or period5/period2<0.4:
                period5_mode=0
            else:
                period5_mode=1
        else:
            if period2/period5>0.9 or period2/period5<0.4:
                period5_mode=0
            else:
                period5_mode=1 

    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==0:
        if period3>period5:
            if period5/period3>0.9 or period5/period3<0.4:
                period5_mode=0
            else:
                period5_mode=1
        else:
            if period3/period5>0.9 or period3/period5<0.4:
                period5_mode=0
            else:
                period5_mode=1 


    elif period1_mode==0 and period2_mode==0 and period3_mode==0 and period4_mode==1:

        if period4>period5:
            if period5/period4>0.9 or period5/period4<0.4:
                period5_mode=0
            else:
                period5_mode=1
        else:
            if period4/period5>0.9 or period4/period5<0.4:
                period5_mode=0
            else:
                period5_mode=1 

    else:
        period5_mode==1



    return  period1_mode,period2_mode,period3_mode,period4_mode,period5_mode

def fourthmodedis(period1,period2,period3,period4,f1_final,f2_final,f3_final,f4_final):
    fre1= int(f1_final)
    fre2= int(f2_final)
    fre3= int(f3_final)
    fre4= int(f4_final)
    if abs(fre2-fre1)<=1:
        if period1>period2:
            if period2/period1>0.9:
                if abs(fre3-fre1)<=1:
                    if period1>period3:
                        if period3/period1>0.9:
                            if abs(fre4-fre1)<=1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=0 
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=0    
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=1
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=0
                                period4_mode=1
                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)<=1 and abs(fre4-fre3)<=1:
                                if period1>period3>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period1>period4:
                                    if period4/period1>0.9 or period1/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period4>period1>period3:
                                    if period3/period1>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period3>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                    
                    else:     
                        if period1/period3>0.9:
                            if abs(fre4-fre1)<=1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=0 
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=0    
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=1
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=0
                                period4_mode=1
                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)<=1 and abs(fre4-fre3)<=1:
                                if period1>period3>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period1>period4:
                                    if period4/period1>0.9 or period1/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period4>period1>period3:
                                    if period3/period1>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period3>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1   
                
                else:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre3)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                    elif abs(fre4-fre1)>1 and abs(fre4-fre3)<=1:
                        if period3>period4:
                            if period4/period3>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                    elif abs(fre4-fre1)<=1 and abs(fre4-fre3)<=1:
                        if period1>period3>period4:
                            if period4/period1>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        elif period1>period4>period3:
                            if period4/period1>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        elif period3>period1>period4:
                            if period4/period1>0.9 or period1/period3>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period1:
                            if period1/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        elif period4>period1>period3:
                            if period3/period1>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period1/period3>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                    elif abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2:
                        period1_mode=1
                        period2_mode=0
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=0
                        period3_mode=1
                        period4_mode=1  

            else:
                if abs(fre3-fre1)<=1 and abs(fre3-fre2)>1:
                    if period1>period3:
                        if period3/period1>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                #412 or 421
                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1   
                                                       
                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                           
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            
                            elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0

                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    else:
                        if period1/period3>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                #412 or 421
                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1   
                                
                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                #234 or 324
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                elif abs(fre3-fre1)>1 and abs(fre3-fre2)<=1:
                    if period2>period3:
                        if period3/period2>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                #234 or 324
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            
                            elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0

                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    else:
                        if period2/period3>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1

                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                #234 or 324
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            
                            elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0

                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1


                elif abs(fre3-fre1)<=1 and abs(fre3-fre2)<=1:

                    if period1>period2>period3 or period2>period1>period3:
                        if period3/period1>0.9 or period3/period2>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                #234 or 324
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1


                    elif period1>period3>period2:
                        if period3/period1>0.9 or period2/period3>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:

                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                else:
                                    if period1/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1


                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                #234 or 324
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif period2>period3>period1:
                        if period1/period4>0.9 or period4/period2>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                #234 or 324
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1


                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1



                        
                elif abs(fre3-abs(fre1+fre2))<=2 or abs(fre3-abs(fre1-fre2))<=2:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        #412 or 421
                        else:
                            if period2/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                    elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1   
                       
                    
                    
                else:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        if period3>period4:
                            if period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        #124 or 214
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        else:
                            if period2/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        #134 or 314
                        if period1>period3>period4 or period3>period1>period4:
                            if period4/period1>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period1>period4>period3:
                            if period4/period1>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period1:
                            if period1/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                        #234 or 324
                        if period2>period3>period4 or period3>period2>period4:
                            if period4/period2>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period2>period4>period3:
                            if period4/period2>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period2:
                            if period2/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    
                    
                    elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    
                    elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
   
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1

        else:
            if period1/period2>0.9:
                if abs(fre3-fre1)<=1:
                    if period1>period3:
                        if period3/period1>0.9:
                            if abs(fre4-fre1)<=1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=0 
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=0    
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=1
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=0
                                period4_mode=1
                                    
                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)<=1 and abs(fre4-fre3)<=1:
                                if period1>period3>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period1>period4:
                                    if period4/period1>0.9 or period1/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period4>period1>period3:
                                    if period3/period1>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period3>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                                
                    else:     
                        if period1/period3>0.9:
                            if abs(fre4-fre1)<=1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=0 
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=0    
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=0
                                        period4_mode=1
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=0
                                period4_mode=1
                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1



                            elif abs(fre4-fre1)<=1 and abs(fre4-fre3)<=1:
                                if period1>period3>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period1>period4:
                                    if period4/period1>0.9 or period1/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                elif period4>period1>period3:
                                    if period3/period1>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period3>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=0
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1   
                else:                    
                    if abs(fre4-fre1)<=1 and abs(fre4-fre3)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                    elif abs(fre4-fre1)>1 and abs(fre4-fre3)<=1:
                        if period3>period4:
                            if period4/period3>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                    elif abs(fre4-fre1)<=1 and abs(fre4-fre3)<=1:
                        if period1>period3>period4:
                            if period4/period1>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        elif period1>period4>period3:
                            if period4/period1>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        elif period3>period1>period4:
                            if period4/period1>0.9 or period1/period3>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period1:
                            if period1/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        elif period4>period1>period3:
                            if period3/period1>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period1/period3>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                    elif abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2:
                        period1_mode=1
                        period2_mode=0
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=0
                        period3_mode=1
                        period4_mode=1  

            else:
                if abs(fre3-fre1)<=1 and abs(fre3-fre2)>1:
                    if period1>period3:
                        if period3/period1>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                #412 or 421
                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1   
                                                    
                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                        
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            
                            elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0

                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    else:
                        if period1/period3>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                #412 or 421
                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1   
                        #123
                                
                        #123       
                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                #234 or 324
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            
                            
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            
                            elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0


                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                elif abs(fre3-fre1)>1 and abs(fre3-fre2)<=1:
                    if period2>period3:
                        if period3/period2>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                            
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                    

                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                #234 or 324
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            
                            elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0

                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1


                    else:
                        if period2/period3>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=0
                            
                            else:
                                period1_mode=1
                                period2_mode=0
                                period3_mode=1
                                period4_mode=1
                    

                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                #234 or 324
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            
                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            
                            elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0

                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1


                elif abs(fre3-fre1)<=1 and abs(fre3-fre2)<=1:
                    #124 or 214
                    if period1>period2>period3 or period2>period1>period3:
                        if period3/period1>0.9 or period3/period2>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1



                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                #234 or 324
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1


                    elif period1>period3>period2:
                        if period3/period1>0.9 or period2/period3>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                #234 or 324
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1


                    elif period2>period3>period1:
                        if period1/period3>0.9 or period3/period2>0.9:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                                else:
                                    if period1/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        else:
                            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                                if period1>period4:
                                    if period4/period1>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                if period2>period4:
                                    if period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                if period3>period4:
                                    if period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:              
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=0
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                                #124 or 214
                                if period1>period2>period4 or period2>period1>period4:
                                    if period4/period1>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period1>period4>period2:
                                    if period4/period1>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                elif period2>period4>period1:
                                    if period1/period4>0.9 or period4/period2>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                                else:
                                    if period2/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1

                            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                                #134 or 314
                                if period1>period3>period4 or period3>period1>period4:
                                    if period4/period1>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period1>period4>period3:
                                    if period4/period1>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period1:
                                    if period1/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period1/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                                #234 or 324
                                if period2>period3>period4 or period3>period2>period4:
                                    if period4/period2>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period2>period4>period3:
                                    if period4/period2>0.9 or period3/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                elif period3>period4>period2:
                                    if period2/period4>0.9 or period4/period3>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                                else:
                                    if period3/period4>0.9 or period2/period4>0.9:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=0
                                    else:
                                        period1_mode=1
                                        period2_mode=1
                                        period3_mode=1
                                        period4_mode=1
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1

                        
                elif abs(fre3-abs(fre1+fre2))<=2 or abs(fre3-abs(fre1-fre2))<=2:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        #412 or 421
                        else:
                            if period2/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                    elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1   
                    
                    
                else:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        if period3>period4:
                            if period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        #124 or 214
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        else:
                            if period2/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        #134 or 314
                        if period1>period3>period4 or period3>period1>period4:
                            if period4/period1>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period1>period4>period3:
                            if period4/period1>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period1:
                            if period1/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                        #234 or 324
                        if period2>period3>period4 or period3>period2>period4:
                            if period4/period2>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period2>period4>period3:
                            if period4/period2>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period2:
                            if period2/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    
                    
                    elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    
                    elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0

                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1
    
    else:
        if abs(fre3-fre1)<=1 and abs(fre3-fre2)>1:
            if period1>period3:
                if period3/period1>0.9:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        #412 or 421
                        else:
                            if period2/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                    elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1   
                
                else:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        if period3>period4:
                            if period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        #124 or 214
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        else:
                            if period2/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        #134 or 314
                        if period1>period3>period4 or period3>period1>period4:
                            if period4/period1>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period1>period4>period3:
                            if period4/period1>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period1:
                            if period1/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                        if period2>period3>period4 or period3>period2>period4:
                            if period4/period2>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period2>period4>period3:
                            if period4/period2>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period2:
                            if period2/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    
                    elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    
                    elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0

                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1

            else:
                if period1/period3>0.9:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                        #124 or 214
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        #412 or 421
                        else:
                            if period2/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                    elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1   
                #123
                        
                    #123       
                else:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        if period3>period4:
                            if period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        #124 or 214
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        else:
                            if period2/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        #134 or 314
                        if period1>period3>period4 or period3>period1>period4:
                            if period4/period1>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period1>period4>period3:
                            if period4/period1>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period1:
                            if period1/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                        #234 or 324
                        if period2>period3>period4 or period3>period2>period4:
                            if period4/period2>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period2>period4>period3:
                            if period4/period2>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period2:
                            if period2/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    
                    
                    elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    
                    elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0


                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1


        elif abs(fre3-fre1)>1 and abs(fre3-fre2)<=1:
            if period2>period3:
                if period3/period2>0.9:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                        #124 or 214
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                    
                    elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    
                    else:
                        period1_mode=1
                        period2_mode=0
                        period3_mode=1
                        period4_mode=1
            
                else:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        if period3>period4:
                            if period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        else:
                            if period2/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        #134 or 314
                        if period1>period3>period4 or period3>period1>period4:
                            if period4/period1>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period1>period4>period3:
                            if period4/period1>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period1:
                            if period1/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                        #234 or 324
                        if period2>period3>period4 or period3>period2>period4:
                            if period4/period2>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period2>period4>period3:
                            if period4/period2>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period2:
                            if period2/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    
                    elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    
                    elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0

                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1


            else:
                if period2/period3>0.9:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1
            

                else:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        if period3>period4:
                            if period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        #124 or 214
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        else:
                            if period2/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        #134 or 314
                        if period1>period3>period4 or period3>period1>period4:
                            if period4/period1>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period1>period4>period3:
                            if period4/period1>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period1:
                            if period1/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                        #234 or 324
                        if period2>period3>period4 or period3>period2>period4:
                            if period4/period2>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period2>period4>period3:
                            if period4/period2>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period2:
                            if period2/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    
                    elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    
                    elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0

                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1


        elif abs(fre3-fre1)<=1 and abs(fre3-fre2)<=1:
            #124 or 214
            if period1>period2>period3 or period2>period1>period3:
                if period3/period1>0.9 or period3/period2>0.9:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                        #124 or 214
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1

                else:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        if period3>period4:
                            if period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        #124 or 214
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        else:
                            if period2/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        #134 or 314
                        if period1>period3>period4 or period3>period1>period4:
                            if period4/period1>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period1>period4>period3:
                            if period4/period1>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period1:
                            if period1/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                        #234 or 324
                        if period2>period3>period4 or period3>period2>period4:
                            if period4/period2>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period2>period4>period3:
                            if period4/period2>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period2:
                            if period2/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1


            elif period1>period3>period2:
                if period3/period1>0.9 or period2/period3>0.9:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                        #124 or 214
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1

                else:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        if period3>period4:
                            if period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        #124 or 214
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        else:
                            if period2/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        #134 or 314
                        if period1>period3>period4 or period3>period1>period4:
                            if period4/period1>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period1>period4>period3:
                            if period4/period1>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period1:
                            if period1/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                        #234 or 324
                        if period2>period3>period4 or period3>period2>period4:
                            if period4/period2>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period2>period4>period3:
                            if period4/period2>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period2:
                            if period2/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1


            elif period2>period3>period1:
                if period1/period3>0.9 or period1/period2>0.9:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                        #124 or 214
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1

                else:
                    if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                        if period1>period4:
                            if period4/period1>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        if period2>period4:
                            if period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        if period3>period4:
                            if period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:              
                                period1_mode=1
                                period2_mode=1
                                period3_mode=0
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                        #124 or 214
                        if period1>period2>period4 or period2>period1>period4:
                            if period4/period1>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period1>period4>period2:
                            if period4/period1>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        elif period2>period4>period1:
                            if period1/period4>0.9 or period4/period2>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                        else:
                            if period2/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1

                    elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                        #134 or 314
                        if period1>period3>period4 or period3>period1>period4:
                            if period4/period1>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period1>period4>period3:
                            if period4/period1>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period1:
                            if period1/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period1/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                        #234 or 324
                        if period2>period3>period4 or period3>period2>period4:
                            if period4/period2>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period2>period4>period3:
                            if period4/period2>0.9 or period3/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        elif period3>period4>period2:
                            if period2/period4>0.9 or period4/period3>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                        else:
                            if period3/period4>0.9 or period2/period4>0.9:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=0
                            else:
                                period1_mode=1
                                period2_mode=1
                                period3_mode=1
                                period4_mode=1
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1


            else:
                period1_mode=1
                period2_mode=1
                period3_mode=0
                period4_mode=1


        elif abs(fre3-abs(fre1+fre2))<=2 or abs(fre3-abs(fre1-fre2))<=2:
            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1:
                if period1>period4:
                    if period4/period1>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    else:              
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1
                else:
                    if period1/period4>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    else:              
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1
            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1:
                if period2>period4:
                    if period4/period2>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    else:              
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1
                else:
                    if period2/period4>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    else:              
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1
            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1:
                if period1>period2>period4 or period2>period1>period4:
                    if period4/period1>0.9 or period4/period2>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1
                elif period1>period4>period2:
                    if period4/period1>0.9 or period2/period4>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1
                elif period2>period4>period1:
                    if period1/period4>0.9 or period4/period2>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1
                #412 or 421
                else:
                    if period2/period4>0.9 or period1/period4>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1
            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2:
                period1_mode=1
                period2_mode=1
                period3_mode=0
                period4_mode=0
            else:
                period1_mode=1
                period2_mode=1
                period3_mode=0
                period4_mode=1   

            
        else:
            if abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)>1:
                if period1>period4:
                    if period4/period1>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:              
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1
                else:
                    if period1/period4>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:              
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1

            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                if period2>period4:
                    if period4/period2>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:              
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1
                else:
                    if period2/period4>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:              
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1

            elif abs(fre4-fre1)>1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                if period3>period4:
                    if period4/period3>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:              
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1
                else:
                    if period3/period4>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:              
                        period1_mode=1
                        period2_mode=1
                        period3_mode=0
                        period4_mode=1

            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)>1:
                #124 or 214
                if period1>period2>period4 or period2>period1>period4:
                    if period4/period1>0.9 or period4/period2>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1

                elif period1>period4>period2:
                    if period4/period1>0.9 or period2/period4>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1

                elif period2>period4>period1:
                    if period1/period4>0.9 or period4/period2>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1

                else:
                    if period2/period4>0.9 or period1/period4>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1

            elif abs(fre4-fre1)<=1 and abs(fre4-fre2)>1 and abs(fre4-fre3)<=1:
                if period1>period3>period4 or period3>period1>period4:
                    if period4/period1>0.9 or period4/period3>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1
                elif period1>period4>period3:
                    if period4/period1>0.9 or period3/period4>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1
                elif period3>period4>period1:
                    if period1/period4>0.9 or period4/period3>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1
                else:
                    if period3/period4>0.9 or period1/period4>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1
            
            elif abs(fre4-fre1)>1 and abs(fre4-fre2)<=1 and abs(fre4-fre3)<=1:
                #234 or 324
                if period2>period3>period4 or period3>period2>period4:
                    if period4/period2>0.9 or period4/period3>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1
                elif period2>period4>period3:
                    if period4/period2>0.9 or period3/period4>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1
                elif period3>period4>period2:
                    if period2/period4>0.9 or period4/period3>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1
                else:
                    if period3/period4>0.9 or period2/period4>0.9:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=0
                    else:
                        period1_mode=1
                        period2_mode=1
                        period3_mode=1
                        period4_mode=1
            elif abs(fre4-abs(fre1+fre2))<=2 or abs(fre4-abs(fre1-fre2))<=2 or abs(fre4-abs(2*fre1+fre2))<=2 or abs(fre4-abs(fre1+2*fre2))<=2 or abs(fre4-abs(3*fre1+fre2))<=2 or abs(fre4-abs(fre1+3*fre2))<=2 or abs(fre4-abs(fre1+fre3))<=2 or abs(fre4-abs(fre1-fre3))<=2 or abs(fre4-abs(fre1+2*fre3))<=2 or abs(fre4-abs(fre1-2*fre3))<=2 or abs(fre4-abs(fre2+fre3))<=2 or abs(fre4-abs(fre2-fre3))<=2 or abs(fre4-abs(fre2+2*fre3))<=2 or abs(fre4-abs(fre2-2*fre3))<=2 or abs(fre4-abs(2*fre2+fre3))<=2 or abs(fre4-abs(2*fre2-fre3))<=2:
                period1_mode=1
                period2_mode=1
                period3_mode=1
                period4_mode=0
            
            elif abs(fre4-abs(fre1+fre2+fre3))<=2:
                period1_mode=1
                period2_mode=1
                period3_mode=1
                period4_mode=0

            else:
                period1_mode=1
                period2_mode=1
                period3_mode=1
                period4_mode=1

    return period1_mode,period2_mode,period3_mode,period4_mode

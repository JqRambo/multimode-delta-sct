def triplemodedis(period1,period2,period3,f1_final,f2_final,f3_final):
    fre1= int(f1_final)
    fre2= int(f2_final)
    fre3= int(f3_final)
    if abs(fre2-fre1)<=1:
        if period1>period2:
            if period2/period1>0.9:
                if abs(fre3-fre1)<=1:
                    if period1>period3:
                        if period3/period1>0.9:
                            period1_mode=1
                            period2_mode=0
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=0
                            period3_mode=1
                    else:
                        if period1/period3>0.9:
                            period1_mode=1
                            period2_mode=0
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=0
                            period3_mode=1
                else:
                    period1_mode=1
                    period2_mode=0
                    period3_mode=1
            else:
                if abs(fre3-fre1)<=1 and abs(fre3-fre2)>1:
                    if period1>period3:
                        if period3/period1>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1    
                    else:
                        if period1/period3>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1

                elif abs(fre3-fre1)>1 and abs(fre3-fre2)<=2:
                    if period2>period3:
                        if period3/period2>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1    
                    else:
                        if period2/period3>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1

                elif abs(fre3-fre1)<=1 and abs(fre3-fre2)<=2:
                    if period1>period2>period3 or period2>period1>period3:
                        if period3/period1>0.9 or period3/period2>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1

                    elif period1>period3>period2:
                        if period3/period1>0.9 or period2/period3>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1

                    elif period2>period3>period1:
                        if period1/period3>0.9 or period3/period2>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1

                    else:
                        if period1/period3>0.9 or period2/period3>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1

                elif abs(fre3-abs(fre1+fre2))<=2 or abs(fre3-abs(fre1-fre2))<=2:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=0

                else:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=1
        else:
            if period1/period2>0.9:
                if abs(fre3-fre1)<=1:
                    if period1>period3:
                        if period3/period1>0.9:
                            period1_mode=1
                            period2_mode=0
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=0
                            period3_mode=1
                    else:
                        if period1/period3>0.9:
                            period1_mode=1
                            period2_mode=0
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=0
                            period3_mode=1
                else:
                    period1_mode=1
                    period2_mode=0
                    period3_mode=1
            else:
                if abs(fre3-fre1)<=1 and abs(fre3-fre2)>1:
                    if period1>period3:
                        if period3/period1>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1    
                    else:
                        if period1/period3>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1

                elif abs(fre3-fre1)>1 and abs(fre3-fre2)<=2:
                    if period2>period3:
                        if period3/period2>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1    
                    else:
                        if period2/period3>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1

                elif abs(fre3-fre1)<=1 and abs(fre3-fre2)<=2:
                    if period1>period2>period3 or period2>period1>period3:
                        if period3/period1>0.9 or period3/period2>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1

                    elif period1>period3>period2:
                        if period3/period1>0.9 or period2/period3>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1

                    elif period2>period3>period1:
                        if period1/period3>0.9 or period3/period2>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1

                    else:
                        if period1/period3>0.9 or period2/period3>0.9:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=0
                        else:
                            period1_mode=1
                            period2_mode=1
                            period3_mode=1

                elif abs(fre3-abs(fre1+fre2))<=2 or abs(fre3-abs(fre1-fre2))<=2:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=0

                else:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=1

    else:
        if abs(fre3-fre1)<=1 and abs(fre3-fre2)>1:
            if period1>period3:
                if period3/period1>0.9:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=0
                else:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=1    
            else:
                if period1/period3>0.9:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=0
                else:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=1

        elif abs(fre3-fre1)>1 and abs(fre3-fre2)<=2:
            if period2>period3:
                if period3/period2>0.9:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=0
                else:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=1    
            else:
                if period2/period3>0.9:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=0
                else:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=1

        elif abs(fre3-fre1)<=1 and abs(fre3-fre2)<=2:
            if period1>period2>period3 or period2>period1>period3:
                if period3/period1>0.9 or period3/period2>0.9:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=0
                else:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=1

            elif period1>period3>period2:
                if period3/period1>0.9 or period2/period3>0.9:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=0
                else:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=1

            elif period2>period3>period1:
                if period1/period3>0.9 or period3/period2>0.9:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=0
                else:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=1

            else:
                if period1/period3>0.9 or period2/period3>0.9:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=0
                else:
                    period1_mode=1
                    period2_mode=1
                    period3_mode=1

        elif abs(fre3-abs(fre1+fre2))<=2 or abs(fre3-abs(fre1-fre2))<=2:
            period1_mode=1
            period2_mode=1
            period3_mode=0

        else:
            period1_mode=1
            period2_mode=1
            period3_mode=1


    return period1_mode,period2_mode,period3_mode


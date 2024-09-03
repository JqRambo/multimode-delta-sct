import fiveth_mode_filter as f5f
import fourth_mode_filter as f4f
import triple_fre_filter as f3f


def sixthmodedis(period1,period2,period3,period4,period5,period6,f1_final,f2_final,f3_final,f4_final,f5_final,f6_final):
    fre1= int(f1_final)
    fre2= int(f2_final)
    fre3= int(f3_final)
    fre4= int(f4_final)
    fre5= int(f5_final)
    fre6= int(f6_final)

    period1_mode,period2_mode,period3_mode,period4_mode,period5_mode=f5f.fivethmodedis(period1,period2,period3,period4,period5,f1_final,f2_final,f3_final,f4_final,f5_final)

    if period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==1:

        if abs(fre6-fre1)<=1 and abs(fre6-fre2)>1 and abs(fre6-fre3)>1 and abs(fre6-fre4)>1 and abs(fre6-fre5)>1:
            if period1>period6:
                if period6/period1>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            else:
                if period1/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1


        elif abs(fre6-fre1)>1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)>1 and abs(fre6-fre4)>1 and abs(fre6-fre5)>1:
            if period2>period6:
                if period6/period2>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            else:
                if period2/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1

        elif abs(fre6-fre1)>1 and abs(fre6-fre2)>1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)>1 and abs(fre6-fre5)>1:
            if period3>period6:
                if period6/period3>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            else:
                if period3/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1

        elif abs(fre6-fre1)>1 and abs(fre6-fre2)>1 and abs(fre6-fre3)>1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)>1:
            if period4>period6:
                if period6/period4>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            else:
                if period4/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1

        elif abs(fre6-fre1)>1 and abs(fre6-fre2)>1 and abs(fre6-fre3)>1 and abs(fre6-fre4)>1 and abs(fre6-fre5)<=1:
            if period5>period6:
                if period6/period5>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            else:
                if period5/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1

        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)>1 and abs(fre6-fre4)>1 and abs(fre6-fre5)>1:
            if period1>period2>period6 or period2>period1>period6:
                if period6/period1>0.9 or period6/period2>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period1>period6>period2:
                if period6/period1>0.9 or period2/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period2>period6>period1:
                if period1/period6>0.9 or period6/period2>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            else:
                if period2/period6>0.9 or period1/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
     
        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)>1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)>1 and abs(fre6-fre5)>1:
            if period1>period3>period6 or period3>period1>period6:
                if period6/period1>0.9 or period6/period3>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period1>period6>period3:
                if period6/period1>0.9 or period3/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period3>period6>period1:
                if period1/period6>0.9 or period6/period3>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            else:
                if period3/period6>0.9 or period1/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1

        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)>1 and abs(fre6-fre3)>1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)>1:
            if period1>period4>period6 or period4>period1>period6:
                if period6/period1>0.9 or period6/period4>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period1>period6>period4:
                if period6/period1>0.9 or period4/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period4>period6>period1:
                if period1/period6>0.9 or period6/period4>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            else:
                if period4/period6>0.9 or period1/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1

        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)>1 and abs(fre6-fre3)>1 and abs(fre6-fre4)>1 and abs(fre6-fre5)<=1:
            if period1>period5>period6 or period5>period1>period6:
                if period6/period1>0.9 or period6/period5>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period1>period6>period5:
                if period6/period1>0.9 or period5/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period5>period6>period1:
                if period1/period6>0.9 or period6/period5>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            else:
                if period5/period6>0.9 or period1/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1

        elif abs(fre6-fre1)>1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)>1 and abs(fre6-fre5)>1:
            if period2>period3>period6 or period3>period2>period6:
                if period6/period2>0.9 or period6/period3>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period2>period6>period3:
                if period6/period2>0.9 or period3/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period3>period6>period2:
                if period2/period6>0.9 or period6/period3>0.9:
                    period6_mode=0
                else:                        
                    period6_mode=1
            else:
                if period3/period6>0.9 or period2/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1

        elif abs(fre6-fre1)>1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)>1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)>1:
            if period2>period4>period6 or period4>period2>period6:
                if period6/period2>0.9 or period6/period4>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period2>period6>period4:
                if period6/period2>0.9 or period4/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period4>period6>period2:
                if period2/period6>0.9 or period6/period4>0.9:
                    period6_mode=0
                else:                        
                    period6_mode=1
            else:
                if period4/period6>0.9 or period2/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1

        elif abs(fre6-fre1)>1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)>1 and abs(fre6-fre4)>1 and abs(fre6-fre5)<=1:
            if period2>period5>period6 or period5>period2>period6:
                if period6/period2>0.9 or period6/period5>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period2>period6>period5:
                if period6/period2>0.9 or period5/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period5>period6>period2:
                if period2/period6>0.9 or period6/period5>0.9:
                    period6_mode=0
                else:                        
                    period6_mode=1
            else:
                if period5/period6>0.9 or period2/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1

        elif abs(fre6-fre1)>1 and abs(fre6-fre2)>1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)>1:
            if period3>period4>period6 or period4>period3>period6:
                if period6/period3>0.9 or period6/period4>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period3>period6>period4:
                if period6/period2>0.9 or period4/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period4>period6>period3:
                if period6/period4>0.9 or period3/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            else:
                if period3/period6>0.9 or period4/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1

        elif abs(fre6-fre1)>1 and abs(fre6-fre2)>1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)>1 and abs(fre6-fre5)<=1:
            if period3>period5>period6 or period5>period3>period6:
                if period6/period3>0.9 or period6/period5>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period3>period6>period5:
                if period6/period2>0.9 or period5/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period5>period6>period3:
                if period6/period5>0.9 or period3/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            else:
                if period3/period6>0.9 or period5/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1

        elif abs(fre6-fre1)>1 and abs(fre6-fre2)>1 and abs(fre6-fre3)>1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)<=1:
            if period4>period5>period6 or period5>period4>period6:
                if period6/period4>0.9 or period6/period5>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period4>period6>period5:
                if period6/period2>0.9 or period5/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            elif period5>period6>period4:
                if period6/period5>0.9 or period4/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1
            else:
                if period4/period6>0.9 or period5/period6>0.9:
                    period6_mode=0
                else:
                    period6_mode=1


        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)>1 and abs(fre6-fre5)>1:
            period6_mode=0

        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)>1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)>1:
            period6_mode=0

        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)>1 and abs(fre6-fre4)>1 and abs(fre6-fre5)<=1:
            period6_mode=0

        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)>1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)>1:
            period6_mode=0

        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)>1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)>1 and abs(fre6-fre5)<=1:
            period6_mode=0


        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)>1 and abs(fre6-fre3)>1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)<=1:
            period6_mode=0


        elif abs(fre6-fre1)>1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)>1:
            period6_mode=0


        elif abs(fre6-fre1)>1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)>1 and abs(fre6-fre5)<=1:
            period6_mode=0


        elif abs(fre6-fre1)>1 and abs(fre6-fre2)>1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)<=1:
            period6_mode=0


        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)>1:
            period6_mode=0


        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)>1 and abs(fre6-fre5)<=1:
            period6_mode=0


        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)>1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)<=1:
            period6_mode=0


        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)>1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)<=1:
            period6_mode=0

        elif abs(fre6-fre1)>1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)<=1:
            period6_mode=0

        elif abs(fre6-fre1)<=1 and abs(fre6-fre2)<=1 and abs(fre6-fre3)<=1 and abs(fre6-fre4)<=1 and abs(fre6-fre5)<=1:
            period6_mode=0

        elif abs(fre6-abs(fre1+fre2))<=2 or abs(fre6-abs(fre1-fre2))<=2 or abs(fre6-abs(2*fre1+fre2))<=2 or abs(fre6-abs(2*fre1+fre2))<=2 or abs(fre6-abs(fre1+2*fre2))<=2 or abs(fre6-abs(fre1+2*fre2))<=2 or abs(fre6-abs(3*fre1+fre2))<=2 or abs(fre6-abs(3*fre1-fre2))<=2 or  abs(fre6-abs(fre1+fre3))<=2 or abs(fre6-abs(fre1-fre3))<=2 or abs(fre6-abs(2*fre1+fre3))<=2 or abs(fre6-abs(2*fre1+fre3))<=2 or abs(fre6-abs(fre1+2*fre3))<=2 or abs(fre6-abs(fre1+2*fre3))<=2 or abs(fre6-abs(3*fre1+fre3))<=2 or abs(fre6-abs(3*fre1-fre3))<=2 or abs(fre6-abs(fre1+fre4))<=2 or abs(fre6-abs(fre1-fre4))<=2 or abs(fre6-abs(2*fre1+fre4))<=2 or abs(fre6-abs(2*fre1+fre4))<=2 or abs(fre6-abs(fre1+2*fre4))<=2 or abs(fre6-abs(fre1+2*fre4))<=2 or abs(fre6-abs(3*fre1+fre4))<=2 or abs(fre6-abs(3*fre1-fre4))<=2 or abs(fre6-abs(fre1+fre5))<=2 or abs(fre6-abs(fre1-fre5))<=2 or abs(fre6-abs(2*fre1+fre5))<=2 or abs(fre6-abs(2*fre1+fre5))<=2 or abs(fre6-abs(fre1+2*fre5))<=2 or abs(fre6-abs(fre1+2*fre5))<=2 or abs(fre6-abs(3*fre1+fre5))<=2 or abs(fre6-abs(3*fre1-fre5))<=2 or abs(fre6-abs(fre2+fre3))<=2 or abs(fre6-abs(fre2-fre3))<=2 or abs(fre6-abs(2*fre2+fre3))<=2 or abs(fre6-abs(2*fre2+fre3))<=2 or abs(fre6-abs(fre2+2*fre3))<=2 or abs(fre6-abs(fre2+2*fre3))<=2 or abs(fre6-abs(3*fre2+fre3))<=2 or abs(fre6-abs(3*fre2-fre3))<=2 or abs(fre6-abs(fre2+fre4))<=2 or abs(fre6-abs(fre2-fre4))<=2 or abs(fre6-abs(2*fre2+fre4))<=2 or abs(fre6-abs(2*fre2+fre4))<=2 or abs(fre6-abs(fre2+2*fre4))<=2 or abs(fre6-abs(fre2+2*fre4))<=2 or abs(fre6-abs(3*fre2+fre4))<=2 or abs(fre6-abs(3*fre2-fre4))<=2 or abs(fre6-abs(fre2+fre5))<=2 or abs(fre6-abs(fre2-fre5))<=2 or abs(fre6-abs(2*fre2+fre5))<=2 or abs(fre6-abs(2*fre2+fre5))<=2 or abs(fre6-abs(fre2+2*fre5))<=2 or abs(fre6-abs(fre2+2*fre5))<=2 or abs(fre6-abs(3*fre2+fre5))<=2 or abs(fre6-abs(3*fre2-fre5))<=2 or abs(fre6-abs(fre3+fre4))<=2 or abs(fre6-abs(fre3-fre4))<=2 or abs(fre6-abs(2*fre3+fre4))<=2 or abs(fre6-abs(2*fre3+fre4))<=2 or abs(fre6-abs(fre3+2*fre4))<=2 or abs(fre6-abs(fre3+2*fre4))<=2 or abs(fre6-abs(3*fre3+fre4))<=2 or abs(fre6-abs(3*fre3-fre4))<=2 or abs(fre6-abs(fre3+fre5))<=2 or abs(fre6-abs(fre3-fre5))<=2 or abs(fre6-abs(2*fre3+fre5))<=2 or abs(fre6-abs(2*fre3+fre5))<=2 or abs(fre6-abs(fre3+2*fre5))<=2 or abs(fre6-abs(fre3+2*fre5))<=2 or abs(fre6-abs(3*fre3+fre5))<=2 or abs(fre6-abs(3*fre3-fre5))<=2:
            period6_mode=0


        elif abs(fre6-abs(fre1+fre2+fre3))<=2 or abs(fre6-abs(fre1+fre2+fre4))<=2 or abs(fre6-abs(fre2+fre3+fre4))<=2 or abs(fre6-abs(fre5+fre2+fre3))<=2 or abs(fre6-abs(fre5+fre2+fre4))<=2 or abs(fre6-abs(fre2+fre3+fre4))<=2 or abs(fre6-abs(fre1+fre5+fre3))<=5 or abs(fre6-abs(fre1+fre5+fre4))<=5 or abs(fre6-abs(fre5+fre3+fre4))<=5 or abs(fre6-abs(fre1+fre2+fre5))<=2 or abs(fre6-abs(fre1+fre2+fre4))<=2 or abs(fre6-abs(fre2+fre5+fre4))<=2 or abs(fre6-abs(fre1+fre2+fre3))<=2 or abs(fre6-abs(fre1+fre2+fre5))<=2 or abs(fre6-abs(fre2+fre3+fre5))<=2:
            period6_mode=0

        elif abs(fre6-abs(fre1+fre2-fre3))<=2 or abs(fre6-abs(fre1+fre2-fre4))<=2 or abs(fre6-abs(fre2+fre3-fre4))<=2 or abs(fre6-abs(fre5+fre2-fre3))<=2 or abs(fre6-abs(fre5+fre2-fre4))<=2 or abs(fre6-abs(fre2+fre3-fre4))<=2 or abs(fre6-abs(fre1+fre5-fre3))<=5 or abs(fre6-abs(fre1+fre5-fre4))<=5 or abs(fre6-abs(fre5+fre3-fre4))<=5 or abs(fre6-abs(fre1+fre2-fre5))<=2 or abs(fre6-abs(fre1+fre2-fre4))<=2 or abs(fre6-abs(fre2+fre5-fre4))<=2 or abs(fre6-abs(fre1+fre2-fre3))<=2 or abs(fre6-abs(fre1+fre2-fre5))<=2 or abs(fre6-abs(fre2+fre3-fre5))<=2:
            period6_mode=0
        
        else:
            period6_mode=1


    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==0:

        t1,t2,t3,t4,period6_mode=f5f.fivethmodedis(period1,period2,period3,period4,period6,f1_final,f2_final,f3_final,f4_final,f6_final)


    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==1:

        t1,t2,t3,t4,period6_mode=f5f.fivethmodedis(period1,period2,period3,period5,period6,f1_final,f2_final,f3_final,f5_final,f6_final)


    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==0:

        t1,t2,t3,t4,period6_mode=f5f.fivethmodedis(period1,period2,period4,period5,period6,f1_final,f2_final,f4_final,f5_final,f6_final)


    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==1:

        t1,t2,t3,t4,period6_mode=f5f.fivethmodedis(period1,period3,period4,period5,period6,f1_final,f3_final,f4_final,f5_final,f6_final)


    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==1:

        t1,t2,t3,t4,period6_mode=f5f.fivethmodedis(period2,period3,period4,period5,period6,f2_final,f3_final,f4_final,f5_final,f6_final)



    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==0:

        q1,q2,q3,period6_mode=f4f.fourthmodedis(period1,period2,period3,period6,f1_final,f2_final,f3_final,f6_final)


    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==0:

        q1,q2,q3,period6_mode=f4f.fourthmodedis(period1,period2,period4,period6,f1_final,f2_final,f4_final,f6_final)


    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==1:

        q1,q2,q3,period6_mode=f4f.fourthmodedis(period1,period2,period5,period6,f1_final,f2_final,f5_final,f6_final)


    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==0:

        q1,q2,q3,period6_mode=f4f.fourthmodedis(period1,period3,period4,period6,f1_final,f3_final,f4_final,f6_final)


    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==0 and period5_mode==1:

        q1,q2,q3,period6_mode=f4f.fourthmodedis(period1,period3,period5,period6,f1_final,f3_final,f5_final,f6_final)


    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==1 and period5_mode==1:

        q1,q2,q3,period6_mode=f4f.fourthmodedis(period1,period4,period5,period6,f1_final,f4_final,f5_final,f6_final)


    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==0:

        q1,q2,q3,period6_mode=f4f.fourthmodedis(period2,period3,period4,period6,f2_final,f3_final,f4_final,f6_final)


    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==1:

        q1,q2,q3,period6_mode=f4f.fourthmodedis(period2,period3,period5,period6,f2_final,f3_final,f5_final,f6_final)


    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==1:

        q1,q2,q3,period6_mode=f4f.fourthmodedis(period2,period4,period5,period6,f2_final,f4_final,f5_final,f6_final)


    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==1:

        q1,q2,q3,period6_mode=f4f.fourthmodedis(period3,period4,period5,period6,f3_final,f4_final,f5_final,f6_final)

# ##
    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==0:

        jq1,jq2,period6_mode=f3f.triplemodedis(period1,period2,period6,f1_final,f2_final,f6_final)


    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==0 and period5_mode==0:

        jq1,jq2,period6_mode=f3f.triplemodedis(period1,period3,period6,f1_final,f3_final,f6_final)


    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==1 and period5_mode==0:

        jq1,jq2,period6_mode=f3f.triplemodedis(period1,period4,period6,f1_final,f4_final,f6_final)


    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==0 and period5_mode==1:

        jq1,jq2,period6_mode=f3f.triplemodedis(period1,period5,period6,f1_final,f5_final,f6_final)


    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==0:

        jq1,jq2,period6_mode=f3f.triplemodedis(period2,period3,period6,f2_final,f3_final,f6_final)

    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==0:

        jq1,jq2,period6_mode=f3f.triplemodedis(period2,period4,period6,f2_final,f4_final,f6_final)

    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==1:

        jq1,jq2,period6_mode=f3f.triplemodedis(period2,period5,period6,f2_final,f5_final,f6_final)

    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==0:

        jq1,jq2,period6_mode=f3f.triplemodedis(period3,period4,period6,f3_final,f4_final,f6_final)

    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==0 and period5_mode==1:

        jq1,jq2,period6_mode=f3f.triplemodedis(period3,period5,period6,f3_final,f5_final,f6_final)


    elif period1_mode==0 and period2_mode==0 and period3_mode==0 and period4_mode==1 and period5_mode==1:

        jq1,jq2,period6_mode=f3f.triplemodedis(period4,period5,period6,f4_final,f5_final,f6_final)


    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==0 and period5_mode==0:
        if period1>period6:
            if period6/period1>0.9 or period6/period1<0.4:
                period6_mode=0
            else:
                period6_mode=1
        else:
            if period1/period6>0.9 or period1/period6<0.4:
                period6_mode=0
            else:
                period6_mode=1 


    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==0:
        if period2>period6:
            if period6/period2>0.9 or period6/period2<0.4:
                period6_mode=0
            else:
                period6_mode=1
        else:
            if period2/period6>0.9 or period2/period6<0.4:
                period6_mode=0
            else:
                period6_mode=1 

    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==0 and period5_mode==0:
        if period3>period6:
            if period6/period3>0.9 or period6/period3<0.4:
                period6_mode=0
            else:
                period6_mode=1
        else:
            if period3/period6>0.9 or period3/period6<0.4:
                period6_mode=0
            else:
                period6_mode=1 

    elif period1_mode==0 and period2_mode==0 and period3_mode==0 and period4_mode==1 and period5_mode==0:

        if period4>period6:
            if period6/period4>0.9 or period6/period4<0.4:
                period6_mode=0
            else:
                period6_mode=1
        else:
            if period4/period6>0.9 or period4/period6<0.4:
                period6_mode=0
            else:
                period6_mode=1 

    elif period1_mode==0 and period2_mode==0 and period3_mode==0 and period4_mode==0 and period5_mode==1:
        if period5>period6:
            if period6/period5>0.9 or period6/period5<0.4:
                period6_mode=0
            else:
                period6_mode=1
        else:
            if period5/period6>0.9 or period5/period6<0.4:
                period6_mode=0
            else:
                period6_mode=1 

    else:
        period6_mode=1


    return period1_mode,period2_mode,period3_mode,period4_mode,period5_mode,period6_mode

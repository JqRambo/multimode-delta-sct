import fourthmodediscern as fm4f
import triplemodediscern as fm3f
import double_modediscern as fm2f

def fivethmodediscern(period1,period2,period3,period4,period5,period1_mode,period2_mode,period3_mode,period4_mode,period5_mode):
    
    if period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==1:

        # period1_hg,period2_hg,period3_hg,period4_hg=fm4f.fourthmodediscern(period1,period2,period3,period4,period1_mode,period2_mode,period3_mode,period4_mode)
        # if period1_hg in ['F', '1O', '2O', '3O'] and period2_hg in ['F', '1O', '2O', '3O'] and period3_hg in ['F', '1O', '2O', '3O'] and period4_hg in ['F', '1O', '2O', '3O']:
        #     period1_Mode,period2_Mode,period3_Mode,period4_Mode=fm4f.fourthmodediscern(period1,period2,period3,period4,period1_mode,period2_mode,period3_mode,period4_mode)
        #     period5_Mode=0
        
        # else:
        #     period1_hg,period2_hg,period3_hg,period5_hg=fm4f.fourthmodediscern(period1,period2,period3,period5,period1_mode,period2_mode,period3_mode,period5_mode)
        #     if period1_hg in ['F', '1O', '2O', '3O'] and period2_hg in ['F', '1O', '2O', '3O'] and period3_hg in ['F', '1O', '2O', '3O'] and period5_hg in ['F', '1O', '2O', '3O']:
        #         period1_Mode,period2_Mode,period3_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period2,period3,period5,period1_mode,period2_mode,period3_mode,period5_mode)
        #         period4_Mode=0

        #     else:
        #         period1_hg,period2_hg,period4_hg,period5_hg=fm4f.fourthmodediscern(period1,period2,period4,period5,period1_mode,period2_mode,period4_mode,period5_mode)
        #         if period1_hg in ['F', '1O', '2O', '3O'] and period2_hg in ['F', '1O', '2O', '3O'] and period4_hg in ['F', '1O', '2O', '3O'] and period5_hg in ['F', '1O', '2O', '3O']:
        #             period1_Mode,period2_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period2,period4,period5,period1_mode,period2_mode,period4_mode,period5_mode)
        #             period3_Mode=0

        #         else:
        #             period1_hg,period3_hg,period4_hg,period5_hg=fm4f.fourthmodediscern(period1,period3,period4,period5,period1_mode,period3_mode,period4_mode,period5_mode)
        #             if period1_hg in ['F', '1O', '2O', '3O'] and period3_hg in ['F', '1O', '2O', '3O'] and period4_hg in ['F', '1O', '2O', '3O'] and period5_hg in ['F', '1O', '2O', '3O']:
        #                 period1_Mode,period3_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period3,period4,period5,period1_mode,period3_mode,period4_mode,period5_mode)
        #                 period2_Mode=0

        #             else:
        #                 period2_Mode,period3_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period2,period3,period4,period5,period2_mode,period3_mode,period4_mode,period5_mode)
        #                 period1_Mode=0

        period1_hg,period2_hg,period3_hg,period4_hg=fm4f.fourthmodediscern(period1,period2,period3,period4,period1_mode,period2_mode,period3_mode,period4_mode)
        dd_count1=0

        if period1_hg in ['F', '1O', '2O', '3O']:
            dd_count1 += 1
        if period2_hg in ['F', '1O', '2O', '3O']:
            dd_count1 +=1
        if period3_hg in ['F', '1O', '2O', '3O']:
            dd_count1 +=1 
        if period4_hg in ['F', '1O', '2O', '3O']:
            dd_count1 +=1

        period1_hs,period2_hs,period3_hs,period5_hs=fm4f.fourthmodediscern(period1,period2,period3,period5,period1_mode,period2_mode,period3_mode,period5_mode)
        dd_count2=0
            
        if period1_hs in ['F', '1O', '2O', '3O']:
            dd_count2 +=1
        if period2_hs in ['F', '1O', '2O', '3O']:
            dd_count2 +=1
        if period3_hs in ['F', '1O', '2O', '3O']:
            dd_count2 +=1
        if period5_hs in ['F', '1O', '2O', '3O']:
            dd_count2 +=1

        period1_hw,period2_hw,period4_hw,period5_hw=fm4f.fourthmodediscern(period1,period2,period4,period5,period1_mode,period2_mode,period4_mode,period5_mode)
        dd_count3=0
        if period1_hw in ['F', '1O', '2O', '3O']:
            dd_count3 +=1
        if period2_hw in ['F', '1O', '2O', '3O']:
            dd_count3 +=1
        if period4_hw in ['F', '1O', '2O', '3O']:
            dd_count3 +=1
        if period5_hw in ['F', '1O', '2O', '3O']:
            dd_count3 +=1
              

        period1_hy,period3_hy,period4_hy,period5_hy=fm4f.fourthmodediscern(period1,period3,period4,period5,period1_mode,period3_mode,period4_mode,period5_mode)
        dd_count4=0
        if period1_hy in ['F', '1O', '2O', '3O']:
            dd_count4 +=1
        if period3_hy in ['F', '1O', '2O', '3O']:
            dd_count4 +=1
        if period4_hy in ['F', '1O', '2O', '3O']:
            dd_count4 +=1
        if period5_hy in ['F', '1O', '2O', '3O']:
            dd_count4 +=1

        period2_hb,period3_hb,period4_hb,period5_hb=fm4f.fourthmodediscern(period2,period3,period4,period5,period2_mode,period3_mode,period4_mode,period5_mode)
        dd_count5=0
        if period2_hb in ['F', '1O', '2O', '3O']:
            dd_count5 +=1
        if period3_hb in ['F', '1O', '2O', '3O']:
            dd_count5 +=1
        if period4_hb in ['F', '1O', '2O', '3O']:
            dd_count5 +=1
        if period5_hb in ['F', '1O', '2O', '3O']:
            dd_count5 +=1
                       

        ##
        # if dd_count1>dd_count2 and dd_count1>dd_count3 and dd_count1>dd_count4 and dd_count1>dd_count5:
        #     period1_Mode,period2_Mode,period3_Mode,period4_Mode=fm4f.fourthmodediscern(period1,period2,period3,period4,period1_mode,period2_mode,period3_mode,period4_mode)
        #     period5_Mode=0
        # elif dd_count2>dd_count1 and dd_count2>dd_count3 and dd_count2>dd_count4 and dd_count2>dd_count5:
        #     period1_Mode,period2_Mode,period3_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period2,period3,period5,period1_mode,period2_mode,period3_mode,period5_mode)
        #     period4_Mode=0
        # elif dd_count3>dd_count1 and dd_count3>dd_count2 and dd_count3>dd_count4 and dd_count3>dd_count5:
        #     period1_Mode,period2_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period2,period4,period5,period1_mode,period2_mode,period4_mode,period5_mode)
        #     period3_Mode=0
        # elif dd_count4>dd_count1 and dd_count4>dd_count2 and dd_count4>dd_count3 and dd_count4>dd_count5:
        #     period1_Mode,period3_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period3,period4,period5,period1_mode,period3_mode,period4_mode,period5_mode)
        #     period2_Mode=0
        # else:
        #     # dd_count4>dd_count1 and dd_count4>dd_count2 and dd_count4>dd_count3 and dd_count4>dd_count5:
        #     period2_Mode,period3_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period2,period3,period4,period5,period2_mode,period3_mode,period4_mode,period5_mode)
        #     period1_Mode=0
        
        if max(dd_count1, dd_count2, dd_count3, dd_count4,dd_count5)==dd_count1:
            period1_Mode,period2_Mode,period3_Mode,period4_Mode=fm4f.fourthmodediscern(period1,period2,period3,period4,period1_mode,period2_mode,period3_mode,period4_mode)
            period5_Mode=0
        elif max(dd_count1, dd_count2, dd_count3, dd_count4,dd_count5)==dd_count2:
            period1_Mode,period2_Mode,period3_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period2,period3,period5,period1_mode,period2_mode,period3_mode,period5_mode)
            period4_Mode=0
        elif max(dd_count1, dd_count2, dd_count3, dd_count4,dd_count5)==dd_count3:
            period1_Mode,period2_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period2,period4,period5,period1_mode,period2_mode,period4_mode,period5_mode)
            period3_Mode=0
        elif max(dd_count1, dd_count2, dd_count3, dd_count4,dd_count5)==dd_count4:
            period1_Mode,period3_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period3,period4,period5,period1_mode,period3_mode,period4_mode,period5_mode)
            period2_Mode=0
        else:
            period2_Mode,period3_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period2,period3,period4,period5,period2_mode,period3_mode,period4_mode,period5_mode)
            period1_Mode=0


    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==0:
        period1_Mode,period2_Mode,period3_Mode,period4_Mode=fm4f.fourthmodediscern(period1,period2,period3,period4,period1_mode,period2_mode,period3_mode,period4_mode)
        period5_Mode=0

    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==1:
        period1_Mode,period2_Mode,period3_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period2,period3,period5,period1_mode,period2_mode,period3_mode,period5_mode)
        period4_Mode=0

    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==1:
        period1_Mode,period2_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period2,period4,period5,period1_mode,period2_mode,period4_mode,period5_mode)
        period3_Mode=0

    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==1:
        period1_Mode,period3_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period1,period3,period4,period5,period1_mode,period3_mode,period4_mode,period5_mode)
        period2_Mode=0

    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==1:
        period2_Mode,period3_Mode,period4_Mode,period5_Mode=fm4f.fourthmodediscern(period2,period3,period4,period5,period2_mode,period3_mode,period4_mode,period5_mode)
        period1_Mode=0

##
    elif period1_mode==1 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==0:
        period4_Mode=0
        period5_Mode=0
        period1_Mode,period2_Mode,period3_Mode=fm3f.triplemodediscern(period1,period2,period3)


    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==0:
        period3_Mode=0
        period5_Mode=0
        period1_Mode,period2_Mode,period4_Mode=fm3f.triplemodediscern(period1,period2,period4)

    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==1:
        period3_Mode=0
        period4_Mode=0
        period1_Mode,period2_Mode,period5_Mode=fm3f.triplemodediscern(period1,period2,period5)

    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==0:
        period2_Mode=0
        period5_Mode=0
        period1_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period1,period3,period4)


    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==0 and period5_mode==1:
        period2_Mode=0
        period4_Mode=0
        period1_Mode,period3_Mode,period5_Mode=fm3f.triplemodediscern(period1,period3,period5)


    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==1 and period5_mode==1:
        period2_Mode=0
        period3_Mode=0
        period1_Mode,period4_Mode,period5_Mode=fm3f.triplemodediscern(period1,period4,period5)

##
    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==1 and period5_mode==0:
        period1_Mode=0
        period5_Mode=0
        period2_Mode,period3_Mode,period4_Mode=fm3f.triplemodediscern(period2,period3,period4)


    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==1:
        period1_Mode=0
        period4_Mode=0
        period2_Mode,period3_Mode,period5_Mode=fm3f.triplemodediscern(period2,period3,period5)



    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==1:
        period1_Mode=0
        period3_Mode=0
        period2_Mode,period4_Mode,period5_Mode=fm3f.triplemodediscern(period2,period4,period5)


    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==1:
        period1_Mode=0
        period2_Mode=0
        period3_Mode,period4_Mode,period5_Mode=fm3f.triplemodediscern(period3,period4,period5)


##
    elif period1_mode==1 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==0:
        period3_Mode=0
        period4_Mode=0
        period5_Mode=0
        period1_Mode,period2_Mode=fm2f.doubleModediscern(period1,period2)


    elif period1_mode==1 and period2_mode==0 and period3_mode==1 and period4_mode==0 and period5_mode==0:
        period2_Mode=0
        period4_Mode=0
        period5_Mode=0
        period1_Mode,period3_Mode=fm2f.doubleModediscern(period1,period3)

        
    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==1 and period5_mode==0:
        period2_Mode=0
        period3_Mode=0
        period5_Mode=0
        period1_Mode,period4_Mode=fm2f.doubleModediscern(period1,period4)

    elif period1_mode==1 and period2_mode==0 and period3_mode==0 and period4_mode==0 and period5_mode==1:
        period2_Mode=0
        period3_Mode=0
        period4_Mode=0
        period1_Mode,period5_Mode=fm2f.doubleModediscern(period1,period5)


    elif period1_mode==0 and period2_mode==1 and period3_mode==1 and period4_mode==0 and period5_mode==0:
        period1_Mode=0
        period4_Mode=0
        period5_Mode=0
        period2_Mode,period3_Mode=fm2f.doubleModediscern(period2,period3)


    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==1 and period5_mode==0:
        period1_Mode=0
        period3_Mode=0
        period5_Mode=0
        period2_Mode,period4_Mode=fm2f.doubleModediscern(period2,period4)
  
    elif period1_mode==0 and period2_mode==1 and period3_mode==0 and period4_mode==0 and period5_mode==1:
        period1_Mode=0
        period3_Mode=0
        period4_Mode=0
        period2_Mode,period5_Mode=fm2f.doubleModediscern(period2,period5)
  

    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==1 and period5_mode==0:
        period1_Mode=0
        period2_Mode=0
        period5_Mode=0
        period3_Mode,period4_Mode=fm2f.doubleModediscern(period3,period4)
  
    elif period1_mode==0 and period2_mode==0 and period3_mode==1 and period4_mode==0 and period5_mode==1:
        period1_Mode=0
        period2_Mode=0
        period4_Mode=0
        period3_Mode,period5_Mode=fm2f.doubleModediscern(period3,period5)
  

    elif period1_mode==0 and period2_mode==0 and period3_mode==0 and period4_mode==1 and period5_mode==1:
        period1_Mode=0
        period2_Mode=0
        period3_Mode=0
        period4_Mode,period5_Mode=fm2f.doubleModediscern(period4,period5)
   

    else:
        period1_Mode=0
        period2_Mode=0
        period3_Mode=0
        period4_Mode=0
        period5_Mode=0


    return period1_Mode,period2_Mode,period3_Mode,period4_Mode,period5_Mode



